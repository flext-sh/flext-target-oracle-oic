"""Configuration for target-oracle-oic using flext-core patterns."""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextResult, FlextValueObject
from pydantic import Field, SecretStr, model_validator


class OICAuthConfig(FlextValueObject):
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

    def validate_domain_rules(self) -> FlextResult[None]:
        """Validate authentication configuration domain rules."""
        try:
            if not self.oauth_client_id.strip():
                return FlextResult.fail("OAuth client ID cannot be empty")
            if not self.oauth_token_url.strip():
                return FlextResult.fail("OAuth token URL cannot be empty")
            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Auth config validation failed: {e}")


class OICConnectionConfig(FlextValueObject):
    """OIC connection configuration using flext-core patterns."""

    base_url: str = Field(
        ...,
        description="Oracle OIC base URL",
        pattern=r"^https://.*\.integration\.ocp\.oraclecloud\.com$",
    )
    timeout: int = Field(
        default=30,
        description="Request timeout in seconds",
        gt=0,
        le=300,
    )
    max_retries: int = Field(
        default=3,
        description="Maximum number of retries",
        ge=0,
        le=10,
    )
    verify_ssl: bool = Field(
        default=True,
        description="Verify SSL certificates",
    )

    def validate_domain_rules(self) -> FlextResult[None]:
        """Validate connection configuration domain rules."""
        try:
            if not self.base_url.strip():
                return FlextResult.fail("Base URL cannot be empty")
            if self.timeout <= 0:
                return FlextResult.fail("Timeout must be positive")
            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Connection config validation failed: {e}")


class OICDeploymentConfig(FlextValueObject):
    """OIC deployment configuration using flext-core patterns."""

    import_mode: str = Field(
        "create_or_update",
        description="Import mode: create_only, update_only, or create_or_update",
        pattern="^(create_only|update_only|create_or_update)$",
    )
    activate_integrations: bool = Field(
        False,
        description="Automatically activate integrations after import",
    )
    validate_connections: bool = Field(
        True,
        description="Validate connections before creating/updating",
    )
    archive_directory: str | None = Field(
        None,
        description="Directory to read integration archives from",
    )
    rollback_on_failure: bool = Field(
        True,
        description="Rollback deployment on failure",
    )
    enable_versioning: bool = Field(
        True,
        description="Enable integration versioning",
    )
    audit_trail: bool = Field(
        True,
        description="Enable audit trail logging",
    )

    def validate_domain_rules(self) -> FlextResult[None]:
        """Validate deployment configuration domain rules."""
        try:
            valid_modes = {"create_only", "update_only", "create_or_update"}
            if self.import_mode not in valid_modes:
                return FlextResult.fail(f"Invalid import mode: {self.import_mode}")
            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Deployment config validation failed: {e}")


class OICProcessingConfig(FlextValueObject):
    """OIC processing configuration using flext-core patterns."""

    batch_size: int = Field(
        100,
        description="Batch size for bulk operations",
        gt=0,
        le=1000,
    )
    enable_validation: bool = Field(
        True,
        description="Enable payload validation before sending to OIC",
    )
    validation_strict_mode: bool = Field(
        False,
        description="Fail on validation errors (vs. warnings)",
    )
    skip_missing_connections: bool = Field(
        False,
        description="Skip integrations with missing connections",
    )
    max_errors: int = Field(
        10,
        description="Maximum number of errors before stopping",
        ge=0,
    )
    ignore_transformation_errors: bool = Field(
        True,
        description="Continue processing on transformation errors",
    )
    dry_run_mode: bool = Field(
        False,
        description="Validate and transform without actually loading data",
    )

    def validate_domain_rules(self) -> FlextResult[None]:
        """Validate processing configuration domain rules."""
        try:
            if self.batch_size <= 0:
                return FlextResult.fail("Batch size must be positive")
            if self.max_errors < 0:
                return FlextResult.fail("Max errors cannot be negative")
            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Processing config validation failed: {e}")


