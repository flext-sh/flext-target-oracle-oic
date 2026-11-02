# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, d, e, h, r, td, tf, tk, tm, x

    from flext_target_oracle_oic import config, main, settings, target_oracle_oic
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
    "c",
    "config",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "target_oracle_oic",
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "TestsFlextTargetOracleOicConstants": ".constants",
        "TestsFlextTargetOracleOicModels": ".models",
        "TestsFlextTargetOracleOicProtocols": ".protocols",
        "TestsFlextTargetOracleOicServiceBase": ".base",
        "TestsFlextTargetOracleOicSettings": ".settings",
        "TestsFlextTargetOracleOicTypes": ".typings",
        "TestsFlextTargetOracleOicUtilities": ".utilities",
        "api": "flext_tests",
        "c": ".constants",
        "config": "flext_target_oracle_oic",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "m": ".models",
        "main": "flext_target_oracle_oic",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "settings": "flext_target_oracle_oic",
        "t": ".typings",
        "target_oracle_oic": "flext_target_oracle_oic",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_tests",
    },
    public_exports=__all__,
)
