"""Oracle OIC exceptions using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import (
    FlextExceptions,
    FlextProcessingError,
    FlextResult,
    FlextValue,
)


# Base Oracle OIC exception
class FlextTargetOracleOicError(FlextExceptions):
    """Base exception for Oracle OIC target operations."""

    def __init__(
        self,
        message: str = "Oracle OIC target error",
        details: dict[str, object] | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize exception with message and optional details."""
        context = kwargs.copy()
        if details:
            context.update(details)

        super().__init__(message, context=context)


class FlextTargetOracleOicAuthenticationError(FlextExceptions):
    """Oracle OIC authentication errors."""

    def __init__(
        self,
        message: str = "Oracle OIC authentication failed",
        auth_method: str | None = None,
        endpoint: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC authentication error with context."""
        context = kwargs.copy()
        if auth_method is not None:
            context["auth_method"] = auth_method
        if endpoint is not None:
            context["endpoint"] = endpoint

        super().__init__(
            f"Oracle OIC auth: {message}",
            context=context,
        )


class FlextTargetOracleOicProcessingError(FlextProcessingError):
    """Oracle OIC processing errors."""

    def __init__(
        self,
        message: str = "Oracle OIC processing failed",
        integration_name: str | None = None,
        processing_stage: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC processing error with context."""
        context = kwargs.copy()
        if integration_name is not None:
            context["integration_name"] = integration_name
        if processing_stage is not None:
            context["processing_stage"] = processing_stage

        super().__init__(
            f"Oracle OIC processing: {message}",
            context=context,
        )


class FlextTargetOracleOicTransformationError(FlextProcessingError):
    """Oracle OIC transformation errors."""

    def __init__(
        self,
        message: str = "Oracle OIC transformation failed",
        transformation_type: str | None = None,
        input_data: dict[str, object] | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC transformation error with context."""
        context = kwargs.copy()
        if transformation_type is not None:
            context["transformation_type"] = transformation_type
        if input_data is not None:
            # Include minimal data info for debugging
            context["input_keys"] = list(input_data.keys())

        super().__init__(
            f"Oracle OIC transformation: {message}",
            context=context,
        )


# Oracle OIC-specific exceptions that need custom behavior
class FlextTargetOracleOicConnectionError(FlextExceptions):
    """Oracle OIC-specific connection errors."""

    def __init__(
        self,
        message: str = "Oracle OIC connection failed",
        oic_instance: str | None = None,
        endpoint: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC connection error with context."""
        context = kwargs.copy()
        if oic_instance is not None:
            context["oic_instance"] = oic_instance
        if endpoint is not None:
            context["endpoint"] = endpoint

        super().__init__(
            f"Oracle OIC connection: {message}",
            context=context,
        )


class FlextTargetOracleOicValidationError(FlextExceptions):
    """Oracle OIC-specific validation errors."""

    def __init__(
        self,
        message: str = "Oracle OIC validation failed",
        field: str | None = None,
        value: object = None,
        integration_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC validation error with context."""
        validation_details: dict[str, object] = {}
        if field is not None:
            validation_details["field"] = field
        if value is not None:
            validation_details["value"] = str(value)[:100]  # Truncate long values

        context = kwargs.copy()
        if integration_name is not None:
            context["integration_name"] = integration_name

        super().__init__(
            f"Oracle OIC validation: {message}",
            context=context,
        )


class FlextTargetOracleOicConfigurationError(FlextExceptions):
    """Oracle OIC-specific configuration errors."""

    def __init__(
        self,
        message: str = "Oracle OIC configuration error",
        config_key: str | None = None,
        integration_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC configuration error with context."""
        context = kwargs.copy()
        if config_key is not None:
            context["config_key"] = config_key
        if integration_name is not None:
            context["integration_name"] = integration_name

        super().__init__(
            f"Oracle OIC config: {message}",
            context=context,
        )


class FlextTargetOracleOicInfrastructureError(FlextTargetOracleOicError):
    """Oracle OIC infrastructure errors."""

    def __init__(
        self,
        message: str = "Oracle OIC infrastructure error",
        component: str | None = None,
        service: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC infrastructure error with context."""
        context = kwargs.copy()
        if component is not None:
            context["component"] = component
        if service is not None:
            context["service"] = service

        super().__init__(f"Oracle OIC infrastructure: {message}", context=context)


class FlextTargetOracleOicAPIError(FlextTargetOracleOicError):
    """Oracle OIC API-specific errors."""

    def __init__(
        self,
        message: str = "Oracle OIC API error",
        status_code: int | None = None,
        endpoint: str | None = None,
        response_body: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC API error with context."""
        context = kwargs.copy()
        if status_code is not None:
            context["status_code"] = status_code
        if endpoint is not None:
            context["endpoint"] = endpoint
        if response_body is not None:
            context["response_body"] = response_body[:500]  # Truncate long responses

        super().__init__(f"Oracle OIC API: {message}", context=context)


class FlextTargetOracleOicErrorDetails(FlextValue):
    """Structured error details using flext-core patterns."""

    error_code: str
    error_type: str
    context: dict[str, object]
    timestamp: str
    source_component: str

    def validate_domain_rules(self) -> FlextResult[None]:
        """Validate domain-specific business rules."""
        try:
            # Validate error code format
            if not self.error_code or not self.error_code.startswith("OIC"):
                return FlextResult[None].fail("Error code must start with 'OIC'")

            # Validate error type is not empty
            if not self.error_type:
                return FlextResult[None].fail("Error type cannot be empty")

            # Validate source component is valid
            valid_components = [
                "connection",
                "patterns",
                "singer",
                "application",
                "infrastructure",
            ]
            if self.source_component not in valid_components:
                return FlextResult[None].fail(
                    f"Invalid source component: {self.source_component}",
                )

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Domain validation failed: {e}")
