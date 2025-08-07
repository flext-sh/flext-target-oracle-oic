"""FlextTargetOracleOic - Oracle Integration Cloud Target using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Enterprise-grade Oracle Integration Cloud target following flext-core architecture:
- FlextTargetOracleOic main class for OIC data integration
- Modular architecture with proper separation of concerns
- Comprehensive exception hierarchy
- OAuth2 authentication with IDCS
- Type-safe operations using FlextResult pattern
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

# Modular architecture components
from flext_target_oracle_oic.application import OICTargetOrchestrator
from flext_target_oracle_oic.auth import OICAuthConfig, OICOAuth2Authenticator
from flext_target_oracle_oic.cli import main as cli_main
from flext_target_oracle_oic.client import OICClient
from flext_target_oracle_oic.connection import OICConnection, OICConnectionConfig

# Exception hierarchy
from flext_target_oracle_oic.exceptions import (
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
)
from flext_target_oracle_oic.patterns import (
    OICDataTransformer,
    OICEntryManager,
    OICSchemaMapper,
    OICTypeConverter,
)
from flext_target_oracle_oic.singer import OICRecordProcessor
from flext_target_oracle_oic.sinks import (
    ConnectionsSink,
    IntegrationsSink,
    LookupsSink,
    PackagesSink,
)

# Main target implementation
from flext_target_oracle_oic.target import TargetOracleOIC

try:
    __version__ = importlib.metadata.version("flext-target-oracle-oic")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


class FlextTargetOracleOic(TargetOracleOIC):
    """FlextTargetOracleOic - Main class following flext patterns."""


class FlextTargetOracleOicConfig(FlextValueObject):
    """Configuration for FlextTargetOracleOic using flext-core patterns."""

    base_url: str
    oauth_client_id: str
    oauth_client_secret: str
    oauth_token_url: str
    oauth_client_aud: str | None = None
    import_mode: str = "create_or_update"
    activate_integrations: bool = False


# Type alias for FlextResult
FlextTargetOracleOicResult = FlextResult


# CLI entry point
def main() -> None:
    """CLI entry point for flext-target-oracle-oic."""
    cli_main()


__all__: list[str] = [
    # === FLEXT-MELTANO COMPLETE RE-EXPORTS ===
    "BatchSink",
    # === SINKS ===
    "ConnectionsSink",
    "FlextMeltanoBaseService",
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextMeltanoEvent",
    "FlextMeltanoTargetService",
    # === CORE RE-EXPORTS ===
    "FlextResult",
    # === PRIMARY CLASSES ===
    "FlextTargetOracleOic",
    # === EXCEPTIONS ===
    "FlextTargetOracleOicAPIError",
    "FlextTargetOracleOicAuthenticationError",
    "FlextTargetOracleOicConfig",
    "FlextTargetOracleOicConfigurationError",
    "FlextTargetOracleOicConnectionError",
    "FlextTargetOracleOicError",
    "FlextTargetOracleOicErrorDetails",
    "FlextTargetOracleOicInfrastructureError",
    "FlextTargetOracleOicProcessingError",
    "FlextTargetOracleOicResult",
    "FlextTargetOracleOicTransformationError",
    "FlextTargetOracleOicValidationError",
    "FlextValueObject",
    "IntegrationsSink",
    "LookupsSink",
    "OAuthAuthenticator",
    # === OIC COMPONENTS ===
    "OICAuthConfig",
    "OICClient",
    "OICConnection",
    "OICConnectionConfig",
    "OICDataTransformer",
    "OICEntryManager",
    "OICOAuth2Authenticator",
    "OICRecordProcessor",
    "OICSchemaMapper",
    "OICTargetOrchestrator",
    "OICTypeConverter",
    "PackagesSink",
    "PropertiesList",
    "Property",
    "SQLSink",
    "Sink",
    "Stream",
    "Tap",
    "Target",
    "TargetOracleOIC",
    # === METADATA ===
    "__version__",
    "__version_info__",
    "create_meltano_target_service",
    "get_tap_test_class",
    "main",
    "singer_typing",
]


# CLI support for direct execution
if __name__ == "__main__":
    main()
