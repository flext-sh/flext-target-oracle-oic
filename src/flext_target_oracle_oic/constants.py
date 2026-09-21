"""Constants for target Oracle OIC."""

from __future__ import annotations

from flext_meltano import c
from flext_oracle_oic import c as _oracle_oic_c, t

from ._constants.base import FlextTargetOracleOicConstantsBase


class FlextTargetOracleOicConstants(c, _oracle_oic_c):
    """Namespace class for OIC target constants."""

    class TargetOracleOic(FlextTargetOracleOicConstantsBase):
        """Target Oracle OIC domain constants."""


c = FlextTargetOracleOicConstants
__all__: t.StrSequence = ("FlextTargetOracleOicConstants", "c")
