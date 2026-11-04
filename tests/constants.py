"""Module skeleton for TestsFlextTargetOracleOicConstants.

Test constants for flext-target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import ClassVar

from flext_target_oracle_oic import FlextTargetOracleOicConstants, t
from flext_tests import FlextTestsConstants


class TestsFlextTargetOracleOicConstants(
    FlextTestsConstants,
    FlextTargetOracleOicConstants,
):
    """Test constants for flext-target-oracle-oic."""

    class TargetOracleOic(FlextTargetOracleOicConstants.TargetOracleOic):
        """Target Oracle OIC-specific test constants namespace."""

        class Tests(FlextTestsConstants.Tests):
            """Target Oracle OIC-specific test constants."""

            PROJECT_ROOT_PARENT_DEPTH: ClassVar[int] = 1
            ALLOWED_MODULE_FUNCTIONS: ClassVar[t.MappingKV[str, frozenset[str]]] = (
                MappingProxyType({"cli.py": frozenset({"main"})})
            )
            DEFAULT_PROPERTIES: ClassVar[Mapping[str, Mapping[str, str]]] = (
                MappingProxyType({"id": MappingProxyType({"type": "string"})})
            )
            STREAM_NAMES: ClassVar[tuple[str, ...]] = (
                "connections",
                "integrations",
                "packages",
                "lookups",
            )


c = TestsFlextTargetOracleOicConstants
__all__: list[str] = ["TestsFlextTargetOracleOicConstants", "c"]
