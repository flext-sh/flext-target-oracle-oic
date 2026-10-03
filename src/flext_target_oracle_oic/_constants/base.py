"""FLEXT Target Oracle OIC base constants — OIC target domain constants.

All constants are flat with descriptive prefixes to explain their usage.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextTargetOracleOicConstantsBase:
    """Base Oracle OIC target constants: target name and stream names."""

    STREAM_CONNECTIONS: Final[str] = "connections"
    STREAM_INTEGRATIONS: Final[str] = "integrations"
    STREAM_PACKAGES: Final[str] = "packages"
    STREAM_LOOKUPS: Final[str] = "lookups"
    TARGET_NAME: Final[str] = "target-oracle-oic"
