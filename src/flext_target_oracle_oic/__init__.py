# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext target oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_target_oracle_oic.__version__ import (
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
    from flext_meltano import d, e, h, r, s, x

    from flext_target_oracle_oic import (
        application as application,
        cli as cli,
        connection as connection,
        constants as constants,
        models as models,
        patterns as patterns,
        protocols as protocols,
        settings as settings,
        singer as singer,
        target as target,
        typings as typings,
        utilities as utilities,
    )
    from flext_target_oracle_oic.application import orchestrator as orchestrator
    from flext_target_oracle_oic.application.orchestrator import (
        FlextTargetOracleOicOrchestrator as FlextTargetOracleOicOrchestrator,
    )
    from flext_target_oracle_oic.cli import main as main
    from flext_target_oracle_oic.connection.connection import (
        FlextTargetOracleOicConnection as FlextTargetOracleOicConnection,
    )
    from flext_target_oracle_oic.connection.settings import (
        FlextTargetOracleOicConnectionSettings as FlextTargetOracleOicConnectionSettings,
        logger as logger,
    )
    from flext_target_oracle_oic.constants import (
        FlextTargetOracleOicConstants as FlextTargetOracleOicConstants,
        FlextTargetOracleOicConstants as c,
    )
    from flext_target_oracle_oic.models import (
        FlextTargetOracleOicModels as FlextTargetOracleOicModels,
        FlextTargetOracleOicModels as m,
    )
    from flext_target_oracle_oic.patterns import oic_patterns as oic_patterns
    from flext_target_oracle_oic.patterns.oic_patterns import (
        FlextTargetOracleOicDataTransformer as FlextTargetOracleOicDataTransformer,
        FlextTargetOracleOicEntryManager as FlextTargetOracleOicEntryManager,
        FlextTargetOracleOicSchemaMapper as FlextTargetOracleOicSchemaMapper,
        FlextTargetOracleOicTypeConverter as FlextTargetOracleOicTypeConverter,
    )
    from flext_target_oracle_oic.protocols import (
        FlextTargetOracleOicProtocols as FlextTargetOracleOicProtocols,
        FlextTargetOracleOicProtocols as p,
    )
    from flext_target_oracle_oic.settings import (
        FlextTargetOracleOicConfig as FlextTargetOracleOicConfig,
    )
    from flext_target_oracle_oic.singer import processors as processors
    from flext_target_oracle_oic.singer.processors import (
        FlextTargetOracleOicProcessedRecord as FlextTargetOracleOicProcessedRecord,
        FlextTargetOracleOicRecordProcessor as FlextTargetOracleOicRecordProcessor,
    )
    from flext_target_oracle_oic.target import (
        FlextTargetOracleOic as FlextTargetOracleOic,
        FlextTargetOracleOicBaseSink as FlextTargetOracleOicBaseSink,
        FlextTargetOracleOicConnectionsSink as FlextTargetOracleOicConnectionsSink,
        FlextTargetOracleOicIntegrationsSink as FlextTargetOracleOicIntegrationsSink,
        FlextTargetOracleOicLookupsSink as FlextTargetOracleOicLookupsSink,
        FlextTargetOracleOicPackagesSink as FlextTargetOracleOicPackagesSink,
    )
    from flext_target_oracle_oic.typings import (
        FlextTargetOracleOicTypes as FlextTargetOracleOicTypes,
        FlextTargetOracleOicTypes as t,
    )
    from flext_target_oracle_oic.utilities import (
        FlextTargetOracleOicAuthenticator as FlextTargetOracleOicAuthenticator,
        FlextTargetOracleOicUtilities as FlextTargetOracleOicUtilities,
        FlextTargetOracleOicUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTargetOracleOic": ["flext_target_oracle_oic.target", "FlextTargetOracleOic"],
    "FlextTargetOracleOicAuthenticator": ["flext_target_oracle_oic.utilities", "FlextTargetOracleOicAuthenticator"],
    "FlextTargetOracleOicBaseSink": ["flext_target_oracle_oic.target", "FlextTargetOracleOicBaseSink"],
    "FlextTargetOracleOicConfig": ["flext_target_oracle_oic.settings", "FlextTargetOracleOicConfig"],
    "FlextTargetOracleOicConnection": ["flext_target_oracle_oic.connection.connection", "FlextTargetOracleOicConnection"],
    "FlextTargetOracleOicConnectionSettings": ["flext_target_oracle_oic.connection.settings", "FlextTargetOracleOicConnectionSettings"],
    "FlextTargetOracleOicConnectionsSink": ["flext_target_oracle_oic.target", "FlextTargetOracleOicConnectionsSink"],
    "FlextTargetOracleOicConstants": ["flext_target_oracle_oic.constants", "FlextTargetOracleOicConstants"],
    "FlextTargetOracleOicDataTransformer": ["flext_target_oracle_oic.patterns.oic_patterns", "FlextTargetOracleOicDataTransformer"],
    "FlextTargetOracleOicEntryManager": ["flext_target_oracle_oic.patterns.oic_patterns", "FlextTargetOracleOicEntryManager"],
    "FlextTargetOracleOicIntegrationsSink": ["flext_target_oracle_oic.target", "FlextTargetOracleOicIntegrationsSink"],
    "FlextTargetOracleOicLookupsSink": ["flext_target_oracle_oic.target", "FlextTargetOracleOicLookupsSink"],
    "FlextTargetOracleOicModels": ["flext_target_oracle_oic.models", "FlextTargetOracleOicModels"],
    "FlextTargetOracleOicOrchestrator": ["flext_target_oracle_oic.application.orchestrator", "FlextTargetOracleOicOrchestrator"],
    "FlextTargetOracleOicPackagesSink": ["flext_target_oracle_oic.target", "FlextTargetOracleOicPackagesSink"],
    "FlextTargetOracleOicProcessedRecord": ["flext_target_oracle_oic.singer.processors", "FlextTargetOracleOicProcessedRecord"],
    "FlextTargetOracleOicProtocols": ["flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"],
    "FlextTargetOracleOicRecordProcessor": ["flext_target_oracle_oic.singer.processors", "FlextTargetOracleOicRecordProcessor"],
    "FlextTargetOracleOicSchemaMapper": ["flext_target_oracle_oic.patterns.oic_patterns", "FlextTargetOracleOicSchemaMapper"],
    "FlextTargetOracleOicTypeConverter": ["flext_target_oracle_oic.patterns.oic_patterns", "FlextTargetOracleOicTypeConverter"],
    "FlextTargetOracleOicTypes": ["flext_target_oracle_oic.typings", "FlextTargetOracleOicTypes"],
    "FlextTargetOracleOicUtilities": ["flext_target_oracle_oic.utilities", "FlextTargetOracleOicUtilities"],
    "application": ["flext_target_oracle_oic.application", ""],
    "c": ["flext_target_oracle_oic.constants", "FlextTargetOracleOicConstants"],
    "cli": ["flext_target_oracle_oic.cli", ""],
    "connection": ["flext_target_oracle_oic.connection", ""],
    "constants": ["flext_target_oracle_oic.constants", ""],
    "d": ["flext_meltano", "d"],
    "e": ["flext_meltano", "e"],
    "h": ["flext_meltano", "h"],
    "logger": ["flext_target_oracle_oic.connection.settings", "logger"],
    "m": ["flext_target_oracle_oic.models", "FlextTargetOracleOicModels"],
    "main": ["flext_target_oracle_oic.cli", "main"],
    "models": ["flext_target_oracle_oic.models", ""],
    "oic_patterns": ["flext_target_oracle_oic.patterns.oic_patterns", ""],
    "orchestrator": ["flext_target_oracle_oic.application.orchestrator", ""],
    "p": ["flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"],
    "patterns": ["flext_target_oracle_oic.patterns", ""],
    "processors": ["flext_target_oracle_oic.singer.processors", ""],
    "protocols": ["flext_target_oracle_oic.protocols", ""],
    "r": ["flext_meltano", "r"],
    "s": ["flext_meltano", "s"],
    "settings": ["flext_target_oracle_oic.settings", ""],
    "singer": ["flext_target_oracle_oic.singer", ""],
    "t": ["flext_target_oracle_oic.typings", "FlextTargetOracleOicTypes"],
    "target": ["flext_target_oracle_oic.target", ""],
    "typings": ["flext_target_oracle_oic.typings", ""],
    "u": ["flext_target_oracle_oic.utilities", "FlextTargetOracleOicUtilities"],
    "utilities": ["flext_target_oracle_oic.utilities", ""],
    "x": ["flext_meltano", "x"],
}

