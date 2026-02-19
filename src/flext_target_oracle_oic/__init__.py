"""FlextTargetOracleOic - Oracle Integration Cloud Target using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_core import FlextModels, FlextResult

# Use FLEXT Meltano wrapper instead of direct singer_sdk import (domain separation)
from flext_meltano import (
    FlextMeltanoBridge,
    FlextMeltanoSettings,
)
from flext_target_oracle_oic.__version__ import __version__, __version_info__
from flext_target_oracle_oic.application import OICTargetOrchestrator
from flext_target_oracle_oic.cli import main, main as cli_main
from flext_target_oracle_oic.client import OICClient
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
    m,
    m_target_oracle_oic,
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
from flext_target_oracle_oic.typings import t
from flext_target_oracle_oic.utilities import FlextTargetOracleOicUtilities

__all__: list[str] = [
    "ConnectionsSink",
    "FlextMeltanoBridge",
    "FlextMeltanoSettings",
    "FlextModels",
    "FlextResult",
    "FlextTargetOracleOicModels",
    "FlextTargetOracleOicProtocols",
    "FlextTargetOracleOicUtilities",
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
    "TargetOracleOic",
    "TargetOracleOicConfig",
    "__version__",
    "__version_info__",
    "cli_main",
    "client_main",
    "create_config_from_dict",
    "create_config_with_env_overrides",
    "create_oic_connection",
    "create_oic_integration",
    "create_oic_lookup",
    "create_oic_package",
    "create_singer_config_schema",
    "m",
    "m_target_oracle_oic",
    "main",
    "t",
]
