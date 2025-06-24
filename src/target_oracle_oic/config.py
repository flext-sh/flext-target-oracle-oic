"""Configuration schema for Oracle Integration Cloud Target."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field
from pydantic.json_schema import GenerateJsonSchema
from singer_sdk import typing as th


class TargetOracleOICConfig(BaseModel):
    """Enterprise configuration for Oracle Integration Cloud Target using Pydantic."""

    # Core OIC instance configuration
    base_url: str = Field(
        ...,
        description="OIC instance base URL (e.g., https://myinstance-region.integration.ocp.oraclecloud.com)",
        min_length=1,
    )

    # OAuth2 IDCS authentication (required)
    oauth_client_id: str = Field(
        ...,
        description="OAuth2 client ID from IDCS application",
        min_length=1,
    )

    oauth_client_secret: str = Field(
        ...,
        description="OAuth2 client secret from IDCS application",
        min_length=1,
    )

    oauth_token_url: str = Field(
        ...,
        description="IDCS token endpoint URL",
        min_length=1,
    )

    oauth_client_aud: str | None = Field(
        None,
        description="IDCS client audience URL for scope building",
    )

    # Target-specific configuration
    import_mode: str = Field(
        default="create_or_update",
        description="Import mode: 'create_only', 'update_only', or 'create_or_update'",
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

    # Request configuration
    request_timeout: int = Field(
        default=30,
        ge=1,
        le=300,
        description="Request timeout in seconds",
    )

    max_retries: int = Field(
        default=3,
        ge=0,
        le=10,
        description="Maximum number of retries for failed requests",
    )

    # Stream control
    disable_collection: bool = Field(
        default=False,
        description="Disable collection of result IDs after operations",
    )

    @classmethod
    def model_json_schema(
        cls,
        by_alias: bool = True,
        ref_template: str = "#/$defs/{model}",
        schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
        mode: Literal["validation", "serialization"] = "validation",
    ) -> dict[str, Any]:
        """Return the JSON schema for the target configuration (Singer SDK compatibility)."""
        # For Singer SDK compatibility, we return the Singer SDK format instead of Pydantic format
        properties = th.PropertiesList(
            # Core OIC instance configuration
            th.Property(
                "base_url",
                th.StringType,
                required=True,
                description="OIC instance base URL (e.g., https://myinstance-region.integration.ocp.oraclecloud.com)",
            ),
            # OAuth2 IDCS authentication (required)
            th.Property(
                "oauth_client_id",
                th.StringType,
                required=True,
                description="OAuth2 client ID from IDCS application",
            ),
            th.Property(
                "oauth_client_secret",
                th.StringType,
                required=True,
                secret=True,
                description="OAuth2 client secret from IDCS application",
            ),
            th.Property(
                "oauth_token_url",
                th.StringType,
                required=True,
                description="IDCS token endpoint URL",
            ),
            th.Property(
                "oauth_client_aud",
                th.StringType,
                description="IDCS client audience URL for scope building",
            ),
            # Target-specific configuration
            th.Property(
                "import_mode",
                th.StringType,
                default="create_or_update",
                description=(
                    "Import mode: 'create_only', 'update_only', or 'create_or_update'"
                ),
            ),
            th.Property(
                "activate_integrations",
                th.BooleanType,
                default=False,
                description="Automatically activate integrations after import",
            ),
            th.Property(
                "validate_connections",
                th.BooleanType,
                default=True,
                description="Validate connections before creating/updating",
            ),
            th.Property(
                "archive_directory",
                th.StringType,
                description="Directory to read integration archives from",
            ),
            # Request configuration
            th.Property(
                "request_timeout",
                th.IntegerType,
                default=30,
                description="Request timeout in seconds",
            ),
            th.Property(
                "max_retries",
                th.IntegerType,
                default=3,
                description="Maximum number of retries for failed requests",
            ),
            # Stream control
            th.Property(
                "disable_collection",
                th.BooleanType,
                default=False,
                description="Disable collection of result IDs after operations",
            ),
        )
        return properties.to_dict()
