"""Target module exports for Oracle OIC singer target."""

from __future__ import annotations

from .target_client import OICBaseSink, TargetOracleOic, main

__all__ = ["OICBaseSink", "TargetOracleOic", "main"]
