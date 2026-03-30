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
        cli,
        constants,
        models,
        protocols,
        settings,
        target,
        typings,
        utilities,
    )
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

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextTargetOracleOic": "flext_target_oracle_oic.target",
    "FlextTargetOracleOicAuthenticator": "flext_target_oracle_oic.utilities",
    "FlextTargetOracleOicBaseSink": "flext_target_oracle_oic.target",
    "FlextTargetOracleOicConfig": "flext_target_oracle_oic.settings",
    "FlextTargetOracleOicConnection": "flext_target_oracle_oic.connection.connection",
    "FlextTargetOracleOicConnectionSettings": "flext_target_oracle_oic.connection.settings",
    "FlextTargetOracleOicConnectionsSink": "flext_target_oracle_oic.target",
    "FlextTargetOracleOicConstants": "flext_target_oracle_oic.constants",
    "FlextTargetOracleOicDataTransformer": "flext_target_oracle_oic.patterns.oic_patterns",
    "FlextTargetOracleOicEntryManager": "flext_target_oracle_oic.patterns.oic_patterns",
    "FlextTargetOracleOicIntegrationsSink": "flext_target_oracle_oic.target",
    "FlextTargetOracleOicLookupsSink": "flext_target_oracle_oic.target",
    "FlextTargetOracleOicModels": "flext_target_oracle_oic.models",
    "FlextTargetOracleOicOrchestrator": "flext_target_oracle_oic.application.orchestrator",
    "FlextTargetOracleOicPackagesSink": "flext_target_oracle_oic.target",
    "FlextTargetOracleOicProcessedRecord": "flext_target_oracle_oic.singer.processors",
    "FlextTargetOracleOicProtocols": "flext_target_oracle_oic.protocols",
    "FlextTargetOracleOicRecordProcessor": "flext_target_oracle_oic.singer.processors",
    "FlextTargetOracleOicSchemaMapper": "flext_target_oracle_oic.patterns.oic_patterns",
    "FlextTargetOracleOicTypeConverter": "flext_target_oracle_oic.patterns.oic_patterns",
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
    "logger": "flext_target_oracle_oic.connection.settings",
    "m": ["flext_target_oracle_oic.models", "FlextTargetOracleOicModels"],
    "main": "flext_target_oracle_oic.cli",
    "models": "flext_target_oracle_oic.models",
    "oic_patterns": "flext_target_oracle_oic.patterns.oic_patterns",
    "orchestrator": "flext_target_oracle_oic.application.orchestrator",
    "p": ["flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"],
    "patterns": "flext_target_oracle_oic.patterns",
    "processors": "flext_target_oracle_oic.singer.processors",
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
