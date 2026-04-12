"""Pattern helpers for schema mapping and data transformation."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_core import r
from flext_target_oracle_oic import t


class FlextTargetOracleOicTypeConverter:
    """Converts incoming values for OIC payloads."""

    def convert(self, value: t.Scalar) -> t.Scalar:
        """Return value unchanged for baseline conversion behavior."""
        return value


class FlextTargetOracleOicSchemaMapper:
    """Maps stream schemas to OIC-compatible schema payloads."""

    def map_schema(
        self,
        stream_name: str,
        schema: t.FlatContainerMapping,
    ) -> r[Mapping[str, str | t.FlatContainerMapping]]:
        """Build schema metadata payload for the given stream."""
        return r[Mapping[str, str | t.FlatContainerMapping]].ok({
            "stream": stream_name,
            "schema": schema,
        })


class FlextTargetOracleOicDataTransformer:
    """Transforms record payloads before sink submission."""

    def transform(self, record: t.ConfigurationMapping) -> r[t.ConfigurationMapping]:
        """Return transformed record payload."""
        return r[t.ScalarMapping].ok(record)


class FlextTargetOracleOicEntryManager:
    """Builds entry collections from transformed records."""

    def build_entries(
        self,
        records: Sequence[t.ConfigurationMapping],
    ) -> r[Sequence[t.ConfigurationMapping]]:
        """Return entry list unchanged for baseline behavior."""
        return r[Sequence[t.ScalarMapping]].ok(records)


__all__: list[str] = [
    "FlextTargetOracleOicDataTransformer",
    "FlextTargetOracleOicEntryManager",
    "FlextTargetOracleOicSchemaMapper",
    "FlextTargetOracleOicTypeConverter",
]
