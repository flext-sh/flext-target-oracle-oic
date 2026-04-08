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

    _utilities = _flext_target_oracle_oic__utilities
    import flext_target_oracle_oic.api as _flext_target_oracle_oic_api
    from flext_target_oracle_oic._utilities import FlextTargetOracleOicServiceRuntime

    api = _flext_target_oracle_oic_api
    import flext_target_oracle_oic.cli as _flext_target_oracle_oic_cli
    from flext_target_oracle_oic.api import (
        FlextTargetOracleOicService,
        FlextTargetOracleOicService as s,
    )
    from flext_target_oracle_oic.application.orchestrator import (
        FlextTargetOracleOicOrchestrator,
    )

    cli = _flext_target_oracle_oic_cli
    import flext_target_oracle_oic.constants as _flext_target_oracle_oic_constants
    from flext_target_oracle_oic.cli import FlextTargetOracleOicCli, main
    from flext_target_oracle_oic.connection.connection import (
        FlextTargetOracleOicConnection,
    )
    from flext_target_oracle_oic.connection.settings import (
        FlextTargetOracleOicConnectionSettings,
    )

    constants = _flext_target_oracle_oic_constants
    import flext_target_oracle_oic.models as _flext_target_oracle_oic_models
    from flext_target_oracle_oic.constants import (
        FlextTargetOracleOicConstants,
        FlextTargetOracleOicConstants as c,
    )

    models = _flext_target_oracle_oic_models
    import flext_target_oracle_oic.protocols as _flext_target_oracle_oic_protocols
    from flext_target_oracle_oic.models import (
        FlextTargetOracleOicModels,
        FlextTargetOracleOicModels as m,
    )
    from flext_target_oracle_oic.patterns.oic_patterns import (
        FlextTargetOracleOicDataTransformer,
        FlextTargetOracleOicEntryManager,
        FlextTargetOracleOicSchemaMapper,
        FlextTargetOracleOicTypeConverter,
    )

    protocols = _flext_target_oracle_oic_protocols
    import flext_target_oracle_oic.settings as _flext_target_oracle_oic_settings
    from flext_target_oracle_oic.protocols import (
        FlextTargetOracleOicProtocols,
        FlextTargetOracleOicProtocols as p,
    )

    settings = _flext_target_oracle_oic_settings
    import flext_target_oracle_oic.target as _flext_target_oracle_oic_target
    from flext_target_oracle_oic.settings import FlextTargetOracleOicConfig
    from flext_target_oracle_oic.singer.processors import (
        FlextTargetOracleOicProcessedRecord,
        FlextTargetOracleOicRecordProcessor,
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
    from flext_target_oracle_oic.utilities import (
        FlextTargetOracleOicUtilities,
        FlextTargetOracleOicUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("flext_target_oracle_oic._utilities",),
    {
        "FlextTargetOracleOic": (
            "flext_target_oracle_oic.target",
            "FlextTargetOracleOic",
        ),
        "FlextTargetOracleOicBaseSink": (
            "flext_target_oracle_oic.target",
            "FlextTargetOracleOicBaseSink",
        ),
        "FlextTargetOracleOicCli": (
            "flext_target_oracle_oic.cli",
            "FlextTargetOracleOicCli",
        ),
        "FlextTargetOracleOicConfig": (
            "flext_target_oracle_oic.settings",
            "FlextTargetOracleOicConfig",
        ),
        "FlextTargetOracleOicConnection": (
            "flext_target_oracle_oic.connection.connection",
            "FlextTargetOracleOicConnection",
        ),
        "FlextTargetOracleOicConnectionSettings": (
            "flext_target_oracle_oic.connection.settings",
            "FlextTargetOracleOicConnectionSettings",
        ),
        "FlextTargetOracleOicConnectionsSink": (
            "flext_target_oracle_oic.target",
            "FlextTargetOracleOicConnectionsSink",
        ),
        "FlextTargetOracleOicConstants": (
            "flext_target_oracle_oic.constants",
            "FlextTargetOracleOicConstants",
        ),
        "FlextTargetOracleOicDataTransformer": (
            "flext_target_oracle_oic.patterns.oic_patterns",
            "FlextTargetOracleOicDataTransformer",
        ),
        "FlextTargetOracleOicEntryManager": (
            "flext_target_oracle_oic.patterns.oic_patterns",
            "FlextTargetOracleOicEntryManager",
        ),
        "FlextTargetOracleOicIntegrationsSink": (
            "flext_target_oracle_oic.target",
            "FlextTargetOracleOicIntegrationsSink",
        ),
        "FlextTargetOracleOicLookupsSink": (
            "flext_target_oracle_oic.target",
            "FlextTargetOracleOicLookupsSink",
        ),
        "FlextTargetOracleOicModels": (
            "flext_target_oracle_oic.models",
            "FlextTargetOracleOicModels",
        ),
        "FlextTargetOracleOicOrchestrator": (
            "flext_target_oracle_oic.application.orchestrator",
            "FlextTargetOracleOicOrchestrator",
        ),
        "FlextTargetOracleOicPackagesSink": (
            "flext_target_oracle_oic.target",
            "FlextTargetOracleOicPackagesSink",
        ),
        "FlextTargetOracleOicProcessedRecord": (
            "flext_target_oracle_oic.singer.processors",
            "FlextTargetOracleOicProcessedRecord",
        ),
        "FlextTargetOracleOicProtocols": (
            "flext_target_oracle_oic.protocols",
            "FlextTargetOracleOicProtocols",
        ),
        "FlextTargetOracleOicRecordProcessor": (
            "flext_target_oracle_oic.singer.processors",
            "FlextTargetOracleOicRecordProcessor",
        ),
        "FlextTargetOracleOicSchemaMapper": (
            "flext_target_oracle_oic.patterns.oic_patterns",
            "FlextTargetOracleOicSchemaMapper",
        ),
        "FlextTargetOracleOicService": (
            "flext_target_oracle_oic.api",
            "FlextTargetOracleOicService",
        ),
        "FlextTargetOracleOicTypeConverter": (
            "flext_target_oracle_oic.patterns.oic_patterns",
            "FlextTargetOracleOicTypeConverter",
        ),
        "FlextTargetOracleOicTypes": (
            "flext_target_oracle_oic.typings",
            "FlextTargetOracleOicTypes",
        ),
        "FlextTargetOracleOicUtilities": (
            "flext_target_oracle_oic.utilities",
            "FlextTargetOracleOicUtilities",
        ),
        "__author__": ("flext_target_oracle_oic.__version__", "__author__"),
        "__author_email__": ("flext_target_oracle_oic.__version__", "__author_email__"),
        "__description__": ("flext_target_oracle_oic.__version__", "__description__"),
        "__license__": ("flext_target_oracle_oic.__version__", "__license__"),
        "__title__": ("flext_target_oracle_oic.__version__", "__title__"),
        "__url__": ("flext_target_oracle_oic.__version__", "__url__"),
        "__version__": ("flext_target_oracle_oic.__version__", "__version__"),
        "__version_info__": ("flext_target_oracle_oic.__version__", "__version_info__"),
        "_utilities": "flext_target_oracle_oic._utilities",
        "api": "flext_target_oracle_oic.api",
        "c": ("flext_target_oracle_oic.constants", "FlextTargetOracleOicConstants"),
        "cli": "flext_target_oracle_oic.cli",
        "constants": "flext_target_oracle_oic.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_target_oracle_oic.models", "FlextTargetOracleOicModels"),
        "main": ("flext_target_oracle_oic.cli", "main"),
        "models": "flext_target_oracle_oic.models",
        "p": ("flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"),
        "protocols": "flext_target_oracle_oic.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_target_oracle_oic.api", "FlextTargetOracleOicService"),
        "settings": "flext_target_oracle_oic.settings",
        "t": ("flext_target_oracle_oic.typings", "FlextTargetOracleOicTypes"),
        "target": "flext_target_oracle_oic.target",
        "typings": "flext_target_oracle_oic.typings",
        "u": ("flext_target_oracle_oic.utilities", "FlextTargetOracleOicUtilities"),
        "utilities": "flext_target_oracle_oic.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

__all__ = [
    "FlextTargetOracleOic",
    "FlextTargetOracleOicBaseSink",
    "FlextTargetOracleOicCli",
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
    "c",
    "cli",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "main",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "settings",
    "t",
    "target",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
