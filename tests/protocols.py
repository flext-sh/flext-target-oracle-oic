"""Test protocol definitions for flext-target-oracle-oic.

Provides TestsFlextTargetOracleOicProtocols, combining FlextTestsProtocols with
FlextTargetOracleOicProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_oic.protocols import FlextTargetOracleOicProtocols
from flext_tests import FlextTestsProtocols


class TestsFlextTargetOracleOicProtocols(
    FlextTestsProtocols,
    FlextTargetOracleOicProtocols,
):
    """Test protocols combining FlextTestsProtocols and FlextTargetOracleOicProtocols.

    Provides access to:
    - p.Tests.Docker.* (from FlextTestsProtocols)
    - p.Tests.Factory.* (from FlextTestsProtocols)
    - p.TargetOracleOic.* (from FlextTargetOracleOicProtocols)
    """

    class Tests(FlextTestsProtocols.Tests):
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with TargetOracleOic-specific protocols.
        """

        class TargetOracleOic:
            """TargetOracleOic-specific test protocols."""


# Runtime aliases
p = TestsFlextTargetOracleOicProtocols
p = TestsFlextTargetOracleOicProtocols

__all__ = ["TestsFlextTargetOracleOicProtocols", "p"]
