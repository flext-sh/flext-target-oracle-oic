"""Settings for flext-target-oracle-oic — namespaced under ``settings.TargetOracleOic``.

Universal fields via MRO; project fields in the ``TargetOracleOic`` group with
simple scalar types (env-settable). OIC connection and OAuth credentials are
owned by ``settings.OracleOic`` (flext-oracle-oic) and never re-declared here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from flext_meltano import FlextMeltanoSettings, m


class FlextTargetOracleOicSettings(FlextMeltanoSettings):
    """Oracle OIC target settings; fields under ``settings.TargetOracleOic.*``."""

    model_config = m.SettingsConfigDict(
        env_prefix="FLEXT_TARGET_ORACLE_OIC_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    class _TargetOracleOic(m.BaseModel):
        """Namespaced Oracle OIC target settings."""

        timeout: Annotated[
            int,
            m.Field(default=30, ge=1, description="HTTP timeout in seconds"),
        ]

    # Why: mro-4p0t — nested namespace uses default_factory only; no build_* wrapper.

    if TYPE_CHECKING:
        TargetOracleOic: _TargetOracleOic
    else:
        TargetOracleOic: _TargetOracleOic = m.Field(
            default_factory=_TargetOracleOic,
            description="Namespaced Oracle OIC target settings.",
        )


settings: FlextTargetOracleOicSettings = FlextTargetOracleOicSettings.fetch_global()
"""Pre-instantiated project settings singleton.

Exposed as ``from flext_target_oracle_oic import settings``.
"""

__all__: list[str] = ["FlextTargetOracleOicSettings", "settings"]
