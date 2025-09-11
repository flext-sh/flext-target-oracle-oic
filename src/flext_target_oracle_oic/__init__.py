"""Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_core import FlextTypes

"""FlextTargetOracleOic - Oracle Integration Cloud Target using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""


import importlib.metadata

# Core flext-core imports
from flext_core import FlextLogger, FlextModels, FlextResult

# === FLEXT-MELTANO INTEGRATION (ACTUAL EXPORTS) ===
from flext_meltano import (
    # Bridge integration
    FlextMeltanoBridge,
    # Configuration and validation
    FlextMeltanoConfig,
)

# === BACKWARD COMPATIBILITY IMPORTS ===
# Import legacy modules for 100% backward compatibility (optional)
from flext_target_oracle_oic.application import OICTargetOrchestrator
from flext_target_oracle_oic.cli import main as cli_main
from flext_target_oracle_oic.client import OICClient
from flext_target_oracle_oic.connection import (
    OICConnection as LegacyOICConnection,
    OICConnectionSettings as LegacyOICConnectionSettings,
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
    OICSchedule,
    OICSchemaMapping,
    create_oic_connection,
    create_oic_integration,
    create_oic_lookup,
    create_oic_package,
)
from flext_target_oracle_oic.patterns import (
    OICDataTransformer,
    OICEntryManager,
    OICSchemaMapper,
    OICTypeConverter,
)
from flext_target_oracle_oic.singer import OICRecordProcessor

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

# Local re-export of script functions to satisfy tests expecting them at package root
try:  # pragma: no cover - simple import shim
    from flext_target_oracle_oic.scripts.generate_config import (
        generate_config as generate_config,
        main as generate_config_main,
    )
except Exception:  # pragma: no cover - tolerate missing during partial installs
    # Provide fallback which mirrors scripts/generate_config.py behavior
    import json
    import os
    from pathlib import Path

    logger = FlextLogger(__name__)

    def generate_config() -> FlextTypes.Core.Dict:
        """Generate configuration from environment variables."""
        return {
            "base_url": os.getenv(
                "OIC_IDCS_CLIENT_AUD",
                "https://your-instance.integration.ocp.oraclecloud.com",
            ),
            "oauth_client_id": os.getenv("OIC_IDCS_CLIENT_ID", ""),
            "oauth_client_secret": os.getenv("OIC_IDCS_CLIENT_SECRET", ""),
            "oauth_token_url": (
                os.getenv("OIC_IDCS_URL", "https://your-identity.oraclecloud.com")
                + "/oauth2/v1/token"
                if os.getenv("OIC_IDCS_URL")
                else "https://your-identity.oraclecloud.com/oauth2/v1/token"
            ),
            "import_mode": os.getenv("OIC_IMPORT_MODE", "create_or_update"),
            "activate_integrations": os.getenv(
                "OIC_ACTIVATE_INTEGRATIONS", "false"
            ).lower()
            == "true",
            "batch_size": int(os.getenv("OIC_BATCH_SIZE", "10")),
            "timeout": int(os.getenv("OIC_TIMEOUT", "30")),
            "max_retries": int(os.getenv("OIC_MAX_RETRIES", "3")),
            "validate_ssl": os.getenv("OIC_VALIDATE_SSL", "true").lower() == "true",
        }

    def generate_config_main() -> None:
        """Generate configuration file interactively."""
        config_path = Path("config.json")
        if config_path.exists():
            response = input("config.json already exists. Overwrite? (y/N): ")
            if response.lower() not in {"y", "yes"}:
                logger.info("Configuration generation skipped.")
                return
        cfg = generate_config()
        config_path.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
        logger.info("✅ Successfully generated target-oracle-oic configuration")


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
    """Entry point expected by tests: generate config.json interactively."""
    generate_config_main()


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
    "OICTargetOrchestrator",  # May be None if legacy not available
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


# ===============================================================================
# CLI SUPPORT FOR DIRECT EXECUTION
# ===============================================================================

if __name__ == "__main__":
    main()
