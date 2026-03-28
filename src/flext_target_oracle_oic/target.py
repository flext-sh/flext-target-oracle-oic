"""Re-export shim — canonical implementation lives in _utilities.target."""

from __future__ import annotations

from flext_target_oracle_oic._utilities.target import (
    FlextTargetOracleOic,
    FlextTargetOracleOicBaseSink,
    FlextTargetOracleOicConnectionsSink,
    FlextTargetOracleOicIntegrationsSink,
    FlextTargetOracleOicLookupsSink,
    FlextTargetOracleOicPackagesSink,
    logger,
    main,
)

__all__ = [
    "FlextTargetOracleOic",
    "FlextTargetOracleOicBaseSink",
    "FlextTargetOracleOicConnectionsSink",
    "FlextTargetOracleOicIntegrationsSink",
    "FlextTargetOracleOicLookupsSink",
    "FlextTargetOracleOicPackagesSink",
    "logger",
    "main",
]
