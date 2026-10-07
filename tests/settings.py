"""Runtime settings for flext-target-oracle-oic tests.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/settings
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsSettings

from flext_target_oracle_oic import FlextTargetOracleOicSettings


class TestsFlextTargetOracleOicSettings(
    FlextTargetOracleOicSettings,
    FlextTestsSettings,
):
    """Target Oracle OIC settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextTargetOracleOicSettings"]
