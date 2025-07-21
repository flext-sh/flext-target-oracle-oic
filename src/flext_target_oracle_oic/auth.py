"""Oracle Integration Cloud authentication using centralized patterns.

Refactored to use centralized OIC authentication patterns from flext-core.
Eliminates code duplication across Oracle OIC projects.
"""

from __future__ import annotations

from typing import Any

from flext_core.config.oracle_oic import (
    OICAuthConfig,
    OICTargetAuthenticator,
)
from flext_observability.logging import get_logger
from singer_sdk.authenticators import OAuthAuthenticator

logger = get_logger(__name__)


class OICOAuth2Authenticator(OAuthAuthenticator):
    """OAuth2 authenticator for Oracle Integration Cloud using centralized patterns.

    Refactored implementation using flext-core centralized authentication.
    Eliminates code duplication while maintaining Singer SDK compatibility.
    """

    def __init__(self, stream: Any) -> None:
        """Initialize authenticator using centralized OIC patterns."""
        auth_endpoint = stream.config.get("oauth_token_url")

        # Create centralized auth config
        auth_config = OICAuthConfig(
            oauth_client_id=stream.config["oauth_client_id"],
            oauth_client_secret=stream.config["oauth_client_secret"],
            oauth_token_url=auth_endpoint,
            oauth_client_aud=stream.config.get("oauth_client_aud"),
            oauth_scope=stream.config.get("oauth_scope", ""),
        )

        # Use centralized authenticator for target operations
        self._central_auth = OICTargetAuthenticator(auth_config)

        # Build OAuth2 scopes using centralized logic
        oauth_scopes = self._central_auth.get_oauth_scopes()

        # Store reference to stream for Singer SDK compatibility
        self._stream = stream

        super().__init__(
            stream=stream,
            auth_endpoint=auth_endpoint,
            oauth_scopes=oauth_scopes,
        )

    @property
    def oauth_request_body(self) -> dict[str, Any]:
        """Generate OAuth request body using centralized patterns.

        Returns:
            Dictionary containing grant_type and scope for OAuth token request.

        """
        return self._central_auth.get_oauth_request_body()

    @property
    def oauth_request_payload(self) -> dict[str, Any]:
        """Get OAuth request payload using centralized patterns.

        Returns:
            OAuth request body for token authentication.

        """
        return self.oauth_request_body

    def update_access_token(self) -> None:
        """Update access token using centralized OAuth2 implementation.

        Uses centralized OIC authentication patterns from flext-core.
        """
        if not self.auth_endpoint:
            error_msg = "OAuth token URL not configured"
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Use centralized authentication
        token_result = self._central_auth.get_access_token()
        if not token_result.is_success:
            error_msg = f"Authentication failed: {token_result.error}"
            logger.error(error_msg)
            raise ValueError(error_msg)

        self.access_token = token_result.data
        logger.info("Successfully obtained OAuth2 access token")
