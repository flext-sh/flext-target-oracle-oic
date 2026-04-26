"""Singer record processor primitives for Oracle OIC streams."""

from __future__ import annotations

from typing import Annotated

from flext_core import u
from flext_target_oracle_oic import m, p, r, t


class FlextTargetOracleOicProcessedRecord(m.ArbitraryTypesModel):
    """Normalized record payload produced by OIC processor."""

    stream_name: Annotated[str, u.Field(description="Singer stream name.")]
    record: Annotated[
        t.ConfigurationMapping,
        u.Field(description="Normalized record payload."),
    ]


class FlextTargetOracleOicRecordProcessor:
    """Transforms Singer records into OIC processing payloads."""

    def process(
        self,
        stream_name: str,
        record: t.ConfigurationMapping,
    ) -> p.Result[FlextTargetOracleOicProcessedRecord]:
        """Return typed stream payload for downstream handling."""
        return r[FlextTargetOracleOicProcessedRecord].ok(
            FlextTargetOracleOicProcessedRecord.model_validate({
                "stream_name": stream_name,
                "record": record,
            }),
        )


__all__: list[str] = [
    "FlextTargetOracleOicProcessedRecord",
    "FlextTargetOracleOicRecordProcessor",
]
