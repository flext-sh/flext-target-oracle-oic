"""Domain models for target Oracle OIC."""

from __future__ import annotations

from enum import StrEnum

from flext_core import FlextResult, t
from flext_meltano import FlextMeltanoModels
from flext_oracle_oic import FlextOracleOicModels
from flext_target_oracle_oic.constants import c
from pydantic import Field


class FlextTargetOracleOicModels(FlextMeltanoModels, FlextOracleOicModels):
    """Namespace class for OIC target models."""

    class TargetOracleOic:
        """TargetOracleOic domain namespace."""

        class OICConnectionAction(StrEnum):
            """Supported connection actions."""

            CREATE = "create"
            UPDATE = "update"

        class OICIntegrationAction(StrEnum):
            """Supported integration actions."""

            IMPORT = "import"
            ACTIVATE = "activate"

        class OICConnection(FlextMeltanoModels.ArbitraryTypesModel):
            """Connection payload model."""

            id: str
            name: str
            adapter_type: str
            properties: dict[str, t.JsonValue] = Field(default_factory=dict)

        class OICIntegration(FlextMeltanoModels.ArbitraryTypesModel):
            """Integration payload model."""

            id: str
            name: str
            version: str = c.TargetOracleOic.DEFAULT_VERSION
            pattern: str = c.TargetOracleOic.DEFAULT_PATTERN

        class OICPackage(FlextMeltanoModels.ArbitraryTypesModel):
            """Package payload model."""

            id: str
            name: str
            version: str = c.TargetOracleOic.DEFAULT_VERSION

        class OICLookup(FlextMeltanoModels.ArbitraryTypesModel):
            """Lookup payload model."""

            name: str
            columns: list[dict[str, object]] = Field(default=[])
            rows: list[dict[str, object]] = Field(default=[])

        class OICProject(FlextMeltanoModels.ArbitraryTypesModel):
            """Project payload model."""

            id: str
            name: str

        class OICSchedule(FlextMeltanoModels.ArbitraryTypesModel):
            """Schedule payload model."""

            name: str
            schedule_type: str = c.TargetOracleOic.DEFAULT_SCHEDULE_TYPE

        class OICDataTransformation(FlextMeltanoModels.ArbitraryTypesModel):
            """Transformation payload model."""

            source_stream: str
            target_entity: str
            mapping: dict[str, str] = Field(default_factory=dict)

        class OICSchemaMapping(FlextMeltanoModels.ArbitraryTypesModel):
            """Schema mapping payload model."""

            stream_name: str
            schema_mapping: dict[str, t.JsonValue] = Field(default_factory=dict)

    @staticmethod
    def validate_connection(
        connection: TargetOracleOic.OICConnection,
    ) -> FlextResult[bool]:
        """Validate minimal connection invariants."""
        if not connection.id.strip() or not connection.name.strip():
            return FlextResult[bool].fail("Connection id/name cannot be empty")
        return FlextResult[bool].ok(value=True)


m = FlextTargetOracleOicModels

__all__ = ["FlextTargetOracleOicModels", "m"]
