# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.constants import (
        TestsFlextTargetOracleOicConstants,
        TestsFlextTargetOracleOicConstants as c,
    )
    from tests.models import (
        TestsFlextTargetOracleOicModels,
        TestsFlextTargetOracleOicModels as m,
    )
    from tests.protocols import (
        TestsFlextTargetOracleOicProtocols,
        TestsFlextTargetOracleOicProtocols as p,
    )
    from tests.typings import (
        TestsFlextTargetOracleOicTypes,
        TestsFlextTargetOracleOicTypes as t,
    )
    from tests.utilities import (
        TestsFlextTargetOracleOicUtilities,
        TestsFlextTargetOracleOicUtilities as u,
    )
_LAZY_IMPORTS = {
    "TestsFlextTargetOracleOicConstants": ".constants",
    "TestsFlextTargetOracleOicModels": ".models",
    "TestsFlextTargetOracleOicProtocols": ".protocols",
    "TestsFlextTargetOracleOicTypes": ".typings",
    "TestsFlextTargetOracleOicUtilities": ".utilities",
    "c": (".constants", "TestsFlextTargetOracleOicConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": (".models", "TestsFlextTargetOracleOicModels"),
    "p": (".protocols", "TestsFlextTargetOracleOicProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": (".typings", "TestsFlextTargetOracleOicTypes"),
    "u": (".utilities", "TestsFlextTargetOracleOicUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
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
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
