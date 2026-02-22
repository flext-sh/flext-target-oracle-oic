"""Test protocol definitions for flext-target-oracle-oic.

Provides TestsFlextTargetOracleOicProtocols, combining FlextTestsProtocols with
FlextTargetOracleOicProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests.protocols import FlextTestsProtocols

from flext_target_oracle_oic.protocols import FlextTargetOracleOicProtocols


class TestsFlextTargetOracleOicProtocols(
    FlextTestsProtocols,
    FlextTargetOracleOicProtocols,
):
    """Test protocols combining FlextTestsProtocols and FlextTargetOracleOicProtocols.

    Provides access to:
    - tp.Tests.Docker.* (from FlextTestsProtocols)
    - tp.Tests.Factory.* (from FlextTestsProtocols)
    - tp.TargetOracleOic.* (from FlextTargetOracleOicProtocols)
    """

    class Tests(FlextTestsProtocols.Tests):
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with TargetOracleOic-specific protocols.
        """

        class TargetOracleOic:
            """TargetOracleOic-specific test protocols."""


# Runtime aliases
p = TestsFlextTargetOracleOicProtocols
tp = TestsFlextTargetOracleOicProtocols

__all__ = ["TestsFlextTargetOracleOicProtocols", "p", "tp"]
