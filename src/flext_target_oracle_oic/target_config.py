"""Target Oracle OIC Configuration - Unified configuration management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

PEP8-compliant configuration management with maximum flext-core composition.
"""

from __future__ import annotations

import os
from pathlib import Path

from flext_core import FlextResult, FlextValueObject
from flext_meltano import singer_typing as th
from flext_meltano.common_schemas import create_oauth2_api_tap_schema
from pydantic import Field, SecretStr, model_validator

# Import auth utilities from flext-oracle-oic-ext for maximum composition
try:
    from flext_oracle_oic_ext.auth import (
        OICAuthConfig as ExtAuthConfig,
        OICOAuth2Authenticator as ExtAuthenticator,
    )

    # Use flext-oracle-oic-ext implementations
    OICAuthConfig = ExtAuthConfig
    OICOAuth2Authenticator = ExtAuthenticator
except ImportError:
    # Fallback implementations if ext not available
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

        def validate_business_rules(self) -> FlextResult[None]:
            """Validate authentication configuration domain rules."""
            try:
                if not self.oauth_client_id.strip():
                    return FlextResult.fail("OAuth client ID cannot be empty")
                if not self.oauth_token_url.strip():
                    return FlextResult.fail("OAuth token URL cannot be empty")
                return FlextResult.ok(None)
            except Exception as e:
                return FlextResult.fail(f"Auth config validation failed: {e}")

    class OICOAuth2Authenticator:
        """Fallback OAuth2 authenticator."""

        def __init__(self, config: OICAuthConfig) -> None:
            self.config = config

        def get_access_token(self) -> FlextResult[str]:
            """Get access token - fallback implementation."""
            return FlextResult.fail("flext-oracle-oic-ext not available")


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

    def validate_business_rules(self) -> FlextResult[None]:
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

    def validate_business_rules(self) -> FlextResult[None]:
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

    def validate_business_rules(self) -> FlextResult[None]:
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

    def validate_business_rules(self) -> FlextResult[None]:
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
    """Complete configuration for target-oracle-oic using flext-core patterns.

    Uses maximum composition from flext-core and flext-oracle-oic-ext.
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
        default_factory=OICDeploymentConfig,
        description="Deployment configuration",
    )
    processing: OICProcessingConfig = Field(
        default_factory=OICProcessingConfig,
        description="Processing configuration",
    )
    entities: OICEntityConfig = Field(
        default_factory=OICEntityConfig,
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
        """Validate complete configuration."""
        msg: str = ""

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
        auth_validation = self.auth.validate_business_rules()
        if not auth_validation.success:
            msg = f"Auth validation failed: {auth_validation.error}"
            raise ValueError(msg)

        connection_validation = self.connection.validate_business_rules()
        if not connection_validation.success:
            msg = f"Connection validation failed: {connection_validation.error}"
            raise ValueError(msg)

        return self

    def get_entity_identifier_field(self, entity_type: str) -> str:
        """Get identifier field for entity type."""
        return self.entities.identifier_fields.get(entity_type, "id")

    def validate_domain_rules(self) -> FlextResult[None]:
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
                    return FlextResult.fail(
                        f"{section_name} validation failed: {validation_result.error}",
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
                oauth_token_url="",
                oauth_client_aud=None,
            ),
            "connection": OICConnectionConfig(
                base_url="https://your-instance.integration.ocp.oraclecloud.com",
            ),
            "deployment": OICDeploymentConfig(),
            "processing": OICProcessingConfig(),
            "entities": OICEntityConfig(),
            "project_name": "flext-target-oracle-oic",
            "project_version": "0.9.0",
        }
        defaults.update(overrides)
        return cls.model_validate(defaults)


# Singer SDK configuration schema creation
def create_singer_config_schema() -> dict[str, object]:
    """Create Singer SDK compatible configuration schema."""
    # Additional target-specific properties
    additional_properties = th.PropertiesList(
        th.Property(
            "oauth_client_aud",
            th.StringType,
            description="OAuth2 client audience",
        ),
        th.Property(
            "import_mode",
            th.StringType,
            allowed_values=["create", "update", "create_or_update"],
            default="create_or_update",
            description="Import mode for integrations",
        ),
        th.Property(
            "activate_integrations",
            th.BooleanType,
            default=False,
            description="Automatically activate integrations after import",
        ),
    )

    return create_oauth2_api_tap_schema(
        additional_properties=additional_properties,
    ).to_dict()


# Configuration factory functions
def create_config_from_dict(config_dict: dict[str, object]) -> TargetOracleOICConfig:
    """Create configuration from dictionary with validation."""
    return TargetOracleOICConfig.model_validate(config_dict)


def create_config_with_env_overrides(
    base_config: dict[str, object] | None = None,
) -> TargetOracleOICConfig:
    """Create configuration with environment variable overrides."""
    config = base_config or {}

    # Override with environment variables
    env_mappings = {
        "TARGET_ORACLE_OIC_BASE_URL": ("connection", "base_url"),
        "TARGET_ORACLE_OIC_OAUTH_CLIENT_ID": ("auth", "oauth_client_id"),
        "TARGET_ORACLE_OIC_OAUTH_CLIENT_SECRET": ("auth", "oauth_client_secret"),
        "TARGET_ORACLE_OIC_OAUTH_TOKEN_URL": ("auth", "oauth_token_url"),
        "TARGET_ORACLE_OIC_OAUTH_CLIENT_AUD": ("auth", "oauth_client_aud"),
        "TARGET_ORACLE_OIC_IMPORT_MODE": ("deployment", "import_mode"),
    }

    for env_key, (section, field) in env_mappings.items():
        if env_key in os.environ:
            if section not in config:
                config[section] = {}
            config[section][field] = os.environ[env_key]

    return TargetOracleOICConfig.model_validate(config)


# Export configuration classes
__all__: list[str] = [
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
