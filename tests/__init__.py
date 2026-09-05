# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from . import unit as unit
    from flext_target_oracle_oic import FlextTargetOracleOicConstants
    from flext_tests import FlextTestsConstants, d, e, h, r, td, tf, tk, tm, tv, x
    from typing import Final

    from .base import (
        TestsFlextTargetOracleOicServiceBase,
        TestsFlextTargetOracleOicServiceBase as s,
    )
    from .constants import (
        TestsFlextTargetOracleOicConstants,
        TestsFlextTargetOracleOicConstants as c,
    )
    from .models import (
        TestsFlextTargetOracleOicModels,
        TestsFlextTargetOracleOicModels as m,
    )
    from .protocols import (
        TestsFlextTargetOracleOicProtocols,
        TestsFlextTargetOracleOicProtocols as p,
    )
    from .settings import TestsFlextTargetOracleOicSettings
    from .typings import (
        TestsFlextTargetOracleOicTypes,
        TestsFlextTargetOracleOicTypes as t,
    )
    from .utilities import (
        TestsFlextTargetOracleOicUtilities,
        TestsFlextTargetOracleOicUtilities as u,
    )
__all__: tuple[str, ...] = (
    "Final",
    "FlextTargetOracleOicConstants",
    "FlextTestsConstants",
    "TestsFlextTargetOracleOicConstants",
    "TestsFlextTargetOracleOicModels",
    "TestsFlextTargetOracleOicProtocols",
    "TestsFlextTargetOracleOicServiceBase",
    "TestsFlextTargetOracleOicSettings",
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
    "unit",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextTargetOracleOicServiceBase", "s"),
            ".constants": ("TestsFlextTargetOracleOicConstants", "c"),
            ".models": ("TestsFlextTargetOracleOicModels", "m"),
            ".protocols": ("TestsFlextTargetOracleOicProtocols", "p"),
            ".settings": ("TestsFlextTargetOracleOicSettings",),
            ".typings": ("TestsFlextTargetOracleOicTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextTargetOracleOicUtilities", "u"),
            "flext_target_oracle_oic": ("FlextTargetOracleOicConstants",),
            "flext_tests": (
                "FlextTestsConstants",
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
            "typing": ("Final",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
