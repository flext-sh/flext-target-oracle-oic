"""Test protocol definitions for flext-target-oracle-oic.

Provides FlextTargetOracleOicTestProtocols, combining FlextTestsProtocols with
FlextTargetOracleOicProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_target_oracle_oic import FlextTargetOracleOicProtocols


class FlextTargetOracleOicTestProtocols(
    FlextTestsProtocols,
    FlextTargetOracleOicProtocols,
):
    """Test protocols combining FlextTestsProtocols and FlextTargetOracleOicProtocols.

    Provides access to:
    - p.Tests.Docker.* (from FlextTestsProtocols)
    - p.Tests.Factory.* (from FlextTestsProtocols)
    - p.FlextTargetOracleOic.* (from FlextTargetOracleOicProtocols)
    """

    class Tests(FlextTestsProtocols.Tests):
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with FlextTargetOracleOic-specific protocols.
        """

        class FlextTargetOracleOic:
            """FlextTargetOracleOic-specific test protocols."""


p = FlextTargetOracleOicTestProtocols
__all__ = ["FlextTargetOracleOicTestProtocols", "p"]
