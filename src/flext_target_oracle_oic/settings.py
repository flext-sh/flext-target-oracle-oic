"""Configuration for target-oracle-oic using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_core import FlextSettings

from flext_target_oracle_oic import c, m, t, u


@FlextSettings.auto_register("target-oracle-oic")
class FlextTargetOracleOicSettings(FlextSettings):
    """Runtime settings for Oracle OIC target authentication and IO."""

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_TARGET_ORACLE_OIC_", extra="ignore"
    )

    oauth_client_id: Annotated[str, u.Field(..., description="OAuth client identifier")]
    oauth_client_secret: Annotated[
        t.SecretStr,
        u.Field(..., description="OAuth client secret"),
    ]
    oauth_token_url: Annotated[
        str, u.Field(..., description="OAuth token endpoint URL")
    ]
    oauth_scope: Annotated[
        str | None,
        u.Field(
            description="OAuth scope used in token requests",
        ),
    ] = c.TargetOracleOic.DEFAULT_OAUTH_SCOPE
    oauth_client_aud: Annotated[
        str | None,
        u.Field(
            description="Optional audience used by OAuth provider",
        ),
    ] = None
    timeout: Annotated[
        int,
        u.Field(
            ge=1,
            description="HTTP timeout in seconds",
        ),
    ] = c.DEFAULT_TIMEOUT_SECONDS

    def get_oauth_client_secret_value(self) -> str:
        """Return the plaintext secret value for outgoing requests."""
        return self.oauth_client_secret.get_secret_value()

    def get_oauth_headers(self) -> t.StrMapping:
        """Return static HTTP headers required for token requests."""
        return {
            c.TargetOracleOic.HEADER_CONTENT_TYPE: c.TargetOracleOic.HEADER_CONTENT_TYPE_FORM,
            c.TargetOracleOic.HEADER_ACCEPT: c.TargetOracleOic.HEADER_CONTENT_TYPE_JSON,
        }


__all__: list[str] = ["FlextTargetOracleOicSettings"]
