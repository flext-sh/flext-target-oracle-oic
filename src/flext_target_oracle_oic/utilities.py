"""Utilities for Oracle OIC Singer payload handling."""

from __future__ import annotations

from collections.abc import Mapping

from flext_api import FlextApi, FlextApiSettings
from flext_core import r
from flext_meltano import FlextMeltanoUtilities
from flext_oracle_oic import FlextOracleOicUtilities
from flext_target_oracle_oic import FlextTargetOracleOicSettings, c, m, t


class FlextTargetOracleOicUtilities(FlextMeltanoUtilities, FlextOracleOicUtilities):
    """Namespace for message-building and validation helpers."""

    class TargetOracleOic:
        """Singer message helper functions."""

        class Validation:
            """Runtime configuration validation helper functions."""

            @staticmethod
            def validate_config(config: t.ConfigurationMapping) -> r[bool]:
                """Validate required OIC target configuration keys."""
                required = {"base_url", "oauth_client_id", "oauth_client_secret"}
                missing = sorted(key for key in required if key not in config)
                if missing:
                    return r[bool].fail(f"Missing required config fields: {missing}")
                return r[bool].ok(value=True)

        class Factories:
            """Factory helpers for OIC model instances."""

            @staticmethod
            def create_oic_connection(
                data: t.FlatContainerMapping,
            ) -> m.TargetOracleOic.OICConnection:
                """Create an OICConnection model from generic payload via Pydantic validation."""
                return m.TargetOracleOic.OICConnection.model_validate({
                    **data,
                    "properties": data,
                })

            @staticmethod
            def create_oic_integration(
                data: t.FlatContainerMapping,
            ) -> m.TargetOracleOic.OICIntegration:
                """Create an OICIntegration model from generic payload via Pydantic validation."""
                return m.TargetOracleOic.OICIntegration.model_validate(data)

            @staticmethod
            def create_oic_package(
                data: t.FlatContainerMapping,
            ) -> m.TargetOracleOic.OICPackage:
                """Create an OICPackage model from generic payload via Pydantic validation."""
                return m.TargetOracleOic.OICPackage.model_validate(data)

            @staticmethod
            def create_oic_lookup(
                data: t.FlatContainerMapping,
            ) -> m.TargetOracleOic.OICLookup:
                """Create an OICLookup model from generic payload via Pydantic validation."""
                return m.TargetOracleOic.OICLookup.model_validate(data)

        class Authenticator:
            """OAuth2 Authenticator for Oracle Integration Cloud."""

            def __init__(self, config: FlextTargetOracleOicSettings) -> None:
                """Initialize the authenticator with target configuration."""
                self._config: FlextTargetOracleOicSettings = config
                self._access_token: str | None = None
                self._auth_scheme: str = c.TargetOracleOic.AUTH_SCHEME_BEARER

            @property
            def auth_headers(self) -> t.StrMapping:
                """Get the authentication headers block for requests."""
                token = self.get_access_token()
                return {"Authorization": f"{self._auth_scheme} {token}"}

            def build_token_request_data(self) -> t.StrMapping:
                """Build the payload for requesting an OAuth2 token."""
                payload: t.MutableStrMapping = {
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
                if self._access_token is not None and (not force_refresh):
                    return self._access_token
                try:
                    api_config = FlextApiSettings.model_validate({
                        "base_url": str(self._config.oauth_token_url),
                        "timeout": self._config.timeout,
                    })
                    response_result = FlextApi(api_config).post(
                        "",
                        data=self.build_token_request_data(),
                        headers=dict(self._config.get_oauth_headers()),
                    )
                    if response_result.failure:
                        msg = f"Failed to request OAuth2 token: {response_result.error}"
                        raise RuntimeError(msg)
                    response = response_result.value
                    if response.status_code >= c.API.HTTP_ERROR_STATUS_THRESHOLD:
                        msg = f"Failed to request OAuth2 token: HTTP {response.status_code}"
                        raise RuntimeError(msg)
                except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
                    msg = f"Failed to request OAuth2 token: {exc}"
                    raise RuntimeError(msg) from exc
                payload = response.body
                if not isinstance(payload, Mapping):
                    msg = "OAuth2 token response did not include a JSON object body"
                    raise TypeError(msg)
                payload_raw: t.ContainerValueMapping = {
                    str(key): value for key, value in payload.items()
                }
                access_token = payload_raw.get("access_token")
                if not isinstance(access_token, str) or not access_token:
                    msg = "OAuth2 token response did not include a valid access_token"
                    raise RuntimeError(msg)
                token_type = payload_raw.get("token_type")
                if isinstance(token_type, str) and token_type:
                    self._auth_scheme = token_type
                self._access_token = access_token
                return access_token

            @staticmethod
            def create_config_from_dict(
                config_dict: t.ConfigurationMapping,
            ) -> FlextTargetOracleOicSettings:
                """Create FlextTargetOracleOicSettings from dictionary."""
                return FlextTargetOracleOicSettings.model_validate(config_dict)

            @staticmethod
            def create_config_with_env_overrides(
                **overrides: t.Scalar,
            ) -> FlextTargetOracleOicSettings:
                """Create FlextTargetOracleOicSettings with environment variable overrides."""
                return FlextTargetOracleOicSettings.model_validate(overrides)

            @staticmethod
            def create_singer_config_schema() -> t.FlatContainerMapping:
                """Create Singer configuration schema from FlextTargetOracleOicSettings."""
                return FlextTargetOracleOicSettings.model_json_schema()


u = FlextTargetOracleOicUtilities
__all__ = [
    "FlextTargetOracleOicUtilities",
    "u",
]
