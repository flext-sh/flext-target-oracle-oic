"""Test protocol definitions for flext-target-oracle-oic.

Provides TestsFlextTargetOracleOicProtocols, combining p with
FlextTargetOracleOicProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import p

from flext_target_oracle_oic.protocols import FlextTargetOracleOicProtocols


class TestsFlextTargetOracleOicProtocols(p, FlextTargetOracleOicProtocols):
    """Test protocols combining p and FlextTargetOracleOicProtocols.

    Provides access to:
    - p.Tests.Docker.* (from p)
    - p.Tests.Factory.* (from p)
    - p.TargetOracleOic.* (from FlextTargetOracleOicProtocols)
    """

    class Tests(p.Tests):
        """Project-specific test protocols.

        Extends p.Tests with TargetOracleOic-specific protocols.
        """

        class TargetOracleOic:
            """TargetOracleOic-specific test protocols."""


__all__ = ["TestsFlextTargetOracleOicProtocols", "p"]

p = TestsFlextTargetOracleOicProtocols
