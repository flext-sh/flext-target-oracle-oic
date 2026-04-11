"""Connection primitives for Oracle OIC target runtime."""

from __future__ import annotations

from flext_core import r
from flext_target_oracle_oic import t


class FlextTargetOracleOicConnection:
    """Holds runtime connection configuration and health checks."""

    def __init__(self, settings: t.ConfigurationMapping | None = None) -> None:
        """Initialize connection with optional configuration mapping."""
        super().__init__()
        self.settings = settings or {}

    def test_connection(self) -> r[bool]:
        """Return a successful health check result."""
        return r[bool].ok(value=True)


__all__ = ["FlextTargetOracleOicConnection"]
