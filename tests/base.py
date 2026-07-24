"""Service base for flext-target-oracle-oic tests."""

from __future__ import annotations

from typing import override

from flext_tests import s

from flext_target_oracle_oic import m, p
from tests.settings import TestsFlextTargetOracleOicSettings


class TestsFlextTargetOracleOicServiceBase(s):
    """Target Oracle OIC test service base with source and test settings namespaces."""

    # NOTE (multi-agent): flext-tests owns fetch_settings; this project
    # declares only its more-specific bootstrap settings type.
    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> p.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(
            settings_type=TestsFlextTargetOracleOicSettings
        )


s = TestsFlextTargetOracleOicServiceBase

__all__: list[str] = ["TestsFlextTargetOracleOicServiceBase", "s"]
