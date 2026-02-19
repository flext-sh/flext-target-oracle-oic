"""Singer record processor primitives for Oracle OIC streams."""

from __future__ import annotations

from flext_core import FlextResult, FlextTypes as t


class OICRecordProcessor:
    """Transforms Singer records into OIC processing payloads."""

    def process(
        self,
        stream_name: str,
        record: dict[str, t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Return stream and record payload for downstream handling."""
        return FlextResult[dict[str, t.GeneralValueType]].ok({
            "stream_name": stream_name,
            "record": record,
        })


__all__ = ["OICRecordProcessor"]
