"""FLEXT Target Oracle OIC base constants — OIC target domain constants.

All constants are flat with descriptive prefixes to explain their usage.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar


class FlextTargetOracleOicConstantsBase:
    """Base Oracle OIC target constants: target name."""

    TARGET_NAME: ClassVar[str] = "target-oracle-oic"


__all__: list[str] = ["FlextTargetOracleOicConstantsBase"]
