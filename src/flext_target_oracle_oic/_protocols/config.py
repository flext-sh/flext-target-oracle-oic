# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_oic/_protocols/config
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols


class FlextTargetOracleOicProtocolsConfig:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class TargetOracleOicNamespace(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""


__all__: list[str] = [
    "FlextTargetOracleOicProtocolsConfig",
]
