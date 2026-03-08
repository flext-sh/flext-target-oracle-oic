"""Singer record processor primitives for Oracle OIC streams."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextResult, t


class OICRecordProcessor:
    """Transforms Singer records into OIC processing payloads."""

    def process(
        self, stream_name: str, record: Mapping[str, t.JsonValue]
    ) -> FlextResult[OICProcessedRecord]:
        """Return typed stream payload for downstream handling."""
        return FlextResult[OICProcessedRecord].ok(
            OICProcessedRecord(stream_name=stream_name, record=record)
        )


__all__ = ["OICProcessedRecord", "OICRecordProcessor"]
