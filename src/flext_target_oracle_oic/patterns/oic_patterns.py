"""Pattern helpers for schema mapping and data transformation."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_core import r

from flext_target_oracle_oic.typings import t


class OICTypeConverter:
    """Converts incoming values for OIC payloads."""

    def convert(self, value: t.Scalar) -> t.Scalar:
        """Return value unchanged for baseline conversion behavior."""
        return value


class OICSchemaMapper:
    """Maps stream schemas to OIC-compatible schema payloads."""

    def map_schema(
        self, stream_name: str, schema: Mapping[str, t.Container]
    ) -> r[Mapping[str, str | Mapping[str, t.Container]]]:
        """Build schema metadata payload for the given stream."""
        return r[Mapping[str, str | Mapping[str, t.Container]]].ok({
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
        self, records: Sequence[Mapping[str, t.Scalar]]
    ) -> r[Sequence[Mapping[str, t.Scalar]]]:
        """Return entry list unchanged for baseline behavior."""
        return r[Sequence[Mapping[str, t.Scalar]]].ok(records)


__all__ = [
    "OICDataTransformer",
    "OICEntryManager",
    "OICSchemaMapper",
    "OICTypeConverter",
]
