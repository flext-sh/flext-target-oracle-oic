# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

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
