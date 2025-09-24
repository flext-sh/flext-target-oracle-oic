"""Enhanced Oracle OIC Target models extending FlextModels.

Contains all Pydantic models for Oracle OIC target operations following
FLEXT standards with enhanced Pydantic 2.11 features and comprehensive validation.
"""

from __future__ import annotations

import json
import uuid
from datetime import UTC, datetime
from decimal import Decimal
from pathlib import Path
from typing import Any, Literal

from pydantic import (
    ConfigDict,
    Field,
    ValidationInfo,
    computed_field,
    field_validator,
)

from flext_core import FlextConstants, FlextModels, FlextResult

# Re-export for convenience
__all__ = ["FlextTargetOracleOICModels"]


class FlextTargetOracleOICModels(FlextModels):
    """Enhanced Oracle OIC Target models extending FlextModels.

    Contains all Pydantic models for Oracle OIC target operations following
    FLEXT standards with enhanced Pydantic 2.11 features and comprehensive validation.
    """

    # Enhanced base models with Pydantic 2.11 features
    class _BaseOICModel(FlextModels.ArbitraryTypesModel):
        """Base OIC model with enhanced Pydantic 2.11 configuration."""

        model_config = ConfigDict(
            # Enhanced Pydantic 2.11 features
            validate_assignment=True,
            use_enum_values=True,
            arbitrary_types_allowed=True,
            validate_return=True,
            ser_json_timedelta="iso8601",
            ser_json_bytes="base64",
            serialize_by_alias=True,
            populate_by_name=True,
            str_strip_whitespace=True,
            defer_build=False,
            coerce_numbers_to_str=False,
            validate_default=True,
            # Custom encoders for complex types
            json_encoders={
                Path: str,
                datetime: lambda dt: dt.isoformat(),
                Decimal: float,
            },
        )

    # Oracle OIC Authentication Models
    class OICAuthConfig(_BaseOICModel):
        """Enhanced Oracle OIC authentication configuration model."""

        oauth_client_id: str = Field(
            description="OAuth client ID",
            min_length=1,
            max_length=255,
        )
        oauth_client_secret: str = Field(
            description="OAuth client secret",
            repr=False,  # Hide in string representation for security
            min_length=1,
            max_length=255,
        )
        oauth_token_url: str = Field(
            description="OAuth token URL",
            min_length=1,
            max_length=500,
        )
        oauth_client_aud: str | None = Field(
            default=None,
            description="OAuth client audience",
            max_length=255,
        )
        oauth_scope: str | None = Field(
            default=None,
            description="OAuth scope",
            max_length=500,
        )
        oauth_grant_type: str = Field(
            default="client_credentials",
            description="OAuth grant type",
        )
        token_expiry_buffer: int = Field(
            default=300,  # 5 minutes
            description="Token expiry buffer in seconds",
            ge=0,
            le=3600,
        )

        @field_validator("oauth_token_url")
        @classmethod
        def validate_token_url(cls, v: str) -> str:
            """Validate OAuth token URL."""
            result = FlextModels.create_validated_http_url(v)
            if result.is_failure:
                raise ValueError(result.error)
            return result.unwrap()

        @field_validator("oauth_grant_type")
        @classmethod
        def validate_grant_type(cls, v: str) -> str:
            """Validate OAuth grant type."""
            valid_types = {
                "client_credentials",
                "authorization_code",
                "password",
                "refresh_token",
            }
            if v.lower() not in valid_types:
                msg = f"Invalid grant type: {v}. Valid types: {valid_types}"
                raise ValueError(msg)
            return v.lower()

        @computed_field
        def is_client_credentials(self) -> bool:
            """Check if using client credentials grant type."""
            return self.oauth_grant_type.lower() == "client_credentials"

        def validate_business_rules(self) -> FlextResult[None]:
            """Validate authentication business rules."""
            try:
                if not self.oauth_client_id.strip():
                    return FlextResult[None].fail("OAuth client ID cannot be empty")
                if not self.oauth_client_secret.strip():
                    return FlextResult[None].fail("OAuth client secret cannot be empty")
                if not self.oauth_token_url.strip():
                    return FlextResult[None].fail("OAuth token URL cannot be empty")
                return FlextResult[None].ok(None)
            except Exception as e:
                return FlextResult[None].fail(f"Authentication validation failed: {e}")

    # Oracle OIC Connection Models
    class OICConnectionConfig(_BaseOICModel):
        """Enhanced Oracle OIC connection configuration model."""

        base_url: str = Field(
            description="Oracle OIC base URL",
            min_length=1,
            max_length=500,
        )
        api_version: str = Field(
            default="v1",
            description="API version",
            min_length=1,
            max_length=10,
        )
        timeout: int = Field(
            default=FlextConstants.Network.DEFAULT_TIMEOUT,
            description="Connection timeout in seconds",
            gt=0,
            le=3600,
        )
        max_retries: int = Field(
            default=FlextConstants.Reliability.MAX_RETRY_ATTEMPTS,
            description="Maximum retry attempts",
            ge=0,
            le=10,
        )
        verify_ssl: bool = Field(
            default=True,
            description="Verify SSL certificates",
        )
        connection_pool_size: int = Field(
            default=FlextConstants.Performance.DEFAULT_DB_POOL_SIZE,
            description="Connection pool size",
            ge=1,
            le=100,
        )

        @field_validator("base_url")
        @classmethod
        def validate_base_url(cls, v: str) -> str:
            """Validate base URL format."""
            result = FlextModels.create_validated_http_url(v)
            if result.is_failure:
                raise ValueError(result.error)
            return result.unwrap()

        @computed_field
        def api_base_url(self) -> str:
            """Get API base URL."""
            return f"{self.base_url.rstrip('/')}/ic/api/{self.api_version}"

        def validate_business_rules(self) -> FlextResult[None]:
            """Validate connection business rules."""
            try:
                if not self.base_url.strip():
                    return FlextResult[None].fail("Base URL cannot be empty")
                return FlextResult[None].ok(None)
            except Exception as e:
                return FlextResult[None].fail(f"Connection validation failed: {e}")

    # Oracle OIC Deployment Models
    class OICDeploymentConfig(_BaseOICModel):
        """Enhanced Oracle OIC deployment configuration model."""

        import_mode: Literal["create", "update", "create_or_update", "replace"] = Field(
            default="create_or_update",
            description="Import mode for deployments",
        )
        activate_integrations: bool = Field(
            default=False,
            description="Activate integrations after deployment",
        )
        validate_connections: bool = Field(
            default=True,
            description="Validate connections during deployment",
        )
        archive_directory: str | None = Field(
            default=None,
            description="Archive directory for deployments",
            max_length=500,
        )
        rollback_on_failure: bool = Field(
            default=True,
            description="Rollback on deployment failure",
        )
        enable_versioning: bool = Field(
            default=True,
            description="Enable versioning for deployments",
        )
        audit_trail: bool = Field(
            default=True,
            description="Enable audit trail",
        )
        deployment_timeout: int = Field(
            default=1800,  # 30 minutes
            description="Deployment timeout in seconds",
            ge=60,
            le=7200,
        )

        @field_validator("archive_directory")
        @classmethod
        def validate_archive_directory(cls, v: str | None) -> str | None:
            """Validate archive directory."""
            if v is None:
                return None
            result = FlextModels.create_validated_directory_path(v)
            if result.is_failure:
                raise ValueError(result.error)
            return result.unwrap()

        @computed_field
        def is_create_mode(self) -> bool:
            """Check if using create mode."""
            return self.import_mode == "create"

        @computed_field
        def is_update_mode(self) -> bool:
            """Check if using update mode."""
            return self.import_mode == "update"

        @computed_field
        def is_create_or_update_mode(self) -> bool:
            """Check if using create or update mode."""
            return self.import_mode == "create_or_update"

        def validate_business_rules(self) -> FlextResult[None]:
            """Validate deployment business rules."""
            try:
                if self.archive_directory:
                    # Directory validation is handled by field validator
                    pass
                return FlextResult[None].ok(None)
            except Exception as e:
                return FlextResult[None].fail(f"Deployment validation failed: {e}")

    # Oracle OIC Processing Models
    class OICProcessingConfig(_BaseOICModel):
        """Enhanced Oracle OIC processing configuration model."""

        batch_size: int = Field(
            default=FlextConstants.Performance.DEFAULT_BATCH_SIZE,
            description="Batch size for processing",
            gt=0,
            le=100000,
        )
        enable_validation: bool = Field(
            default=True,
            description="Enable validation during processing",
        )
        validation_strict_mode: bool = Field(
            default=False,
            description="Enable strict validation mode",
        )
        skip_missing_connections: bool = Field(
            default=False,
            description="Skip missing connections",
        )
        max_errors: int = Field(
            default=10,
            description="Maximum errors before stopping",
            ge=0,
            le=1000,
        )
        ignore_transformation_errors: bool = Field(
            default=True,
            description="Ignore transformation errors",
        )
        dry_run_mode: bool = Field(
            default=False,
            description="Enable dry run mode",
        )
        parallel_processing: bool = Field(
            default=False,
            description="Enable parallel processing",
        )
        max_workers: int = Field(
            default=FlextConstants.Container.MAX_WORKERS,
            description="Maximum worker threads",
            ge=1,
            le=32,
        )

        @computed_field
        def effective_batch_size(self) -> int:
            """Get effective batch size considering parallel processing."""
            if self.parallel_processing:
                return self.batch_size // self.max_workers
            return self.batch_size

        def validate_business_rules(self) -> FlextResult[None]:
            """Validate processing business rules."""
            try:
                if self.batch_size <= 0:
                    return FlextResult[None].fail("Batch size must be positive")
                if self.max_workers <= 0:
                    return FlextResult[None].fail("Max workers must be positive")
                return FlextResult[None].ok(None)
            except Exception as e:
                return FlextResult[None].fail(f"Processing validation failed: {e}")

    # Oracle OIC Entity Models
    class OICEntityConfig(_BaseOICModel):
        """Enhanced Oracle OIC entity configuration model."""

        integration_identifier_field: str = Field(
            default="code",
            description="Integration identifier field",
            min_length=1,
            max_length=100,
        )
        connection_identifier_field: str = Field(
            default="code",
            description="Connection identifier field",
            min_length=1,
            max_length=100,
        )
        lookup_identifier_field: str = Field(
            default="name",
            description="Lookup identifier field",
            min_length=1,
            max_length=100,
        )
        identifier_fields: dict[str, str] = Field(
            default_factory=dict,
            description="Entity-specific identifier fields",
        )
        custom_fields: dict[str, Any] = Field(
            default_factory=dict,
            description="Custom entity fields",
        )
        field_mappings: dict[str, str] = Field(
            default_factory=dict,
            description="Field mappings for transformations",
        )

        @field_validator("identifier_fields")
        @classmethod
        def validate_identifier_fields(cls, v: dict[str, str]) -> dict[str, str]:
            """Validate identifier fields."""
            for key, value in v.items():
                if not key.strip() or not value.strip():
                    msg = f"Invalid identifier field mapping: {key} -> {value}"
                    raise ValueError(msg)
            return v

        def get_identifier_field(self, entity_type: str) -> str:
            """Get identifier field for entity type."""
            return self.identifier_fields.get(entity_type, "id")

        def validate_business_rules(self) -> FlextResult[None]:
            """Validate entity business rules."""
            try:
                if not self.integration_identifier_field.strip():
                    return FlextResult[None].fail(
                        "Integration identifier field cannot be empty"
                    )
                if not self.connection_identifier_field.strip():
                    return FlextResult[None].fail(
                        "Connection identifier field cannot be empty"
                    )
                if not self.lookup_identifier_field.strip():
                    return FlextResult[None].fail(
                        "Lookup identifier field cannot be empty"
                    )
                return FlextResult[None].ok(None)
            except Exception as e:
                return FlextResult[None].fail(f"Entity validation failed: {e}")

    # Oracle OIC Target Record Models
    class OICTargetRecord(_BaseOICModel):
        """Enhanced Oracle OIC target record model."""

        record_id: str = Field(
            default_factory=lambda: str(uuid.uuid4()),
            description="Unique record identifier",
            min_length=1,
            max_length=255,
        )
        entity_type: str = Field(
            description="OIC entity type",
            min_length=1,
            max_length=100,
        )
        entity_id: str = Field(
            description="OIC entity identifier",
            min_length=1,
            max_length=255,
        )
        data: dict[str, Any] = Field(
            description="Record data",
            min_length=1,
        )
        operation: Literal["CREATE", "UPDATE", "DELETE", "UPSERT"] = Field(
            default="CREATE",
            description="Database operation type",
        )
        timestamp: datetime = Field(
            default_factory=lambda: datetime.now(UTC),
            description="Record timestamp",
        )
        batch_id: str | None = Field(
            default=None,
            description="Batch identifier",
        )
        sequence_number: int = Field(
            default=0,
            description="Sequence number within batch",
            ge=0,
        )
        metadata: dict[str, Any] = Field(
            default_factory=dict,
            description="Record metadata",
        )

        @field_validator("entity_type")
        @classmethod
        def validate_entity_type(cls, v: str) -> str:
            """Validate entity type."""
            valid_types = {"integration", "connection", "lookup", "package", "flow"}
            if v.lower() not in valid_types:
                msg = f"Invalid entity type: {v}. Valid types: {valid_types}"
                raise ValueError(msg)
            return v.lower()

        @computed_field
        def data_size_bytes(self) -> int:
            """Calculate data size in bytes."""
            try:
                serialized = json.dumps(self.data, default=str)
                return len(serialized.encode("utf-8"))
            except Exception:
                return 0

        @computed_field
        def is_create_operation(self) -> bool:
            """Check if this is a create operation."""
            return self.operation == "CREATE"

        @computed_field
        def is_update_operation(self) -> bool:
            """Check if this is an update operation."""
            return self.operation == "UPDATE"

        @computed_field
        def is_delete_operation(self) -> bool:
            """Check if this is a delete operation."""
            return self.operation == "DELETE"

        @computed_field
        def is_upsert_operation(self) -> bool:
            """Check if this is an upsert operation."""
            return self.operation == "UPSERT"

    # Oracle OIC Target Batch Models
    class OICTargetBatch(_BaseOICModel):
        """Enhanced Oracle OIC target batch model."""

        batch_id: str = Field(
            default_factory=lambda: str(uuid.uuid4()),
            description="Unique batch identifier",
            min_length=1,
            max_length=255,
        )
        records: list[FlextTargetOracleOICModels.OICTargetRecord] = Field(
            description="Batch records",
            min_length=1,
        )
        batch_size: int = Field(
            description="Number of records in batch",
            ge=1,
        )
        entity_type: str = Field(
            description="OIC entity type",
            min_length=1,
            max_length=100,
        )
        created_at: datetime = Field(
            default_factory=lambda: datetime.now(UTC),
            description="Batch creation timestamp",
        )
        status: Literal["PENDING", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED"] = (
            Field(
                default="PENDING",
                description="Batch processing status",
            )
        )
        error_message: str | None = Field(
            default=None,
            description="Error message if batch failed",
        )
        processing_started_at: datetime | None = None
        processing_completed_at: datetime | None = None
        records_processed: int = Field(default=0, ge=0)
        records_failed: int = Field(default=0, ge=0)

        @field_validator("batch_size")
        @classmethod
        def validate_batch_size(cls, v: int, info: ValidationInfo) -> int:
            """Validate batch size matches actual records count."""
            if "records" in info.data and v != len(info.data["records"]):
                msg = "Batch size must match actual records count"
                raise ValueError(msg)
            return v

        @computed_field
        def total_data_size_bytes(self) -> int:
            """Calculate total data size in bytes."""
            return sum(record.data_size_bytes for record in self.records)

        @computed_field
        def success_rate(self) -> float:
            """Calculate success rate percentage."""
            total = self.records_processed + self.records_failed
            if total == 0:
                return 0.0
            return (self.records_processed / total) * 100.0

        @computed_field
        def is_completed(self) -> bool:
            """Check if batch is completed."""
            return self.status == "COMPLETED"

        @computed_field
        def is_failed(self) -> bool:
            """Check if batch failed."""
            return self.status == "FAILED"

        def start_processing(self) -> None:
            """Start batch processing."""
            self.status = "PROCESSING"
            self.processing_started_at = datetime.now(UTC)

        def complete_processing(
            self, records_processed: int = 0, records_failed: int = 0
        ) -> None:
            """Complete batch processing."""
            self.status = "COMPLETED"
            self.processing_completed_at = datetime.now(UTC)
            self.records_processed = records_processed
            self.records_failed = records_failed

        def fail_processing(self, error_message: str) -> None:
            """Fail batch processing."""
            self.status = "FAILED"
            self.processing_completed_at = datetime.now(UTC)
            self.error_message = error_message

    # Oracle OIC Target Operation Models
    class OICTargetOperation(_BaseOICModel):
        """Enhanced Oracle OIC target operation model."""

        operation_id: str = Field(
            default_factory=lambda: str(uuid.uuid4()),
            description="Operation identifier",
        )
        operation_type: Literal["DEPLOY", "SYNC", "VALIDATE", "CLEANUP"] = Field(
            description="Operation type",
        )
        entity_type: str = Field(
            description="OIC entity type",
            min_length=1,
            max_length=100,
        )
        status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"] = (
            Field(
                default="PENDING",
                description="Operation status",
            )
        )
        started_at: datetime | None = None
        completed_at: datetime | None = None
        records_processed: int = Field(default=0, ge=0)
        records_failed: int = Field(default=0, ge=0)
        error_message: str | None = None
        metadata: dict[str, Any] = Field(
            default_factory=dict,
            description="Operation metadata",
        )

        @computed_field
        def duration_seconds(self) -> float | None:
            """Calculate operation duration in seconds."""
            if self.started_at and self.completed_at:
                return (self.completed_at - self.started_at).total_seconds()
            return None

        @computed_field
        def success_rate(self) -> float:
            """Calculate success rate percentage."""
            total = self.records_processed + self.records_failed
            if total == 0:
                return 0.0
            return (self.records_processed / total) * 100.0

        def start_operation(self) -> None:
            """Start operation."""
            self.status = "RUNNING"
            self.started_at = datetime.now(UTC)

        def complete_operation(
            self, records_processed: int = 0, records_failed: int = 0
        ) -> None:
            """Complete operation."""
            self.status = "COMPLETED"
            self.completed_at = datetime.now(UTC)
            self.records_processed = records_processed
            self.records_failed = records_failed

        def fail_operation(self, error_message: str) -> None:
            """Fail operation."""
            self.status = "FAILED"
            self.completed_at = datetime.now(UTC)
            self.error_message = error_message

    # Factory methods for creating model instances
    @classmethod
    def create_oic_target_record(
        cls,
        entity_type: str,
        entity_id: str,
        data: dict[str, object],
        operation: str = "CREATE",
        **kwargs: object,
    ) -> FlextResult[FlextTargetOracleOICModels.OICTargetRecord]:
        """Create OIC target record with validation."""
        try:
            record = cls.OICTargetRecord(
                entity_type=entity_type,
                entity_id=entity_id,
                data=data,
                operation=operation,
                **kwargs,
            )
            return FlextResult[cls.OICTargetRecord].ok(record)
        except Exception as e:
            return FlextResult[cls.OICTargetRecord].fail(f"Record creation failed: {e}")

    @classmethod
    def create_oic_target_batch(
        cls,
        entity_type: str,
        records: list[FlextTargetOracleOICModels.OICTargetRecord],
        **kwargs: object,
    ) -> FlextResult[FlextTargetOracleOICModels.OICTargetBatch]:
        """Create OIC target batch with validation."""
        try:
            batch = cls.OICTargetBatch(
                entity_type=entity_type,
                records=records,
                batch_size=len(records),
                **kwargs,
            )
            return FlextResult[cls.OICTargetBatch].ok(batch)
        except Exception as e:
            return FlextResult[cls.OICTargetBatch].fail(f"Batch creation failed: {e}")

    @classmethod
    def create_oic_target_operation(
        cls,
        operation_type: str,
        entity_type: str,
        **kwargs: object,
    ) -> FlextResult[FlextTargetOracleOICModels.OICTargetOperation]:
        """Create OIC target operation with validation."""
        try:
            operation = cls.OICTargetOperation(
                operation_type=operation_type,
                entity_type=entity_type,
                **kwargs,
            )
            return FlextResult[cls.OICTargetOperation].ok(operation)
        except Exception as e:
            return FlextResult[cls.OICTargetOperation].fail(
                f"Operation creation failed: {e}"
            )
