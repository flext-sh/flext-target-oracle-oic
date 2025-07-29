"""Oracle OIC exceptions - CONSOLIDATED to eliminate duplication.

Uses flext-meltano common exception patterns. Eliminates 82-line duplication
with target-ldif and other target projects.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Any

from flext_core import FlextValueObject

# Import consolidated target exceptions from flext-meltano common
# MIGRATED: Singer SDK imports centralized via flext-meltano
from flext_meltano.common import (
    FlextMeltanoTargetAuthenticationError,
    FlextMeltanoTargetError,
    FlextMeltanoTargetProcessingError,
    FlextMeltanoTargetTransformationError,
)

# Use consolidated base target exception
FlextTargetOracleOicError = FlextMeltanoTargetError
FlextTargetOracleOicAuthenticationError = FlextMeltanoTargetAuthenticationError
FlextTargetOracleOicProcessingError = FlextMeltanoTargetProcessingError
FlextTargetOracleOicTransformationError = FlextMeltanoTargetTransformationError


# Oracle OIC-specific exceptions that need custom behavior
class FlextTargetOracleOicConnectionError(FlextMeltanoTargetError):
    """Oracle OIC-specific connection errors."""


class FlextTargetOracleOicValidationError(FlextMeltanoTargetError):
    """Oracle OIC-specific validation errors."""


class FlextTargetOracleOicConfigurationError(FlextMeltanoTargetError):
    """Oracle OIC-specific configuration errors."""


class FlextTargetOracleOicInfrastructureError(FlextMeltanoTargetError):
    """Oracle OIC infrastructure errors."""


class FlextTargetOracleOicAPIError(FlextMeltanoTargetError):
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

    def validate_domain_rules(self) -> None:
        """Validate domain-specific business rules."""
        # Validate error code format
        if not self.error_code or not self.error_code.startswith("OIC"):
            msg = "Error code must start with 'OIC'"
            raise ValueError(msg)

        # Validate error type is not empty
        if not self.error_type:
            msg = "Error type cannot be empty"
            raise ValueError(msg)

        # Validate source component is valid
        valid_components = [
            "connection",
            "patterns",
            "singer",
            "application",
            "infrastructure",
        ]
        if self.source_component not in valid_components:
            msg = f"Invalid source component: {self.source_component}"
            raise ValueError(msg)
