"""Module skeleton for TestsFlextTargetOracleOicUtilities.

Test utilities for flext-target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_target_oracle_oic import FlextTargetOracleOicUtilities


class TestsFlextTargetOracleOicUtilities(
    FlextTestsUtilities,
    FlextTargetOracleOicUtilities,
):
    """Test utilities for flext-target-oracle-oic."""


u = TestsFlextTargetOracleOicUtilities
__all__ = ["TestsFlextTargetOracleOicUtilities", "u"]
