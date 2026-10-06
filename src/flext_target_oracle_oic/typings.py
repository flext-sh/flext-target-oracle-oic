"""Project type aliases for target Oracle OIC.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_oic/typings
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoTypes
from flext_oracle_oic import FlextOracleOicTypes


class FlextTargetOracleOicTypes(FlextMeltanoTypes, FlextOracleOicTypes):
    """Type namespace for target Oracle OIC domain."""


t = FlextTargetOracleOicTypes
__all__: list[str] = ["FlextTargetOracleOicTypes", "t"]
