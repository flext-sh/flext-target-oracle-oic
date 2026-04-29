"""Domain models for target Oracle OIC."""

from __future__ import annotations

from types import MappingProxyType
from typing import Annotated

from flext_meltano import m
from flext_oracle_oic import FlextOracleOicModels, u
from flext_target_oracle_oic import c, p, r, t


class FlextTargetOracleOicModels(m, FlextOracleOicModels):
    """Namespace class for OIC target models."""

    class TargetOracleOic:
        """TargetOracleOic domain namespace."""

        class OICConnection(m.ArbitraryTypesModel):
            """Connection payload model."""

            id: Annotated[
                t.NonEmptyStr, u.Field(description="Unique connection identifier")
            ]
            name: Annotated[t.NonEmptyStr, u.Field(description="Connection name")]
            adapter_type: Annotated[
                t.NonEmptyStr, u.Field(description="Type of adapter used")
            ]
            properties: Annotated[
                t.JsonMapping,
                u.Field(description="Connection properties and configuration"),
            ] = u.Field(default_factory=MappingProxyType)

        class OICIntegration(m.ArbitraryTypesModel):
            """Integration payload model."""

            id: Annotated[
                t.NonEmptyStr, u.Field(description="Unique integration identifier")
            ]
            name: Annotated[t.NonEmptyStr, u.Field(description="Integration name")]
            version: Annotated[str, u.Field(description="Integration version")] = (
                c.TargetOracleOic.DEFAULT_VERSION
            )
            pattern: Annotated[str, u.Field(description="Integration pattern type")] = (
                c.TargetOracleOic.DEFAULT_PATTERN
            )

        class OICPackage(m.ArbitraryTypesModel):
            """Package payload model."""

            id: Annotated[
                t.NonEmptyStr, u.Field(description="Unique package identifier")
            ]
            name: Annotated[t.NonEmptyStr, u.Field(description="Package name")]
            version: Annotated[str, u.Field(description="Package version")] = (
                c.TargetOracleOic.DEFAULT_VERSION
            )

        class OICLookup(m.ArbitraryTypesModel):
            """Lookup payload model."""

            name: Annotated[t.NonEmptyStr, u.Field(description="Lookup name")]
            columns: Annotated[
                tuple[t.ConfigurationMapping, ...],
                u.Field(description="Column definitions for the lookup"),
            ] = ()
            rows: Annotated[
                tuple[t.ConfigurationMapping, ...],
                u.Field(description="Row data for the lookup"),
            ] = ()

        class OICProject(m.ArbitraryTypesModel):
            """Project payload model."""

            id: Annotated[
                t.NonEmptyStr, u.Field(description="Unique project identifier")
            ]
            name: Annotated[t.NonEmptyStr, u.Field(description="Project name")]

        class OICSchedule(m.ArbitraryTypesModel):
            """Schedule payload model."""

            name: Annotated[t.NonEmptyStr, u.Field(description="Schedule name")]
            schedule_type: Annotated[
                str,
                u.Field(description="Type of schedule (e.g., cron, interval)"),
            ] = c.TargetOracleOic.DEFAULT_SCHEDULE_TYPE

        class OICDataTransformation(m.ArbitraryTypesModel):
            """Transformation payload model."""

            source_stream: Annotated[
                t.NonEmptyStr,
                u.Field(description="Name of the source stream"),
            ]
            target_entity: Annotated[
                t.NonEmptyStr,
                u.Field(description="Name of the target entity"),
            ]
            mapping: Annotated[
                t.StrMapping,
                u.Field(description="Field mapping from source to target"),
            ] = u.Field(default_factory=MappingProxyType)

        class OICSchemaMapping(m.ArbitraryTypesModel):
            """Schema mapping payload model."""

            stream_name: Annotated[
                t.NonEmptyStr,
                u.Field(description="Name of the stream being mapped"),
            ]
            schema_mapping: Annotated[
                t.JsonMapping,
                u.Field(description="Schema field mapping configuration"),
            ] = u.Field(default_factory=MappingProxyType)

    @staticmethod
    def validate_connection(
        connection: TargetOracleOic.OICConnection,
    ) -> p.Result[bool]:
        """Validate minimal connection invariants."""
        if not connection.id.strip() or not connection.name.strip():
            return r[bool].fail("Connection id/name cannot be empty")
        return r[bool].ok(value=True)


m = FlextTargetOracleOicModels

__all__: list[str] = ["FlextTargetOracleOicModels", "m"]
