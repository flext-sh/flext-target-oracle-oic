"""Pattern helpers for schema mapping and data transformation."""

from __future__ import annotations

from flext_core import FlextResult, FlextTypes as t


class OICTypeConverter:
    """Converts incoming values for OIC payloads."""

    def convert(self, value: t.GeneralValueType) -> t.GeneralValueType:
        """Return value unchanged for baseline conversion behavior."""
        return value


class OICSchemaMapper:
    """Maps stream schemas to OIC-compatible schema payloads."""

    def map_schema(
        self,
        stream_name: str,
        schema: dict[str, t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Build schema metadata payload for the given stream."""
        return FlextResult[dict[str, t.GeneralValueType]].ok({
            "stream": stream_name,
            "schema": schema,
        })


class OICDataTransformer:
    """Transforms record payloads before sink submission."""

    def transform(
        self,
        record: dict[str, t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Return transformed record payload."""
        return FlextResult[dict[str, t.GeneralValueType]].ok(record)


class OICEntryManager:
    """Builds entry collections from transformed records."""

    def build_entries(
        self,
        records: list[dict[str, t.GeneralValueType]],
    ) -> FlextResult[list[dict[str, t.GeneralValueType]]]:
        """Return entry list unchanged for baseline behavior."""
        return FlextResult[list[dict[str, t.GeneralValueType]]].ok(records)


__all__ = [
    "OICDataTransformer",
    "OICEntryManager",
    "OICSchemaMapper",
    "OICTypeConverter",
]
