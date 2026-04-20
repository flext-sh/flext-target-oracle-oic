"""Domain models for target Oracle OIC."""

from __future__ import annotations

from typing import ClassVar

from flext_meltano import m
from flext_oracle_oic import FlextOracleOicModels, u

from flext_target_oracle_oic import c, p, r, t


class FlextTargetOracleOicModels(m, FlextOracleOicModels):
    """Namespace class for OIC target models."""

    class TargetOracleOic:
        """TargetOracleOic domain namespace."""

        OICConnectionAction = c.TargetOracleOic.OICConnectionAction
        OICIntegrationAction = c.TargetOracleOic.OICIntegrationAction

        class OICConnection(m.ArbitraryTypesModel):
            """Connection payload model."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            id: t.NonEmptyStr
            name: t.NonEmptyStr
            adapter_type: t.NonEmptyStr
            properties: t.FlatContainerMapping = u.Field(default_factory=dict)

        class OICIntegration(m.ArbitraryTypesModel):
            """Integration payload model."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            id: t.NonEmptyStr
            name: t.NonEmptyStr
            version: str = c.TargetOracleOic.DEFAULT_VERSION
            pattern: str = c.TargetOracleOic.DEFAULT_PATTERN

        class OICPackage(m.ArbitraryTypesModel):
            """Package payload model."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            id: t.NonEmptyStr
            name: t.NonEmptyStr
            version: str = c.TargetOracleOic.DEFAULT_VERSION

        class OICLookup(m.ArbitraryTypesModel):
            """Lookup payload model."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            name: t.NonEmptyStr
            columns: tuple[t.ConfigurationMapping, ...] = ()
            rows: tuple[t.ConfigurationMapping, ...] = ()

        class OICProject(m.ArbitraryTypesModel):
            """Project payload model."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            id: t.NonEmptyStr
            name: t.NonEmptyStr

        class OICSchedule(m.ArbitraryTypesModel):
            """Schedule payload model."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            name: t.NonEmptyStr
            schedule_type: str = c.TargetOracleOic.DEFAULT_SCHEDULE_TYPE

        class OICDataTransformation(m.ArbitraryTypesModel):
            """Transformation payload model."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            source_stream: t.NonEmptyStr
            target_entity: t.NonEmptyStr
            mapping: t.StrMapping = u.Field(default_factory=dict)

        class OICSchemaMapping(m.ArbitraryTypesModel):
            """Schema mapping payload model."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            stream_name: t.NonEmptyStr
            schema_mapping: t.FlatContainerMapping = u.Field(default_factory=dict)

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
