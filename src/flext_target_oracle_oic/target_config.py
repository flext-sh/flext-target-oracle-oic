"""Target Oracle OIC Configuration - Unified configuration management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Any

from flext_core import FlextTypes
from flext_target_oracle_oic.config import TargetOracleOICConfig

# Temporary authenticator placeholder until proper implementation
OICOAuth2Authenticator = object

# Backward compatibility aliases - all Config classes now use the single TargetOracleOICConfig
# These provide compatibility for existing code while directing to the standardized Config
OICAuthConfig = TargetOracleOICConfig
OICConnectionConfig = TargetOracleOICConfig
OICDeploymentConfig = TargetOracleOICConfig
OICProcessingConfig = TargetOracleOICConfig
OICEntityConfig = TargetOracleOICConfig


def create_config_from_dict(config_dict: dict[str, Any]) -> TargetOracleOICConfig:
    """Create TargetOracleOICConfig from dictionary."""
    return TargetOracleOICConfig.model_validate(config_dict)


def create_config_with_env_overrides(**overrides: Any) -> TargetOracleOICConfig:
    """Create TargetOracleOICConfig with environment variable overrides."""
    return TargetOracleOICConfig.get_or_create_shared_instance(
        project_name="flext-target-oracle-oic", **overrides
    )


def create_singer_config_schema() -> dict[str, Any]:
    """Create Singer configuration schema from TargetOracleOICConfig."""
    return TargetOracleOICConfig.model_json_schema()


__all__: FlextTypes.Core.StringList = [
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
]
