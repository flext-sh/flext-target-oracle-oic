"""Pure config namespace declarations for flext-target-oracle-oic.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import m


class FlextTargetOracleOicModelsConfig:
    """Field-only Pydantic declarations for the TargetOracleOic config singleton."""

    class TargetOracleOicNamespace(m.BaseModel):
        """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

        model_config = m.ConfigDict(extra="allow", frozen=True)


__all__: tuple[str, ...] = ("FlextTargetOracleOicModelsConfig",)
