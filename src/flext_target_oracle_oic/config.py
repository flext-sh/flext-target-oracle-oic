"""Configuration for target-oracle-oic using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Self

from pydantic import Field, SecretStr, model_validator
from pydantic_settings import SettingsConfigDict

from flext_core import FlextConfig, FlextConstants, FlextModels, FlextResult, FlextTypes


class OICAuthConfig(FlextConfig):
    """OIC authentication configuration using flext-core patterns."""

    oauth_client_id: str = Field(
        ...,
        description="OAuth2 client ID for Oracle OIC authentication",
        min_length=1,
    )
    oauth_client_secret: SecretStr = Field(
        ...,
        description="OAuth2 client secret for Oracle OIC authentication",
    )
    oauth_token_url: str = Field(
        ...,
        description="OAuth2 token URL for Oracle OIC authentication",
        pattern=r"^https?://",
    )
    oauth_client_aud: str | None = Field(
        None,
        description="OAuth2 client audience (optional)",
    )
    oauth_scope: str = Field(
        default="",
        description="OAuth2 scope for Oracle OIC access",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate authentication configuration domain rules."""
        try:
            if not self.oauth_client_id.strip():
                return FlextResult[None].fail("OAuth client ID cannot be empty")
            if not self.oauth_token_url.strip():
                return FlextResult[None].fail("OAuth token URL cannot be empty")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Auth config validation failed: {e}")


