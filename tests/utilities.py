"""Module skeleton for FlextTargetOracleOicTestUtilities.

Test utilities for flext-target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_target_oracle_oic.utilities import FlextTargetOracleOicUtilities


class FlextTargetOracleOicTestUtilities(
    FlextTestsUtilities, FlextTargetOracleOicUtilities
):
    """Test utilities for flext-target-oracle-oic."""


u = FlextTargetOracleOicTestUtilities
__all__ = ["FlextTargetOracleOicTestUtilities", "u"]
