# AUTO-GENERATED FILE — Regenerate with: make gen
"""Constants for target Oracle OIC.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import c as flext_meltano_c
from flext_oracle_oic import c as flext_oracle_oic_c

from flext_target_oracle_oic._constants import FlextTargetOracleOicConstantsBase


class FlextTargetOracleOicConstants(flext_meltano_c, flext_oracle_oic_c):
    """Namespace class for OIC target constants."""

    class TargetOracleOic(FlextTargetOracleOicConstantsBase):
        """Target Oracle OIC domain constants."""


c = FlextTargetOracleOicConstants
__all__: list[str] = ["FlextTargetOracleOicConstants", "c"]
