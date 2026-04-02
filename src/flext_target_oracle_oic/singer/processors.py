"""Singer record processor primitives for Oracle OIC streams."""

from __future__ import annotations

from flext_core import r
from flext_target_oracle_oic import m, t


class FlextTargetOracleOicProcessedRecord(m.ArbitraryTypesModel):
    """Normalized record payload produced by OIC processor."""

    stream_name: str
    record: t.ConfigurationMapping


class FlextTargetOracleOicRecordProcessor:
    """Transforms Singer records into OIC processing payloads."""

    def process(
        self,
        stream_name: str,
        record: t.ConfigurationMapping,
    ) -> r[FlextTargetOracleOicProcessedRecord]:
        """Return typed stream payload for downstream handling."""
        return r[FlextTargetOracleOicProcessedRecord].ok(
            FlextTargetOracleOicProcessedRecord.model_validate({
                "stream_name": stream_name,
                "record": record,
            }),
        )


__all__ = ["FlextTargetOracleOicProcessedRecord", "FlextTargetOracleOicRecordProcessor"]
