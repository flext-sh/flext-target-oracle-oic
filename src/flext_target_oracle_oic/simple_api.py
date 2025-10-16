"""Simple API for FLEXT target-oracle-oic setup and configuration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from os import getenv

from flext_core import FlextResult, FlextTypes
from pydantic import SecretStr

from flext_target_oracle_oic.config import TargetOracleOicConfig


def setup_oic_target(
    config: TargetOracleOicConfig | None = None,
) -> FlextResult[TargetOracleOicConfig]:
    """Set up Oracle Integration Cloud target with configuration.

    Args:
      config: Optional configuration. If None, creates defaults.

    Returns:
      FlextResult with TargetOracleOicConfig or error message.

    """
    try:
        if config is None:
            # Create with intelligent defaults using the singleton pattern
            config = TargetOracleOicConfig.get_global_instance()

        # Validate configuration
        validation_result = config.validate_business_rules()
        if validation_result.is_failure:
            return FlextResult[TargetOracleOicConfig].fail(
                f"Configuration validation failed: {validation_result.error}"
            )

        return FlextResult[TargetOracleOicConfig].ok(config)

    except (RuntimeError, ValueError, TypeError) as e:
        return FlextResult[TargetOracleOicConfig].fail(
            f"Failed to set up OIC target: {e}",
        )


def create_development_oic_target_config(
    **overrides: FlextTypes.Value,
) -> TargetOracleOicConfig:
    """Create development OIC target configuration with defaults.

    Args:
      **overrides: Configuration overrides

    Returns:
      TargetOracleOicConfig for development use.

    """
    dev_config_overrides: dict[str, FlextTypes.Value] = {
        # Authentication configuration
        "oauth_client_id": getenv("OIC_DEV_CLIENT_ID", "dev-client-id"),
        "oauth_client_secret": SecretStr(
            getenv("OIC_DEV_CLIENT_SECRET", "dev-client-secret"),
        ),
        "oauth_token_url": getenv(
            "OIC_OAUTH_TOKEN_URL",
            "https://identity.oraclecloud.com/oauth2/v1/token",
        ),
        "oauth_client_aud": None,
        "oauth_scope": "",
        # Connection configuration
        "base_url": "https://dev-instance.integration.ocp.oraclecloud.com",
        "timeout": 120,
        "max_retries": 3,
        "verify_ssl": True,
        # Deployment configuration
        "import_mode": "create_or_update",
        "activate_integrations": False,
        "validate_connections": True,
        "rollback_on_failure": True,
        "archive_directory": None,
        "enable_versioning": True,
        "audit_trail": True,
        # Processing configuration
        "batch_size": 50,
        "enable_validation": True,
        "validation_strict_mode": False,
        "dry_run_mode": True,
        "skip_missing_connections": False,
        "max_errors": 50,
        "ignore_transformation_errors": True,
        # Entity configuration
        "integration_identifier_field": "integration_id",
        "connection_identifier_field": "connection_id",
        "lookup_identifier_field": "lookup_id",
        "identifier_fields": {
            "integrations": "code",
            "connections": "code",
            "lookups": "name",
        },
        **overrides,
    }

    return TargetOracleOicConfig.create_for_development(**dev_config_overrides)


def create_production_oic_target_config(
    **overrides: FlextTypes.Value,
) -> TargetOracleOicConfig:
    """Create production OIC target configuration with defaults.

    Args:
      **overrides: Configuration overrides

    Returns:
      TargetOracleOicConfig for production use.

    """
    prod_config_overrides: dict[str, FlextTypes.Value] = {
        # Authentication configuration
        "oauth_client_id": getenv("OIC_PROD_CLIENT_ID", ""),
        "oauth_client_secret": SecretStr(
            getenv("OIC_PROD_CLIENT_SECRET", ""),
        ),
        "oauth_token_url": getenv(
            "OIC_OAUTH_TOKEN_URL",
            "https://identity.oraclecloud.com/oauth2/v1/token",
        ),
        # Connection configuration
        "base_url": getenv(
            "OIC_PROD_BASE_URL", "https://prod-instance.integration.ocp.oraclecloud.com"
        ),
        "timeout": 300,
        "max_retries": 5,
        "verify_ssl": True,
        # Deployment configuration
        "import_mode": "create_or_update",
        "activate_integrations": True,
        "validate_connections": True,
        "rollback_on_failure": True,
        "enable_versioning": True,
        "audit_trail": True,
        # Processing configuration
        "batch_size": 100,
        "enable_validation": True,
        "validation_strict_mode": False,
        "dry_run_mode": False,
        "max_errors": 10,
        "ignore_transformation_errors": False,
        **overrides,
    }

    return TargetOracleOicConfig.create_for_production(**prod_config_overrides)


def create_testing_oic_target_config(
    **overrides: FlextTypes.Value,
) -> TargetOracleOicConfig:
    """Create testing OIC target configuration with defaults.

    Args:
      **overrides: Configuration overrides

    Returns:
      TargetOracleOicConfig for testing use.

    """
    test_config_overrides: dict[str, FlextTypes.Value] = {
        # Authentication configuration
        "oauth_client_id": getenv("OIC_TEST_CLIENT_ID", "test-client-id"),
        "oauth_client_secret": SecretStr(
            getenv("OIC_TEST_CLIENT_SECRET", "test-client-secret"),
        ),
        "oauth_token_url": getenv(
            "OIC_OAUTH_TOKEN_URL",
            "https://identity.oraclecloud.com/oauth2/v1/token",
        ),
        # Connection configuration
        "base_url": "https://test-instance.integration.ocp.oraclecloud.com",
        "timeout": 60,
        "max_retries": 2,
        # Processing configuration for testing
        "batch_size": 5,
        "enable_validation": True,
        "validation_strict_mode": True,
        "dry_run_mode": True,
        "max_errors": 3,
        **overrides,
    }

    return TargetOracleOicConfig.create_for_testing(**test_config_overrides)


def validate_oic_target_config(config: TargetOracleOicConfig) -> FlextResult[None]:
    """Validate Oracle Integration Cloud target configuration.

    Args:
      config: Configuration to validate

    Returns:
      FlextResult indicating validation success or failure

    """
    return config.validate_business_rules()


def get_oic_target_config_schema() -> FlextTypes.Dict:
    """Get JSON schema for Oracle Integration Cloud target configuration.

    Returns:
      JSON schema dictionary for TargetOracleOicConfig

    """
    return TargetOracleOicConfig.model_json_schema()


__all__: FlextTypes.StringList = [
    "create_development_oic_target_config",
    "create_production_oic_target_config",
    "create_testing_oic_target_config",
    "get_oic_target_config_schema",
    "setup_oic_target",
    "validate_oic_target_config",
]
