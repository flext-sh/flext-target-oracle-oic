# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_meltano import d, e, h, r, s, x
    from flext_target_oracle_oic.__version__ import (
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_target_oracle_oic._utilities.service_runtime import (
        FlextTargetOracleOicServiceRuntime,
    )
    from flext_target_oracle_oic.api import (
        FlextTargetOracleOicService,
        target_oracle_oic,
    )
    from flext_target_oracle_oic.cli import FlextTargetOracleOicCli, main
    from flext_target_oracle_oic.constants import FlextTargetOracleOicConstants, c
    from flext_target_oracle_oic.models import FlextTargetOracleOicModels, m
    from flext_target_oracle_oic.protocols import FlextTargetOracleOicProtocols, p
    from flext_target_oracle_oic.settings import FlextTargetOracleOicSettings
    from flext_target_oracle_oic.target import (
        FlextTargetOracleOic,
        FlextTargetOracleOicBaseSink,
        FlextTargetOracleOicConnectionsSink,
        FlextTargetOracleOicIntegrationsSink,
        FlextTargetOracleOicLookupsSink,
        FlextTargetOracleOicPackagesSink,
    )
    from flext_target_oracle_oic.typings import FlextTargetOracleOicTypes, t
    from flext_target_oracle_oic.utilities import FlextTargetOracleOicUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (
        "._utilities",
        ".application",
        ".connection",
        ".patterns",
        ".singer",
    ),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            "._utilities.service_runtime": ("FlextTargetOracleOicServiceRuntime",),
            ".api": (
                "FlextTargetOracleOicService",
                "target_oracle_oic",
            ),
            ".cli": (
                "FlextTargetOracleOicCli",
                "main",
            ),
            ".constants": (
                "FlextTargetOracleOicConstants",
                "c",
            ),
            ".models": (
                "FlextTargetOracleOicModels",
                "m",
            ),
            ".patterns.oic_patterns": (
            ),
            ".protocols": (
                "FlextTargetOracleOicProtocols",
                "p",
            ),
            ".settings": ("FlextTargetOracleOicSettings",),
            ".singer.processors": (
            ),
            ".target": (
                "FlextTargetOracleOic",
                "FlextTargetOracleOicBaseSink",
                "FlextTargetOracleOicConnectionsSink",
                "FlextTargetOracleOicIntegrationsSink",
                "FlextTargetOracleOicLookupsSink",
                "FlextTargetOracleOicPackagesSink",
            ),
            ".typings": (
                "FlextTargetOracleOicTypes",
                "t",
            ),
            ".utilities": (
                "FlextTargetOracleOicUtilities",
                "u",
            ),
            "flext_meltano": (
                "d",
                "e",
                "h",
                "r",
                "s",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "FlextTargetOracleOic",
    "FlextTargetOracleOicBaseSink",
    "FlextTargetOracleOicCli",
    "FlextTargetOracleOicConnectionsSink",
    "FlextTargetOracleOicConstants",
    "FlextTargetOracleOicIntegrationsSink",
    "FlextTargetOracleOicLookupsSink",
    "FlextTargetOracleOicModels",
    "FlextTargetOracleOicPackagesSink",
    "FlextTargetOracleOicProtocols",
    "FlextTargetOracleOicService",
    "FlextTargetOracleOicServiceRuntime",
    "FlextTargetOracleOicSettings",
    "FlextTargetOracleOicTypes",
    "FlextTargetOracleOicUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "target_oracle_oic",
    "u",
    "x",
]
