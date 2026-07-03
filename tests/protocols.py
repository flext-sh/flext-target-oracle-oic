"""Test protocol definitions for flext-target-oracle-oic.

Provides TestsFlextTargetOracleOicProtocols, combining TestsFlextProtocols with
FlextTargetOracleOicProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_target_oracle_oic import FlextTargetOracleOicProtocols


class TestsFlextTargetOracleOicProtocols(
    FlextTestsProtocols,
    FlextTargetOracleOicProtocols,
):
    """Test protocols combining TestsFlextProtocols and FlextTargetOracleOicProtocols.

    Provides access to:
    - p.Tests.Docker.* (from TestsFlextProtocols)
    - p.Tests.Factory.* (from TestsFlextProtocols)
    - p.FlextTargetOracleOic.* (from FlextTargetOracleOicProtocols)
    """

    class Tests(FlextTestsProtocols.Tests):
        """Project-specific test protocols.

        Extends TestsFlextProtocols.Tests with FlextTargetOracleOic-specific protocols.
        """

        class FlextTargetOracleOic:
            """FlextTargetOracleOic-specific test protocols."""


p = TestsFlextTargetOracleOicProtocols
__all__: list[str] = ["TestsFlextTargetOracleOicProtocols", "p"]
