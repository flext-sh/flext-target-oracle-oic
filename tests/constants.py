"""Module skeleton for TestsFlextTargetOracleOicConstants.

Test constants for flext-target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

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

            PROJECT_ROOT_PARENT_DEPTH: ClassVar[int] = 1
            SRC_DIR: ClassVar[str] = "src"
            PACKAGE_DIR: ClassVar[str] = "flext_target_oracle_oic"
            OAUTH_ENDPOINT_URL: ClassVar[str] = (
                "https://idcs.example.com/oauth2/v1/token"
            )
            ALLOWED_MODULE_FUNCTIONS: ClassVar[dict[str, frozenset[str]]] = {
                "cli.py": frozenset({"main"})
            }
            DEFAULT_PROPERTIES: ClassVar[dict[str, dict[str, str]]] = {
                "id": {"type": "string"}
            }


c = TestsFlextTargetOracleOicConstants
__all__: list[str] = ["TestsFlextTargetOracleOicConstants", "c"]
