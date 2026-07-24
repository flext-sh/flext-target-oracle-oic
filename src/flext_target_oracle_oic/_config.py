"""FlextTargetOracleOicConfig — frozen config singleton for flext-target-oracle-oic (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``TargetOracleOic:`` key and
are exposed through the open ``config.TargetOracleOic`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.TargetOracleOic.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from flext_meltano import FlextMeltanoConfig


class _TargetOracleOicNamespace(BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = ConfigDict(extra="allow", frozen=True)


class FlextTargetOracleOicConfig(FlextMeltanoConfig):
    """TargetOracleOic config auto-loaded model-less from ``config/*.yaml``."""

    TargetOracleOic: _TargetOracleOicNamespace = _TargetOracleOicNamespace()


config: FlextTargetOracleOicConfig = FlextTargetOracleOicConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_target_oracle_oic import config``."""

__all__: list[str] = ["FlextTargetOracleOicConfig", "config"]
