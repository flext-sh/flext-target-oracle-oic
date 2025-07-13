"""Configuration for target-oracle-oic using flext-core patterns.

MIGRATED TO FLEXT-CORE:
Uses flext-core SingerTargetConfig with structured value objects. Zero tolerance for code duplication.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from flext_core.domain.pydantic_base import DomainValueObject


class OICAuthConfig(DomainValueObject):
    """OIC authentication configuration value object using flext-core patterns."""

    oauth_client_id: str = Field(
        default="",
        description="OAuth2 client ID from IDCS application",
    )
    oauth_client_secret: str = Field(
        default="",
        description="OAuth2 client secret from IDCS application",
        json_schema_extra={"secret": True},
    )
    oauth_token_url: str = Field(
        default="",
        description="IDCS token endpoint URL",
    )
    oauth_client_aud: str | None = Field(
        default=None,
        description="IDCS client audience URL for scope building",
    )

    @field_validator("oauth_token_url")
    @classmethod
    def validate_oauth_token_url(cls, v: str) -> str:
        """Validate OAuth token URL format.

        Args:
            v: The OAuth token URL to validate.

        Returns:
            The validated URL.

        Raises:
            ValueError: If URL doesn't start with http:// or https://.

        """
        if not v.startswith(("http://", "https://")):
            msg = "oauth_token_url must start with http:// or https://"
            raise ValueError(msg)
        return v


class OICConnectionConfig(DomainValueObject):
    """OIC connection configuration value object using flext-core patterns."""

    base_url: str = Field(
        default="",
        description="OIC instance base URL (e.g., https://myinstance-region.integration.ocp.oraclecloud.com)",
    )
    timeout: int = Field(
        default=30,
        description="Request timeout in seconds",
        gt=0,
        le=300,
    )
    max_retries: int = Field(
        default=3,
        description="Maximum number of retry attempts",
        ge=0,
        le=10,
    )
    retry_delay: float = Field(
        default=1.0,
        description="Delay between retries in seconds",
        gt=0.0,
        le=60.0,
    )
    max_concurrent_requests: int = Field(
        default=5,
        description="Maximum concurrent requests",
        gt=0,
        le=20,
    )

    @field_validator("base_url")
    @classmethod
    def validate_base_url(cls, v: str) -> str:
        """Validate base URL format.

        Args:
            v: The base URL to validate.

        Returns:
            The validated URL with trailing slash removed.

        Raises:
            ValueError: If URL doesn't start with http:// or https://.

        """
        if not v.startswith(("http://", "https://")):
            msg = "base_url must start with http:// or https://"
            raise ValueError(msg)
        return v.rstrip("/")


class OICDeploymentConfig(DomainValueObject):
    """OIC deployment configuration value object using flext-core patterns."""

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


class OICProcessingConfig(DomainValueObject):
    """OIC processing configuration value object using flext-core patterns."""

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


class OICEntityConfig(DomainValueObject):
    """OIC entity configuration value object using flext-core patterns."""

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


class TargetOracleOICConfig(BaseSettings):
    """Complete configuration for target-oracle-oic v0.7.0 using flext-core patterns.

    Uses flext-core patterns with structured value objects. Zero tolerance for legacy patterns or code duplication.
    """

    model_config = SettingsConfigDict(
        env_prefix="TARGET_ORACLE_OIC_",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="allow",
        validate_assignment=True,
        str_strip_whitespace=True,
        use_enum_values=True,
    )

    # Structured configuration using value objects
    auth: OICAuthConfig = Field(
        default_factory=OICAuthConfig,
        description="Authentication configuration",
    )
    connection: OICConnectionConfig = Field(
        default_factory=OICConnectionConfig,
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
    transformation_rules: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Custom transformation rules",
    )

    # Project identification
    project_name: str = Field(
        default="flext-target-oracle-oic",
        description="Project name",
    )
    project_version: str = Field(
        default="0.7.0",
        description="Project version",
    )

    @model_validator(mode="after")
    def validate_configuration(self) -> TargetOracleOICConfig:
        """Validate complete configuration."""
        # Validate archive directory if provided
        if self.deployment.archive_directory:
            archive_path = Path(self.deployment.archive_directory)
            if not archive_path.exists():
                msg = f"Archive directory does not exist: {archive_path}"
                raise ValueError(msg)
            if not archive_path.is_dir():
                msg = f"Archive directory is not a directory: {archive_path}"
                raise ValueError(msg)

        return self

    def get_oauth_headers(self) -> dict[str, str]:
        """Get OAuth headers (implemented by client using flext-auth)."""
        # Placeholder - will use flext-auth OAuth2 implementation
        return {
            "Authorization": "Bearer <token>",
            "Content-Type": "application/json",
        }

    def get_entity_identifier_field(self, entity_type: str) -> str:
        """Get identifier field for entity type."""
        return self.entities.identifier_fields.get(entity_type, "id")

    @classmethod
    def create_with_defaults(cls, **overrides: Any) -> TargetOracleOICConfig:
        """Create configuration with intelligent defaults."""
        defaults = {
            "auth": OICAuthConfig(
                oauth_client_id="your-client-id",
                oauth_client_secret="your-client-secret",
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
            "project_version": "0.7.0",
        }
        defaults.update(overrides)
        return cls.model_validate(defaults)


# Export main configuration classes
__all__ = [
    "OICAuthConfig",
    "OICConnectionConfig",
    "OICDeploymentConfig",
    "OICEntityConfig",
    "OICProcessingConfig",
    "TargetOracleOICConfig",
]
