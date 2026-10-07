"""Utilities facade for target Oracle OIC.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_oic/utilities
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_oic import FlextOracleOicUtilities


class FlextTargetOracleOicUtilities(FlextMeltanoUtilities, FlextOracleOicUtilities):
    """Utilities composed from Meltano and Oracle OIC via MRO."""


u = FlextTargetOracleOicUtilities
__all__: list[str] = ["FlextTargetOracleOicUtilities", "u"]
