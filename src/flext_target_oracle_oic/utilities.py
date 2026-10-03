"""Utilities facade for target Oracle OIC."""

from __future__ import annotations

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_oic import FlextOracleOicUtilities


class FlextTargetOracleOicUtilities(FlextMeltanoUtilities, FlextOracleOicUtilities):
    """Utilities composed from Meltano and Oracle OIC via MRO."""


u = FlextTargetOracleOicUtilities
__all__: list[str] = ["FlextTargetOracleOicUtilities", "u"]
