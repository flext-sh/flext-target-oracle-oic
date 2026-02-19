"""Exception hierarchy for target Oracle OIC package."""

from __future__ import annotations

from flext_core import FlextExceptions, FlextTypes as t


class FlextTargetOracleOicError(Exception):
    """Base target exception with optional details mapping."""

    def __init__(
        self,
        message: str = "Oracle OIC target error",
        *,
        details: dict[str, t.GeneralValueType] | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize base exception context."""
        self.details = {**(details or {}), **kwargs}
        super().__init__(message)


class FlextTargetOracleOicAuthenticationError(FlextExceptions.AuthenticationError):
    """Authentication failure for Oracle OIC target operations."""

    pass


class FlextTargetOracleOicConnectionError(FlextExceptions.ConnectionError):
    """Connection failure for Oracle OIC target operations."""

    pass


class FlextTargetOracleOicProcessingError(FlextExceptions.OperationError):
    """Processing failure for Oracle OIC target operations."""

    pass


class FlextTargetOracleOicValidationError(FlextExceptions.ValidationError):
    """Validation failure for Oracle OIC target operations."""

    pass


class FlextTargetOracleOicSettingsurationError(FlextExceptions.ConfigurationError):
    """Configuration failure for Oracle OIC target operations."""

    pass


__all__ = [
    "FlextTargetOracleOicAuthenticationError",
    "FlextTargetOracleOicConnectionError",
    "FlextTargetOracleOicError",
    "FlextTargetOracleOicProcessingError",
    "FlextTargetOracleOicSettingsurationError",
    "FlextTargetOracleOicValidationError",
]
