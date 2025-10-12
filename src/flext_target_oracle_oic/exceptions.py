"""Oracle Integration Cloud target exceptions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from typing import override

from flext_core import FlextCore


# Base Oracle OIC exception
class FlextTargetOracleOicError(FlextCore.Exceptions.Error):
    """Base exception for Oracle OIC target operations."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC target error",
        *,
        details: FlextCore.Types.Dict | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize exception with message and optional details."""
        # Store domain-specific attributes before extracting common kwargs
        self.details = details

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with OIC-specific fields
        context = self._build_context(
            base_context,
            **(details or {}),
        )

        # Call parent with complete error information
        super().__init__(
            message,
            code=error_code or "TARGET_ORACLE_OIC_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTargetOracleOicAuthenticationError(FlextCore.Exceptions.AuthenticationError):
    """Oracle OIC authentication errors."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC authentication failed",
        *,
        auth_method: str | None = None,
        endpoint: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC authentication error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.auth_method = auth_method
        self.endpoint = endpoint

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with authentication-specific fields
        context = self._build_context(
            base_context,
            auth_method=auth_method,
            endpoint=endpoint,
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle OIC auth: {message}",
            code=error_code or "TARGET_ORACLE_OIC_AUTH_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTargetOracleOicProcessingError(FlextCore.Exceptions.ProcessingError):
    """Oracle OIC processing errors."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC processing failed",
        *,
        integration_name: str | None = None,
        processing_stage: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC processing error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.integration_name = integration_name
        self.processing_stage = processing_stage

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with processing-specific fields
        context = self._build_context(
            base_context,
            integration_name=integration_name,
            processing_stage=processing_stage,
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle OIC processing: {message}",
            code=error_code or "TARGET_ORACLE_OIC_PROCESSING_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTargetOracleOicTransformationError(FlextCore.Exceptions.ProcessingError):
    """Oracle OIC transformation errors."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC transformation failed",
        *,
        transformation_type: str | None = None,
        input_data: FlextCore.Types.Dict | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC transformation error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.transformation_type = transformation_type
        self.input_data = input_data

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with transformation-specific fields
        context = self._build_context(
            base_context,
            transformation_type=transformation_type,
            input_keys=list(input_data.keys()) if input_data is not None else None,
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle OIC transformation: {message}",
            code=error_code or "TARGET_ORACLE_OIC_TRANSFORMATION_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


# Oracle OIC-specific exceptions that need custom behavior
class FlextTargetOracleOicConnectionError(FlextCore.Exceptions.ConnectionError):
    """Oracle OIC-specific connection errors."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC connection failed",
        *,
        oic_instance: str | None = None,
        endpoint: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC connection error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.oic_instance = oic_instance
        self.endpoint = endpoint

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with connection-specific fields
        context = self._build_context(
            base_context,
            oic_instance=oic_instance,
            endpoint=endpoint,
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle OIC connection: {message}",
            code=error_code or "TARGET_ORACLE_OIC_CONNECTION_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTargetOracleOicValidationError(FlextCore.Exceptions.ValidationError):
    """Oracle OIC-specific validation errors."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC validation failed",
        *,
        field: str | None = None,
        value: object = None,
        integration_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC validation error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.field = field
        self.value = value
        self.integration_name = integration_name

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with validation-specific fields
        context = self._build_context(
            base_context,
            field=field,
            value=str(value)[:100]
            if value is not None
            else None,  # Truncate long values
            integration_name=integration_name,
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle OIC validation: {message}",
            code=error_code or "TARGET_ORACLE_OIC_VALIDATION_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTargetOracleOicConfigurationError(FlextCore.Exceptions.ConfigurationError):
    """Oracle OIC-specific configuration errors."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC configuration error",
        *,
        config_key: str | None = None,
        integration_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC configuration error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.config_key = config_key
        self.integration_name = integration_name

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with configuration-specific fields
        context = self._build_context(
            base_context,
            config_key=config_key,
            integration_name=integration_name,
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle OIC config: {message}",
            code=error_code or "TARGET_ORACLE_OIC_CONFIGURATION_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTargetOracleOicInfrastructureError(FlextTargetOracleOicError):
    """Oracle OIC infrastructure errors."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC infrastructure error",
        *,
        component: str | None = None,
        service: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC infrastructure error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.component = component
        self.service = service

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with infrastructure-specific fields
        context = self._build_context(
            base_context,
            component=component,
            service=service,
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle OIC infrastructure: {message}",
            details=context,
            code=error_code or "TARGET_ORACLE_OIC_INFRASTRUCTURE_ERROR",
            correlation_id=correlation_id,
        )


class FlextTargetOracleOicAPIError(FlextTargetOracleOicError):
    """Oracle OIC API-specific errors."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC API error",
        *,
        status_code: int | None = None,
        endpoint: str | None = None,
        response_body: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC API error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.status_code = status_code
        self.endpoint = endpoint
        self.response_body = response_body

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with API-specific fields
        context = self._build_context(
            base_context,
            status_code=status_code,
            endpoint=endpoint,
            response_body=response_body[:500]
            if response_body is not None
            else None,  # Truncate long responses
        )

        # Call parent with complete error information
        super().__init__(
            f"Oracle OIC API: {message}",
            details=context,
            code=error_code or "TARGET_ORACLE_OIC_API_ERROR",
            correlation_id=correlation_id,
        )


class FlextTargetOracleOicErrorDetails(FlextCore.Models):
    """Structured error details using flext-core patterns."""

    error_code: str
    error_type: str
    context: FlextCore.Types.Dict
    timestamp: str
    source_component: str

    def validate_domain_rules(self) -> FlextCore.Result[None]:
        """Validate domain-specific business rules."""
        try:
            # Validate error code format
            if not self.error_code or not self.error_code.startswith("OIC"):
                return FlextCore.Result[None].fail("Error code must start with 'OIC'")

            # Validate error type is not empty
            if not self.error_type:
                return FlextCore.Result[None].fail("Error type cannot be empty")

            # Validate source component is valid
            valid_components = [
                "connection",
                "patterns",
                "singer",
                "application",
                "infrastructure",
            ]
            if self.source_component not in valid_components:
                return FlextCore.Result[None].fail(
                    f"Invalid source component: {self.source_component}",
                )

            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(f"Domain validation failed: {e}")
