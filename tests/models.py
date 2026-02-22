"""Test models for flext-target-oracle-oic tests.

Provides TestsFlextTargetOracleOicModels, extending FlextTestsModels with
flext-target-oracle-oic-specific models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests.models import FlextTestsModels

from flext_target_oracle_oic.models import FlextTargetOracleOicModels


class TestsFlextTargetOracleOicModels(FlextTestsModels, FlextTargetOracleOicModels):
    """Models for flext-target-oracle-oic tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. FlextTestsModels - for test infrastructure (.Tests.*)
    2. FlextTargetOracleOicModels - for domain models

    Access patterns:
    - tm.Tests.* (generic test models from FlextTestsModels)
    - tm.* (Target Oracle OIC domain models)
    - m.* (production models via alternative alias)
    """

    class Tests:
        """Project-specific test fixtures namespace."""

        class TargetOracleOic:
            """Target Oracle OIC-specific test fixtures."""


# Short aliases per FLEXT convention
tm = TestsFlextTargetOracleOicModels
m = TestsFlextTargetOracleOicModels

__all__ = [
    "TestsFlextTargetOracleOicModels",
    "m",
    "tm",
]
