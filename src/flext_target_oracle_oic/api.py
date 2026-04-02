"""FLEXT service orchestrator for target-oracle-oic.

Thin facade — all infrastructure from ``FlextMeltanoTargetServiceBase`` via MRO.
Only domain-specific sink creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_meltano import FlextMeltanoSingerSinkBase, FlextMeltanoTargetServiceBase

from flext_target_oracle_oic import FlextTargetOracleOicBaseSink, t


class FlextTargetOracleOicService(FlextMeltanoTargetServiceBase):
    """Orchestrator for target-oracle-oic. All behavior from base via MRO."""

    target_name: t.NonEmptyStr = "target-oracle-oic"

    @override
    def create_sink(
        self,
        stream_name: str,
        schema: t.FlatContainerMapping,
    ) -> FlextMeltanoSingerSinkBase:
        """Create an Oracle OIC sink for a stream."""
        return FlextTargetOracleOicBaseSink(
            target=None,
            stream_name=stream_name,
            schema=dict(schema),
            key_properties=[],
        )


__all__ = ["FlextTargetOracleOicService"]
