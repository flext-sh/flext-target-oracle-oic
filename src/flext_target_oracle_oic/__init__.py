# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext target oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

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

if TYPE_CHECKING:
    from flext_meltano import *

    from flext_target_oracle_oic import (
        application,
        cli,
        connection,
        constants,
        models,
        patterns,
        protocols,
        settings,
        singer,
        target,
        typings,
        utilities,
    )
    from flext_target_oracle_oic.application import orchestrator
    from flext_target_oracle_oic.application.orchestrator import *
    from flext_target_oracle_oic.cli import *
    from flext_target_oracle_oic.connection.connection import *
    from flext_target_oracle_oic.connection.settings import *
    from flext_target_oracle_oic.constants import *
    from flext_target_oracle_oic.models import *
    from flext_target_oracle_oic.patterns import oic_patterns
    from flext_target_oracle_oic.patterns.oic_patterns import *
    from flext_target_oracle_oic.protocols import *
    from flext_target_oracle_oic.settings import *
    from flext_target_oracle_oic.singer import processors
    from flext_target_oracle_oic.singer.processors import *
    from flext_target_oracle_oic.target import *
    from flext_target_oracle_oic.typings import *
    from flext_target_oracle_oic.utilities import *

from flext_target_oracle_oic.application import _LAZY_IMPORTS as _APPLICATION_LAZY
from flext_target_oracle_oic.connection import _LAZY_IMPORTS as _CONNECTION_LAZY
from flext_target_oracle_oic.patterns import _LAZY_IMPORTS as _PATTERNS_LAZY
from flext_target_oracle_oic.singer import _LAZY_IMPORTS as _SINGER_LAZY

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    **_APPLICATION_LAZY,
    **_CONNECTION_LAZY,
    **_PATTERNS_LAZY,
    **_SINGER_LAZY,
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
    "c": ["flext_target_oracle_oic.constants", "FlextTargetOracleOicConstants"],
    "cli": "flext_target_oracle_oic.cli",
    "connection": "flext_target_oracle_oic.connection",
    "constants": "flext_target_oracle_oic.constants",
    "d": "flext_meltano",
    "e": "flext_meltano",
    "h": "flext_meltano",
    "m": ["flext_target_oracle_oic.models", "FlextTargetOracleOicModels"],
    "main": "flext_target_oracle_oic.cli",
    "models": "flext_target_oracle_oic.models",
    "p": ["flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"],
    "patterns": "flext_target_oracle_oic.patterns",
    "protocols": "flext_target_oracle_oic.protocols",
    "r": "flext_meltano",
    "s": "flext_meltano",
    "settings": "flext_target_oracle_oic.settings",
    "singer": "flext_target_oracle_oic.singer",
    "t": ["flext_target_oracle_oic.typings", "FlextTargetOracleOicTypes"],
    "target": "flext_target_oracle_oic.target",
    "typings": "flext_target_oracle_oic.typings",
    "u": ["flext_target_oracle_oic.utilities", "FlextTargetOracleOicUtilities"],
    "utilities": "flext_target_oracle_oic.utilities",
    "x": "flext_meltano",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
