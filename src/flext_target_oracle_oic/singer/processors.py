"""Singer record processor primitives for Oracle OIC streams."""

from __future__ import annotations

from typing import Annotated

from flext_core import u
from flext_target_oracle_oic import m, t


class FlextTargetOracleOicProcessedRecord(m.ArbitraryTypesModel):
    """Normalized record payload produced by OIC processor."""

    stream_name: Annotated[str, u.Field(description="Singer stream name.")]
    record: Annotated[
        t.ConfigurationMapping,
        u.Field(description="Normalized record payload."),
    ]


__all__: list[str] = [
    "FlextTargetOracleOicProcessedRecord",
]
