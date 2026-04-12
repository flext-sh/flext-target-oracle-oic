"""Module skeleton for TestsFlextTargetOracleOicConstants.

Test constants for flext-target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_target_oracle_oic import FlextTargetOracleOicConstants


class TestsFlextTargetOracleOicConstants(
    FlextTestsConstants, FlextTargetOracleOicConstants
):
    """Test constants for flext-target-oracle-oic."""


c = TestsFlextTargetOracleOicConstants
__all__: list[str] = ["TestsFlextTargetOracleOicConstants", "c"]
