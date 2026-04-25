# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_tests import td, tf, tk, tm, tv

    from flext_target_oracle_oic import d, e, h, r, s, x
    from tests.constants import TestsFlextTargetOracleOicConstants, c
    from tests.models import TestsFlextTargetOracleOicModels, m
    from tests.protocols import TestsFlextTargetOracleOicProtocols, p
    from tests.typings import TestsFlextTargetOracleOicTypes, t
    from tests.unit.test_cli_entrypoint import TestsFlextTargetOracleOicCliEntrypoint
    from tests.unit.test_e2e import DummySingerTargetE2E, TestsFlextTargetOracleOicE2e
    from tests.unit.test_module_governance import (
        TestsFlextTargetOracleOicModuleGovernance,
    )
    from tests.unit.test_target import (
        AuthTestSettings,
        DummySingerTarget,
        TestsFlextTargetOracleOicTarget,
    )
    from tests.utilities import TestsFlextTargetOracleOicUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".constants": (
                "TestsFlextTargetOracleOicConstants",
                "c",
            ),
            ".models": (
                "TestsFlextTargetOracleOicModels",
                "m",
            ),
            ".protocols": (
                "TestsFlextTargetOracleOicProtocols",
                "p",
            ),
            ".typings": (
                "TestsFlextTargetOracleOicTypes",
                "t",
            ),
            ".unit.test_cli_entrypoint": ("TestsFlextTargetOracleOicCliEntrypoint",),
            ".unit.test_e2e": (
                "DummySingerTargetE2E",
                "TestsFlextTargetOracleOicE2e",
            ),
            ".unit.test_module_governance": (
                "TestsFlextTargetOracleOicModuleGovernance",
            ),
            ".unit.test_target": (
                "AuthTestSettings",
                "DummySingerTarget",
                "TestsFlextTargetOracleOicTarget",
            ),
            ".utilities": (
                "TestsFlextTargetOracleOicUtilities",
                "u",
            ),
            "flext_target_oracle_oic": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "AuthTestSettings",
    "DummySingerTarget",
    "DummySingerTargetE2E",
    "TestsFlextTargetOracleOicCliEntrypoint",
    "TestsFlextTargetOracleOicConstants",
    "TestsFlextTargetOracleOicE2e",
    "TestsFlextTargetOracleOicModels",
    "TestsFlextTargetOracleOicModuleGovernance",
    "TestsFlextTargetOracleOicProtocols",
    "TestsFlextTargetOracleOicTarget",
    "TestsFlextTargetOracleOicTypes",
    "TestsFlextTargetOracleOicUtilities",
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
]
