# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext target oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_target_oracle_oic.__version__ import *

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_target_oracle_oic import (
        _utilities,
        api,
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
    from flext_target_oracle_oic._utilities import (
        FlextTargetOracleOicServiceRuntime,
        service_runtime,
    )
    from flext_target_oracle_oic.api import FlextTargetOracleOicService
    from flext_target_oracle_oic.application import (
        FlextTargetOracleOicOrchestrator,
        orchestrator,
    )
    from flext_target_oracle_oic.cli import main
    from flext_target_oracle_oic.connection import (
        FlextTargetOracleOicConnection,
        FlextTargetOracleOicConnectionSettings,
        logger,
    )
    from flext_target_oracle_oic.constants import (
        FlextTargetOracleOicConstants,
        FlextTargetOracleOicConstants as c,
    )
    from flext_target_oracle_oic.models import (
        FlextTargetOracleOicModels,
        FlextTargetOracleOicModels as m,
    )
    from flext_target_oracle_oic.patterns import (
        FlextTargetOracleOicDataTransformer,
        FlextTargetOracleOicEntryManager,
        FlextTargetOracleOicSchemaMapper,
        FlextTargetOracleOicTypeConverter,
        oic_patterns,
    )
    from flext_target_oracle_oic.protocols import (
        FlextTargetOracleOicProtocols,
        FlextTargetOracleOicProtocols as p,
    )
    from flext_target_oracle_oic.settings import FlextTargetOracleOicConfig
    from flext_target_oracle_oic.singer import (
        FlextTargetOracleOicProcessedRecord,
        FlextTargetOracleOicRecordProcessor,
        processors,
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
        FlextTargetOracleOicAuthenticator,
        FlextTargetOracleOicUtilities,
        FlextTargetOracleOicUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