_EXPORTS: Sequence[str] = [
    "FlextTargetOracleOic",
    "FlextTargetOracleOicAuthenticator",
    "FlextTargetOracleOicBaseSink",
    "FlextTargetOracleOicConfig",
    "FlextTargetOracleOicConnection",
    "FlextTargetOracleOicConnectionSettings",
    "FlextTargetOracleOicConnectionsSink",
    "FlextTargetOracleOicConstants",
    "FlextTargetOracleOicDataTransformer",
    "FlextTargetOracleOicEntryManager",
    "FlextTargetOracleOicIntegrationsSink",
    "FlextTargetOracleOicLookupsSink",
    "FlextTargetOracleOicModels",
    "FlextTargetOracleOicOrchestrator",
    "FlextTargetOracleOicPackagesSink",
    "FlextTargetOracleOicProcessedRecord",
    "FlextTargetOracleOicProtocols",
    "FlextTargetOracleOicRecordProcessor",
    "FlextTargetOracleOicSchemaMapper",
    "FlextTargetOracleOicTypeConverter",
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
    "application",
    "c",
    "cli",
    "connection",
    "constants",
    "d",
    "e",
    "h",
    "logger",
    "m",
    "main",
    "models",
    "oic_patterns",
    "orchestrator",
    "p",
    "patterns",
    "processors",
    "protocols",
    "r",
    "s",
    "settings",
    "singer",
    "t",
    "target",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
