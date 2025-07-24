"""Oracle Integration Cloud authentication using dependency injection.

Refactored to use dependency injection for Oracle OIC authentication patterns.
Follows Clean Architecture principles by using abstract interfaces.
"""

from __future__ import annotations

# Removed circular dependency - use DI pattern
import logging
from typing import TYPE_CHECKING, Any

from singer_sdk.authenticators import OAuthAuthenticator

if TYPE_CHECKING:
    from typing import Any as OracleConfigurationProvider

logger = logging.getLogger(__name__)

# Oracle configuration provider will be injected at runtime
_config_provider: OracleConfigurationProvider | None = None


def set_configuration_provider(provider: OracleConfigurationProvider) -> None:
    """Set the Oracle configuration provider via dependency injection.

    Args:
        provider: Oracle configuration provider implementation

    """
    global _config_provider
    _config_provider = provider


def _get_configuration_provider() -> OracleConfigurationProvider:
    """Get configuration provider or raise error if not set.

    Returns:
        Oracle configuration provider

    Raises:
        RuntimeError: If no configuration provider has been injected

    """
    if _config_provider is None:
        error_msg = "Oracle configuration provider not injected - call set_configuration_provider() first"
        logger.error(error_msg)
        raise RuntimeError(error_msg)
    return _config_provider


class OICOAuth2Authenticator(OAuthAuthenticator):
    """OAuth2 authenticator for Oracle Integration Cloud using dependency injection.

    Refactored implementation using dependency injection for Oracle authentication.
    Follows Clean Architecture principles while maintaining Singer SDK compatibility.
    """

    def __init__(self, stream: Any) -> None:
        """Initialize authenticator using dependency injection patterns."""
        auth_endpoint = stream.config.get("oauth_token_url")

        # Store stream reference for Singer SDK compatibility
        self._stream = stream

        scopes = self._get_oauth_scopes()
        super().__init__(
            stream=stream,
            auth_endpoint=auth_endpoint,
            oauth_scopes=" ".join(scopes) if scopes else None,
        )

    def _get_oauth_scopes(self) -> list[str]:
        """Get OAuth2 scopes using dependency injection.

        Returns:
            List of OAuth2 scopes, fallback if provider not available

        """
        try:
            provider = _get_configuration_provider()
            scopes = provider.get_oauth_scopes()
            return scopes if isinstance(scopes, list) else ["read", "write"]
        except RuntimeError:
            # Provider not injected - use fallback behavior
            logger.warning(
                "Oracle configuration provider not available, using fallback OAuth scopes",
            )
            return ["read", "write"]

    @property
    def oauth_request_body(self) -> dict[str, Any]:
        """Generate OAuth request body using dependency injection.

        Returns:
            Dictionary containing grant_type and scope for OAuth token request.

        """
        try:
            provider = _get_configuration_provider()
            body = provider.get_oauth_request_body()
            return body if isinstance(body, dict) else self._get_fallback_body()
        except RuntimeError:
            # Provider not injected - use fallback behavior
            logger.warning(
                "Oracle configuration provider not available, using fallback OAuth request body",
            )
            return self._get_fallback_body()

    def _get_fallback_body(self) -> dict[str, Any]:
        """Get fallback OAuth request body."""
        return {
            "grant_type": "client_credentials",
            "scope": " ".join(self.oauth_scopes) if self.oauth_scopes else "",
        }

    @property
    def oauth_request_payload(self) -> dict[str, Any]:
        """Get OAuth request payload using dependency injection.

        Returns:
            OAuth request body for token authentication.

        """
        return self.oauth_request_body

    def update_access_token(self) -> None:
        """Update access token using dependency injection.

        Uses dependency injection for Oracle OIC authentication patterns.
        """
        if not self.auth_endpoint:
            error_msg = "OAuth token URL not configured"
            logger.error(error_msg)
            raise ValueError(error_msg)

        try:
            # Try to use injected configuration provider
            provider = _get_configuration_provider()
            token_result = provider.get_access_token()

            if not token_result.is_success:
                error_msg = f"Authentication failed: {token_result.error}"
                logger.error(error_msg)
                raise ValueError(error_msg)

            self.access_token = token_result.data
            logger.info("Successfully obtained OAuth2 access token using DI provider")

        except RuntimeError:
            # Provider not injected - use fallback behavior
            logger.warning(
                "Oracle configuration provider not available, using fallback authentication",
            )
            self._update_access_token_fallback()

    def _update_access_token_fallback(self) -> None:
        """Fallback token update when DI provider not available."""
        # This would implement basic OAuth2 flow as fallback
        # For now, just log the fallback usage
        logger.warning(
            "Using fallback OAuth2 authentication - inject provider for full functionality",
        )

        # Basic fallback implementation
        import base64

        import requests

        client_id = self._stream.config.get("oauth_client_id")
        client_secret = self._stream.config.get("oauth_client_secret")

        if not client_id or not client_secret:
            error_msg = "OAuth credentials not configured"
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Prepare Basic Authentication header
        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = self.oauth_request_body

        try:
            response = requests.post(
                self.auth_endpoint,
                headers=headers,
                data=data,
                timeout=30,
            )
            response.raise_for_status()

            token_data = response.json()
            self.access_token = token_data.get("access_token")

            if not self.access_token:
                msg = "No access token in response"
                raise ValueError(msg)

            logger.info(
                "Successfully obtained OAuth2 access token using fallback method",
            )

        except Exception as e:
            error_msg = f"Fallback authentication failed: {e}"
            logger.exception(error_msg)
            raise ValueError(error_msg) from e
