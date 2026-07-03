"""Module skeleton for TestsFlextTargetOracleOicConstants.

Test constants for flext-target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_tests import FlextTestsConstants

from flext_target_oracle_oic import FlextTargetOracleOicConstants


class TestsFlextTargetOracleOicConstants(
    FlextTestsConstants, FlextTargetOracleOicConstants
):
    """Test constants for flext-target-oracle-oic."""

    class TargetOracleOic(FlextTargetOracleOicConstants.TargetOracleOic):
        """Target Oracle OIC domain test constants namespace."""

        class Tests(FlextTestsConstants.Tests):
            """Target Oracle OIC-specific test constants."""

            PROJECT_ROOT_PARENT_DEPTH: Final[int] = 1
            SRC_DIR: Final[str] = "src"
            PACKAGE_DIR: Final[str] = "flext_target_oracle_oic"
            ALLOWED_MODULE_FUNCTIONS: Final[dict[str, frozenset[str]]] = {
                "cli.py": frozenset({"main"}),
            }
            DEFAULT_PROPERTIES: Final[dict[str, dict[str, str]]] = {
                "id": {"type": "string"},
            }


c = TestsFlextTargetOracleOicConstants
__all__: list[str] = ["TestsFlextTargetOracleOicConstants", "c"]
