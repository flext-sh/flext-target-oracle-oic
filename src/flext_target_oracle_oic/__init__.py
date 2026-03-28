# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext target oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_meltano import d, e, h, r, s, x

    from flext_target_oracle_oic import application, connection, patterns, singer
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
    from flext_target_oracle_oic.application.orchestrator import (
        FlextTargetOracleOicOrchestrator,
    )
    from flext_target_oracle_oic.cli import main
    from flext_target_oracle_oic.connection.connection import (
        FlextTargetOracleOicConnection,
    )
    from flext_target_oracle_oic.connection.settings import (
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
    )
    from flext_target_oracle_oic.target_client import (
        FlextTargetOracleOicConnectionsSink,
        FlextTargetOracleOicIntegrationsSink,
        FlextTargetOracleOicLookupsSink,
        FlextTargetOracleOicPackagesSink,
    )
    from flext_target_oracle_oic.target_config import FlextTargetOracleOicAuthenticator
    from flext_target_oracle_oic.typings import (
        FlextTargetOracleOicTypes,
        FlextTargetOracleOicTypes as t,
    )
    from flext_target_oracle_oic.utilities import (
        FlextTargetOracleOicUtilities,
        FlextTargetOracleOicUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTargetOracleOic": ["flext_target_oracle_oic.target", "FlextTargetOracleOic"],
    "FlextTargetOracleOicAuthenticator": [
        "flext_target_oracle_oic.target_config",
        "FlextTargetOracleOicAuthenticator",
    ],
    "FlextTargetOracleOicBaseSink": [
        "flext_target_oracle_oic.target",
        "FlextTargetOracleOicBaseSink",
    ],
    "FlextTargetOracleOicConfig": [
        "flext_target_oracle_oic.settings",
        "FlextTargetOracleOicConfig",
    ],
    "FlextTargetOracleOicConnection": [
        "flext_target_oracle_oic.connection.connection",
        "FlextTargetOracleOicConnection",
    ],
    "FlextTargetOracleOicConnectionSettings": [
        "flext_target_oracle_oic.connection.settings",
        "FlextTargetOracleOicConnectionSettings",
    ],
    "FlextTargetOracleOicConnectionsSink": [
        "flext_target_oracle_oic.target_client",
        "FlextTargetOracleOicConnectionsSink",
    ],
    "FlextTargetOracleOicConstants": [
        "flext_target_oracle_oic.constants",
        "FlextTargetOracleOicConstants",
    ],
    "FlextTargetOracleOicDataTransformer": [
        "flext_target_oracle_oic.patterns.oic_patterns",
        "FlextTargetOracleOicDataTransformer",
    ],
    "FlextTargetOracleOicEntryManager": [
        "flext_target_oracle_oic.patterns.oic_patterns",
        "FlextTargetOracleOicEntryManager",
    ],
    "FlextTargetOracleOicIntegrationsSink": [
        "flext_target_oracle_oic.target_client",
        "FlextTargetOracleOicIntegrationsSink",
    ],
    "FlextTargetOracleOicLookupsSink": [
        "flext_target_oracle_oic.target_client",
        "FlextTargetOracleOicLookupsSink",
    ],
    "FlextTargetOracleOicModels": [
        "flext_target_oracle_oic.models",
        "FlextTargetOracleOicModels",
    ],
    "FlextTargetOracleOicOrchestrator": [
        "flext_target_oracle_oic.application.orchestrator",
        "FlextTargetOracleOicOrchestrator",
    ],
    "FlextTargetOracleOicPackagesSink": [
        "flext_target_oracle_oic.target_client",
        "FlextTargetOracleOicPackagesSink",
    ],
    "FlextTargetOracleOicProcessedRecord": [
        "flext_target_oracle_oic.singer.processors",
        "FlextTargetOracleOicProcessedRecord",
    ],
    "FlextTargetOracleOicProtocols": [
        "flext_target_oracle_oic.protocols",
        "FlextTargetOracleOicProtocols",
    ],
    "FlextTargetOracleOicRecordProcessor": [
        "flext_target_oracle_oic.singer.processors",
        "FlextTargetOracleOicRecordProcessor",
    ],
    "FlextTargetOracleOicSchemaMapper": [
        "flext_target_oracle_oic.patterns.oic_patterns",
        "FlextTargetOracleOicSchemaMapper",
    ],
    "FlextTargetOracleOicTypeConverter": [
        "flext_target_oracle_oic.patterns.oic_patterns",
        "FlextTargetOracleOicTypeConverter",
    ],
    "FlextTargetOracleOicTypes": [
        "flext_target_oracle_oic.typings",
        "FlextTargetOracleOicTypes",
    ],
    "FlextTargetOracleOicUtilities": [
        "flext_target_oracle_oic.utilities",
        "FlextTargetOracleOicUtilities",
    ],
    "__all__": ["flext_target_oracle_oic.__version__", "__all__"],
    "__author__": ["flext_target_oracle_oic.__version__", "__author__"],
    "__author_email__": ["flext_target_oracle_oic.__version__", "__author_email__"],
    "__description__": ["flext_target_oracle_oic.__version__", "__description__"],
    "__license__": ["flext_target_oracle_oic.__version__", "__license__"],
    "__title__": ["flext_target_oracle_oic.__version__", "__title__"],
    "__url__": ["flext_target_oracle_oic.__version__", "__url__"],
    "__version__": ["flext_target_oracle_oic.__version__", "__version__"],
    "__version_info__": ["flext_target_oracle_oic.__version__", "__version_info__"],
    "application": ["flext_target_oracle_oic.application", ""],
    "c": ["flext_target_oracle_oic.constants", "FlextTargetOracleOicConstants"],
    "connection": ["flext_target_oracle_oic.connection", ""],
    "d": ["flext_meltano", "d"],
    "e": ["flext_meltano", "e"],
    "h": ["flext_meltano", "h"],
    "logger": ["flext_target_oracle_oic.connection.settings", "logger"],
    "m": ["flext_target_oracle_oic.models", "FlextTargetOracleOicModels"],
    "main": ["flext_target_oracle_oic.cli", "main"],
    "p": ["flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"],
    "patterns": ["flext_target_oracle_oic.patterns", ""],
    "r": ["flext_meltano", "r"],
    "s": ["flext_meltano", "s"],
    "singer": ["flext_target_oracle_oic.singer", ""],
    "t": ["flext_target_oracle_oic.typings", "FlextTargetOracleOicTypes"],
    "u": ["flext_target_oracle_oic.utilities", "FlextTargetOracleOicUtilities"],
    "x": ["flext_meltano", "x"],
}

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
    "FlextTargetOracleOicTypeConverter",
    "FlextTargetOracleOicTypes",
    "FlextTargetOracleOicUtilities",
    "__all__",
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
    "connection",
    "d",
    "e",
    "h",
    "logger",
    "m",
    "main",
    "p",
    "patterns",
    "r",
    "s",
    "singer",
    "t",
    "u",
    "x",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
