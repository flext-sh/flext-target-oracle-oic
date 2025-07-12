"""Oracle Integration Cloud authentication using flext-core patterns.

REFACTORED: Clean OAuth2 implementation using flext-core patterns.
Zero tolerance for code duplication.
"""

from __future__ import annotations

import base64
from typing import Any

import requests
from singer_sdk.authenticators import OAuthAuthenticator

from flext_observability.logging import get_logger

logger = get_logger(__name__)


class OICOAuth2Authenticator(OAuthAuthenticator):
    """OAuth2 authenticator for Oracle Integration Cloud using flext-core patterns.

    Clean implementation following SOLID principles.
    Uses standard OAuth2 client credentials flow.
    """

    def __init__(self, stream: Any) -> None:
        auth_endpoint = stream.config.get("oauth_token_url")

        # Build OAuth2 scope for OIC
        client_aud = stream.config.get("oauth_client_aud", "")
        if client_aud:
            # Build scope like: "audience:443urn:opc:resource:consumer:all ..."
            resource_aud = f"{client_aud}:443urn:opc:resource:consumer:all"
            api_aud = f"{client_aud}:443/ic/api/"
            oauth_scopes = f"{resource_aud} {api_aud}"
        else:
            # Fallback to simple scope if no audience configured:
            oauth_scopes = stream.config.get(
                "oauth_scope",
                "urn:opc:resource:consumer:all",
            )

        # Store reference to stream for access to config during token refresh
        self._stream = stream

        super().__init__(
            stream=stream,
            auth_endpoint=auth_endpoint,
            oauth_scopes=oauth_scopes,
        )

    @property
    def oauth_request_body(self) -> dict[str, Any]:
        """Generate OAuth request body for client credentials flow.

        Returns:
            Dictionary containing grant_type and scope for OAuth token request.

        """
        return {
            "grant_type": "client_credentials",
            "scope": self.oauth_scopes or "urn:opc:resource:consumer:all",
        }

    @property
    def oauth_request_payload(self) -> dict[str, Any]:
        """Get OAuth request payload.

        Returns:
            OAuth request body for token authentication.

        """
        return self.oauth_request_body

    def update_access_token(self) -> None:
        """Update the access token by making OAuth client credentials request.

        Raises:
            ValueError: If OAuth token URL is not configured.
            HTTPError: If token request fails.

        """
        if not self.auth_endpoint:
            msg = "OAuth token URL is required"
            raise ValueError(msg)

        client_id = self._stream.config["oauth_client_id"]
        client_secret = self._stream.config["oauth_client_secret"]

        # Encode client credentials for HTTP Basic authentication per RFC 7617
        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        logger.debug("Requesting OAuth2 token from %s", self.auth_endpoint)

        response = requests.post(
            self.auth_endpoint,
            headers=headers,
            data=self.oauth_request_payload,
            timeout=30,
        )
        response.raise_for_status()

        token_data = response.json()
        self.access_token = token_data["access_token"]

        logger.info("Successfully obtained OAuth2 access token")
