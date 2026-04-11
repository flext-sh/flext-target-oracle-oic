"""FLEXT service orchestrator for target-oracle-oic.

Thin facade — all infrastructure from ``FlextMeltanoTargetServiceBase`` via MRO.
Only domain-specific sink creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_meltano import FlextMeltanoTargetServiceBase
from flext_target_oracle_oic import (
    FlextTargetOracleOicServiceRuntime,
    p,
    t,
)


class FlextTargetOracleOicService(FlextMeltanoTargetServiceBase):
    """Orchestrator for target-oracle-oic. All behavior from base via MRO."""

    target_name: t.NonEmptyStr = "target-oracle-oic"

    @override
    def create_sink(
        self,
        stream_name: str,
        schema: t.FlatContainerMapping,
    ) -> p.Meltano.SingerDrainSink:
        """Create an Oracle OIC sink for a stream."""
        target_config: t.ContainerMapping = (
            self.config_overrides if self.config_overrides is not None else {}
        )
        return FlextTargetOracleOicServiceRuntime.create_sink(
            stream_name=stream_name,
            schema=schema,
            target_config=target_config,
        )


target_oracle_oic = FlextTargetOracleOicService

__all__ = ["FlextTargetOracleOicService", "target_oracle_oic"]
