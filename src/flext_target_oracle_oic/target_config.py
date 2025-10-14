"""Target Oracle OIC Configuration - Unified configuration management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextCore

from flext_target_oracle_oic.config import TargetOracleOicConfig

# Temporary authenticator placeholder until proper implementation
OICOAuth2Authenticator = object

# Backward compatibility aliases - all Config classes now use the single TargetOracleOicConfig
# These provide compatibility for existing code while directing to the standardized Config
OICAuthConfig = TargetOracleOicConfig
OICConnectionConfig = TargetOracleOicConfig
OICDeploymentConfig = TargetOracleOicConfig
OICProcessingConfig = TargetOracleOicConfig
OICEntityConfig = TargetOracleOicConfig


def create_config_from_dict(config_dict: FlextCore.Types.Dict) -> TargetOracleOicConfig:
    """Create TargetOracleOicConfig from dictionary."""
    return TargetOracleOicConfig.model_validate(config_dict)


def create_config_with_env_overrides(
    **overrides: FlextCore.Types.Dict,
) -> TargetOracleOicConfig:
    """Create TargetOracleOicConfig with environment variable overrides."""
    return TargetOracleOicConfig.get_or_create_shared_instance(
        project_name="flext-target-oracle-oic", **overrides
    )


def create_singer_config_schema() -> FlextCore.Types.Dict:
    """Create Singer configuration schema from TargetOracleOicConfig."""
    return TargetOracleOicConfig.model_json_schema()


__all__: FlextCore.Types.StringList = [
    "OICAuthConfig",
    "OICConnectionConfig",
    "OICDeploymentConfig",
    "OICEntityConfig",
    "OICOAuth2Authenticator",
    "OICProcessingConfig",
    "TargetOracleOicConfig",
    "create_config_from_dict",
    "create_config_with_env_overrides",
    "create_singer_config_schema",
]
