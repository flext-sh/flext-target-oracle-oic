# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Oic package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_meltano import (
        build_lazy_import_map,
        cleanup_submodule_namespace,
        cli,
        core,
        d,
        e,
        h,
        install_lazy_exports,
        lazy,
        lazy_getattr,
        lazy_member,
        meltano,
        merge_lazy_imports,
        normalize_lazy_imports,
        r,
        resolve_lazy_members,
        s,
        x,
    )
    from flext_oracle_oic import api, auth, oracle_oic, web

    from flext_target_oracle_oic.__version__ import (
        FlextTargetOracleOicVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_target_oracle_oic._config import FlextTargetOracleOicConfig, config
    from flext_target_oracle_oic._settings import FlextTargetOracleOicSettings, settings
    from flext_target_oracle_oic.api import (
        FlextTargetOracleOicService,
        target_oracle_oic,
    )
    from flext_target_oracle_oic.cli import FlextTargetOracleOicCli, main
    from flext_target_oracle_oic.constants import FlextTargetOracleOicConstants, c
    from flext_target_oracle_oic.models import FlextTargetOracleOicModels, m
    from flext_target_oracle_oic.protocols import FlextTargetOracleOicProtocols, p
    from flext_target_oracle_oic.target import FlextTargetOracleOic
    from flext_target_oracle_oic.typings import FlextTargetOracleOicTypes, t
    from flext_target_oracle_oic.utilities import FlextTargetOracleOicUtilities, u


__all__: tuple[str, ...] = (
    "FlextTargetOracleOic",
    "FlextTargetOracleOicCli",
    "FlextTargetOracleOicConfig",
    "FlextTargetOracleOicConstants",
    "FlextTargetOracleOicModels",
    "FlextTargetOracleOicProtocols",
    "FlextTargetOracleOicService",
    "FlextTargetOracleOicSettings",
    "FlextTargetOracleOicTypes",
    "FlextTargetOracleOicUtilities",
    "FlextTargetOracleOicVersion",
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
    "build_lazy_import_map",
    "c",
    "cleanup_submodule_namespace",
    "cli",
    "config",
    "core",
    "d",
    "e",
    "h",
    "install_lazy_exports",
    "lazy",
    "lazy_getattr",
    "lazy_member",
    "m",
    "main",
    "meltano",
    "merge_lazy_imports",
    "normalize_lazy_imports",
    "oracle_oic",
    "p",
    "r",
    "resolve_lazy_members",
    "s",
    "settings",
    "t",
    "target_oracle_oic",
    "u",
    "web",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTargetOracleOic": ".target",
        "FlextTargetOracleOicCli": ".cli",
        "FlextTargetOracleOicConfig": "._config",
        "FlextTargetOracleOicConstants": ".constants",
        "FlextTargetOracleOicModels": ".models",
        "FlextTargetOracleOicProtocols": ".protocols",
        "FlextTargetOracleOicService": ".api",
        "FlextTargetOracleOicSettings": "._settings",
        "FlextTargetOracleOicTypes": ".typings",
        "FlextTargetOracleOicUtilities": ".utilities",
        "FlextTargetOracleOicVersion": ".__version__",
        "__author__": ".__version__",
        "__author_email__": ".__version__",
        "__description__": ".__version__",
        "__license__": ".__version__",
        "__title__": ".__version__",
        "__url__": ".__version__",
        "__version_info__": ".__version__",
        "api": "flext_oracle_oic",
        "auth": "flext_oracle_oic",
        "build_lazy_import_map": "flext_meltano",
        "c": ".constants",
        "cleanup_submodule_namespace": "flext_meltano",
        "cli": "flext_meltano",
        "config": "._config",
        "core": "flext_meltano",
        "d": "flext_meltano",
        "e": "flext_meltano",
        "h": "flext_meltano",
        "install_lazy_exports": "flext_meltano",
        "lazy": "flext_meltano",
        "lazy_getattr": "flext_meltano",
        "lazy_member": "flext_meltano",
        "m": ".models",
        "main": ".cli",
        "meltano": "flext_meltano",
        "merge_lazy_imports": "flext_meltano",
        "normalize_lazy_imports": "flext_meltano",
        "oracle_oic": "flext_oracle_oic",
        "p": ".protocols",
        "r": "flext_meltano",
        "resolve_lazy_members": "flext_meltano",
        "s": "flext_meltano",
        "settings": "._settings",
        "t": ".typings",
        "target_oracle_oic": ".api",
        "u": ".utilities",
        "web": "flext_oracle_oic",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)

if not TYPE_CHECKING:
    from flext_target_oracle_oic.__version__ import __version__
