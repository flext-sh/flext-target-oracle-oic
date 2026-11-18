"""FLEXT service orchestrator for target-oracle-oic.

Thin facade over ``meltano.Target`` — all infrastructure from the base via MRO.
The sink factory is declared, never overridden.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_meltano import FlextMeltanoTargetServiceBase

from flext_target_oracle_oic import c, m, p, t, u


class FlextTargetOracleOicService(FlextMeltanoTargetServiceBase):
    """Orchestrator for target-oracle-oic. All behavior from base via MRO."""

    target_name: Annotated[t.NonEmptyStr, m.Field(description="Singer target name")] = (
        c.TargetOracleOic.TARGET_NAME
    )

    sink_factory: ClassVar[p.Meltano.SinkFactory] = u.create_sink


_service: FlextTargetOracleOicService = FlextTargetOracleOicService.fetch_global()

target_oracle_oic: FlextTargetOracleOicService = _service
"""Shared FlextTargetOracleOicService facade instance."""

__all__: list[str] = ["FlextTargetOracleOicService", "target_oracle_oic"]
