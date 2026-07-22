"""Settings for flext-target-oracle-oic — namespaced under ``settings.TargetOracleOic``.

Universal fields via MRO; project fields in the ``TargetOracleOic`` group with
simple scalar types (env-settable). Secrets are plain strings so they can come
from env/params; consumers wrap them as needed.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field
from pydantic_settings import SettingsConfigDict

from flext_meltano import FlextMeltanoSettings


class FlextTargetOracleOicSettings(FlextMeltanoSettings):
    """Oracle OIC target settings; fields under ``settings.TargetOracleOic.*``."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_TARGET_ORACLE_OIC_", env_nested_delimiter="__", extra="ignore"
    )

    class _TargetOracleOic(BaseModel):
        """Namespaced Oracle OIC target settings."""

        oauth_client_id: Annotated[
            str, Field(default="", description="OAuth client identifier")
        ]
        oauth_client_secret: Annotated[
            str, Field(default="", description="OAuth client secret")
        ]
        oauth_token_url: Annotated[
            str, Field(default="", description="OAuth token endpoint URL")
        ]
        oauth_scope: Annotated[
            str | None,
            Field(
                default="oic_instance", description="OAuth scope used in token requests"
            ),
        ]
        oauth_client_aud: Annotated[
            str | None,
            Field(default=None, description="Optional audience used by OAuth provider"),
        ]
        timeout: Annotated[
            int, Field(default=30, ge=1, description="HTTP timeout in seconds")
        ]

    if TYPE_CHECKING:
        TargetOracleOic: _TargetOracleOic
    else:
        TargetOracleOic: _TargetOracleOic = Field(
            default_factory=_TargetOracleOic,
            description="Namespaced Oracle OIC target settings.",
        )


settings: FlextTargetOracleOicSettings = FlextTargetOracleOicSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_target_oracle_oic import settings``."""

__all__: list[str] = ["FlextTargetOracleOicSettings", "settings"]