class OICConnectionConfig(FlextConfig):
    """OIC connection configuration using flext-core patterns."""

    base_url: str = Field(
        ...,
        description="Oracle OIC base URL",
        pattern=r"^https://.*\.integration\.ocp\.oraclecloud\.com$",
    )
    timeout: int = Field(
        default=FlextConstants.Network.DEFAULT_TIMEOUT,
        description="Request timeout in seconds",
        gt=0,
        le=300,
    )
    max_retries: int = Field(
        default=FlextConstants.Reliability.MAX_RETRY_ATTEMPTS,
        description="Maximum number of retries",
        ge=0,
        le=10,
    )
    verify_ssl: bool = Field(
        default=True,
        description="Verify SSL certificates",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate connection configuration domain rules."""
        try:
            if not self.base_url.strip():
                return FlextResult[None].fail("Base URL cannot be empty")
            if self.timeout <= 0:
                return FlextResult[None].fail("Timeout must be positive")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Connection config validation failed: {e}")


class OICDeploymentConfig(FlextConfig):
    """OIC deployment configuration using flext-core patterns."""

    import_mode: str = Field(
        "create_or_update",
        description='Import mode: "create_only", "update_only", or "create_or_update"',
        pattern="^(create_only|update_only|create_or_update)$",
    )
    activate_integrations: bool = Field(
        default=False,
        description="Automatically activate integrations after import",
    )
    validate_connections: bool = Field(
        default=True,
        description="Validate connections before creating/updating",
    )
    archive_directory: str | None = Field(
        None,
        description="Directory to read integration archives from",
    )
    rollback_on_failure: bool = Field(
        default=True,
        description="Rollback deployment on failure",
    )
    enable_versioning: bool = Field(
        default=True,
        description="Enable integration versioning",
    )
    audit_trail: bool = Field(
        default=True,
        description="Enable audit trail logging",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate deployment configuration domain rules."""
        try:
            valid_modes = {"create_only", "update_only", "create_or_update"}
            if self.import_mode not in valid_modes:
                return FlextResult[None].fail(
                    f"Invalid import mode: {self.import_mode}",
                )
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Deployment config validation failed: {e}")


class OICProcessingConfig(FlextConfig):
    """OIC processing configuration using flext-core patterns."""

    batch_size: int = Field(
        100,
        description="Batch size for bulk operations",
        gt=0,
        le=1000,
    )
    enable_validation: bool = Field(
        default=True,
        description="Enable payload validation before sending to OIC",
    )
    validation_strict_mode: bool = Field(
        default=False,
        description="Fail on validation errors (vs. warnings)",
    )
    skip_missing_connections: bool = Field(
        default=False,
        description="Skip integrations with missing connections",
    )
    max_errors: int = Field(
        10,
        description="Maximum number of errors before stopping",
        ge=0,
    )
    ignore_transformation_errors: bool = Field(
        default=True,
        description="Continue processing on transformation errors",
    )
    dry_run_mode: bool = Field(
        default=False,
        description="Validate and transform without actually loading data",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate processing configuration domain rules."""
        try:
            if self.batch_size <= 0:
                return FlextResult[None].fail("Batch size must be positive")
            if self.max_errors < 0:
                return FlextResult[None].fail("Max errors cannot be negative")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Processing config validation failed: {e}")


class OICEntityConfig(FlextConfig):
    """OIC entity configuration using flext-core patterns."""

    integration_identifier_field: str = Field(
        default="integration_id",
        description="Field name to use as integration identifier",
    )
    connection_identifier_field: str = Field(
        default="connection_id",
        description="Field name to use as connection identifier",
    )
    lookup_identifier_field: str = Field(
        default="lookup_id",
        description="Field name to use as lookup identifier",
    )
    identifier_fields: FlextTypes.Core.Headers = Field(
        default_factory=lambda: {
            "integrations": "code",
            "connections": "code",
            "lookups": "name",
        },
        description="Identifier fields per entity type",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate entity configuration domain rules."""
        try:
            required_fields = [
                "integration_identifier_field",
                "connection_identifier_field",
                "lookup_identifier_field",
            ]
            for field in required_fields:
                value = getattr(self, field)
                if not value or not value.strip():
                    return FlextResult[None].fail(f"{field} cannot be empty")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Entity config validation failed: {e}")


class TargetOracleOICConfig(FlextConfig):
    """Complete configuration for target-oracle-oic using dependency injection.

    Uses dependency injection patterns to access Oracle OIC functionality.
    Zero tolerance for architectural violations.
    """

    model_config = SettingsConfigDict(
        env_prefix="TARGET_ORACLE_OIC_",
        case_sensitive=False,
        extra="ignore",
        str_strip_whitespace=True,
        validate_assignment=True,
        arbitrary_types_allowed=True,
        frozen=False,
    )

    # Structured configuration using value objects
    auth: OICAuthConfig = Field(
        default_factory=lambda: OICAuthConfig(
            oauth_client_id="",
            oauth_client_secret=SecretStr(""),
            oauth_token_url="",
            oauth_client_aud=None,
        ),
        description="Authentication configuration",
    )
    connection: OICConnectionConfig = Field(
        default_factory=lambda: OICConnectionConfig(
            base_url="https://your-instance.integration.ocp.oraclecloud.com",
        ),
        description="Connection configuration",
    )
    deployment: OICDeploymentConfig = Field(
        default_factory=lambda: OICDeploymentConfig(
            import_mode="create_or_update",
            activate_integrations=False,
            validate_connections=True,
            archive_directory=None,
            rollback_on_failure=True,
            enable_versioning=True,
            audit_trail=True,
        ),
        description="Deployment configuration",
    )
    processing: OICProcessingConfig = Field(
        default_factory=lambda: OICProcessingConfig(
            batch_size=100,
            enable_validation=True,
            validation_strict_mode=False,
            skip_missing_connections=False,
            max_errors=10,
            ignore_transformation_errors=True,
            dry_run_mode=False,
        ),
        description="Processing configuration",
    )
    entities: OICEntityConfig = Field(
        default_factory=lambda: OICEntityConfig(
            integration_identifier_field="integration_id",
            connection_identifier_field="connection_id",
            lookup_identifier_field="lookup_id",
            identifier_fields={},
        ),
        description="Entity configuration",
    )

    # Custom transformation rules
    transformation_rules: list[FlextTypes.Core.Dict] = Field(
        default_factory=list,
        description="Custom transformation rules",
    )

    # Project identification
    project_name: str = Field(
        default="flext-target-oracle-oic",
        description="Project name",
    )
    project_version: str = Field(
        default="0.9.0",
        description="Project version",
    )

    @model_validator(mode="after")
    def validate_configuration(self: object) -> TargetOracleOICConfig:
        """Validate complete configuration using dependency injection."""
        msg: str = ""  # Declare msg here
        # Use centralized FlextModels validation instead of duplicate path logic
        if self.deployment.archive_directory:
            validation_result = FlextModels.create_validated_directory_path(
                self.deployment.archive_directory,
            )
            if validation_result.is_failure:
                msg = f"Archive directory validation failed: {validation_result.error}"
                raise ValueError(msg)

        # Validate each configuration section
        auth_validation = self.auth.validate_business_rules()
        if not auth_validation.success:
            msg = f"Auth validation failed: {auth_validation.error}"
            raise ValueError(msg)

        connection_validation = self.connection.validate_business_rules()
        if not connection_validation.success:
            msg = f"Connection validation failed: {connection_validation.error}"
            raise ValueError(msg)

        return self

    def get_oauth_headers(self: object) -> FlextTypes.Core.Headers:
        """Get OAuth headers for API requests."""
        # Return authentication headers directly - no duplication
        return {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }

    def get_entity_identifier_field(self, entity_type: str) -> str:
        """Get identifier field for entity type."""
        return self.entities.identifier_fields.get(entity_type, "id")

    def validate_domain_rules(self: object) -> FlextResult[None]:
        """Validate configuration domain rules."""
        try:
            # Validate each section - collect all validations first
            validations = [
                ("Auth", self.auth.validate_business_rules()),
                ("Connection", self.connection.validate_business_rules()),
                ("Deployment", self.deployment.validate_business_rules()),
                ("Processing", self.processing.validate_business_rules()),
                ("Entities", self.entities.validate_business_rules()),
            ]

            # Check for first failure
            for section_name, validation_result in validations:
                if not validation_result.success:
                    return FlextResult[None].fail(
                        f"{section_name} validation failed: {validation_result.error}",
                    )

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Configuration validation failed: {e}")

    # Pydantic/FlextModels compatibility: provide business rule validator expected by base class
    def validate_business_rules(self: object) -> FlextResult[None]:
        """Alias to validate_domain_rules for business rule validation."""
        return self.validate_domain_rules()

    @classmethod
    def get_global_instance(cls) -> Self:
        """Get the global singleton instance using enhanced FlextConfig pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-target-oracle-oic")

    @classmethod
    def create_for_development(cls, **overrides: object) -> Self:
        """Create configuration for development environment."""
        dev_overrides: dict[str, object] = {
            "processing": OICProcessingConfig(
                batch_size=10,  # Smaller batches for development
                enable_validation=True,
                validation_strict_mode=True,
                dry_run_mode=True,
            ),
            "deployment": OICDeploymentConfig(
                import_mode="create_or_update",
                activate_integrations=False,
                validate_connections=True,
            ),
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-target-oracle-oic", **dev_overrides
        )

    @classmethod
    def create_for_production(cls, **overrides: object) -> Self:
        """Create configuration for production environment."""
        prod_overrides: dict[str, object] = {
            "processing": OICProcessingConfig(
                batch_size=100,
                enable_validation=True,
                validation_strict_mode=False,
                dry_run_mode=False,
            ),
            "deployment": OICDeploymentConfig(
                import_mode="create_or_update",
                activate_integrations=True,
                validate_connections=True,
                rollback_on_failure=True,
            ),
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-target-oracle-oic", **prod_overrides
        )

    @classmethod
    def create_for_testing(cls, **overrides: object) -> Self:
        """Create configuration for testing environment."""
        test_overrides: dict[str, object] = {
            "processing": OICProcessingConfig(
                batch_size=5,
                enable_validation=True,
                validation_strict_mode=True,
                dry_run_mode=True,
            ),
            "connection": OICConnectionConfig(
                base_url="https://test-instance.integration.ocp.oraclecloud.com",
            ),
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-target-oracle-oic", **test_overrides
        )

    @classmethod
    def create_with_defaults(
        cls,
        **overrides: FlextTypes.Core.Dict,
    ) -> TargetOracleOICConfig:
        """Create configuration with intelligent defaults."""
        defaults = {
            "auth": OICAuthConfig(
                oauth_client_id="your-client-id",
                oauth_client_secret=SecretStr("your-client-secret"),  # nosec B106 - Example configuration value
                oauth_token_url="",
                oauth_client_aud=None,
            ),
            "connection": OICConnectionConfig(
                base_url="https://your-instance.integration.ocp.oraclecloud.com",
            ),
            "deployment": OICDeploymentConfig(
                import_mode="create_or_update",
                activate_integrations=False,
                validate_connections=True,
                archive_directory=None,
                rollback_on_failure=True,
                enable_versioning=True,
                audit_trail=True,
            ),
            "processing": OICProcessingConfig(
                batch_size=100,
                enable_validation=True,
                validation_strict_mode=False,
                skip_missing_connections=False,
                max_errors=10,
                ignore_transformation_errors=True,
                dry_run_mode=False,
            ),
            "entities": OICEntityConfig(
                integration_identifier_field="code",
                connection_identifier_field="code",
                lookup_identifier_field="name",
                identifier_fields={},
            ),
            "project_name": "flext-target-oracle-oic",
            "project_version": "0.9.0",
        }
        defaults.update(overrides)
        return cls.model_validate(defaults)


# Export configuration classes
__all__: FlextTypes.Core.StringList = [
    "OICAuthConfig",
    "OICConnectionConfig",
    "OICDeploymentConfig",
    "OICEntityConfig",
    "OICProcessingConfig",
    "TargetOracleOICConfig",
]
