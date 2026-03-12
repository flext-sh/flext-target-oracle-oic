"""Singer record processor primitives for Oracle OIC streams."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import r, t
from flext_meltano import FlextMeltanoModels


class OICProcessedRecord(FlextMeltanoModels.ArbitraryTypesModel):
    """Normalized record payload produced by OIC processor."""

    stream_name: str
    record: Mapping[str, object


class OICRecordProcessor:
    """Transforms Singer records into OIC processing payloads."""

    def process(
        self, stream_name: str, record: Mapping[str, object
    ) -> r[OICProcessedRecord]:
        """Return typed stream payload for downstream handling."""
        payload: dict[str, object"stream_name": stream_name, "record": record}
        return r[OICProcessedRecord].ok(OICProcessedRecord.model_validate(payload))


__all__ = ["OICProcessedRecord", "OICRecordProcessor"]
