"""Target Oracle OIC Configuration - Unified configuration management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping

from flext_target_oracle_oic.settings import TargetOracleOicConfig
from flext_target_oracle_oic.typings import t

# Temporary authenticator placeholder until proper implementation
OICOAuth2Authenticator = object

# Backward compatibility aliases - all Config classes now use the single TargetOracleOicConfig
# These provide compatibility for existing code while directing to the standardized Config
OICAuthConfig = TargetOracleOicConfig
OICConnectionConfig = TargetOracleOicConfig
OICDeploymentConfig = TargetOracleOicConfig
OICProcessingConfig = TargetOracleOicConfig
OICEntityConfig = TargetOracleOicConfig


def create_config_from_dict(
    config_dict: Mapping[str, t.JsonValue],
) -> TargetOracleOicConfig:
    """Create TargetOracleOicConfig from dictionary."""
    return TargetOracleOicConfig.model_validate(config_dict)


def create_config_with_env_overrides(
    **overrides: t.JsonValue,
) -> TargetOracleOicConfig:
    """Create TargetOracleOicConfig with environment variable overrides."""
    return TargetOracleOicConfig.model_validate(overrides)


def create_singer_config_schema() -> Mapping[str, t.JsonValue]:
    """Create Singer configuration schema from TargetOracleOicConfig."""
    return TargetOracleOicConfig.model_json_schema()


__all__: list[str] = [
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
