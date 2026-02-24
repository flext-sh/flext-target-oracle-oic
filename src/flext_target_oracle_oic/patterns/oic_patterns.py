"""Pattern helpers for schema mapping and data transformation."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextResult, t


class OICTypeConverter:
    """Converts incoming values for OIC payloads."""

    def convert(self, value: t.JsonValue) -> t.JsonValue:
        """Return value unchanged for baseline conversion behavior."""
        return value


class OICSchemaMapper:
    """Maps stream schemas to OIC-compatible schema payloads."""

    def map_schema(
        self,
        stream_name: str,
        schema: Mapping[str, t.JsonValue],
    ) -> FlextResult[Mapping[str, t.JsonValue]]:
        """Build schema metadata payload for the given stream."""
        return FlextResult[Mapping[str, t.JsonValue]].ok({
            "stream": stream_name,
            "schema": schema,
        })


class OICDataTransformer:
    """Transforms record payloads before sink submission."""

    def transform(
        self,
        record: Mapping[str, t.JsonValue],
    ) -> FlextResult[Mapping[str, t.JsonValue]]:
        """Return transformed record payload."""
        return FlextResult[Mapping[str, t.JsonValue]].ok(record)


class OICEntryManager:
    """Builds entry collections from transformed records."""

    def build_entries(
        self,
        records: list[Mapping[str, t.JsonValue]],
    ) -> FlextResult[list[Mapping[str, t.JsonValue]]]:
        """Return entry list unchanged for baseline behavior."""
        return FlextResult[list[Mapping[str, t.JsonValue]]].ok(records)


__all__ = [
    "OICDataTransformer",
    "OICEntryManager",
    "OICSchemaMapper",
    "OICTypeConverter",
]
