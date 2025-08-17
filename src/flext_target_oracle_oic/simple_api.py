"""Simple API for FLEXT target-oracle-oic setup and configuration.

MIGRATED TO FLEXT-CORE:
Provides enterprise-ready setup utilities with FlextResult pattern support.
"""

from __future__ import annotations

from os import getenv

from flext_core import FlextResult
from pydantic import SecretStr

from flext_target_oracle_oic.config import (
    OICAuthConfig,
    OICConnectionConfig,
    OICDeploymentConfig,
    OICEntityConfig,
    OICProcessingConfig,
    TargetOracleOICConfig,
)


def setup_oic_target(
    config: TargetOracleOICConfig | None = None,
) -> FlextResult[TargetOracleOICConfig]:
    """Set up Oracle Integration Cloud target with configuration.

    Args:
      config: Optional configuration. If None, creates defaults.

    Returns:
      FlextResult with TargetOracleOICConfig or error message.

    """
    try:
        if config is None:
            # Create with intelligent defaults
            config = TargetOracleOICConfig.create_with_defaults()

        # Validate configuration
        config.model_validate(config.model_dump())

        return FlextResult.ok(config)

    except (RuntimeError, ValueError, TypeError) as e:
        return FlextResult.fail(f"Failed to set up OIC target: {e}")


def create_development_oic_target_config(**overrides: object) -> TargetOracleOICConfig:
    """Create development OIC target configuration with defaults.

    Args:
      **overrides: Configuration overrides

    Returns:
      TargetOracleOICConfig for development use.

    """
    auth_config = OICAuthConfig(
        oauth_client_id=getenv("OIC_DEV_CLIENT_ID", "dev-client-id"),
        oauth_client_secret=SecretStr(
            getenv("OIC_DEV_CLIENT_SECRET", "dev-client-secret"),
        ),
        oauth_token_url=getenv(
            "OIC_OAUTH_TOKEN_URL",
            "https://identity.oraclecloud.com/oauth2/v1/token",
        ),
    )

    connection_config = OICConnectionConfig(
        base_url="https://dev-instance.integration.ocp.oraclecloud.com",
        timeout=120,
        max_retries=3,
    )

    deployment_config = OICDeploymentConfig(
        import_mode="create_or_update",
        activate_integrations=False,
        validate_connections=True,
        rollback_on_failure=True,
        archive_directory=None,
        enable_versioning=True,
        audit_trail=True,
    )

    processing_config = OICProcessingConfig(
        batch_size=50,
        enable_validation=True,
        validation_strict_mode=False,
        dry_run_mode=True,
        skip_missing_connections=False,
        max_errors=50,
        ignore_transformation_errors=True,
    )

    config = TargetOracleOICConfig(
        auth=auth_config,
        connection=connection_config,
        deployment=deployment_config,
        processing=processing_config,
        entities=OICEntityConfig(
            integration_identifier_field="code",
            connection_identifier_field="code",
            lookup_identifier_field="name",
            identifier_fields={},
        ),
        project_name="flext-target-oracle-oic-dev",
        project_version="0.9.0",
    )

    # Apply overrides
    if overrides:
        config_dict = config.model_dump()
        config_dict.update(overrides)
        config = TargetOracleOICConfig.model_validate(config_dict)

    return config


def create_production_oic_target_config(**overrides: object) -> TargetOracleOICConfig:
    """Create production OIC target configuration with security defaults.

    Args:
      **overrides: Configuration overrides

    Returns:
      TargetOracleOICConfig for production use.

    """
    auth_config = OICAuthConfig(
        oauth_client_id=getenv("OIC_PROD_CLIENT_ID", "prod-client-id"),
        oauth_client_secret=SecretStr(
            getenv("OIC_PROD_CLIENT_SECRET", "prod-client-secret"),
        ),
        oauth_token_url=getenv(
            "OIC_OAUTH_TOKEN_URL",
            "https://identity.oraclecloud.com/oauth2/v1/token",
        ),
    )

    connection_config = OICConnectionConfig(
        base_url="https://prod-instance.integration.ocp.oraclecloud.com",
        timeout=300,
        max_retries=5,
    )

    deployment_config = OICDeploymentConfig(
        import_mode="create_or_update",
        activate_integrations=True,
        validate_connections=True,
        rollback_on_failure=True,
        archive_directory=None,
        enable_versioning=True,
        audit_trail=True,
    )

    processing_config = OICProcessingConfig(
        batch_size=100,
        enable_validation=True,
        validation_strict_mode=True,
        dry_run_mode=False,
        skip_missing_connections=False,
        max_errors=10,
        ignore_transformation_errors=False,
    )

    config = TargetOracleOICConfig(
        auth=auth_config,
        connection=connection_config,
        deployment=deployment_config,
        processing=processing_config,
        entities=OICEntityConfig(
            integration_identifier_field="code",
            connection_identifier_field="code",
            lookup_identifier_field="name",
            identifier_fields={},
        ),
        project_name="flext-data.targets.flext-data.targets.flext-target-oracle-oic",
        project_version="0.9.0",
    )

    # Apply overrides
    if overrides:
        config_dict = config.model_dump()
        config_dict.update(overrides)
        config = TargetOracleOICConfig.model_validate(config_dict)

    return config


