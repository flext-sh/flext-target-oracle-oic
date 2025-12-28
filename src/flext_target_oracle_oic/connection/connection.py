"""Oracle OIC connection management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import json
from typing import override

import requests
import urllib3
from flext_core import FlextLogger, FlextResult, FlextTypes as t

from flext_target_oracle_oic.connection.settings import OICConnectionSettings
from flext_target_oracle_oic.target_exceptions import (
    FlextTargetOracleOicAuthenticationError,
)

# Constants
HTTP_OK = 200
HTTP_BAD_REQUEST = 400


logger = FlextLogger(__name__)


class OICConnection:
    """Oracle OIC connection using flext-core patterns."""

    @override
    def __init__(self, config: OICConnectionSettings) -> None:
        """Initialize OIC connection."""
        self.config: OICConnectionSettings = config
        self._access_token: str | None = None
        self._session: requests.Session | None = None

    def connect(self: object) -> FlextResult[None]:
        """Establish OIC connection with OAuth2 authentication."""
        try:
            if self._session:
                return FlextResult[None].ok(None)

            self._session = requests.Session()

            # Configure session
            if not self.config.verify_ssl:
                self._session.verify = False

                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            # Authenticate and get access token
            auth_result: FlextResult[object] = self._authenticate()
            if not auth_result.success:
                return FlextResult[None].fail(
                    auth_result.error or "Authentication failed",
                )

            logger.info("Connected to OIC server: %s", self.config.base_url)
            return FlextResult[None].ok(None)

        except FlextTargetOracleOicAuthenticationError as e:
            logger.exception("OIC authentication failed")
            return FlextResult[None].fail(f"Authentication failed: {e}")
        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC connection failed")
            return FlextResult[None].fail(f"Connection failed: {e}")

    def disconnect(self: object) -> FlextResult[None]:
        """Close OIC connection."""
        try:
            if self._session:
                self._session.close()
                self._session = None
                self._access_token = None
                logger.info("OIC connection closed")

            return FlextResult[None].ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC disconnect failed")
            return FlextResult[None].fail(f"Disconnect failed: {e}")

    def _authenticate(self: object) -> FlextResult[str]:
        """Authenticate with OAuth2 and get access token."""
        try:
            if not self._session:
                return FlextResult[str].fail("Session not initialized")

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
                return FlextResult[str].fail(
                    f"Authentication failed: {response.status_code} - {response.text}",
                )

            token_data: dict[str, t.GeneralValueType] = response.json()
            self._access_token = token_data.get("access_token")

            if not self._access_token:
                return FlextResult[str].fail("No access token received")

            return FlextResult[str].ok(self._access_token)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC authentication failed")
            return FlextResult[str].fail(f"Authentication failed: {e}")

    def test_connection(self: object) -> FlextResult[bool]:
        """Test OIC connection."""
        try:
            if not self._session or not self._access_token:
                connect_result: FlextResult[object] = self.connect()
                if not connect_result.success:
                    return FlextResult[bool].fail(
                        connect_result.error or "Connection failed",
                    )

            # Test with simple API call
            api_url = f"{self.config.build_api_base_url()}/integrations"
            if not self._access_token:
                return FlextResult[bool].fail("No access token available")
            headers = self.config.get_api_headers(self._access_token)

            if not self._session:
                return FlextResult[bool].fail("No active session available")
            response = self._session.get(
                api_url,
                headers=headers,
                timeout=self.config.timeout,
            )

            if response.status_code in {
                200,
                401,
            }:  # 401 means we connected but not authorized
                return FlextResult[bool].ok(data=True)

            return FlextResult[bool].fail(
                f"Connection test failed: {response.status_code}",
            )

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC connection test failed")
            return FlextResult[bool].fail(f"Connection test failed: {e}")

    def make_request(
        self,
        method: str,
        endpoint: str,
        data: dict[str, t.GeneralValueType] | None = None,
        params: dict[str, t.GeneralValueType] | None = None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Make authenticated request to OIC API."""
        try:
            if not self._session or not self._access_token:
                connect_result: FlextResult[object] = self.connect()
                if not connect_result.success:
                    return FlextResult[dict[str, t.GeneralValueType]].fail(
                        connect_result.error or "Connection failed",
                    )

            url = f"{self.config.build_api_base_url()}/{endpoint.lstrip('/')}"
            if not self._access_token:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    "No access token available",
                )
            headers = self.config.get_api_headers(self._access_token)

            # Make request
            if not self._session:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    "No active session available",
                )

            # Prepare params as strings to satisfy typing
            prepared_params = {k: str(v) for k, v in params.items()} if params else None
            response = self._session.request(
                method.upper(),
                url,
                headers=headers,
                timeout=self.config.timeout,
                params=prepared_params,
                json=data or None,
            )

            # Handle response
            if response.status_code >= HTTP_BAD_REQUEST:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"API request failed: {response.status_code} - {response.text}",
                )

            try:
                response_data_obj: object = response.json()
            except json.JSONDecodeError:
                response_data_obj = {"text": response.text}

            response_dict: dict[str, t.GeneralValueType]
            if isinstance(response_data_obj, dict):
                # Cast to dict[str, t.GeneralValueType] for proper typing
                response_dict = response_data_obj
            else:
                response_dict = {"data": "response_data_obj"}

            return FlextResult[dict[str, t.GeneralValueType]].ok(response_dict)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC API request failed: %s %s", method, endpoint)
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"API request failed: {e}"
            )

    @property
    def is_connected(self: object) -> bool:
        """Check if connection is active."""
        return self._session is not None and self._access_token is not None
