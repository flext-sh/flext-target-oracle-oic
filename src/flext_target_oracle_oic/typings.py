"""Project type aliases for target Oracle OIC."""

from __future__ import annotations

from flext_meltano import t
from flext_oracle_oic import t as _oracle_oic_t


class FlextTargetOracleOicTypes(t, _oracle_oic_t):
    """Type namespace for target Oracle OIC domain."""


t = FlextTargetOracleOicTypes
__all__: list[str] = ["FlextTargetOracleOicTypes", "t"]
