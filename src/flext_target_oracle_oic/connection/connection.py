"""Connection primitives for Oracle OIC target runtime."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextResult, t


class OICConnection:
    """Holds runtime connection configuration and health checks."""

    def __init__(self, config: Mapping[str, t.JsonValue] | None = None) -> None:
        """Initialize connection with optional configuration mapping."""
        super().__init__()
        self.config = config or {}

    def test_connection(self) -> FlextResult[bool]:
        """Return a successful health check result."""
        return FlextResult[bool].ok(value=True)


__all__ = ["OICConnection"]
