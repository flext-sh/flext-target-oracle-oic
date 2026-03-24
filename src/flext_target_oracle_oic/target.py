"""Target module exports for Oracle OIC singer target."""

from __future__ import annotations

from flext_target_oracle_oic.target_client import (
    FlextTargetOracleOic,
    FlextTargetOracleOicBaseSink,
    main,
)

__all__ = ["FlextTargetOracleOic", "FlextTargetOracleOicBaseSink", "main"]
