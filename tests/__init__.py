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
    from tests.unit.test_e2e import DummySingerTarget, TestTargetOracleOicE2E
    from tests.unit.test_target import AuthTestSettings, TestTargetOracleOic
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
            ".unit.test_e2e": (
                "DummySingerTarget",
                "TestTargetOracleOicE2E",
            ),
            ".unit.test_target": (
                "AuthTestSettings",
                "TestTargetOracleOic",
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
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "AuthTestSettings",
    "DummySingerTarget",
    "TestTargetOracleOic",
    "TestTargetOracleOicE2E",
    "TestsFlextTargetOracleOicConstants",
    "TestsFlextTargetOracleOicModels",
    "TestsFlextTargetOracleOicProtocols",
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
