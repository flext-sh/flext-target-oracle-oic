"""Pattern helpers for schema mapping and data transformation."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import r, t


class OICTypeConverter:
    """Converts incoming values for OIC payloads."""

    def convert(self, value: t.Scalar) -> t.Scalar:
        """Return value unchanged for baseline conversion behavior."""
        return value


class OICSchemaMapper:
    """Maps stream schemas to OIC-compatible schema payloads."""

    def map_schema(
        self, stream_name: str, schema: Mapping[str, t.Container]
    ) -> r[t.Dict]:
        """Build schema metadata payload for the given stream."""
        return r[t.Dict].ok({
            "stream": stream_name,
            "schema": schema,
        })


class OICDataTransformer:
    """Transforms record payloads before sink submission."""

    def transform(self, record: Mapping[str, t.Scalar]) -> r[Mapping[str, t.Scalar]]:
        """Return transformed record payload."""
        return r[Mapping[str, t.Scalar]].ok(record)


class OICEntryManager:
    """Builds entry collections from transformed records."""

    def build_entries(
        self, records: list[Mapping[str, t.Scalar]]
    ) -> r[list[Mapping[str, t.Scalar]]]:
        """Return entry list unchanged for baseline behavior."""
        return r[list[Mapping[str, t.Scalar]]].ok(records)


__all__ = [
    "OICDataTransformer",
    "OICEntryManager",
    "OICSchemaMapper",
    "OICTypeConverter",
]
