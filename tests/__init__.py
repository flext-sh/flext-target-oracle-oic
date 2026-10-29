# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import (
        api,
        build_lazy_import_map,
        cleanup_submodule_namespace,
        cli,
        config,
        core,
        d,
        e,
        h,
        install_lazy_exports,
        install_local_packages,
        lazy,
        lazy_getattr,
        lazy_member,
        main,
        merge_lazy_imports,
        normalize_lazy_imports,
        r,
        resolve_lazy_members,
        settings,
        td,
        tf,
        tk,
        tm,
        x,
    )

    from flext_target_oracle_oic import (
        auth,
        meltano,
        oracle_oic,
        target_oracle_oic,
        web,
    )
    from tests.base import TestsFlextTargetOracleOicServiceBase, s
    from tests.constants import TestsFlextTargetOracleOicConstants, c
    from tests.models import TestsFlextTargetOracleOicModels, m
    from tests.protocols import TestsFlextTargetOracleOicProtocols, p
    from tests.settings import TestsFlextTargetOracleOicSettings
    from tests.typings import TestsFlextTargetOracleOicTypes, t
    from tests.utilities import TestsFlextTargetOracleOicUtilities, u


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
    "install_local_packages",
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
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "web",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "TestsFlextTargetOracleOicConstants": ".constants",
        "TestsFlextTargetOracleOicModels": ".models",
        "TestsFlextTargetOracleOicProtocols": ".protocols",
        "TestsFlextTargetOracleOicServiceBase": ".base",
        "TestsFlextTargetOracleOicSettings": ".settings",
        "TestsFlextTargetOracleOicTypes": ".typings",
        "TestsFlextTargetOracleOicUtilities": ".utilities",
        "api": "flext_tests",
        "auth": "flext_target_oracle_oic",
        "build_lazy_import_map": "flext_tests",
        "c": ".constants",
        "cleanup_submodule_namespace": "flext_tests",
        "cli": "flext_tests",
        "config": "flext_tests",
        "core": "flext_tests",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "install_lazy_exports": "flext_tests",
        "install_local_packages": "flext_tests",
        "lazy": "flext_tests",
        "lazy_getattr": "flext_tests",
        "lazy_member": "flext_tests",
        "m": ".models",
        "main": "flext_tests",
        "meltano": "flext_target_oracle_oic",
        "merge_lazy_imports": "flext_tests",
        "normalize_lazy_imports": "flext_tests",
        "oracle_oic": "flext_target_oracle_oic",
        "p": ".protocols",
        "r": "flext_tests",
        "resolve_lazy_members": "flext_tests",
        "s": ".base",
        "settings": "flext_tests",
        "t": ".typings",
        "target_oracle_oic": "flext_target_oracle_oic",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "web": "flext_target_oracle_oic",
        "x": "flext_tests",
    }),
    public_exports=__all__,
)
