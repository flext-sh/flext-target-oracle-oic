"""Runtime settings for flext-target-oracle-oic tests."""

from __future__ import annotations

from flext_tests.settings import FlextTestsSettings

from flext_target_oracle_oic import FlextTargetOracleOicSettings


class TestsFlextTargetOracleOicSettings(
    FlextTargetOracleOicSettings,
    FlextTestsSettings,
):
    """Target Oracle OIC settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextTargetOracleOicSettings"]
