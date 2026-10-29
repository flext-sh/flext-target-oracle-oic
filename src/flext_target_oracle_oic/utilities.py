# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utilities facade for target Oracle OIC.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import u as flext_meltano_u
from flext_oracle_oic import u as flext_oracle_oic_u

from flext_target_oracle_oic._utilities import (
    FlextTargetOracleOicServiceRuntime,
    FlextTargetOracleOicSink,
)


class FlextTargetOracleOicUtilities(
    FlextTargetOracleOicServiceRuntime,
    FlextTargetOracleOicSink,
    flext_meltano_u,
    flext_oracle_oic_u,
):
    """Utilities composed from Meltano and Oracle OIC via MRO."""


u = FlextTargetOracleOicUtilities
__all__: list[str] = ["FlextTargetOracleOicUtilities", "u"]
