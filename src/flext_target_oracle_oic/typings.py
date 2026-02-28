"""Project type aliases for target Oracle OIC."""

from __future__ import annotations

from flext_core import FlextTypes
from flext_meltano import FlextMeltanoTypes
from flext_oracle_oic import FlextOracleOicTypes


class FlextTargetOracleOicTypes(FlextMeltanoTypes, FlextOracleOicTypes):
    """Type namespace for target Oracle OIC domain."""


t = FlextTargetOracleOicTypes

__all__ = ["FlextTargetOracleOicTypes", "t"]
