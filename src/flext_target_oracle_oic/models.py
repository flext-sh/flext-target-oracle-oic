"""Domain models for target Oracle OIC."""

from __future__ import annotations

from flext_meltano import FlextMeltanoModels
from flext_oracle_oic import FlextOracleOicModels


class FlextTargetOracleOicModels(FlextMeltanoModels, FlextOracleOicModels):
    """Models composed from Meltano and Oracle OIC via MRO."""


m = FlextTargetOracleOicModels

__all__: list[str] = ["FlextTargetOracleOicModels", "m"]
