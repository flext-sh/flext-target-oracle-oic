"""Configuration for target-oracle-oic using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Self

from flext_core import FlextConstants, FlextResult, FlextSettings
from flext_target_oracle_oic.typings import t
from pydantic import (
    AnyUrl,
    BaseModel,
    ConfigDict,
    Field,
    SecretStr,
    computed_field,
    field_validator,
    model_validator,
)
from pydantic_settings import SettingsConfigDict


class TargetOracleOicConfig(FlextSettings):
    """Single flat Config class for target-oracle-oic extending FlextSettings.

    Follows standardized FLEXT Config pattern:
    - Single flat class extending FlextSettings
    - Uses Pydantic 2 Settings with SettingsConfigDict
    - Uses SecretStr for sensitive data
    - Implements singleton pattern with inverse dependency injection
    - All fields with defaults from constants
    - Uses BaseModel structures for validation helpers
    """

    # BaseModel structures for configuration validation
    class AuthConfigDict(BaseModel):
        """Authentication configuration dictionary structure."""

        model_config = ConfigDict(frozen=False, extra="forbid")

        oauth_client_id: str
        oauth_client_secret: str  # Note: will be SecretStr in actual fields
        oauth_token_url: str
        oauth_client_aud: str | None = None
        oauth_scope: str

    class ConnectionConfigDict(BaseModel):
        """Connection configuration dictionary structure."""

        model_config = ConfigDict(frozen=False, extra="forbid")

        base_url: str
        timeout: int
        max_retries: int
        verify_ssl: bool

    class DeploymentConfigDict(BaseModel):
        """Deployment configuration dictionary structure."""

        model_config = ConfigDict(frozen=False, extra="forbid")

        import_mode: str
        activate_integrations: bool
        validate_connections: bool
        archive_directory: str | None = None
        rollback_on_failure: bool
        enable_versioning: bool
        audit_trail: bool

    class ProcessingConfigDict(BaseModel):
        """Processing configuration dictionary structure."""

        model_config = ConfigDict(frozen=False, extra="forbid")

        batch_size: int
        enable_validation: bool
        validation_strict_mode: bool
        skip_missing_connections: bool
        max_errors: int
        ignore_transformation_errors: bool
        dry_run_mode: bool

    class EntityConfigDict(BaseModel):
        """Entity configuration dictionary structure."""

        model_config = ConfigDict(frozen=False, extra="forbid")

        integration_identifier_field: str
        connection_identifier_field: str
        lookup_identifier_field: str
        identifier_fields: dict[str, str]

    model_config = SettingsConfigDict(
        env_prefix="TARGET_ORACLE_OIC_",
        case_sensitive=False,
        extra="allow",
        str_strip_whitespace=True,
        validate_assignment=True,
        arbitrary_types_allowed=True,
        frozen=False,
        # Enhanced Pydantic 2.11+ features
        json_schema_extra={
            "title": "Target Oracle OIC Configuration",
            "description": (
                "Enterprise Oracle OIC target configuration extending FlextSettings"
            ),
        },
    )

    # Authentication configuration fields
    oauth_client_id: str = Field(
        ...,
        description="OAuth2 client ID for Oracle OIC authentication",
        min_length=1,
    )
    oauth_client_secret: SecretStr = Field(
        ...,
        description="OAuth2 client secret for Oracle OIC authentication",
    )
    oauth_token_url: AnyUrl = Field(
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

    # Connection configuration fields
    base_url: AnyUrl = Field(
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

    # Deployment configuration fields
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

    # Processing configuration fields
    batch_size: int = Field(
        FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE // 10,
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
        FlextConstants.Reliability.MAX_RETRY_ATTEMPTS * 3 + 1,
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

    # Entity configuration fields
    integration_identifier_field: str = Field(
        default="integration_id",
        min_length=1,
        description="Field name to use as integration identifier",
    )
    connection_identifier_field: str = Field(
        default="connection_id",
        min_length=1,
        description="Field name to use as connection identifier",
    )
    lookup_identifier_field: str = Field(
        default="lookup_id",
        min_length=1,
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

    # Additional configuration fields
    transformation_rules: list[dict[str, t.JsonValue]] = Field(
        default_factory=list,
        description="Custom transformation rules",
    )
    project_name: str = Field(
        default="flext-target-oracle-oic",
        description="Project name",
    )
    project_version: str = Field(
        default="0.9.0",
        description="Project version",
    )

    # Field validators
    @field_validator("import_mode")
    @classmethod
    def validate_import_mode(cls, v: str) -> str:
        """Validate import mode."""
        valid_modes = {"create_only", "update_only", "create_or_update"}
        if v not in valid_modes:
            msg = f"Invalid import mode: {v}. Must be one of: {', '.join(sorted(valid_modes))}"
            raise ValueError(msg)
        return v

    # Model validator
    @model_validator(mode="after")
    def validate_configuration(self) -> Self:
        """Validate complete configuration."""
        # Validate timeout
        if self.timeout <= 0:
            msg = "Timeout must be positive"
            raise ValueError(msg)

        # Validate batch size
        if self.batch_size <= 0:
            msg = "Batch size must be positive"
            raise ValueError(msg)

        # Validate max errors
        if self.max_errors < 0:
            msg = "Max errors cannot be negative"
            raise ValueError(msg)

        return self

    # Computed fields
    @computed_field
    def auth_config(self) -> Mapping[str, str | None]:
        """Get authentication configuration as dictionary."""
        return {
            "oauth_client_id": self.oauth_client_id,
            "oauth_client_secret": self.oauth_client_secret.get_secret_value(),
            "oauth_token_url": str(self.oauth_token_url),
            "oauth_client_aud": self.oauth_client_aud,
            "oauth_scope": self.oauth_scope,
        }

    @computed_field
    def connection_config(self) -> Mapping[str, str | int | bool]:
        """Get connection configuration as dictionary."""
        return {
            "base_url": str(self.base_url),
            "timeout": self.timeout,
            "max_retries": self.max_retries,
            "verify_ssl": self.verify_ssl,
        }

    @computed_field
    def deployment_config(self) -> Mapping[str, str | bool | None]:
        """Get deployment configuration as dictionary."""
        return {
            "import_mode": self.import_mode,
            "activate_integrations": self.activate_integrations,
            "validate_connections": self.validate_connections,
            "archive_directory": self.archive_directory,
            "rollback_on_failure": self.rollback_on_failure,
            "enable_versioning": self.enable_versioning,
            "audit_trail": self.audit_trail,
        }

    @computed_field
    def processing_config(self) -> Mapping[str, int | bool]:
        """Get processing configuration as dictionary."""
        return {
            "batch_size": self.batch_size,
            "enable_validation": self.enable_validation,
            "validation_strict_mode": self.validation_strict_mode,
            "skip_missing_connections": self.skip_missing_connections,
            "max_errors": self.max_errors,
            "ignore_transformation_errors": self.ignore_transformation_errors,
            "dry_run_mode": self.dry_run_mode,
        }

    @computed_field
    def entity_config(self) -> Mapping[str, str | Mapping[str, str]]:
        """Get entity configuration as dictionary."""
        return {
            "integration_identifier_field": self.integration_identifier_field,
            "connection_identifier_field": self.connection_identifier_field,
            "lookup_identifier_field": self.lookup_identifier_field,
            "identifier_fields": self.identifier_fields,
        }

    # Utility methods
    def get_oauth_headers(self) -> Mapping[str, str]:
        """Get OAuth headers for API requests."""
        return {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }

    def get_entity_identifier_field(self, entity_type: str) -> str:
        """Get identifier field for entity type."""
        return self.identifier_fields.get(entity_type, "id")

    def get_oauth_client_secret_value(self) -> str:
        """Get the actual OAuth client secret value (safely extract from SecretStr)."""
        return self.oauth_client_secret.get_secret_value()

    def validate_business_rules(self) -> FlextResult[bool]:
        """Validate configuration business rules."""
        try:
            # Validate authentication configuration
            if not self.oauth_client_id:
                return FlextResult[bool].fail("OAuth client ID cannot be empty")
            if not str(self.oauth_token_url):
                return FlextResult[bool].fail("OAuth token URL cannot be empty")

            # Validate connection configuration
            if not str(self.base_url):
                return FlextResult[bool].fail("Base URL cannot be empty")
            if self.timeout <= 0:
                return FlextResult[bool].fail("Timeout must be positive")

            # Validate deployment configuration
            valid_modes = {"create_only", "update_only", "create_or_update"}
            if self.import_mode not in valid_modes:
                return FlextResult[bool].fail(
                    f"Invalid import mode: {self.import_mode}",
                )

            # Validate processing configuration
            if self.batch_size <= 0:
                return FlextResult[bool].fail("Batch size must be positive")
            if self.max_errors < 0:
                return FlextResult[bool].fail("Max errors cannot be negative")

            return FlextResult[bool].ok(value=True)
        except (ValueError, TypeError, KeyError, AttributeError, OSError, RuntimeError, ImportError) as e:
            return FlextResult[bool].fail(f"Configuration validation failed: {e}")

    # Singleton pattern methods
    @classmethod
    def get_global_instance(cls) -> Self:
        """Get the global singleton instance using enhanced FlextSettings pattern."""
        return cls()

    @classmethod
    def create_for_development(cls, **overrides: t.JsonValue) -> Self:
        """Create configuration for development environment."""
        dev_overrides: dict[str, t.JsonValue] = {
            "batch_size": FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
            // 100,
            "enable_validation": True,
            "validation_strict_mode": True,
            "dry_run_mode": True,
            "activate_integrations": False,
            "validate_connections": True,
            **overrides,
        }
        return cls(**dev_overrides)

    @classmethod
    def create_for_production(cls, **overrides: t.JsonValue) -> Self:
        """Create configuration for production environment."""
        prod_overrides: dict[str, t.JsonValue] = {
            "batch_size": FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE // 10,
            "enable_validation": True,
            "validation_strict_mode": False,
            "dry_run_mode": False,
            "activate_integrations": True,
            "validate_connections": True,
            "rollback_on_failure": True,
            **overrides,
        }
        return cls(**prod_overrides)

    @classmethod
    def create_for_testing(cls, **overrides: t.JsonValue) -> Self:
        """Create configuration for testing environment."""
        test_overrides: dict[str, t.JsonValue] = {
            "batch_size": FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
            // 200,
            "enable_validation": True,
            "validation_strict_mode": True,
            "dry_run_mode": True,
            "base_url": "https://test-instance.integration.ocp.oraclecloud.com",
            **overrides,
        }
        return cls(**test_overrides)


# Export configuration class (single class only)
__all__: list[str] = [
    "TargetOracleOicConfig",
]
