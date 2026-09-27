"""Constants for target Oracle OIC."""

from __future__ import annotations

from flext_meltano import FlextMeltanoConstants
from flext_oracle_oic import FlextOracleOicConstants, t

from ._constants.base import FlextTargetOracleOicConstantsBase


class FlextTargetOracleOicConstants(FlextMeltanoConstants, FlextOracleOicConstants):
    """Namespace class for OIC target constants."""

    class TargetOracleOic(FlextTargetOracleOicConstantsBase):
        """Target Oracle OIC domain constants."""


c = FlextTargetOracleOicConstants
__all__: t.StrSequence = ("FlextTargetOracleOicConstants", "c")
