"""FlextTargetOracleOic - Oracle Integration Cloud Target using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core._utilities.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import (
        FlextDecorators,
        FlextDecorators as d,
        FlextExceptions,
        FlextExceptions as e,
        FlextHandlers,
        FlextHandlers as h,
        FlextMixins,
        FlextMixins as x,
        FlextModels,
        FlextResult,
        FlextResult as r,
        FlextService,
        FlextService as s,
    )
    from flext_meltano import FlextMeltanoBridge, FlextMeltanoSettings
    from flext_target_oracle_oic.__version__ import __version__, __version_info__
    from flext_target_oracle_oic.application import OICTargetOrchestrator
    from flext_target_oracle_oic.cli import main, main as cli_main
    from flext_target_oracle_oic.client import OICClient
    from flext_target_oracle_oic.connection import OICConnection, OICConnectionSettings
    from flext_target_oracle_oic.constants import (
        FlextTargetOracleOicConstants,
        FlextTargetOracleOicConstants as c,
    )
    from flext_target_oracle_oic.models import (
        FlextTargetOracleOicModels,
        FlextTargetOracleOicModels as m,
    )
    from flext_target_oracle_oic.patterns import (
        OICDataTransformer,
        OICEntryManager,
        OICSchemaMapper,
        OICTypeConverter,
    )
    from flext_target_oracle_oic.protocols import (
        FlextTargetOracleOicProtocols,
        FlextTargetOracleOicProtocols as p,
    )
    from flext_target_oracle_oic.singer import OICRecordProcessor
    from flext_target_oracle_oic.target_client import (
        ConnectionsSink,
        IntegrationsSink,
        LookupsSink,
        OICBaseSink,
        PackagesSink,
        TargetOracleOic,
        main as client_main,
    )
    from flext_target_oracle_oic.target_config import (
        OICOAuth2Authenticator,
        TargetOracleOicConfig,
        create_config_from_dict,
        create_config_with_env_overrides,
        create_singer_config_schema,
    )
    from flext_target_oracle_oic.target_models import (
        create_oic_connection,
        create_oic_integration,
        create_oic_lookup,
        create_oic_package,
    )
    from flext_target_oracle_oic.typings import (
        FlextTargetOracleOicTypes,
        FlextTargetOracleOicTypes as t,
    )
    from flext_target_oracle_oic.utilities import (
        FlextTargetOracleOicUtilities,
        FlextTargetOracleOicUtilities as u,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "ConnectionsSink": ("flext_target_oracle_oic.target_client", "ConnectionsSink"),
    "FlextDecorators": ("flext_core", "FlextDecorators"),
    "FlextExceptions": ("flext_core", "FlextExceptions"),
    "FlextHandlers": ("flext_core", "FlextHandlers"),
    "FlextMeltanoBridge": ("flext_meltano", "FlextMeltanoBridge"),
    "FlextMeltanoSettings": ("flext_meltano", "FlextMeltanoSettings"),
    "FlextMixins": ("flext_core", "FlextMixins"),
    "FlextModels": ("flext_core", "FlextModels"),
    "FlextResult": ("flext_core", "FlextResult"),
    "FlextService": ("flext_core", "FlextService"),
    "FlextTargetOracleOicConstants": (
        "flext_target_oracle_oic.constants",
        "FlextTargetOracleOicConstants",
    ),
    "FlextTargetOracleOicModels": (
        "flext_target_oracle_oic.models",
        "FlextTargetOracleOicModels",
    ),
    "FlextTargetOracleOicProtocols": (
        "flext_target_oracle_oic.protocols",
        "FlextTargetOracleOicProtocols",
    ),
    "FlextTargetOracleOicTypes": (
        "flext_target_oracle_oic.typings",
        "FlextTargetOracleOicTypes",
    ),
    "FlextTargetOracleOicUtilities": (
        "flext_target_oracle_oic.utilities",
        "FlextTargetOracleOicUtilities",
    ),
    "IntegrationsSink": ("flext_target_oracle_oic.target_client", "IntegrationsSink"),
    "LookupsSink": ("flext_target_oracle_oic.target_client", "LookupsSink"),
    "OICBaseSink": ("flext_target_oracle_oic.target_client", "OICBaseSink"),
    "OICClient": ("flext_target_oracle_oic.client", "OICClient"),
    "OICConnection": ("flext_target_oracle_oic.connection", "OICConnection"),
    "OICConnectionSettings": (
        "flext_target_oracle_oic.connection",
        "OICConnectionSettings",
    ),
    "OICDataTransformer": ("flext_target_oracle_oic.patterns", "OICDataTransformer"),
    "OICEntryManager": ("flext_target_oracle_oic.patterns", "OICEntryManager"),
    "OICOAuth2Authenticator": (
        "flext_target_oracle_oic.target_config",
        "OICOAuth2Authenticator",
    ),
    "OICRecordProcessor": ("flext_target_oracle_oic.singer", "OICRecordProcessor"),
    "OICSchemaMapper": ("flext_target_oracle_oic.patterns", "OICSchemaMapper"),
    "OICTargetOrchestrator": (
        "flext_target_oracle_oic.application",
        "OICTargetOrchestrator",
    ),
    "OICTypeConverter": ("flext_target_oracle_oic.patterns", "OICTypeConverter"),
    "PackagesSink": ("flext_target_oracle_oic.target_client", "PackagesSink"),
    "TargetOracleOic": ("flext_target_oracle_oic.target_client", "TargetOracleOic"),
    "TargetOracleOicConfig": (
        "flext_target_oracle_oic.target_config",
        "TargetOracleOicConfig",
    ),
    "__version__": ("flext_target_oracle_oic.__version__", "__version__"),
    "__version_info__": ("flext_target_oracle_oic.__version__", "__version_info__"),
    "c": ("flext_target_oracle_oic.constants", "FlextTargetOracleOicConstants"),
    "cli_main": ("flext_target_oracle_oic.cli", "main"),
    "client_main": ("flext_target_oracle_oic.target_client", "main"),
    "create_config_from_dict": (
        "flext_target_oracle_oic.target_config",
        "create_config_from_dict",
    ),
    "create_config_with_env_overrides": (
        "flext_target_oracle_oic.target_config",
        "create_config_with_env_overrides",
    ),
    "create_oic_connection": (
        "flext_target_oracle_oic.target_models",
        "create_oic_connection",
    ),
    "create_oic_integration": (
        "flext_target_oracle_oic.target_models",
        "create_oic_integration",
    ),
    "create_oic_lookup": ("flext_target_oracle_oic.target_models", "create_oic_lookup"),
    "create_oic_package": (
        "flext_target_oracle_oic.target_models",
        "create_oic_package",
    ),
    "create_singer_config_schema": (
        "flext_target_oracle_oic.target_config",
        "create_singer_config_schema",
    ),
    "d": ("flext_core", "FlextDecorators"),
    "e": ("flext_core", "FlextExceptions"),
    "h": ("flext_core", "FlextHandlers"),
    "m": ("flext_target_oracle_oic.models", "FlextTargetOracleOicModels"),
    "main": ("flext_target_oracle_oic.cli", "main"),
    "p": ("flext_target_oracle_oic.protocols", "FlextTargetOracleOicProtocols"),
    "r": ("flext_core", "FlextResult"),
    "s": ("flext_core", "FlextService"),
    "t": ("flext_target_oracle_oic.typings", "FlextTargetOracleOicTypes"),
    "u": ("flext_target_oracle_oic.utilities", "FlextTargetOracleOicUtilities"),
    "x": ("flext_core", "FlextMixins"),
}

__all__ = [
    "ConnectionsSink",
    "FlextDecorators",
    "FlextExceptions",
    "FlextHandlers",
    "FlextMeltanoBridge",
    "FlextMeltanoSettings",
    "FlextMixins",
    "FlextModels",
    "FlextResult",
    "FlextService",
    "FlextTargetOracleOicConstants",
    "FlextTargetOracleOicModels",
    "FlextTargetOracleOicProtocols",
    "FlextTargetOracleOicTypes",
    "FlextTargetOracleOicUtilities",
    "IntegrationsSink",
    "LookupsSink",
    "OICBaseSink",
    "OICClient",
    "OICConnection",
    "OICConnectionSettings",
    "OICDataTransformer",
    "OICEntryManager",
    "OICOAuth2Authenticator",
    "OICRecordProcessor",
    "OICSchemaMapper",
    "OICTargetOrchestrator",
    "OICTypeConverter",
    "PackagesSink",
    "TargetOracleOic",
    "TargetOracleOicConfig",
    "__version__",
    "__version_info__",
    "c",
    "cli_main",
    "client_main",
    "create_config_from_dict",
    "create_config_with_env_overrides",
    "create_oic_connection",
    "create_oic_integration",
    "create_oic_lookup",
    "create_oic_package",
    "create_singer_config_schema",
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


def __getattr__(name: str) -> Any:  # noqa: ANN401
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
