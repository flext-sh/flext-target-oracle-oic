# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_cli_entrypoint": ("TestsFlextTargetOracleOicCliEntrypoint",),
        ".test_e2e": (
            "DummySingerTargetE2E",
            "TestsFlextTargetOracleOicE2e",
        ),
        ".test_module_governance": ("TestsFlextTargetOracleOicModuleGovernance",),
        ".test_target": (
            "AuthTestSettings",
            "DummySingerTarget",
            "TestsFlextTargetOracleOicTarget",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
