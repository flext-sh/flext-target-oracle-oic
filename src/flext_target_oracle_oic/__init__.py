# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext target oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

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

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_meltano import d, e, h, r, s, x

    from flext_target_oracle_oic.application import *
    from flext_target_oracle_oic.cli import *
    from flext_target_oracle_oic.connection import *
    from flext_target_oracle_oic.constants import *
    from flext_target_oracle_oic.models import *
    from flext_target_oracle_oic.patterns import *
    from flext_target_oracle_oic.protocols import *
    from flext_target_oracle_oic.settings import *
    from flext_target_oracle_oic.singer import *
    from flext_target_oracle_oic.target import *
    from flext_target_oracle_oic.typings import *
    from flext_target_oracle_oic.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = merge_lazy_imports(
    (
        "flext_target_oracle_oic.application",
        "flext_target_oracle_oic.connection",
        "flext_target_oracle_oic.patterns",
        "flext_target_oracle_oic.singer",
    ),
    {
        "FlextTargetOracleOic": "flext_target_oracle_oic.target",
        "FlextTargetOracleOicAuthenticator": "flext_target_oracle_oic.utilities",
        "FlextTargetOracleOicBaseSink": "flext_target_oracle_oic.target",
        "FlextTargetOracleOicConfig": "flext_target_oracle_oic.settings",
        "FlextTargetOracleOicConnectionsSink": "flext_target_oracle_oic.target",
        "FlextTargetOracleOicConstants": "flext_target_oracle_oic.constants",
        "FlextTargetOracleOicIntegrationsSink": "flext_target_oracle_oic.target",
        "FlextTargetOracleOicLookupsSink": "flext_target_oracle_oic.target",
        "FlextTargetOracleOicModels": "flext_target_oracle_oic.models",
        "FlextTargetOracleOicPackagesSink": "flext_target_oracle_oic.target",
        "FlextTargetOracleOicProtocols": "flext_target_oracle_oic.protocols",
        "FlextTargetOracleOicTypes": "flext_target_oracle_oic.typings",
        "FlextTargetOracleOicUtilities": "flext_target_oracle_oic.utilities",
        "application": "flext_target_oracle_oic.application",
        "c": ("flext_target_oracle_oic.constants", "FlextTargetOracleOicConstants"),
        "cli": "flext_target_oracle_oic.cli",
        "connection": "flext_target_oracle_oic.connection",
        "constants": "flext_target_oracle_oic.constants",
        "d": "flext_meltano",
        "e": "flext_meltano",
        "h": "flext_meltano",
        "m": ("flext_target_oracle_oic.models", "FlextTargetOracleOicModels"),
        "main": "flext_target_oracle_oic.cli",
        "models": "flext_target_oracle_oic.models",
        "p": ("flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"),
        "patterns": "flext_target_oracle_oic.patterns",
        "protocols": "flext_target_oracle_oic.protocols",
        "r": "flext_meltano",
        "s": "flext_meltano",
        "settings": "flext_target_oracle_oic.settings",
        "singer": "flext_target_oracle_oic.singer",
        "t": ("flext_target_oracle_oic.typings", "FlextTargetOracleOicTypes"),
        "target": "flext_target_oracle_oic.target",
        "typings": "flext_target_oracle_oic.typings",
        "u": ("flext_target_oracle_oic.utilities", "FlextTargetOracleOicUtilities"),
        "utilities": "flext_target_oracle_oic.utilities",
        "x": "flext_meltano",
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)
