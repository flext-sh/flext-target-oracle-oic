"""FlextTargetOracleOic - Oracle Integration Cloud Target using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

import importlib.metadata

from flext_core import FlextModels, FlextResult, FlextTypes
from flext_meltano import (
    FlextMeltanoBridge,
    FlextMeltanoConfig,
    Target,
)

from flext_target_oracle_oic.application import OICTargetOrchestrator
from flext_target_oracle_oic.cli import main as cli_main
from flext_target_oracle_oic.client import OICClient
from flext_target_oracle_oic.connection import (
    OICConnection as LegacyOICConnection,
    OICConnectionManager,
    OICConnectionPool,
    OICConnectionSettings as LegacyOICConnectionSettings,
)
from flext_target_oracle_oic.models import (
    OICConnection,
    OICConnectionAction,
    OICDataTransformation,
    OICIntegration,
    OICIntegrationAction,
    OICLookup,
    OICPackage,
    OICProject,
    OICSchedule,
    OICSchemaMapping,
    OICTargetModel,
    OICTargetRecord,
    create_oic_connection,
    create_oic_integration,
    create_oic_lookup,
    create_oic_package,
)
from flext_target_oracle_oic.patterns import (
    OICDataTransformer,
    OICEntryManager,
    OICSchemaMapper,
    OICTargetPattern,
    OICTypeConverter,
)
from flext_target_oracle_oic.scripts.generate_config import (
    generate_config as generate_config,
    main as generate_config_main,
)
from flext_target_oracle_oic.singer import OICRecordProcessor
from flext_target_oracle_oic.target_client import (
    ConnectionsSink,
    FlextTargetOracleOIC,
    IntegrationsSink,
    LookupsSink,
    OICBaseSink,
    OICTargetClient,
    PackagesSink,
    TargetOracleOIC,
    main as client_main,
)
from flext_target_oracle_oic.target_config import (
    FlextTargetOracleOICConfig,
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
from flext_target_oracle_oic.target_exceptions import (
    FlextTargetOracleOicAPIError,
    FlextTargetOracleOicAuthenticationError,
    FlextTargetOracleOicConfigurationError,
    FlextTargetOracleOICConnectionError,
    FlextTargetOracleOicConnectionError,
    FlextTargetOracleOICError,
    FlextTargetOracleOicError,
    FlextTargetOracleOicErrorDetails,
    FlextTargetOracleOicInfrastructureError,
    FlextTargetOracleOicProcessingError,
    FlextTargetOracleOicTransformationError,
    FlextTargetOracleOICValidationError,
    FlextTargetOracleOicValidationError,
    create_api_error,
    create_authentication_error,
    create_configuration_error,
    create_connection_error,
    create_processing_error,
    create_validation_error,
)

# Version information
try:
    __version__ = importlib.metadata.version("flext-target-oracle-oic")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


# Import main classes and aliases from dedicated modules
# Import main function from CLI module
from flext_target_oracle_oic.cli import main

# ===============================================================================
# EXPORTS - PEP8 ORGANIZED
# ===============================================================================

__all__: FlextTypes.Core.StringList = [
    # === UNIFIED CLIENT (SINKS) ===
    "ConnectionsSink",
    # === FLEXT-MELTANO RE-EXPORTS ===
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextModels",
    # === CORE RE-EXPORTS ===
    "FlextResult",
    "FlextTargetOracleOIC",
    "FlextTargetOracleOICConfig",
    "FlextTargetOracleOICConnectionError",
    "FlextTargetOracleOICError",
    "FlextTargetOracleOICValidationError",
    # === PRIMARY CLASSES ===
    "FlextTargetOracleOic",
    # === UNIFIED EXCEPTIONS ===
    "FlextTargetOracleOicAPIError",
    "FlextTargetOracleOicAuthenticationError",
    # === UNIFIED CONFIGURATION ===
    "FlextTargetOracleOicConfig",  # Backward compatibility alias
    "FlextTargetOracleOicConfigurationError",
    "FlextTargetOracleOicConnectionError",
    "FlextTargetOracleOicError",
    "FlextTargetOracleOicErrorDetails",
    "FlextTargetOracleOicInfrastructureError",
    "FlextTargetOracleOicProcessingError",
    "FlextTargetOracleOicResult",
    "FlextTargetOracleOicTransformationError",
    "FlextTargetOracleOicValidationError",
    "IntegrationsSink",
    "LegacyOICConnection",
    "LegacyOICConnectionSettings",
    "LookupsSink",
    "OICAuthConfig",
    "OICBaseSink",
    # === BACKWARD COMPATIBILITY (LEGACY) ===
    "OICClient",  # May be None if legacy not available
    # === UNIFIED MODELS ===
    "OICConnection",
    "OICConnectionAction",
    "OICConnectionConfig",
    # === CONNECTION MANAGEMENT ===
    "OICConnectionManager",
    "OICConnectionPool",
    "OICDataTransformation",
    "OICDataTransformer",  # May be None if legacy not available
    "OICDeploymentConfig",
    "OICEntityConfig",
    "OICEntryManager",  # May be None if legacy not available
    "OICIntegration",
    "OICIntegrationAction",
    "OICLookup",
    "OICOAuth2Authenticator",
    "OICPackage",
    "OICProcessingConfig",
    "OICProject",
    "OICRecordProcessor",  # May be None if legacy not available
    "OICSchedule",
    "OICSchemaMapper",  # May be None if legacy not available
    "OICSchemaMapping",
    "OICTargetClient",
    "OICTargetModel",
    "OICTargetOrchestrator",  # May be None if legacy not available
    "OICTargetPattern",
    "OICTargetRecord",
    "OICTypeConverter",  # May be None if legacy not available
    "PackagesSink",
    "Target",
    "TargetOracleOIC",
    "TargetOracleOICConfig",
    # === METADATA ===
    "__version__",
    "__version_info__",
    "cli_main",
    "client_main",
    "create_api_error",
    "create_authentication_error",
    "create_config_from_dict",
    "create_config_with_env_overrides",
    "create_configuration_error",
    "create_connection_error",
    "create_oic_connection",
    "create_oic_integration",
    "create_oic_lookup",
    "create_oic_package",
    "create_processing_error",
    "create_singer_config_schema",
    "create_validation_error",
    # === SCRIPT UTILITIES ===
    "generate_config",
    "generate_config_main",
    "main",
]
