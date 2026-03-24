# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
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
    from flext_target_oracle_oic.application.orchestrator import OICTargetOrchestrator
    from flext_target_oracle_oic.cli import main
    from flext_target_oracle_oic.connection.connection import OICConnection
    from flext_target_oracle_oic.connection.settings import (
        OICConnectionSettings,
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
        OICDataTransformer,
        OICEntryManager,
        OICSchemaMapper,
        OICTypeConverter,
    )
    from flext_target_oracle_oic.protocols import (
        FlextTargetOracleOicProtocols,
        FlextTargetOracleOicProtocols as p,
    )
    from flext_target_oracle_oic.settings import TargetOracleOicConfig
    from flext_target_oracle_oic.singer.processors import (
        OICProcessedRecord,
        OICRecordProcessor,
    )
    from flext_target_oracle_oic.target import OICBaseSink, TargetOracleOic
    from flext_target_oracle_oic.target_client import (
        ConnectionsSink,
        IntegrationsSink,
        LookupsSink,
        PackagesSink,
    )
    from flext_target_oracle_oic.target_config import (
        OICOAuth2Authenticator,
        create_config_from_dict,
        create_config_with_env_overrides,
        create_singer_config_schema,
    )
    from flext_target_oracle_oic.typings import (
        FlextTargetOracleOicTypes,
        FlextTargetOracleOicTypes as t,
    )
    from flext_target_oracle_oic.utilities import (
        FlextTargetOracleOicUtilities,
        FlextTargetOracleOicUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, tuple[str, str]] = {
    "ConnectionsSink": ("flext_target_oracle_oic.target_client", "ConnectionsSink"),
    "FlextTargetOracleOicConstants": ("flext_target_oracle_oic.constants", "FlextTargetOracleOicConstants"),
    "FlextTargetOracleOicModels": ("flext_target_oracle_oic.models", "FlextTargetOracleOicModels"),
    "FlextTargetOracleOicProtocols": ("flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"),
    "FlextTargetOracleOicTypes": ("flext_target_oracle_oic.typings", "FlextTargetOracleOicTypes"),
    "FlextTargetOracleOicUtilities": ("flext_target_oracle_oic.utilities", "FlextTargetOracleOicUtilities"),
    "IntegrationsSink": ("flext_target_oracle_oic.target_client", "IntegrationsSink"),
    "LookupsSink": ("flext_target_oracle_oic.target_client", "LookupsSink"),
    "OICBaseSink": ("flext_target_oracle_oic.target", "OICBaseSink"),
    "OICConnection": ("flext_target_oracle_oic.connection.connection", "OICConnection"),
    "OICConnectionSettings": ("flext_target_oracle_oic.connection.settings", "OICConnectionSettings"),
    "OICDataTransformer": ("flext_target_oracle_oic.patterns.oic_patterns", "OICDataTransformer"),
    "OICEntryManager": ("flext_target_oracle_oic.patterns.oic_patterns", "OICEntryManager"),
    "OICOAuth2Authenticator": ("flext_target_oracle_oic.target_config", "OICOAuth2Authenticator"),
    "OICProcessedRecord": ("flext_target_oracle_oic.singer.processors", "OICProcessedRecord"),
    "OICRecordProcessor": ("flext_target_oracle_oic.singer.processors", "OICRecordProcessor"),
    "OICSchemaMapper": ("flext_target_oracle_oic.patterns.oic_patterns", "OICSchemaMapper"),
    "OICTargetOrchestrator": ("flext_target_oracle_oic.application.orchestrator", "OICTargetOrchestrator"),
    "OICTypeConverter": ("flext_target_oracle_oic.patterns.oic_patterns", "OICTypeConverter"),
    "PackagesSink": ("flext_target_oracle_oic.target_client", "PackagesSink"),
    "TargetOracleOic": ("flext_target_oracle_oic.target", "TargetOracleOic"),
    "TargetOracleOicConfig": ("flext_target_oracle_oic.settings", "TargetOracleOicConfig"),
    "__all__": ("flext_target_oracle_oic.__version__", "__all__"),
    "__author__": ("flext_target_oracle_oic.__version__", "__author__"),
    "__author_email__": ("flext_target_oracle_oic.__version__", "__author_email__"),
    "__description__": ("flext_target_oracle_oic.__version__", "__description__"),
    "__license__": ("flext_target_oracle_oic.__version__", "__license__"),
    "__title__": ("flext_target_oracle_oic.__version__", "__title__"),
    "__url__": ("flext_target_oracle_oic.__version__", "__url__"),
    "__version__": ("flext_target_oracle_oic.__version__", "__version__"),
    "__version_info__": ("flext_target_oracle_oic.__version__", "__version_info__"),
    "application": ("flext_target_oracle_oic.application", ""),
    "c": ("flext_target_oracle_oic.constants", "FlextTargetOracleOicConstants"),
    "connection": ("flext_target_oracle_oic.connection", ""),
    "create_config_from_dict": ("flext_target_oracle_oic.target_config", "create_config_from_dict"),
    "create_config_with_env_overrides": ("flext_target_oracle_oic.target_config", "create_config_with_env_overrides"),
    "create_singer_config_schema": ("flext_target_oracle_oic.target_config", "create_singer_config_schema"),
    "d": ("flext_meltano", "d"),
    "e": ("flext_meltano", "e"),
    "h": ("flext_meltano", "h"),
    "logger": ("flext_target_oracle_oic.connection.settings", "logger"),
    "m": ("flext_target_oracle_oic.models", "FlextTargetOracleOicModels"),
    "main": ("flext_target_oracle_oic.cli", "main"),
    "p": ("flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"),
    "patterns": ("flext_target_oracle_oic.patterns", ""),
    "r": ("flext_meltano", "r"),
    "s": ("flext_meltano", "s"),
    "singer": ("flext_target_oracle_oic.singer", ""),
    "t": ("flext_target_oracle_oic.typings", "FlextTargetOracleOicTypes"),
    "u": ("flext_target_oracle_oic.utilities", "FlextTargetOracleOicUtilities"),
    "x": ("flext_meltano", "x"),
}

__all__ = [
    "ConnectionsSink",
    "FlextTargetOracleOicConstants",
    "FlextTargetOracleOicModels",
    "FlextTargetOracleOicProtocols",
    "FlextTargetOracleOicTypes",
    "FlextTargetOracleOicUtilities",
    "IntegrationsSink",
    "LookupsSink",
    "OICBaseSink",
    "OICConnection",
    "OICConnectionSettings",
    "OICDataTransformer",
    "OICEntryManager",
    "OICOAuth2Authenticator",
    "OICProcessedRecord",
    "OICRecordProcessor",
    "OICSchemaMapper",
    "OICTargetOrchestrator",
    "OICTypeConverter",
    "PackagesSink",
    "TargetOracleOic",
    "TargetOracleOicConfig",
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
    "create_config_from_dict",
    "create_config_with_env_overrides",
    "create_singer_config_schema",
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
