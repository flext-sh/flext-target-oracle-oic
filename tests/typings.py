"""Module skeleton for FlextTargetOracleOicTestTypes.

Test type aliases for flext-target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_target_oracle_oic import FlextTargetOracleOicTypes


class FlextTargetOracleOicTestTypes(FlextTestsTypes, FlextTargetOracleOicTypes):
    """Test type aliases for flext-target-oracle-oic."""


t = FlextTargetOracleOicTestTypes
__all__ = ["FlextTargetOracleOicTestTypes", "t"]
