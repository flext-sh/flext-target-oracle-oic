# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

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
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
