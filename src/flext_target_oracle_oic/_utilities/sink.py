"""Singer sink used by every Oracle OIC target stream.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_oic/_utilities/sink
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_target_oracle_oic import m, t


class FlextTargetOracleOicSink(m.Meltano.SingerSinkBase):
    """Sink for Oracle OIC streams; the stream identity is ``stream_name``."""

    @override
    def process_batch(self, context: t.MutableJsonMapping) -> None:
        """Singer batch hook implementation."""
        _ = context

    @override
    def process_record(
        self,
        record: t.MutableJsonMapping,
        context: t.MutableJsonMapping,
    ) -> None:
        """Log incoming record metadata for the sink's stream."""
        _ = context
        self.logger.debug("Processing OIC record: %s", record.keys())


__all__: list[str] = ["FlextTargetOracleOicSink"]
