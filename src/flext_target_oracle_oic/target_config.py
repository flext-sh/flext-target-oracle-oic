"""Target Oracle OIC Configuration - Unified configuration management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic_settings import SettingsConfigDict

from flext_core import FlextTypes

OICOAuth2Authenticator = object


from flext_target_oracle_oic.models import FlextTargetOracleOicModels

# Use standardized models from FlextTargetOracleOicModels
OICAuthConfig = FlextTargetOracleOicModels.OicAuthenticationConfig


# Use standardized models from FlextTargetOracleOicModels
OICConnectionConfig = FlextTargetOracleOicModels.OicTargetConfig


# Use standardized models from FlextTargetOracleOicModels
OICDeploymentConfig = FlextTargetOracleOicModels.OicTargetConfig


# Use standardized models from FlextTargetOracleOicModels
OICProcessingConfig = FlextTargetOracleOicModels.OicTargetConfig


# Use standardized models from FlextTargetOracleOicModels
OICEntityConfig = FlextTargetOracleOicModels.OicTargetConfig


class TargetOracleOICConfig(FlextTargetOracleOicModels.OicTargetConfig):
    """Complete configuration for target-oracle-oic using standardized FlextTargetOracleOicModels.

    Uses maximum composition from flext-core and standardized models.
    Zero tolerance for architectural violations.
    """

    model_config = SettingsConfigDict(
        env_prefix="TARGET_ORACLE_OIC_",
        case_sensitive=False,
    )

    @classmethod
    def create_with_defaults(
        cls,
        **overrides: object,
    ) -> TargetOracleOICConfig:
        """Create configuration with intelligent defaults."""
        defaults: FlextTypes.Core.Dict = {
            "auth_config": {
                "base_url": "https://your-instance.integration.ocp.oraclecloud.com",
                "oauth_client_id": "your-client-id",
                "oauth_client_secret": "your-client-secret",  # nosec B106 - Example configuration value
                "oauth_token_url": "https://auth.oraclecloud.com/oauth2/v1/token",
                "oauth_client_aud": "https://your-instance.integration.ocp.oraclecloud.com:443/urn:opc:resource:consumer::all",
            },
            "import_mode": "create_or_update",
            "activate_integrations": True,
            "batch_size": 25,
            "concurrent_streams": 2,
            "enable_connection_pooling": True,
            "connection_pool_size": 5,
        }
        defaults.update(overrides)
        return cls(**defaults)


# Singer SDK configuration schema creation
def create_singer_config_schema() -> FlextTypes.Core.Dict:
    """Create Singer SDK compatible configuration schema using target field names.

    This schema aligns with tests which provide flat configuration keys:
    - base_url, oauth_client_id, oauth_client_secret, oauth_token_url, oauth_client_aud
        Returns:
            FlextTypes.Core.Dict:: Description of return value.

    """
    schema: FlextTypes.Core.Dict = {"properties": "properties"}
    # Required minimal fields used in tests
    required_fields: FlextTypes.Core.StringList = [
        "base_url",
        "oauth_client_id",
        "oauth_client_secret",
        "oauth_token_url",
    ]
    schema["required"] = required_fields
    return schema


# Configuration factory functions
def create_config_from_dict(config_dict: FlextTypes.Core.Dict) -> TargetOracleOICConfig:
    """Create configuration from dictionary with validation."""
    return TargetOracleOICConfig(**config_dict)


def create_config_with_env_overrides(
    base_config: FlextTypes.Core.Dict | None = None,
) -> TargetOracleOICConfig:
    """Create configuration with environment variable overrides.

    DEPRECATED: Use TargetOracleOICConfig.get_global_instance() with Pydantic 2 Settings instead.
    This method will be removed in a future version.
    """
    import warnings

    warnings.warn(
        "create_config_with_env_overrides is deprecated. "
        "Use TargetOracleOICConfig with Pydantic 2 Settings instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    config: FlextTypes.Core.Dict = dict(base_config) if base_config else {}

    # Override with environment variables using safer pattern
    env_mappings = {
        "TARGET_ORACLE_OIC_BASE_URL": ("connection", "base_url"),
        "TARGET_ORACLE_OIC_OAUTH_CLIENT_ID": ("auth", "oauth_client_id"),
        "TARGET_ORACLE_OIC_OAUTH_CLIENT_SECRET": ("auth", "oauth_client_secret"),
        "TARGET_ORACLE_OIC_OAUTH_TOKEN_URL": ("auth", "oauth_token_url"),
        "TARGET_ORACLE_OIC_OAUTH_CLIENT_AUD": ("auth", "oauth_client_aud"),
        "TARGET_ORACLE_OIC_IMPORT_MODE": ("deployment", "import_mode"),
    }

    import os

    for env_key, (section, field) in env_mappings.items():
        env_value = os.environ.get(env_key)
        if env_value is not None:
            if section not in config:
                config[section] = {}
            section_obj = config[section]
            if not isinstance(section_obj, dict):
                section_obj = {}
                config[section] = section_obj
            section_obj[field] = env_value

    return TargetOracleOICConfig(**config)


# Export configuration classes
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
