# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Oic package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import (
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__ as __version__,
    __version_info__ as __version_info__,
)

if TYPE_CHECKING:
<<<<<<< HEAD
    from flext_meltano import (
        cli,
        core,
        d,
        e,
        h,
        lazy_attribute,
        meltano,
        r,
        s,
        services,
        x,
    )
    from flext_oracle_oic import api, auth, oracle_oic, providers, web
=======
    from flext_api import api
    from flext_auth import auth
    from flext_cli import cli
    from flext_meltano import meltano, s
    from flext_oracle_oic import oracle_oic
    from flext_web import web

    from flext_core import core, d, e, h, lazy_attribute, r, x
>>>>>>> origin/chore/regen-20260923

    from ._config import FlextTargetOracleOicConfig, config
    from ._settings import FlextTargetOracleOicSettings, settings
    from .api import FlextTargetOracleOicService, target_oracle_oic
    from .cli import FlextTargetOracleOicCli, main
    from .constants import FlextTargetOracleOicConstants, c
    from .models import FlextTargetOracleOicModels, m
    from .protocols import FlextTargetOracleOicProtocols, p
    from .target import (
        FlextTargetOracleOic,
        FlextTargetOracleOicBaseSink,
        FlextTargetOracleOicConnectionsSink,
        FlextTargetOracleOicIntegrationsSink,
        FlextTargetOracleOicLookupsSink,
        FlextTargetOracleOicPackagesSink,
    )
    from .typings import FlextTargetOracleOicTypes, t
    from .utilities import FlextTargetOracleOicUtilities, u


__all__: tuple[str, ...] = (
    "FlextTargetOracleOic",
    "FlextTargetOracleOicBaseSink",
    "FlextTargetOracleOicCli",
    "FlextTargetOracleOicConfig",
    "FlextTargetOracleOicConnectionsSink",
    "FlextTargetOracleOicConstants",
    "FlextTargetOracleOicIntegrationsSink",
    "FlextTargetOracleOicLookupsSink",
    "FlextTargetOracleOicModels",
    "FlextTargetOracleOicPackagesSink",
    "FlextTargetOracleOicProtocols",
    "FlextTargetOracleOicService",
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
    "api",
    "auth",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "e",
    "h",
    "lazy_attribute",
    "m",
    "main",
    "meltano",
    "oracle_oic",
    "p",
    "providers",
    "r",
    "s",
    "settings",
    "t",
    "target_oracle_oic",
    "u",
    "web",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config": ("FlextTargetOracleOicConfig", "config"),
            "._settings": ("FlextTargetOracleOicSettings", "settings"),
            ".api": ("FlextTargetOracleOicService", "target_oracle_oic"),
            ".cli": ("FlextTargetOracleOicCli", "main"),
            ".constants": ("FlextTargetOracleOicConstants", "c"),
            ".models": ("FlextTargetOracleOicModels", "m"),
            ".protocols": ("FlextTargetOracleOicProtocols", "p"),
            ".target": (
                "FlextTargetOracleOic",
                "FlextTargetOracleOicBaseSink",
                "FlextTargetOracleOicConnectionsSink",
                "FlextTargetOracleOicIntegrationsSink",
                "FlextTargetOracleOicLookupsSink",
                "FlextTargetOracleOicPackagesSink",
            ),
            ".typings": ("FlextTargetOracleOicTypes", "t"),
            ".utilities": ("FlextTargetOracleOicUtilities", "u"),
<<<<<<< HEAD
            "flext_meltano": (
                "cli",
                "core",
                "d",
                "e",
                "h",
                "lazy_attribute",
                "meltano",
                "r",
                "s",
                "services",
                "x",
            ),
            "flext_oracle_oic": ("api", "auth", "oracle_oic", "providers", "web"),
=======
            "flext_api": ("api",),
            "flext_auth": ("auth",),
            "flext_cli": ("cli",),
            "flext_core": ("core", "d", "e", "h", "lazy_attribute", "r", "x"),
            "flext_meltano": ("meltano", "s"),
            "flext_oracle_oic": ("oracle_oic",),
            "flext_web": ("web",),
>>>>>>> origin/chore/regen-20260923
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
