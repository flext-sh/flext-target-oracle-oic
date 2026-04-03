# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext target oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_target_oracle_oic.__version__ import (
    __all__,
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
        oic_patterns,
        orchestrator,
        patterns,
        processors,
        protocols,
        service_runtime,
        settings,
        singer,
        target,
        typings,
        utilities,
    )
    from flext_target_oracle_oic._utilities import FlextTargetOracleOicServiceRuntime
    from flext_target_oracle_oic.api import FlextTargetOracleOicService
    from flext_target_oracle_oic.application import FlextTargetOracleOicOrchestrator
    from flext_target_oracle_oic.cli import main
    from flext_target_oracle_oic.connection import (
        FlextTargetOracleOicConnection,
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
    from flext_target_oracle_oic.patterns import FlextTargetOracleOicTypeConverter
    from flext_target_oracle_oic.protocols import (
        FlextTargetOracleOicProtocols,
        FlextTargetOracleOicProtocols as p,
    )
    from flext_target_oracle_oic.settings import FlextTargetOracleOicConfig
    from flext_target_oracle_oic.singer import (
        FlextTargetOracleOicProcessedRecord,
        FlextTargetOracleOicRecordProcessor,
    )
    from flext_target_oracle_oic.target import FlextTargetOracleOicBaseSink, logger
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
        "FlextTargetOracleOicAuthenticator": "flext_target_oracle_oic.utilities",
        "FlextTargetOracleOicBaseSink": "flext_target_oracle_oic.target",
        "FlextTargetOracleOicConfig": "flext_target_oracle_oic.settings",
        "FlextTargetOracleOicConstants": "flext_target_oracle_oic.constants",
        "FlextTargetOracleOicModels": "flext_target_oracle_oic.models",
        "FlextTargetOracleOicProtocols": "flext_target_oracle_oic.protocols",
        "FlextTargetOracleOicService": "flext_target_oracle_oic.api",
        "FlextTargetOracleOicTypes": "flext_target_oracle_oic.typings",
        "FlextTargetOracleOicUtilities": "flext_target_oracle_oic.utilities",
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
        "logger": "flext_target_oracle_oic.target",
        "m": ("flext_target_oracle_oic.models", "FlextTargetOracleOicModels"),
        "main": "flext_target_oracle_oic.cli",
        "models": "flext_target_oracle_oic.models",
        "oic_patterns": "flext_target_oracle_oic.oic_patterns",
        "orchestrator": "flext_target_oracle_oic.orchestrator",
        "p": ("flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"),
        "patterns": "flext_target_oracle_oic.patterns",
        "processors": "flext_target_oracle_oic.processors",
        "protocols": "flext_target_oracle_oic.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "service_runtime": "flext_target_oracle_oic.service_runtime",
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


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__all__",
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
