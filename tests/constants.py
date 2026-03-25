"""Module skeleton for FlextTargetOracleOicTestConstants.

Test constants for flext-target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_target_oracle_oic import FlextTargetOracleOicConstants


class FlextTargetOracleOicTestConstants(
    FlextTestsConstants, FlextTargetOracleOicConstants
):
    """Test constants for flext-target-oracle-oic."""


c = FlextTargetOracleOicTestConstants
__all__ = ["FlextTargetOracleOicTestConstants", "c"]
