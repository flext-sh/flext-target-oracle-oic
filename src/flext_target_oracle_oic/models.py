# AUTO-GENERATED FILE — Regenerate with: make gen
"""Domain models for target Oracle OIC.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import m
from flext_oracle_oic import m as flext_oracle_oic_m

from flext_target_oracle_oic._models import FlextTargetOracleOicModelsConfig


class FlextTargetOracleOicModels(
    FlextTargetOracleOicModelsConfig, m, flext_oracle_oic_m
):
    """Models composed from Meltano and Oracle OIC via MRO."""


m = FlextTargetOracleOicModels
__all__: list[str] = ["FlextTargetOracleOicModels", "m"]
