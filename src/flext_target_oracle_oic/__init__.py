# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext target oracle oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_target_oracle_oic.__version__ import *

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_target_oracle_oic._utilities.service_runtime import (
        FlextTargetOracleOicServiceRuntime,
    )
    from flext_target_oracle_oic.api import (
        FlextTargetOracleOicService,
        FlextTargetOracleOicService as s,
    )
    from flext_target_oracle_oic.application.orchestrator import (
        FlextTargetOracleOicOrchestrator,
    )
    from flext_target_oracle_oic.cli import FlextTargetOracleOicCli
    from flext_target_oracle_oic.connection.connection import (
        FlextTargetOracleOicConnection,
    )
    from flext_target_oracle_oic.connection.settings import (
        FlextTargetOracleOicConnectionSettings,
    )
    from flext_target_oracle_oic.constants import (
        FlextTargetOracleOicConstants,
        FlextTargetOracleOicConstants as c,
    )
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
    from flext_target_oracle_oic.protocols import (
        FlextTargetOracleOicProtocols,
        FlextTargetOracleOicProtocols as p,
    )
    from flext_target_oracle_oic.settings import FlextTargetOracleOicConfig
    from flext_target_oracle_oic.singer.processors import (
        FlextTargetOracleOicProcessedRecord,
        FlextTargetOracleOicRecordProcessor,
    )
    from flext_target_oracle_oic.target import (
        FlextTargetOracleOic,
        FlextTargetOracleOicBaseSink,
        FlextTargetOracleOicConnectionsSink,
        FlextTargetOracleOicIntegrationsSink,
        FlextTargetOracleOicLookupsSink,
        FlextTargetOracleOicPackagesSink,
    )
    from flext_target_oracle_oic.typings import (
        FlextTargetOracleOicTypes,
        FlextTargetOracleOicTypes as t,
    )
    from flext_target_oracle_oic.utilities import (
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
        "FlextTargetOracleOicConnectionsSink": (
            "flext_target_oracle_oic.target",
            "FlextTargetOracleOicConnectionsSink",
        ),
        "FlextTargetOracleOicConstants": (
            "flext_target_oracle_oic.constants",
            "FlextTargetOracleOicConstants",
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
        "FlextTargetOracleOicPackagesSink": (
            "flext_target_oracle_oic.target",
            "FlextTargetOracleOicPackagesSink",
        ),
        "FlextTargetOracleOicProtocols": (
            "flext_target_oracle_oic.protocols",
            "FlextTargetOracleOicProtocols",
        ),
        "FlextTargetOracleOicService": (
            "flext_target_oracle_oic.api",
            "FlextTargetOracleOicService",
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
        "c": ("flext_target_oracle_oic.constants", "FlextTargetOracleOicConstants"),
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_target_oracle_oic.models", "FlextTargetOracleOicModels"),
        "p": ("flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"),
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_target_oracle_oic.api", "FlextTargetOracleOicService"),
        "t": ("flext_target_oracle_oic.typings", "FlextTargetOracleOicTypes"),
        "u": ("flext_target_oracle_oic.utilities", "FlextTargetOracleOicUtilities"),
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("logger", None)
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