class OICEntityConfig(FlextValueObject):
    """OIC entity configuration using flext-core patterns."""

    integration_identifier_field: str = Field(
        "code",
        description="Field name to use as integration identifier",
    )
    connection_identifier_field: str = Field(
        "code",
        description="Field name to use as connection identifier",
    )
    lookup_identifier_field: str = Field(
        "name",
        description="Field name to use as lookup identifier",
    )
    identifier_fields: dict[str, str] = Field(
        default_factory=lambda: {
            "integrations": "code",
            "connections": "code",
            "lookups": "name",
        },
        description="Identifier fields per entity type",
    )

    def validate_domain_rules(self) -> FlextResult[None]:
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
                    return FlextResult.fail(f"{field} cannot be empty")
            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Entity config validation failed: {e}")


class TargetOracleOICConfig(FlextValueObject):
    """Complete configuration for target-oracle-oic using dependency injection.

    Uses dependency injection patterns to access Oracle OIC functionality.
    Zero tolerance for architectural violations.
    """

    class Config:
        """Pydantic configuration."""

        env_prefix = "TARGET_ORACLE_OIC_"
        case_sensitive = False

    # Structured configuration using value objects
    auth: OICAuthConfig = Field(
        default_factory=lambda: OICAuthConfig(
            oauth_client_id="",
            oauth_client_secret=SecretStr(""),
            oauth_token_url="",
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
            integration_identifier_field="code",
            connection_identifier_field="code",
            lookup_identifier_field="name",
            identifier_fields={},
        ),
        description="Entity configuration",
    )

    # Custom transformation rules
    transformation_rules: list[dict[str, object]] = Field(
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
    def validate_configuration(self) -> TargetOracleOICConfig:
        """Validate complete configuration using dependency injection."""
        # Validate archive directory if provided
        if self.deployment.archive_directory:
            archive_path = Path(self.deployment.archive_directory)
            if not archive_path.exists():
                msg = f"Archive directory does not exist: {archive_path}"
                raise ValueError(msg)
            if not archive_path.is_dir():
                msg = f"Archive path is not a directory: {archive_path}"
                raise ValueError(msg)

        # Validate each configuration section
        auth_validation = self.auth.validate_domain_rules()
        if not auth_validation.is_success:
            msg = f"Auth validation failed: {auth_validation.error}"
            raise ValueError(msg)

        connection_validation = self.connection.validate_domain_rules()
        if not connection_validation.is_success:
            msg = f"Connection validation failed: {connection_validation.error}"
            raise ValueError(msg)

        return self

    def get_oauth_headers(self) -> dict[str, str]:
        """Get OAuth headers for API requests."""
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def get_entity_identifier_field(self, entity_type: str) -> str:
        """Get identifier field for entity type."""
        return self.entities.identifier_fields.get(entity_type, "id")

    def validate_domain_rules(self) -> FlextResult[None]:
        """Validate configuration domain rules."""
        try:
            # Validate each section
            auth_validation = self.auth.validate_domain_rules()
            if not auth_validation.is_success:
                return FlextResult.fail(
                    f"Auth validation failed: {auth_validation.error}",
                )

            connection_validation = self.connection.validate_domain_rules()
            if not connection_validation.is_success:
                return FlextResult.fail(
                    f"Connection validation failed: {connection_validation.error}",
                )

            deployment_validation = self.deployment.validate_domain_rules()
            if not deployment_validation.is_success:
                return FlextResult.fail(
                    f"Deployment validation failed: {deployment_validation.error}",
                )

            processing_validation = self.processing.validate_domain_rules()
            if not processing_validation.is_success:
                return FlextResult.fail(
                    f"Processing validation failed: {processing_validation.error}",
                )

            entities_validation = self.entities.validate_domain_rules()
            if not entities_validation.is_success:
                return FlextResult.fail(
                    f"Entities validation failed: {entities_validation.error}",
                )

            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Configuration validation failed: {e}")

    @classmethod
    def create_with_defaults(
        cls,
        **overrides: dict[str, object],
    ) -> TargetOracleOICConfig:
        """Create configuration with intelligent defaults."""
        defaults = {
            "auth": OICAuthConfig(
                oauth_client_id="your-client-id",
                oauth_client_secret=SecretStr("your-client-secret"),  # nosec B106 - Example configuration value
                oauth_token_url="https://idcs-url/oauth2/v1/token",
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
__all__ = [
    "OICAuthConfig",
    "OICConnectionConfig",
    "OICDeploymentConfig",
    "OICEntityConfig",
    "OICProcessingConfig",
    "TargetOracleOICConfig",
]
