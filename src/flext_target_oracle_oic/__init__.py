# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext target oracle oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_target_oracle_oic.__version__ import *

if _t.TYPE_CHECKING:
    import flext_target_oracle_oic._utilities as _flext_target_oracle_oic__utilities
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

    _utilities = _flext_target_oracle_oic__utilities
    import flext_target_oracle_oic.api as _flext_target_oracle_oic_api
    from flext_target_oracle_oic._utilities import (
        FlextTargetOracleOicServiceRuntime,
        service_runtime,
    )

    api = _flext_target_oracle_oic_api
    import flext_target_oracle_oic.application as _flext_target_oracle_oic_application
    from flext_target_oracle_oic.api import FlextTargetOracleOicService

    application = _flext_target_oracle_oic_application
    import flext_target_oracle_oic.cli as _flext_target_oracle_oic_cli
    from flext_target_oracle_oic.application import (
        FlextTargetOracleOicOrchestrator,
        orchestrator,
    )

    cli = _flext_target_oracle_oic_cli
    import flext_target_oracle_oic.connection as _flext_target_oracle_oic_connection
    from flext_target_oracle_oic.cli import main

    connection = _flext_target_oracle_oic_connection
    import flext_target_oracle_oic.constants as _flext_target_oracle_oic_constants
    from flext_target_oracle_oic.connection import (
        FlextTargetOracleOicConnection,
        FlextTargetOracleOicConnectionSettings,
        logger,
    )

    constants = _flext_target_oracle_oic_constants
    import flext_target_oracle_oic.models as _flext_target_oracle_oic_models
    from flext_target_oracle_oic.constants import (
        FlextTargetOracleOicConstants,
        FlextTargetOracleOicConstants as c,
    )

    models = _flext_target_oracle_oic_models
    import flext_target_oracle_oic.patterns as _flext_target_oracle_oic_patterns
    from flext_target_oracle_oic.models import (
        FlextTargetOracleOicModels,
        FlextTargetOracleOicModels as m,
    )

    patterns = _flext_target_oracle_oic_patterns
    import flext_target_oracle_oic.protocols as _flext_target_oracle_oic_protocols
    from flext_target_oracle_oic.patterns import (
        FlextTargetOracleOicDataTransformer,
        FlextTargetOracleOicEntryManager,
        FlextTargetOracleOicSchemaMapper,
        FlextTargetOracleOicTypeConverter,
        oic_patterns,
    )

    protocols = _flext_target_oracle_oic_protocols
    import flext_target_oracle_oic.settings as _flext_target_oracle_oic_settings
    from flext_target_oracle_oic.protocols import (
        FlextTargetOracleOicProtocols,
        FlextTargetOracleOicProtocols as p,
    )

    settings = _flext_target_oracle_oic_settings
    import flext_target_oracle_oic.singer as _flext_target_oracle_oic_singer
    from flext_target_oracle_oic.settings import FlextTargetOracleOicConfig

    singer = _flext_target_oracle_oic_singer
    import flext_target_oracle_oic.target as _flext_target_oracle_oic_target
    from flext_target_oracle_oic.singer import (
        FlextTargetOracleOicProcessedRecord,
        FlextTargetOracleOicRecordProcessor,
        processors,
    )

    target = _flext_target_oracle_oic_target
    import flext_target_oracle_oic.typings as _flext_target_oracle_oic_typings
    from flext_target_oracle_oic.target import (
        FlextTargetOracleOic,
        FlextTargetOracleOicBaseSink,
        FlextTargetOracleOicConnectionsSink,
        FlextTargetOracleOicIntegrationsSink,
        FlextTargetOracleOicLookupsSink,
        FlextTargetOracleOicPackagesSink,
    )

    typings = _flext_target_oracle_oic_typings
    import flext_target_oracle_oic.utilities as _flext_target_oracle_oic_utilities
    from flext_target_oracle_oic.typings import (
        FlextTargetOracleOicTypes,
        FlextTargetOracleOicTypes as t,
    )

    utilities = _flext_target_oracle_oic_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_target_oracle_oic.utilities import (
        FlextTargetOracleOicAuthenticator,
        FlextTargetOracleOicUtilities,
        FlextTargetOracleOicUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (
        "flext_target_oracle_oic._utilities",
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
        "FlextTargetOracleOicService": "flext_target_oracle_oic.api",
        "FlextTargetOracleOicTypes": "flext_target_oracle_oic.typings",
        "FlextTargetOracleOicUtilities": "flext_target_oracle_oic.utilities",
        "__author__": "flext_target_oracle_oic.__version__",
        "__author_email__": "flext_target_oracle_oic.__version__",
        "__description__": "flext_target_oracle_oic.__version__",
        "__license__": "flext_target_oracle_oic.__version__",
        "__title__": "flext_target_oracle_oic.__version__",
        "__url__": "flext_target_oracle_oic.__version__",
        "__version__": "flext_target_oracle_oic.__version__",
        "__version_info__": "flext_target_oracle_oic.__version__",
        "_utilities": "flext_target_oracle_oic._utilities",
        "api": "flext_target_oracle_oic.api",
        "application": "flext_target_oracle_oic.application",
        "c": ("flext_target_oracle_oic.constants", "FlextTargetOracleOicConstants"),
        "cli": "flext_target_oracle_oic.cli",
        "connection": "flext_target_oracle_oic.connection",
        "constants": "flext_target_oracle_oic.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_target_oracle_oic.models", "FlextTargetOracleOicModels"),
        "main": "flext_target_oracle_oic.cli",
        "models": "flext_target_oracle_oic.models",
        "p": ("flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"),
        "patterns": "flext_target_oracle_oic.patterns",
        "protocols": "flext_target_oracle_oic.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "settings": "flext_target_oracle_oic.settings",
        "singer": "flext_target_oracle_oic.singer",
        "t": ("flext_target_oracle_oic.typings", "FlextTargetOracleOicTypes"),
        "target": "flext_target_oracle_oic.target",
        "typings": "flext_target_oracle_oic.typings",
        "u": ("flext_target_oracle_oic.utilities", "FlextTargetOracleOicUtilities"),
        "utilities": "flext_target_oracle_oic.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)

__all__ = [
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
    "FlextTargetOracleOicService",
    "FlextTargetOracleOicServiceRuntime",
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
    "_utilities",
    "api",
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
    "service_runtime",
    "settings",
    "singer",
    "t",
    "target",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
