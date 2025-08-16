"""FlextTargetOracleOic - Oracle Integration Cloud Target using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

PEP8-compliant Oracle Integration Cloud target following flext-core architecture:
- Maximum composition from flext-core, flext-meltano, and flext-oracle-oic-ext
- Unified target_config.py for configuration management
- Unified target_client.py for target/loader/plugin functionality
- Unified target_models.py for all OIC data models
- Unified target_exceptions.py for error handling
- Zero tolerance for architectural violations
- 100% backward compatibility maintained
"""

from __future__ import annotations

import importlib.metadata

# Core flext-core imports
from flext_core import FlextResult, FlextValueObject

# === FLEXT-MELTANO COMPLETE INTEGRATION ===
# Re-export ALL flext-meltano facilities for full ecosystem integration
from flext_meltano import (
    BatchSink,
    FlextMeltanoBaseService,
    # Bridge integration
    FlextMeltanoBridge,
    # Configuration and validation
    FlextMeltanoConfig,
    FlextMeltanoEvent,
    # Enterprise services from flext-meltano.base
    FlextMeltanoTargetService,
    # Authentication patterns
    OAuthAuthenticator,
    # Typing definitions
    PropertiesList,
    Property,
    Sink,
    SQLSink,
    # Core Singer SDK classes (centralized from flext-meltano)
    Stream,
    Tap,
    Target,
    create_meltano_target_service,
    # Testing utilities
    get_tap_test_class,
    # Singer typing utilities (centralized)
    singer_typing,
)

# === PEP8 UNIFIED IMPORTS - NEW STRUCTURE ===
# Unified configuration management
from flext_target_oracle_oic.target_config import (
    OICAuthConfig,
    OICConnectionConfig,
    OICDeploymentConfig,
    OICEntityConfig,
    OICOAuth2Authenticator,
    OICProcessingConfig,
    TargetOracleOICConfig,
    create_config_from_dict,
    create_config_with_env_overrides,
    create_singer_config_schema,
)

# Unified client implementation (target + loader + plugin)
from flext_target_oracle_oic.target_client import (
    ConnectionsSink,
    IntegrationsSink,
    LookupsSink,
    OICBaseSink,
    PackagesSink,
    TargetOracleOIC,
    main as client_main,
)

# Unified data models
from flext_target_oracle_oic.models import (
    OICConnection,
    OICConnectionAction,
    OICDataTransformation,
    OICIntegration,
    OICIntegrationAction,
    OICLookup,
    OICPackage,
    OICProject,
    OICSchemaMapping,
    OICSchedule,
    create_oic_connection,
    create_oic_integration,
    create_oic_lookup,
    create_oic_package,
)

# Unified exception handling (factory pattern)
from flext_target_oracle_oic.target_exceptions import (
    FlextTargetOracleOicAPIError,
    FlextTargetOracleOicAuthenticationError,
    FlextTargetOracleOicConfigurationError,
    FlextTargetOracleOicConnectionError,
    FlextTargetOracleOicError,
    FlextTargetOracleOicErrorDetails,
    FlextTargetOracleOicInfrastructureError,
    FlextTargetOracleOicProcessingError,
    FlextTargetOracleOicTransformationError,
    FlextTargetOracleOicValidationError,
    create_api_error,
    create_authentication_error,
    create_configuration_error,
    create_connection_error,
    create_processing_error,
    create_validation_error,
)

# === BACKWARD COMPATIBILITY IMPORTS ===
# Import legacy modules for 100% backward compatibility (optional)
from flext_target_oracle_oic.application import OICTargetOrchestrator
from flext_target_oracle_oic.cli import main as cli_main
from flext_target_oracle_oic.client import OICClient
from flext_target_oracle_oic.connection import OICConnection as LegacyOICConnection
from flext_target_oracle_oic.connection import (
    OICConnectionConfig as LegacyOICConnectionConfig,
)
from flext_target_oracle_oic.patterns import (
    OICDataTransformer,
    OICEntryManager,
    OICSchemaMapper,
    OICTypeConverter,
)
from flext_target_oracle_oic.singer import OICRecordProcessor

