"""FlextTargetOracleOic - Oracle Integration Cloud Target using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_target_oracle_oic.__version__ import __version__, __version_info__

import importlib.metadata

from flext_core import FlextModels, FlextResult

# Use FLEXT Meltano wrapper instead of direct singer_sdk import (domain separation)
from flext_meltano import (
    FlextMeltanoBridge,
    FlextMeltanoConfig,
    FlextTarget as Target,
)

from flext_target_oracle_oic.application import OICTargetOrchestrator
from flext_target_oracle_oic.cli import main as cli_main
from flext_target_oracle_oic.client import OICClient
from flext_target_oracle_oic.config import TargetOracleOICConfig
from flext_target_oracle_oic.connection import (
    OICConnection as LegacyOICConnection,
    OICConnectionSettings as LegacyOICConnectionSettings,
)
from flext_target_oracle_oic.models import (
    FlextTargetOracleOicModels,
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
)
from flext_target_oracle_oic.patterns import (
    OICDataTransformer,
    OICEntryManager,
    OICSchemaMapper,
    OICTypeConverter,
)
from flext_target_oracle_oic.protocols import FlextTargetOracleOicProtocols
from flext_target_oracle_oic.singer import OICRecordProcessor
from flext_target_oracle_oic.target_client import (
    ConnectionsSink,
    IntegrationsSink,
    LookupsSink,
    OICBaseSink,
    PackagesSink,
    TargetOracleOIC,
    main as client_main,
)
from flext_target_oracle_oic.target_config import (
    OICOAuth2Authenticator,
    create_config_from_dict,
    create_config_with_env_overrides,
    create_singer_config_schema,
)
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
from flext_target_oracle_oic.target_models import (
    create_oic_connection,
    create_oic_integration,
    create_oic_lookup,
    create_oic_package,
)
from flext_target_oracle_oic.utilities import FlextTargetOracleOicUtilities
from flext_target_oracle_oic.version import VERSION, FlextTargetOracleOicVersion

try:
    __version__ = importlib.metadata.version("flext-target-oracle-oic")
    __version_info__: tuple[int | str, ...] = VERSION.version_info
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

from flext_target_oracle_oic.cli import main
from flext_target_oracle_oic.typings import FlextTargetOracleOicTypes

__all__: FlextTargetOracleOicTypes.Core.StringList = [
    "VERSION",
    "ConnectionsSink",
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextModels",
    "FlextResult",
    "FlextTargetOracleOicAPIError",
    "FlextTargetOracleOicAuthenticationError",
    "FlextTargetOracleOicConfigurationError",
    "FlextTargetOracleOicConnectionError",
    "FlextTargetOracleOicError",
    "FlextTargetOracleOicErrorDetails",
    "FlextTargetOracleOicInfrastructureError",
    "FlextTargetOracleOicModels",
    "FlextTargetOracleOicProcessingError",
    "FlextTargetOracleOicProtocols",
    "FlextTargetOracleOicTransformationError",
    "FlextTargetOracleOicUtilities",
    "FlextTargetOracleOicValidationError",
    "FlextTargetOracleOicVersion",
    "IntegrationsSink",
    "LegacyOICConnection",
    "LegacyOICConnectionSettings",
    "LookupsSink",
    "OICBaseSink",
    "OICClient",
    "OICConnection",
    "OICConnectionAction",
    "OICDataTransformation",
    "OICDataTransformer",
    "OICEntryManager",
    "OICIntegration",
    "OICIntegrationAction",
    "OICLookup",
    "OICOAuth2Authenticator",
    "OICPackage",
    "OICProject",
    "OICRecordProcessor",
    "OICSchedule",
    "OICSchemaMapper",
    "OICSchemaMapping",
    "OICTargetOrchestrator",
    "OICTypeConverter",
    "PackagesSink",
    "Target",
    "TargetOracleOIC",
    "TargetOracleOICConfig",
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
    "main",
]
