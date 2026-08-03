"""Module skeleton for TestsFlextTargetOracleOicUtilities.

Test utilities for flext-target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_oic import FlextTargetOracleOicUtilities
from flext_tests import FlextTestsUtilities


class TestsFlextTargetOracleOicUtilities(
    FlextTestsUtilities, FlextTargetOracleOicUtilities
):
    """Test utilities for flext-target-oracle-oic."""


u = TestsFlextTargetOracleOicUtilities
__all__: list[str] = ["TestsFlextTargetOracleOicUtilities", "u"]
