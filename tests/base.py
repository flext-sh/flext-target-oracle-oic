"""Service base for flext-target-oracle-oic tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_target_oracle_oic import m
from tests.settings import TestsFlextTargetOracleOicSettings


class TestsFlextTargetOracleOicServiceBase(tests_s):
    """Target Oracle OIC test service base with source and test settings namespaces."""

    @classmethod
    @override
    def fetch_settings(cls) -> TestsFlextTargetOracleOicSettings:
        """Return the typed Target Oracle OIC+Tests settings singleton."""
        return TestsFlextTargetOracleOicSettings.fetch_global()

    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(
            settings_type=TestsFlextTargetOracleOicSettings
        )


s = TestsFlextTargetOracleOicServiceBase

__all__: list[str] = ["TestsFlextTargetOracleOicServiceBase", "s"]
