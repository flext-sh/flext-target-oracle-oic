# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_cli_entrypoint": ("test_cli_entrypoint",),
        ".test_e2e": (
            "DummySingerTarget",
            "TestTargetOracleOicE2E",
        ),
        ".test_module_governance": ("test_module_governance",),
        ".test_target": (
            "AuthTestSettings",
            "TestTargetOracleOic",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
