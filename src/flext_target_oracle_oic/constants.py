"""Constants for target Oracle OIC.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_meltano import FlextMeltanoConstants
from flext_oracle_oic import FlextOracleOicConstants

from flext_target_oracle_oic._constants.base import FlextTargetOracleOicConstantsBase

if TYPE_CHECKING:
    from flext_target_oracle_oic import t


class FlextTargetOracleOicConstants(FlextMeltanoConstants, FlextOracleOicConstants):
    """Namespace class for OIC target constants."""

    class TargetOracleOic(FlextTargetOracleOicConstantsBase):
        """Target Oracle OIC domain constants."""


c = FlextTargetOracleOicConstants
__all__: t.StrSequence = ("FlextTargetOracleOicConstants", "c")
