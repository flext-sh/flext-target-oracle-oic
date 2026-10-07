"""Domain models for target Oracle OIC.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_oic/models
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoModels
from flext_oracle_oic import FlextOracleOicModels


class FlextTargetOracleOicModels(FlextMeltanoModels, FlextOracleOicModels):
    """Models composed from Meltano and Oracle OIC via MRO."""


m = FlextTargetOracleOicModels

__all__: list[str] = ["FlextTargetOracleOicModels", "m"]
