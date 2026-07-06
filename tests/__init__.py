# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if TYPE_CHECKING:
    from flext_tests import d, e, h, r, td, tf, tk, tm, tv, x

    from tests.base import TestsFlextTargetOracleOicServiceBase, s
    from tests.constants import TestsFlextTargetOracleOicConstants, c
    from tests.models import TestsFlextTargetOracleOicModels, m
    from tests.protocols import TestsFlextTargetOracleOicProtocols, p
    from tests.settings import TestsFlextTargetOracleOicSettings
    from tests.typings import TestsFlextTargetOracleOicTypes, t
    from tests.unit.test_cli_entrypoint import TestsFlextTargetOracleOicCliEntrypoint
    from tests.unit.test_e2e import TestsFlextTargetOracleOicE2e
    from tests.unit.test_e2e_sinks import (
        DummySingerTargetE2E,
        TestsFlextTargetOracleOicE2eSinks,
    )
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
            ".base": (
                "TestsFlextTargetOracleOicServiceBase",
                "s",
            ),
            ".conftest": ("conftest",),
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
            ".settings": ("TestsFlextTargetOracleOicSettings",),
            ".typings": (
                "TestsFlextTargetOracleOicTypes",
                "t",
            ),
            ".unit": ("unit",),
            ".unit.test_cli_entrypoint": ("TestsFlextTargetOracleOicCliEntrypoint",),
            ".unit.test_e2e": ("TestsFlextTargetOracleOicE2e",),
            ".unit.test_e2e_sinks": (
                "DummySingerTargetE2E",
                "TestsFlextTargetOracleOicE2eSinks",
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
            "flext_tests": (
                "d",
                "e",
                "h",
                "r",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
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


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
