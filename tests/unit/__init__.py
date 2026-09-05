# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests.unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import c, d, e, h, m, p, r, s, t, td, tf, tk, tm, tv, u, x

    from .test_cli_entrypoint import TestsFlextTargetOracleOicCliEntrypoint
    from .test_e2e import TestsFlextTargetOracleOicE2e, load_test_config, target
    from .test_e2e_sinks import (
        DummySingerTargetE2E,
        TestsFlextTargetOracleOicE2eSinks,
        singer_target,
    )
    from .test_module_governance import TestsFlextTargetOracleOicModuleGovernance
    from .test_target import (
        AuthTestSettings,
        DummySingerTarget,
        TestsFlextTargetOracleOicTarget,
    )
__all__: tuple[str, ...] = (
    "AuthTestSettings",
    "DummySingerTarget",
    "DummySingerTargetE2E",
    "TestsFlextTargetOracleOicCliEntrypoint",
    "TestsFlextTargetOracleOicE2e",
    "TestsFlextTargetOracleOicE2eSinks",
    "TestsFlextTargetOracleOicModuleGovernance",
    "TestsFlextTargetOracleOicTarget",
    "c",
    "d",
    "e",
    "h",
    "load_test_config",
    "m",
    "p",
    "r",
    "s",
    "singer_target",
    "t",
    "target",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".test_cli_entrypoint": ("TestsFlextTargetOracleOicCliEntrypoint",),
            ".test_e2e": ("TestsFlextTargetOracleOicE2e", "load_test_config", "target"),
            ".test_e2e_sinks": (
                "DummySingerTargetE2E",
                "TestsFlextTargetOracleOicE2eSinks",
                "singer_target",
            ),
            ".test_module_governance": ("TestsFlextTargetOracleOicModuleGovernance",),
            ".test_target": (
                "AuthTestSettings",
                "DummySingerTarget",
                "TestsFlextTargetOracleOicTarget",
            ),
            "flext_tests": (
                "c",
                "d",
                "e",
                "h",
                "m",
                "p",
                "r",
                "s",
                "t",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "u",
                "x",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
