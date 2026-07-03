# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_oic.tests.unit.test_cli_entrypoint import (
        TestsFlextTargetOracleOicCliEntrypoint as TestsFlextTargetOracleOicCliEntrypoint,
    )
    from flext_target_oracle_oic.tests.unit.test_e2e import (
        TestsFlextTargetOracleOicE2e as TestsFlextTargetOracleOicE2e,
    )
    from flext_target_oracle_oic.tests.unit.test_e2e_sinks import (
        DummySingerTargetE2E as DummySingerTargetE2E,
        TestsFlextTargetOracleOicE2eSinks as TestsFlextTargetOracleOicE2eSinks,
    )
    from flext_target_oracle_oic.tests.unit.test_module_governance import (
        TestsFlextTargetOracleOicModuleGovernance as TestsFlextTargetOracleOicModuleGovernance,
    )
    from flext_target_oracle_oic.tests.unit.test_target import (
        AuthTestSettings as AuthTestSettings,
        DummySingerTarget as DummySingerTarget,
        TestsFlextTargetOracleOicTarget as TestsFlextTargetOracleOicTarget,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_cli_entrypoint": ("TestsFlextTargetOracleOicCliEntrypoint",),
        ".test_e2e": ("TestsFlextTargetOracleOicE2e",),
        ".test_e2e_sinks": (
            "DummySingerTargetE2E",
            "TestsFlextTargetOracleOicE2eSinks",
        ),
        ".test_module_governance": ("TestsFlextTargetOracleOicModuleGovernance",),
        ".test_target": (
            "AuthTestSettings",
            "DummySingerTarget",
            "TestsFlextTargetOracleOicTarget",
        ),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
