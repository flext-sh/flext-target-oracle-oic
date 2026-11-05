"""Singer sink used by every Oracle OIC target stream.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_target_oracle_oic import m, t


class FlextTargetOracleOicSink(m.Meltano.SingerSinkBase):
    """Sink for Oracle OIC streams; the stream identity is ``stream_name``."""

    @override
    def process_batch(self, context: t.MutableJsonMapping) -> None:
        """Accept a Singer batch without additional processing.

        Args:
            context: Singer batch context supplied by the target pipeline.

        """
        _ = context

    @override
    def process_record(
        self,
        record: t.MutableJsonMapping,
        context: t.MutableJsonMapping,
    ) -> None:
        """Log incoming record metadata for the sink's stream.

        Args:
            record: Raw record mapping received for the stream.
            context: Singer record context supplied by the target pipeline.

        """
        _ = context
        self.logger.debug("Processing OIC record: %s", record.keys())


__all__: list[str] = ["FlextTargetOracleOicSink"]
