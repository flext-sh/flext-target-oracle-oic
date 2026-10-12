"""FlextTargetOracleOicConfig — frozen config singleton for flext-target-oracle-oic.

See ADR-005 §7.

Model-less: business rules live in ``config/*.yaml`` under the ``TargetOracleOic:``
key, exposed through the open ``config.TargetOracleOic`` namespace (``extra="allow"``)
with no per-domain model. Access is ``config.TargetOracleOic.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import FlextMeltanoConfig, m

from flext_target_oracle_oic._models.config import FlextTargetOracleOicModelsConfig


class FlextTargetOracleOicConfig(FlextMeltanoConfig):
    """TargetOracleOic config auto-loaded model-less from ``config/*.yaml``.

    MRO carries ``FlextSettings`` FIRST (ENFORCE-042); the class stays a frozen,
    YAML-validated config singleton.
    """

    TargetOracleOic: Annotated[
        FlextTargetOracleOicModelsConfig.TargetOracleOicNamespace,
        m.Field(
            description=(
                "Open namespace exposing ``config/*.yaml`` under ``TargetOracleOic``."
            ),
        ),
    ] = FlextTargetOracleOicModelsConfig.TargetOracleOicNamespace()


config: FlextTargetOracleOicConfig = FlextTargetOracleOicConfig.fetch_global()
"""Pre-instantiated frozen config singleton.

Exposed as ``from flext_target_oracle_oic import config``.
"""

__all__: list[str] = ["FlextTargetOracleOicConfig", "config"]
