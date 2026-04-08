# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_target_oracle_oic.__version__ import *

if _t.TYPE_CHECKING:
    from flext_core.decorators import d
    from flext_core.exceptions import e
    from flext_core.handlers import h
    from flext_core.mixins import x
    from flext_core.result import r
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
    from flext_target_oracle_oic.cli import FlextTargetOracleOicCli, main
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
    from flext_target_oracle_oic.settings import FlextTargetOracleOicSettings
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
        "._utilities",
        ".application",
        ".connection",
        ".patterns",
        ".singer",
    ),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            ".api": ("FlextTargetOracleOicService",),
            ".cli": (
                "FlextTargetOracleOicCli",
                "main",
            ),
            ".constants": ("FlextTargetOracleOicConstants",),
            ".models": ("FlextTargetOracleOicModels",),
            ".protocols": ("FlextTargetOracleOicProtocols",),
            ".settings": ("FlextTargetOracleOicSettings",),
            ".target": (
                "FlextTargetOracleOic",
                "FlextTargetOracleOicBaseSink",
                "FlextTargetOracleOicConnectionsSink",
                "FlextTargetOracleOicIntegrationsSink",
                "FlextTargetOracleOicLookupsSink",
                "FlextTargetOracleOicPackagesSink",
            ),
            ".typings": ("FlextTargetOracleOicTypes",),
            ".utilities": ("FlextTargetOracleOicUtilities",),
            "flext_core.decorators": ("d",),
            "flext_core.exceptions": ("e",),
            "flext_core.handlers": ("h",),
            "flext_core.mixins": ("x",),
            "flext_core.result": ("r",),
        },
        alias_groups={
            ".api": (("s", "FlextTargetOracleOicService"),),
            ".constants": (("c", "FlextTargetOracleOicConstants"),),
            ".models": (("m", "FlextTargetOracleOicModels"),),
            ".protocols": (("p", "FlextTargetOracleOicProtocols"),),
            ".typings": (("t", "FlextTargetOracleOicTypes"),),
            ".utilities": (("u", "FlextTargetOracleOicUtilities"),),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
    ),
    module_name=__name__,
)

__all__ = [
    "FlextTargetOracleOic",
    "FlextTargetOracleOicBaseSink",
    "FlextTargetOracleOicCli",
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
    "FlextTargetOracleOicSettings",
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
    "main",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
