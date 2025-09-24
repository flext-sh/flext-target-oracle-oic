"""FLEXT Target Oracle OIC Constants - Oracle OIC target loading constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextConstants


class FlextTargetOracleOicConstants(FlextConstants):
    """Oracle OIC target loading-specific constants following flext-core patterns."""

    # Oracle OIC Connection Configuration
    DEFAULT_OIC_TIMEOUT = 30
    DEFAULT_MAX_RETRIES = 3

    # Singer Target Configuration
    DEFAULT_BATCH_SIZE = 1000
    MAX_BATCH_SIZE = 10000

    # OIC Load Methods
    LOAD_METHODS: ClassVar[list[str]] = ["BULK_INSERT", "INCREMENTAL", "UPSERT"]


__all__ = ["FlextTargetOracleOicConstants"]
