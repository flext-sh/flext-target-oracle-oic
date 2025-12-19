"""Target Oracle OIC Configuration - Unified configuration management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_target_oracle_oic.settings import TargetOracleOicSettings

# Temporary authenticator placeholder until proper implementation
OICOAuth2Authenticator = object

# Backward compatibility aliases - all Config classes now use the single TargetOracleOicSettings
# These provide compatibility for existing code while directing to the standardized Config
OICAuthConfig = TargetOracleOicSettings
OICConnectionConfig = TargetOracleOicSettings
OICDeploymentConfig = TargetOracleOicSettings
OICProcessingConfig = TargetOracleOicSettings
OICEntityConfig = TargetOracleOicSettings


def create_config_from_dict(config_dict: dict[str, object]) -> TargetOracleOicSettings:
    """Create TargetOracleOicSettings from dictionary."""
    return TargetOracleOicSettings.model_validate(config_dict)


def create_config_with_env_overrides(
    **overrides: dict[str, object],
) -> TargetOracleOicSettings:
    """Create TargetOracleOicSettings with environment variable overrides."""
    return TargetOracleOicSettings.get_or_create_shared_instance(
        project_name="flext-target-oracle-oic",
        **overrides,
    )


def create_singer_config_schema() -> dict[str, object]:
    """Create Singer configuration schema from TargetOracleOicSettings."""
    return TargetOracleOicSettings.model_json_schema()


__all__: list[str] = [
    "OICAuthConfig",
    "OICConnectionConfig",
    "OICDeploymentConfig",
    "OICEntityConfig",
    "OICOAuth2Authenticator",
    "OICProcessingConfig",
    "TargetOracleOicSettings",
    "create_config_from_dict",
    "create_config_with_env_overrides",
    "create_singer_config_schema",
]
