"""Configuration for target-oracle-oic using dependency injection patterns.

Refactored to use dependency injection for Oracle OIC configuration.
Eliminates architectural violations by using abstract interfaces.
"""

from __future__ import annotations

from pathlib import Path

# Oracle OIC validation provider will be injected at runtime
from typing import Any, Any as ValidationProvider

from flext_core import Field
from flext_core.domain.pydantic_base import DomainValueObject
from pydantic import SecretStr, model_validator
from pydantic_settings import BaseSettings as PydanticSettings, SettingsConfigDict

_oic_validation_provider: ValidationProvider | None = None


def set_oic_validation_provider(provider: ValidationProvider) -> None:
    """Set the Oracle OIC validation provider via dependency injection.

    Args:
        provider: Oracle OIC validation provider implementation

    """
    global _oic_validation_provider
    _oic_validation_provider = provider


def _get_oic_validation_provider() -> ValidationProvider | None:
    """Get OIC validation provider if available.

    Returns:
        Oracle OIC validation provider or None if not injected

    """
    return _oic_validation_provider


class OICAuthConfig(DomainValueObject):
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


class OICConnectionConfig(DomainValueObject):
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


class OICDeploymentConfig(DomainValueObject):
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


class OICProcessingConfig(DomainValueObject):
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


class OICEntityConfig(DomainValueObject):
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


class TargetOracleOICConfig(PydanticSettings):
    """Complete configuration for target-oracle-oic using dependency injection.

    Uses dependency injection patterns to access Oracle OIC functionality.
    Zero tolerance for architectural violations.
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

        # Try to use injected OIC validation provider
        provider = _get_oic_validation_provider()
        if provider:
            # Use provider for additional validation if available
            validation_result = provider.validate_oic_record(
                {
                    "oauth_client_id": self.auth.oauth_client_id,
                    "base_url": self.connection.base_url,
                },
            )
            if not validation_result.is_success:
                msg = f"OIC validation failed: {validation_result.error}"
                raise ValueError(msg)

        return self

    def get_oauth_headers(self) -> dict[str, str]:
        """Get OAuth headers using dependency injection or fallback."""
        # Try to use injected provider first
        provider = _get_oic_validation_provider()
        if provider:
            # Provider would implement this functionality
            return {
                "Authorization": "Bearer <token-from-provider>",
                "Content-Type": "application/json",
            }

        # Fallback implementation
        return {
            "Authorization": "Bearer <token>",
            "Content-Type": "application/json",
        }

    def get_entity_identifier_field(self, entity_type: str) -> str:
        """Get identifier field for entity type."""
        return self.entities.identifier_fields.get(entity_type, "id")

    @classmethod
    def create_with_defaults(cls, **overrides: dict[str, Any]) -> TargetOracleOICConfig:
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
            "project_version": "0.7.0",
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
    "set_oic_validation_provider",
]
