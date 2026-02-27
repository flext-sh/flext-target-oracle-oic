"""Target Oracle OIC Configuration - Unified configuration management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping

import requests

from .settings import TargetOracleOicConfig
from .typings import t


class OICOAuth2Authenticator:
    """OAuth2 Authenticator for Oracle Integration Cloud."""

    def __init__(self, config: TargetOracleOicConfig) -> None:
        """Initialize the authenticator with target configuration."""
        self._config: TargetOracleOicConfig = config
        self._access_token: str | None = None
        self._token_type: str = "Bearer"

    def build_token_request_data(self) -> dict[str, str]:
        """Build the payload for requesting an OAuth2 token."""
        payload = {
            "grant_type": "client_credentials",
            "client_id": self._config.oauth_client_id,
            "client_secret": self._config.get_oauth_client_secret_value(),
        }
        if self._config.oauth_scope:
            payload["scope"] = self._config.oauth_scope
        if self._config.oauth_client_aud:
            payload["audience"] = self._config.oauth_client_aud
        return payload

    def get_access_token(self, *, force_refresh: bool = False) -> str:
        """Get the current access token, optionally forcing a refresh."""
        if self._access_token is not None and not force_refresh:
            return self._access_token

        try:
            response = requests.post(
                str(self._config.oauth_token_url),
                data=self.build_token_request_data(),
                headers=dict(self._config.get_oauth_headers()),
                timeout=self._config.timeout,
            )
            response.raise_for_status()
        except requests.RequestException as exc:
            msg = f"Failed to request OAuth2 token: {exc}"
            raise RuntimeError(msg) from exc

        payload_raw = response.json()
        if not isinstance(payload_raw, dict):
            msg = "OAuth2 token response is not a JSON object"
            raise TypeError(msg)

        token_payload = payload_raw
        access_token = token_payload.get("access_token")
        if not isinstance(access_token, str) or not access_token:
            msg = "OAuth2 token response did not include a valid access_token"
            raise RuntimeError(msg)

        token_type = token_payload.get("token_type")
        if isinstance(token_type, str) and token_type:
            self._token_type = token_type

        self._access_token = access_token
        return access_token

    @property
    def auth_headers(self) -> Mapping[str, str]:
        """Get the authentication headers block for requests."""
        token = self.get_access_token()
        return {"Authorization": f"{self._token_type} {token}"}


# Backward compatibility aliases - all Config classes now use the single TargetOracleOicConfig
# These provide compatibility for existing code while directing to the standardized Config
OICAuthConfig = TargetOracleOicConfig
OICConnectionConfig = TargetOracleOicConfig
OICDeploymentConfig = TargetOracleOicConfig
OICProcessingConfig = TargetOracleOicConfig
OICEntityConfig = TargetOracleOicConfig


def create_config_from_dict(
    config_dict: Mapping[str, t.JsonValue],
) -> TargetOracleOicConfig:
    """Create TargetOracleOicConfig from dictionary."""
    return TargetOracleOicConfig.model_validate(config_dict)


def create_config_with_env_overrides(
    **overrides: t.JsonValue,
) -> TargetOracleOicConfig:
    """Create TargetOracleOicConfig with environment variable overrides."""
    return TargetOracleOicConfig.model_validate(overrides)


def create_singer_config_schema() -> Mapping[str, t.JsonValue]:
    """Create Singer configuration schema from TargetOracleOicConfig."""
    return TargetOracleOicConfig.model_json_schema()


__all__: list[str] = [
    "OICAuthConfig",
    "OICConnectionConfig",
    "OICDeploymentConfig",
    "OICEntityConfig",
    "OICOAuth2Authenticator",
    "OICProcessingConfig",
    "TargetOracleOicConfig",
    "create_config_from_dict",
    "create_config_with_env_overrides",
    "create_singer_config_schema",
]
