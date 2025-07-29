"""Oracle OIC exceptions using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Any

from flext_core import FlextError, FlextResult, FlextValueObject


# Base Oracle OIC exception
class FlextTargetOracleOicError(FlextError):
    """Base exception for Oracle OIC target operations."""

    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        """Initialize exception with message and optional details."""
        super().__init__(message)
        self.message = message
        self.details = details or {}


class FlextTargetOracleOicAuthenticationError(FlextTargetOracleOicError):
    """Oracle OIC authentication errors."""


class FlextTargetOracleOicProcessingError(FlextTargetOracleOicError):
    """Oracle OIC processing errors."""


class FlextTargetOracleOicTransformationError(FlextTargetOracleOicError):
    """Oracle OIC transformation errors."""


# Oracle OIC-specific exceptions that need custom behavior
class FlextTargetOracleOicConnectionError(FlextTargetOracleOicError):
    """Oracle OIC-specific connection errors."""


class FlextTargetOracleOicValidationError(FlextTargetOracleOicError):
    """Oracle OIC-specific validation errors."""


class FlextTargetOracleOicConfigurationError(FlextTargetOracleOicError):
    """Oracle OIC-specific configuration errors."""


class FlextTargetOracleOicInfrastructureError(FlextTargetOracleOicError):
    """Oracle OIC infrastructure errors."""


class FlextTargetOracleOicAPIError(FlextTargetOracleOicError):
    """Oracle OIC API-specific errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Initialize API error with status code."""
        super().__init__(message, details)
        self.status_code = status_code


class FlextTargetOracleOicErrorDetails(FlextValueObject):
    """Structured error details using flext-core patterns."""

    error_code: str
    error_type: str
    context: dict[str, Any]
    timestamp: str
    source_component: str

    def validate_domain_rules(self) -> FlextResult[None]:
        """Validate domain-specific business rules."""
        try:
            # Validate error code format
            if not self.error_code or not self.error_code.startswith("OIC"):
                return FlextResult.fail("Error code must start with 'OIC'")

            # Validate error type is not empty
            if not self.error_type:
                return FlextResult.fail("Error type cannot be empty")

            # Validate source component is valid
            valid_components = [
                "connection",
                "patterns",
                "singer",
                "application",
                "infrastructure",
            ]
            if self.source_component not in valid_components:
                return FlextResult.fail(f"Invalid source component: {self.source_component}")

            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Domain validation failed: {e}")
