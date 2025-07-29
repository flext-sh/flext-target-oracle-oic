"""Oracle OIC connection management using flext-core patterns."""

import urllib3


from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import requests

# Import from flext-core for foundational patterns
from flext_core import FlextResult, get_logger

# Import exception classes
from flext_target_oracle_oic.exceptions import (
# Constants
HTTP_OK = 200

    FlextTargetOracleOicAuthenticationError,
)

if TYPE_CHECKING:
    from flext_target_oracle_oic.connection.config import OICConnectionConfig

logger = get_logger(__name__)


class OICConnection:
    """Oracle OIC connection using flext-core patterns."""

    def __init__(self, config: OICConnectionConfig) -> None:
        """Initialize OIC connection."""
        self.config = config
        self._access_token: str | None = None
        self._session: requests.Session | None = None

    def connect(self) -> FlextResult[None]:
        """Establish OIC connection with OAuth2 authentication."""
        try:
            if self._session:
                return FlextResult.ok(None)

            self._session = requests.Session()

            # Configure session
            if not self.config.verify_ssl:
                self._session.verify = False


                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            # Authenticate and get access token
            auth_result = self._authenticate()
            if not auth_result.is_success:
                return FlextResult.fail(auth_result.error or "Authentication failed")

            logger.info(f"Connected to OIC server: {self.config.server_url}")
            return FlextResult.ok(None)

        except FlextTargetOracleOicAuthenticationError as e:
            logger.exception("OIC authentication failed")
            return FlextResult.fail(f"Authentication failed: {e}")
        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC connection failed")
            return FlextResult.fail(f"Connection failed: {e}")

    def disconnect(self) -> FlextResult[None]:
        """Close OIC connection."""
        try:
            if self._session:
                self._session.close()
                self._session = None
                self._access_token = None
                logger.info("OIC connection closed")

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC disconnect failed")
            return FlextResult.fail(f"Disconnect failed: {e}")

    def _authenticate(self) -> FlextResult[str]:
        """Authenticate with OAuth2 and get access token."""
        try:
            if not self._session:
                return FlextResult.fail("Session not initialized")

            auth_url = self.config.build_auth_url()
            headers = self.config.get_auth_headers()

            # Prepare OAuth2 data
            data = {
                "grant_type": "client_credentials",
                "client_id": self.config.client_id,
                "client_secret": self.config.client_secret,
                "scope": self.config.scope,
            }

            # Add username/password if provided
            if self.config.username and self.config.password:
                data.update(
                    {
                        "grant_type": "password",
                        "username": self.config.username,
                        "password": self.config.password,
                    },
                )

            response = self._session.post(
                auth_url,
                headers=headers,
                data=data,
                timeout=self.config.timeout,
            )

            if response.status_code != HTTP_OK:
                return FlextResult.fail(
                    f"Authentication failed: {response.status_code} - {response.text}",
                )

            token_data = response.json()
            self._access_token = token_data.get("access_token")

            if not self._access_token:
                return FlextResult.fail("No access token received")

            return FlextResult.ok(self._access_token)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC authentication failed")
            return FlextResult.fail(f"Authentication failed: {e}")

    def test_connection(self) -> FlextResult[bool]:
        """Test OIC connection."""
        try:
            if not self._session or not self._access_token:
                connect_result = self.connect()
                if not connect_result.is_success:
                    return FlextResult.fail(connect_result.error)

            # Test with simple API call
            api_url = f"{self.config.build_api_base_url()}/integrations"
            headers = self.config.get_api_headers(self._access_token)

            response = self._session.get(
                api_url,
                headers=headers,
                timeout=self.config.timeout,
            )

            if response.status_code in {
                200,
                401,
            }:  # 401 means we connected but not authorized
                return FlextResult.ok(True)

            return FlextResult.fail(f"Connection test failed: {response.status_code}")

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC connection test failed")
            return FlextResult.fail(f"Connection test failed: {e}")

    def make_request(
        self,
        method: str,
        endpoint: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Make authenticated request to OIC API."""
        try:
            if not self._session or not self._access_token:
                connect_result = self.connect()
                if not connect_result.is_success:
                    return FlextResult.fail(connect_result.error)

            url = f"{self.config.build_api_base_url()}/{endpoint.lstrip('/')}"
            headers = self.config.get_api_headers(self._access_token)

            # Prepare request arguments
            request_kwargs = {
                "headers": headers,
                "timeout": self.config.timeout,
            }

            if params:
                request_kwargs["params"] = params

            if data:
                request_kwargs["data"] = json.dumps(data)

            # Make request
            response = self._session.request(method.upper(), url, **request_kwargs)

            # Handle response
            if response.status_code >= 400:
                return FlextResult.fail(
                    f"API request failed: {response.status_code} - {response.text}",
                )

            try:
                response_data = response.json()
            except json.JSONDecodeError:
                response_data = {"text": response.text}

            return FlextResult.ok(response_data)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception(f"OIC API request failed: {method} {endpoint}")
            return FlextResult.fail(f"API request failed: {e}")

    @property
    def is_connected(self) -> bool:
        """Check if connection is active."""
        return self._session is not None and self._access_token is not None
