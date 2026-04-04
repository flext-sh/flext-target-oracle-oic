"""Domain models for target Oracle OIC."""

from __future__ import annotations

from pydantic import Field

from flext_core import r
from flext_meltano import FlextMeltanoModels
from flext_oracle_oic import FlextOracleOicModels
from flext_target_oracle_oic import c, t


class FlextTargetOracleOicModels(FlextMeltanoModels, FlextOracleOicModels):
    """Namespace class for OIC target models."""

    class TargetOracleOic:
        """TargetOracleOic domain namespace."""

        OICConnectionAction = c.TargetOracleOic.OICConnectionAction
        OICIntegrationAction = c.TargetOracleOic.OICIntegrationAction

        class OICConnection(FlextMeltanoModels.ArbitraryTypesModel):
            """Connection payload model."""

            id: t.NonEmptyStr
            name: t.NonEmptyStr
            adapter_type: t.NonEmptyStr
            properties: t.FlatContainerMapping = Field(default_factory=dict)

        class OICIntegration(FlextMeltanoModels.ArbitraryTypesModel):
            """Integration payload model."""

            id: t.NonEmptyStr
            name: t.NonEmptyStr
            version: str = c.TargetOracleOic.DEFAULT_VERSION
            pattern: str = c.TargetOracleOic.DEFAULT_PATTERN

        class OICPackage(FlextMeltanoModels.ArbitraryTypesModel):
            """Package payload model."""

            id: t.NonEmptyStr
            name: t.NonEmptyStr
            version: str = c.TargetOracleOic.DEFAULT_VERSION

        class OICLookup(FlextMeltanoModels.ArbitraryTypesModel):
            """Lookup payload model."""

            name: t.NonEmptyStr
            columns: tuple[t.ConfigurationMapping, ...] = ()
            rows: tuple[t.ConfigurationMapping, ...] = ()

        class OICProject(FlextMeltanoModels.ArbitraryTypesModel):
            """Project payload model."""

            id: t.NonEmptyStr
            name: t.NonEmptyStr

        class OICSchedule(FlextMeltanoModels.ArbitraryTypesModel):
            """Schedule payload model."""

            name: t.NonEmptyStr
            schedule_type: str = c.TargetOracleOic.DEFAULT_SCHEDULE_TYPE

        class OICDataTransformation(FlextMeltanoModels.ArbitraryTypesModel):
            """Transformation payload model."""

            source_stream: t.NonEmptyStr
            target_entity: t.NonEmptyStr
            mapping: t.StrMapping = Field(default_factory=dict)

        class OICSchemaMapping(FlextMeltanoModels.ArbitraryTypesModel):
            """Schema mapping payload model."""

            stream_name: t.NonEmptyStr
            schema_mapping: t.FlatContainerMapping = Field(default_factory=dict)

    @staticmethod
    def validate_connection(
        connection: TargetOracleOic.OICConnection,
    ) -> r[bool]:
        """Validate minimal connection invariants."""
        if not connection.id.strip() or not connection.name.strip():
            return r[bool].fail("Connection id/name cannot be empty")
        return r[bool].ok(value=True)


m = FlextTargetOracleOicModels

__all__ = ["FlextTargetOracleOicModels", "m"]
