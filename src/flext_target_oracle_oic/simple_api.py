"""Simple API for FLEXT target-oracle-oic setup and configuration using flext-core patterns.

MIGRATED TO FLEXT-CORE:
Provides enterprise-ready setup utilities with ServiceResult pattern support.
"""

from __future__ import annotations

from typing import Any

# Use centralized ServiceResult from flext-core - ELIMINATE DUPLICATION
from flext_core.domain.shared_types import ServiceResult
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
) -> ServiceResult[Any]:
    """Setup Oracle Integration Cloud target with configuration.

    Args:
        config: Optional configuration. If None, creates defaults.

    Returns:
        ServiceResult with TargetOracleOICConfig or error message.

    """
    try:
        if config is None:
            # Create with intelligent defaults
            config = TargetOracleOICConfig.create_with_defaults()

        # Validate configuration
        config.model_validate(config.model_dump())

        return ServiceResult.ok(config)

    except Exception as e:
        return ServiceResult.fail(f"Failed to setup OIC target: {e}")


def create_development_oic_target_config(**overrides: Any) -> TargetOracleOICConfig:
    """Create development OIC target configuration with defaults.

    Args:
        **overrides: Configuration overrides

    Returns:
        TargetOracleOICConfig for development use.

    """
    auth_config = OICAuthConfig(
        oauth_client_id="dev-client-id",
        oauth_client_secret=SecretStr("dev-client-secret"),  # nosec B106 - Example development value
        oauth_token_url="https://identity.oraclecloud.com/oauth2/v1/token",
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
        project_version="0.7.0",
    )

    # Apply overrides
    if overrides:
        config_dict = config.model_dump()
        config_dict.update(overrides)
        config = TargetOracleOICConfig(**config_dict)

    return config


def create_production_oic_target_config(**overrides: Any) -> TargetOracleOICConfig:
    """Create production OIC target configuration with security defaults.

    Args:
        **overrides: Configuration overrides

    Returns:
        TargetOracleOICConfig for production use.

    """
    auth_config = OICAuthConfig(
        oauth_client_id="prod-client-id",
        oauth_client_secret=SecretStr("prod-client-secret"),  # nosec B106 - Example production value
        oauth_token_url="https://identity.oraclecloud.com/oauth2/v1/token",
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
        project_version="0.7.0",
    )

    # Apply overrides
    if overrides:
        config_dict = config.model_dump()
        config_dict.update(overrides)
        config = TargetOracleOICConfig(**config_dict)

    return config


def create_migration_oic_target_config(**overrides: Any) -> TargetOracleOICConfig:
    """Create OIC target configuration optimized for large-scale migrations.

    Args:
        **overrides: Configuration overrides

    Returns:
        TargetOracleOICConfig optimized for migrations.

    """
    auth_config = OICAuthConfig(
        oauth_client_id="migration-client-id",
        oauth_client_secret=SecretStr("migration-client-secret"),  # nosec B106 - Example migration value
        oauth_token_url="https://identity.oraclecloud.com/oauth2/v1/token",
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
        project_version="0.7.0",
    )

    # Apply overrides
    if overrides:
        config_dict = config.model_dump()
        config_dict.update(overrides)
        config = TargetOracleOICConfig(**config_dict)

    return config


def validate_oic_target_config(config: TargetOracleOICConfig) -> ServiceResult[Any]:
    """Validate OIC target configuration.

    Args:
        config: Configuration to validate

    Returns:
        ServiceResult with validation success or error message.

    """
    try:
        # Validate using Pydantic model validation
        config.model_validate(config.model_dump())

        # Additional business rule validations
        if not config.connection.base_url:
            return ServiceResult.fail("Base URL is required")

        if not config.auth.oauth_client_id:
            return ServiceResult.fail("OAuth client ID is required")

        if not config.auth.oauth_client_secret:
            return ServiceResult.fail("OAuth client secret is required")

        if not config.auth.oauth_token_url:
            return ServiceResult.fail("OAuth token URL is required")

        return ServiceResult.ok(True)

    except Exception as e:
        return ServiceResult.fail(f"Configuration validation failed: {e}")


def create_test_connection_config(**overrides: Any) -> TargetOracleOICConfig:
    """Create configuration for testing OIC connections.

    Args:
        **overrides: Configuration overrides

    Returns:
        TargetOracleOICConfig optimized for connection testing.

    """
    auth_config = OICAuthConfig(
        oauth_client_id="test-client-id",
        oauth_client_secret=SecretStr("test-client-secret"),  # nosec B106 - Example testing value
        oauth_token_url="https://identity.oraclecloud.com/oauth2/v1/token",
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
        project_version="0.7.0",
    )

    # Apply overrides
    if overrides:
        config_dict = config.model_dump()
        config_dict.update(overrides)
        config = TargetOracleOICConfig(**config_dict)

    return config


# Export convenience functions
__all__ = [
    "ServiceResult",
    "create_development_oic_target_config",
    "create_migration_oic_target_config",
    "create_production_oic_target_config",
    "create_test_connection_config",
    "setup_oic_target",
    "validate_oic_target_config",
]
