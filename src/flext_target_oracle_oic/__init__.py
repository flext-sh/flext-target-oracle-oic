"""FLEXT Target Oracle OIC - Oracle Integration Cloud Data Loading with simplified imports.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Version 0.7.0 - Target Oracle OIC with simplified public API:
- All common imports available from root: from flext_target_oracle_oic import TargetOracleOIC
- Built on flext-core foundation for robust Oracle OIC data loading
- Deprecation warnings for internal imports

This target provides:
- OAuth2 authentication with Oracle Identity Cloud Service (IDCS)
- Support for connections, integrations, packages, and lookups
- Batch processing for efficient data loading
- Enterprise-grade error handling and logging
- Archive-based integration deployment
"""

from __future__ import annotations

import contextlib
import importlib.metadata
import warnings

# Import from flext-core for foundational patterns
# Foundation patterns - ALWAYS from flext-core
# 🚨 ARCHITECTURAL COMPLIANCE: Using DI container
from flext_target_oracle_oic.infrastructure.di_container import (
    get_base_config,
    get_domain_entity,
    get_domain_value_object,
    get_field,
    get_service_result,
)

ServiceResult = get_service_result()
DomainEntity = get_domain_entity()
Field = get_field()
DomainValueObject = get_domain_value_object()
BaseConfig = get_base_config()

# Core exports from flext-core
OICBaseConfig = BaseConfig  # Configuration base
BaseModel = DomainEntity  # Base for OIC models
OICError = Exception  # OIC-specific errors
ValidationError = ValueError  # Validation errors

try:
    __version__ = importlib.metadata.version("flext-target-oracle-oic")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.7.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


class FlextTargetOracleOicDeprecationWarning(DeprecationWarning):
    """Custom deprecation warning for FLEXT TARGET ORACLE OIC import changes."""


def _show_deprecation_warning(old_import: str, new_import: str) -> None:
    """Show deprecation warning for import paths."""
    message_parts = [
        f"⚠️  DEPRECATED IMPORT: {old_import}",
        f"✅ USE INSTEAD: {new_import}",
        "🔗 This will be removed in version 1.0.0",
        "📖 See FLEXT TARGET ORACLE OIC docs for migration guide",
    ]
    warnings.warn(
        "\n".join(message_parts),
        FlextTargetOracleOicDeprecationWarning,
        stacklevel=3,
    )


# ================================
# SIMPLIFIED PUBLIC API EXPORTS
# ================================

# Singer Target exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_target_oracle_oic.target import TargetOracleOIC

# OIC Client exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_target_oracle_oic.auth import OICOAuth2Authenticator as OICAuthenticator

# OIC Sinks exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_target_oracle_oic.sinks import (
        ConnectionsSink,
        IntegrationsSink,
        LookupsSink,
        PackagesSink,
    )

# ================================
# PUBLIC API EXPORTS
# ================================

__all__ = [
    "BaseModel",  # from flext_target_oracle_oic import BaseModel
    # OIC Sinks (simplified access)
    "ConnectionsSink",  # from flext_target_oracle_oic import ConnectionsSink
    # Deprecation utilities
    "FlextTargetOracleOicDeprecationWarning",
    # OIC Sinks (simplified access)
    "IntegrationsSink",  # from flext_target_oracle_oic import IntegrationsSink
    "LookupsSink",  # from flext_target_oracle_oic import LookupsSink
    # OIC Authentication (simplified access)
    "OICAuthenticator",  # from flext_target_oracle_oic import OICAuthenticator
    # Core Patterns (from flext-core)
    "OICBaseConfig",  # from flext_target_oracle_oic import OICBaseConfig
    "OICError",  # from flext_target_oracle_oic import OICError
    "PackagesSink",  # from flext_target_oracle_oic import PackagesSink
    "ServiceResult",  # from flext_target_oracle_oic import ServiceResult
    # Main Singer Target (simplified access)
    "TargetOracleOIC",  # from flext_target_oracle_oic import TargetOracleOIC
    "ValidationError",  # from flext_target_oracle_oic import ValidationError
    # Version
    "__version__",
    "__version_info__",
]


def main() -> None:
    """Main entry point for target-oracle-oic CLI."""
    TargetOracleOIC.cli()


if __name__ == "__main__":
    main()
