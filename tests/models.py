"""Test models for flext-target-oracle-oic tests.

Provides TestsFlextTargetOracleOicModels, extending TestsFlextModels with
flext-target-oracle-oic-specific models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_oic import FlextTargetOracleOicModels
from flext_tests import FlextTestsModels


class TestsFlextTargetOracleOicModels(FlextTestsModels, FlextTargetOracleOicModels):
    """Models for flext-target-oracle-oic tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. TestsFlextModels - for test infrastructure (.Tests.*)
    2. FlextTargetOracleOicModels - for domain models

    Access patterns:
    - m.Tests.* (generic test models from TestsFlextModels)
    - m.* (Target Oracle OIC domain models via shared MRO)
    """

    class Tests(FlextTestsModels.Tests):
        """Project-specific test fixtures namespace."""

        class FlextTargetOracleOic:
            """Target Oracle OIC-specific test fixtures."""


m = TestsFlextTargetOracleOicModels

__all__: list[str] = ["TestsFlextTargetOracleOicModels", "m"]