def create_migration_oic_target_config(**overrides: object) -> TargetOracleOICConfig:
    """Create OIC target configuration optimized for large-scale migrations.

    Args:
      **overrides: Configuration overrides

    Returns:
      TargetOracleOICConfig optimized for migrations.

    """
    auth_config = OICAuthConfig(
        oauth_client_id=getenv("OIC_MIG_CLIENT_ID", "migration-client-id"),
        oauth_client_secret=SecretStr(
            getenv("OIC_MIG_CLIENT_SECRET", "migration-client-secret"),
        ),
        oauth_token_url=getenv(
            "OIC_OAUTH_TOKEN_URL",
            "https://identity.oraclecloud.com/oauth2/v1/token",
        ),
    )

    connection_config = OICConnectionConfig(
        base_url="https://migration-instance.integration.ocp.oraclecloud.com",
        timeout=600,
        max_retries=10,
    )

    deployment_config = OICDeploymentConfig(
        import_mode="create_or_update",
        activate_integrations=False,
        validate_connections=True,
        rollback_on_failure=False,  # Continue processing on errors during migration
        archive_directory=None,
        enable_versioning=True,
        audit_trail=True,
    )

    processing_config = OICProcessingConfig(
        batch_size=500,
        enable_validation=True,
        validation_strict_mode=False,
        dry_run_mode=False,
        skip_missing_connections=False,
        max_errors=1000,  # Higher tolerance for migrations
        ignore_transformation_errors=True,
    )

    config = TargetOracleOICConfig(
        auth=auth_config,
        connection=connection_config,
        deployment=deployment_config,
        processing=processing_config,
        entities=OICEntityConfig(
            integration_identifier_field="code",
            connection_identifier_field="code",
            lookup_identifier_field="name",
            identifier_fields={},
        ),
        project_name="flext-data.targets.flext-data.targets.flext-target-oracle-oic-migration",
        project_version="0.9.0",
    )

    # Apply overrides
    if overrides:
        config_dict = config.model_dump()
        config_dict.update(overrides)
        config = TargetOracleOICConfig.model_validate(config_dict)

    return config


def validate_oic_target_config(config: TargetOracleOICConfig) -> FlextResult[bool]:  # noqa: PLR0911
    """Validate OIC target configuration.

    Args:
      config: Configuration to validate

    Returns:
      FlextResult with validation success or error message.

    """
    try:
        # Validate using Pydantic model validation
        config.model_validate(config.model_dump())
        # Validate business/domain rules
        domain_result = config.validate_domain_rules()
        if not domain_result.success:
            return FlextResult.fail(str(domain_result.error))

        # Additional business rule validations
        if not config.connection.base_url:
            return FlextResult.fail("Base URL is required")

        if not config.auth.oauth_client_id:
            return FlextResult.fail("OAuth client ID is required")

        if not config.auth.oauth_client_secret:
            return FlextResult.fail("OAuth client secret is required")

        if not config.auth.oauth_token_url:
            return FlextResult.fail("OAuth token URL is required")

        return FlextResult.ok(data=True)

    except (RuntimeError, ValueError, TypeError) as e:
        return FlextResult.fail(f"Configuration validation failed: {e}")


def create_test_connection_config(**overrides: object) -> TargetOracleOICConfig:
    """Create configuration for testing OIC connections.

    Args:
      **overrides: Configuration overrides

    Returns:
      TargetOracleOICConfig optimized for connection testing.

    """
    auth_config = OICAuthConfig(
        oauth_client_id=getenv("OIC_TEST_CLIENT_ID", "test-client-id"),
        oauth_client_secret=SecretStr(
            getenv("OIC_TEST_CLIENT_SECRET", "test-client-secret"),
        ),
        oauth_token_url=getenv(
            "OIC_OAUTH_TOKEN_URL",
            "https://identity.oraclecloud.com/oauth2/v1/token",
        ),
    )

    connection_config = OICConnectionConfig(
        base_url="https://test-instance.integration.ocp.oraclecloud.com",
        timeout=30,
        max_retries=1,
    )

    processing_config = OICProcessingConfig(
        batch_size=1,
        enable_validation=False,
        validation_strict_mode=False,
        dry_run_mode=True,
        skip_missing_connections=False,
        max_errors=1,
        ignore_transformation_errors=True,
    )

    config = TargetOracleOICConfig(
        auth=auth_config,
        connection=connection_config,
        deployment=OICDeploymentConfig(
            import_mode="create_or_update",
            activate_integrations=False,
            validate_connections=True,
            rollback_on_failure=True,
            archive_directory=None,
            enable_versioning=True,
            audit_trail=True,
        ),
        processing=processing_config,
        entities=OICEntityConfig(
            integration_identifier_field="code",
            connection_identifier_field="code",
            lookup_identifier_field="name",
            identifier_fields={},
        ),
        project_name="flext-data.targets.flext-data.targets.flext-target-oracle-oic-test",
        project_version="0.9.0",
    )

    # Apply overrides
    if overrides:
        config_dict = config.model_dump()
        config_dict.update(overrides)
        config = TargetOracleOICConfig(**config_dict)

    return config


# Export convenience functions
__all__: list[str] = [
    "FlextResult",
    "create_development_oic_target_config",
    "create_migration_oic_target_config",
    "create_production_oic_target_config",
    "create_test_connection_config",
    "setup_oic_target",
    "validate_oic_target_config",
]
