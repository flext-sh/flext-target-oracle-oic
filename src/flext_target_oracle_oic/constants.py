"""Constants for target Oracle OIC."""

from __future__ import annotations

from flext_meltano import FlextMeltanoConstants
from flext_oracle_oic import FlextOracleOicConstants


class FlextTargetOracleOicConstants(FlextMeltanoConstants, FlextOracleOicConstants):
    """Namespace class for OIC target constants."""


c = FlextTargetOracleOicConstants

__all__ = ["FlextTargetOracleOicConstants", "c"]
