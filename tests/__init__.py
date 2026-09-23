# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_meltano import meltano
    from flext_oracle_oic import auth, oracle_oic, providers, web
    from flext_tests import (
        api,
        cli,
        config,
        core,
        d,
        e,
        h,
        install_local_packages,
        lazy_attribute,
        load_infra_report,
        r,
        services,
        settings,
        td,
        tf,
        tk,
        tm,
        tv,
        x,
    )

    from flext_target_oracle_oic import main, target_oracle_oic

    from . import unit
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
    "TestsFlextTargetOracleOicConstants",
    "TestsFlextTargetOracleOicModels",
    "TestsFlextTargetOracleOicProtocols",
    "TestsFlextTargetOracleOicServiceBase",
    "TestsFlextTargetOracleOicSettings",
    "TestsFlextTargetOracleOicTypes",
    "TestsFlextTargetOracleOicUtilities",
    "api",
    "auth",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "e",
    "h",
    "install_local_packages",
    "lazy_attribute",
    "load_infra_report",
    "m",
    "main",
    "meltano",
    "oracle_oic",
    "p",
    "providers",
    "r",
    "s",
    "services",
    "settings",
    "t",
    "target_oracle_oic",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "unit",
    "web",
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
            "flext_meltano": ("meltano",),
            "flext_oracle_oic": ("auth", "oracle_oic", "providers", "web"),
            "flext_target_oracle_oic": ("main", "target_oracle_oic"),
            "flext_tests": (
                "api",
                "cli",
                "config",
                "core",
                "d",
                "e",
                "h",
                "install_local_packages",
                "lazy_attribute",
                "load_infra_report",
                "r",
                "services",
                "settings",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