# Version information
try:
    __version__ = importlib.metadata.version("flext-target-oracle-oic")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


# ===============================================================================
# MAIN CLASSES AND ALIASES
# ===============================================================================


class FlextTargetOracleOic(TargetOracleOIC):
    """FlextTargetOracleOic - Main class following flext patterns with new structure."""


# Backward compatibility alias - use new unified config
FlextTargetOracleOicConfig = TargetOracleOICConfig

# Type alias for FlextResult
FlextTargetOracleOicResult = FlextResult


# ===============================================================================
# CLI ENTRY POINT
# ===============================================================================


def main() -> None:
    """CLI entry point for flext-target-oracle-oic."""  # Use new unified client main
    client_main()


# ===============================================================================
# EXPORTS - PEP8 ORGANIZED
# ===============================================================================

__all__: list[str] = [
    # === FLEXT-MELTANO COMPLETE RE-EXPORTS ===
    "BatchSink",
    "FlextMeltanoBaseService",
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextMeltanoEvent",
    "FlextMeltanoTargetService",
    "OAuthAuthenticator",
    "PropertiesList",
    "Property",
    "Sink",
    "SQLSink",
    "Stream",
    "Tap",
    "Target",
    "create_meltano_target_service",
    "get_tap_test_class",
    "singer_typing",
    # === CORE RE-EXPORTS ===
    "FlextResult",
    "FlextValueObject",
    # === PRIMARY CLASSES ===
    "FlextTargetOracleOic",
    "TargetOracleOIC",
    # === UNIFIED CONFIGURATION ===
    "FlextTargetOracleOicConfig",  # Backward compatibility alias
    "OICAuthConfig",
    "OICConnectionConfig",
    "OICDeploymentConfig",
    "OICEntityConfig",
    "OICOAuth2Authenticator",
    "OICProcessingConfig",
    "TargetOracleOICConfig",
    "create_config_from_dict",
    "create_config_with_env_overrides",
    "create_singer_config_schema",
    # === UNIFIED CLIENT (SINKS) ===
    "ConnectionsSink",
    "IntegrationsSink",
    "LookupsSink",
    "OICBaseSink",
    "PackagesSink",
    # === UNIFIED MODELS ===
    "OICConnection",
    "OICConnectionAction",
    "OICDataTransformation",
    "OICIntegration",
    "OICIntegrationAction",
    "OICLookup",
    "OICPackage",
    "OICProject",
    "OICSchemaMapping",
    "OICSchedule",
    "create_oic_connection",
    "create_oic_integration",
    "create_oic_lookup",
    "create_oic_package",
    # === UNIFIED EXCEPTIONS ===
    "FlextTargetOracleOicAPIError",
    "FlextTargetOracleOicAuthenticationError",
    "FlextTargetOracleOicConfigurationError",
    "FlextTargetOracleOicConnectionError",
    "FlextTargetOracleOicError",
    "FlextTargetOracleOicErrorDetails",
    "FlextTargetOracleOicInfrastructureError",
    "FlextTargetOracleOicProcessingError",
    "FlextTargetOracleOicResult",
    "FlextTargetOracleOicTransformationError",
    "FlextTargetOracleOicValidationError",
    "create_api_error",
    "create_authentication_error",
    "create_configuration_error",
    "create_connection_error",
    "create_processing_error",
    "create_validation_error",
    # === BACKWARD COMPATIBILITY (LEGACY) ===
    "OICClient",  # May be None if legacy not available
    "OICDataTransformer",  # May be None if legacy not available
    "OICEntryManager",  # May be None if legacy not available
    "OICRecordProcessor",  # May be None if legacy not available
    "OICSchemaMapper",  # May be None if legacy not available
    "OICTargetOrchestrator",  # May be None if legacy not available
    "OICTypeConverter",  # May be None if legacy not available
    # === METADATA ===
    "__version__",
    "__version_info__",
    "main",
]


# ===============================================================================
# CLI SUPPORT FOR DIRECT EXECUTION
# ===============================================================================

if __name__ == "__main__":
    main()
