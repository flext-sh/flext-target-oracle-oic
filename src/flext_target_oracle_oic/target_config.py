"""Target Oracle OIC Configuration - Unified configuration management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

PEP8-compliant configuration management with maximum flext-core composition.
"""

from __future__ import annotations

import os
from pathlib import Path

# Replace singer_typing import with direct typing
# Skip flext-oracle-oic-ext import - not available
# from flext_oracle_oic_ext.ext_client import (
#     OICExtensionAuthenticator as OICOAuth2Authenticator,
# )
from typing import object as OICOAuth2Authenticator

from flext_core import FlextModels, FlextResult
from pydantic import BaseModel, Field, SecretStr, model_validator
from pydantic_settings import SettingsConfigDict


class OICAuthConfig(BaseModel):
    oauth_client_id: str = ""
    oauth_client_secret: SecretStr = SecretStr("")
    oauth_token_url: str = ""
    oauth_client_aud: str | None = None
    oauth_scope: str = ""


class OICConnectionConfig(FlextModels):
    """OIC connection configuration using flext-core patterns."""

    base_url: str = Field(
        default="https://your-instance.integration.ocp.oraclecloud.com",
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
                return FlextResult[None].fail("Base URL cannot be empty")
            if self.timeout <= 0:
                return FlextResult[None].fail("Timeout must be positive")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Connection config validation failed: {e}")


class OICDeploymentConfig(FlextModels):
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
                return FlextResult[None].fail(
                    f"Invalid import mode: {self.import_mode}"
                )
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Deployment config validation failed: {e}")


class OICProcessingConfig(FlextModels):
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
                return FlextResult[None].fail("Batch size must be positive")
            if self.max_errors < 0:
                return FlextResult[None].fail("Max errors cannot be negative")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Processing config validation failed: {e}")


class OICEntityConfig(FlextModels):
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
                    return FlextResult[None].fail(f"{field} cannot be empty")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Entity config validation failed: {e}")


class TargetOracleOICConfig(FlextModels):
    """Complete configuration for target-oracle-oic using flext-core patterns.

    Uses maximum composition from flext-core and flext-oracle-oic-ext.
    Zero tolerance for architectural violations.
    """

    model_config = SettingsConfigDict(
        env_prefix="TARGET_ORACLE_OIC_",
        case_sensitive=False,
    )

    # Structured configuration using value objects
    auth: OICAuthConfig = Field(
        default_factory=lambda: OICAuthConfig(
            oauth_client_id="",
            oauth_client_secret=SecretStr(""),
            oauth_token_url="",
            oauth_client_aud="",
            oauth_scope="",
        ),
        description="Authentication configuration",
    )
    connection: OICConnectionConfig = Field(
        default_factory=OICConnectionConfig,
        description="Connection configuration",
    )
    deployment: OICDeploymentConfig = Field(
        default_factory=lambda: OICDeploymentConfig(
            import_mode="create_or_update",
            archive_directory="",
        ),
        description="Deployment configuration",
    )
    processing: OICProcessingConfig = Field(
        default_factory=lambda: OICProcessingConfig(
            batch_size=100,
            max_errors=5,
        ),
        description="Processing configuration",
    )
    entities: OICEntityConfig = Field(
        default_factory=lambda: OICEntityConfig(
            integration_identifier_field="code",
            connection_identifier_field="code",
            lookup_identifier_field="name",
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
        # Auth model comes from flext-oracle-oic-ext; validate required fields
        if not self.auth.oauth_client_id:
            msg = "Auth validation failed: oauth_client_id required"
            raise ValueError(msg)
        if not self.auth.oauth_token_url:
            msg = "Auth validation failed: oauth_token_url required"
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

    # Backward compatibility with base interface expectations
    def validate_business_rules(self) -> FlextResult[None]:
        """Alias to domain rules validation for compatibility."""
        return self.validate_domain_rules()

    @classmethod
    def create_with_defaults(
        cls,
        **overrides: dict[str, object],
    ) -> TargetOracleOICConfig:
        """Create configuration with intelligent defaults."""
        defaults: dict[
            str,
            OICAuthConfig
            | OICConnectionConfig
            | OICDeploymentConfig
            | OICProcessingConfig
            | OICEntityConfig
            | str,
        ] = {
            "auth": OICAuthConfig(
                oauth_client_id="your-client-id",
                oauth_client_secret=SecretStr("your-client-secret"),  # nosec B106 - Example configuration value
                oauth_token_url="",
                oauth_client_aud=None,
                oauth_scope="",
            ),
            "connection": OICConnectionConfig(),
            "deployment": OICDeploymentConfig(
                import_mode="create_or_update",
                archive_directory="",
            ),
            "processing": OICProcessingConfig(
                batch_size=100,
                max_errors=5,
            ),
            "entities": OICEntityConfig(
                integration_identifier_field="code",
                connection_identifier_field="code",
                lookup_identifier_field="name",
            ),
            "project_name": "flext-target-oracle-oic",
            "project_version": "0.9.0",
        }
        defaults.update(overrides)
        return cls.model_validate(defaults)


# Singer SDK configuration schema creation
def create_singer_config_schema() -> dict[str, object]:
    """Create Singer SDK compatible configuration schema using target field names.

    This schema aligns with tests which provide flat configuration keys:
    - base_url, oauth_client_id, oauth_client_secret, oauth_token_url, oauth_client_aud
    """
    properties = {
        "base_url": {
            "type": "string",
            "description": "Oracle OIC base URL",
        },
        "oauth_client_id": {
            "type": "string",
            "description": "OAuth2 client ID",
        },
        "oauth_client_secret": {
            "type": "string",
            "description": "OAuth2 client secret",
            "secret": True,
        },
        "oauth_token_url": {
            "type": "string",
            "description": "OAuth2 token URL",
        },
        "oauth_client_aud": {
            "type": "string",
            "description": "OAuth2 client audience",
        },
        "import_mode": {
            "type": "string",
            "allowed_values": ["create", "update", "create_or_update"],
            "default": "create_or_update",
            "description": "Import mode for integrations",
        },
        "activate_integrations": {
            "type": "boolean",
            "default": False,
            "description": "Automatically activate integrations after import",
        },
    }

    schema = {"properties": properties}
    # Required minimal fields used in tests
    schema["required"] = [
        "base_url",
        "oauth_client_id",
        "oauth_client_secret",
        "oauth_token_url",
    ]
    return schema


# Configuration factory functions
def create_config_from_dict(config_dict: dict[str, object]) -> TargetOracleOICConfig:
    """Create configuration from dictionary with validation."""
    return TargetOracleOICConfig.model_validate(config_dict)


def create_config_with_env_overrides(
    base_config: dict[str, object] | None = None,
) -> TargetOracleOICConfig:
    """Create configuration with environment variable overrides."""
    config: dict[str, object] = dict(base_config) if base_config else {}

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
            section_obj = config[section]
            if not isinstance(section_obj, dict):
                section_obj = {}
                config[section] = section_obj
            section_obj[field] = os.environ[env_key]

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
