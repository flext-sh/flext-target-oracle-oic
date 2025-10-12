"""Target Oracle OIC Exceptions - Factory pattern using flext-core exceptions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

PEP8-compliant exception hierarchy with maximum flext-core composition.
"""

from __future__ import annotations

from typing import override

from flext_core import FlextCore

# ===============================================================================
# BASE ORACLE OIC EXCEPTION
# ===============================================================================


class FlextTargetOracleOicError(Exception):
    """Base exception for Oracle OIC target operations using flext-core patterns."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC target error",
        *,
        details: FlextCore.Types.Dict | None = None,
        integration_name: str | None = None,
        oic_instance: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize exception with Oracle OIC context."""
        context = kwargs.copy()

        if details:
            context.update(details)
        if integration_name is not None:
            context["integration_name"] = integration_name
        if oic_instance is not None:
            context["oic_instance"] = oic_instance

        # Initialize base without prefixing the message for test expectations
        self.message = message
        self.details = context or {}
        super().__init__(message)


# ===============================================================================
# SPECIALIZED ORACLE OIC EXCEPTIONS
# ===============================================================================


class FlextTargetOracleOicAuthenticationError(
    FlextCore.Exceptions.ModuleBaseError.ModuleAuthenticationError
):
    """Oracle OIC authentication errors using flext-core patterns."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC authentication failed",
        *,
        auth_method: str | None = None,
        endpoint: str | None = None,
        oic_instance: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC authentication error with context."""
        context = kwargs.copy()

        if auth_method is not None:
            context["auth_method"] = auth_method
        if endpoint is not None:
            context["endpoint"] = endpoint
        if oic_instance is not None:
            context["oic_instance"] = oic_instance

        # Use proper flext-core initialization
        super().__init__(
            f"Oracle OIC auth: {message}",
            auth_method=auth_method,
            **context,
        )


class FlextTargetOracleOicConnectionError(
    FlextCore.Exceptions.ModuleBaseError.ModuleConnectionError
):
    """Oracle OIC connection errors using flext-core patterns."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC connection failed",
        *,
        oic_instance: str | None = None,
        endpoint: str | None = None,
        connection_type: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC connection error with context."""
        context = kwargs.copy()

        if oic_instance is not None:
            context["oic_instance"] = oic_instance
        if endpoint is not None:
            context["endpoint"] = endpoint
        if connection_type is not None:
            context["connection_type"] = connection_type

        # Use proper flext-core initialization
        super().__init__(
            f"Oracle OIC connection: {message}",
            service=oic_instance or "Oracle OIC",
            endpoint=endpoint,
            **context,
        )


class FlextTargetOracleOicProcessingError(
    FlextCore.Exceptions.ModuleBaseError.ModuleProcessingError
):
    """Oracle OIC processing errors using flext-core patterns."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC processing failed",
        *,
        integration_name: str | None = None,
        processing_stage: str | None = None,
        record_count: int | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC processing error with context."""
        context = kwargs.copy()

        if integration_name is not None:
            context["integration_name"] = integration_name
        if processing_stage is not None:
            context["processing_stage"] = processing_stage
        if record_count is not None:
            context["record_count"] = record_count

        # Use proper flext-core initialization
        super().__init__(
            f"Oracle OIC processing: {message}",
            operation=processing_stage,
            business_rule=None,
            **context,
        )


class FlextTargetOracleOicValidationError(
    FlextCore.Exceptions.ModuleBaseError.ModuleValidationError
):
    """Oracle OIC validation errors using flext-core patterns."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC validation failed",
        *,
        field: str | None = None,
        value: object = None,
        integration_name: str | None = None,
        entity_type: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC validation error with context."""
        validation_details: FlextCore.Types.Dict = {}
        context = kwargs.copy()

        if integration_name is not None:
            context["integration_name"] = integration_name
        if entity_type is not None:
            context["entity_type"] = entity_type

        # Prepare validation details for flext-core
        if field is not None:
            validation_details["field"] = field
        if value is not None:
            validation_details["value"] = str(value)[:100]  # Truncate long values
        if validation_details:
            context.update(validation_details)

        # Use proper flext-core initialization
        super().__init__(
            f"Oracle OIC validation: {message}",
            field=field,
            value=value,
            validation_details=validation_details or None,
            **context,
        )


class FlextTargetOracleOicConfigurationError(
    FlextCore.Exceptions.ModuleBaseError.ModuleConfigurationError
):
    """Oracle OIC configuration errors using flext-core patterns."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC configuration error",
        *,
        config_key: str | None = None,
        config_section: str | None = None,
        integration_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC configuration error with context."""
        context = kwargs.copy()

        if config_section is not None:
            context["config_section"] = config_section
        if integration_name is not None:
            context["integration_name"] = integration_name

        # Use proper flext-core initialization
        super().__init__(
            f"Oracle OIC config: {message}",
            config_key=config_key,
            config_file=config_section,  # Map config_section to config_file for flext-core
            **context,
        )


# ===============================================================================
# ADDITIONAL SPECIALIZED EXCEPTIONS
# ===============================================================================


class FlextTargetOracleOicTransformationError(FlextTargetOracleOicError):
    """Oracle OIC transformation errors using flext-core patterns."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC transformation failed",
        *,
        transformation_type: str | None = None,
        input_schema: FlextCore.Types.Dict | None = None,
        output_schema: FlextCore.Types.Dict | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC transformation error with context."""
        context = kwargs.copy()

        if transformation_type is not None:
            context["transformation_type"] = transformation_type
        if input_schema is not None:
            # Include minimal schema info for debugging
            properties: FlextCore.Types.Dict = input_schema.get("properties", {})
            if isinstance(properties, dict):
                context["input_schema_keys"] = list(properties.keys())
        if output_schema is not None:
            properties: FlextCore.Types.Dict = output_schema.get("properties", {})
            if isinstance(properties, dict):
                context["output_schema_keys"] = list(properties.keys())

        super().__init__(
            f"Oracle OIC transformation: {message}",
            details=context,
        )


class FlextTargetOracleOicInfrastructureError(FlextTargetOracleOicError):
    """Oracle OIC infrastructure errors using flext-core patterns."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC infrastructure error",
        *,
        component: str | None = None,
        service: str | None = None,
        health_status: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC infrastructure error with context."""
        context = kwargs.copy()

        if component is not None:
            context["component"] = component
        if service is not None:
            context["service"] = service
        if health_status is not None:
            context["health_status"] = health_status

        super().__init__(
            f"Oracle OIC infrastructure: {message}",
            details=context,
        )


class FlextTargetOracleOicAPIError(FlextTargetOracleOicError):
    """Oracle OIC API-specific errors using flext-core patterns."""

    @override
    def __init__(
        self,
        message: str = "Oracle OIC API error",
        *,
        status_code: int | None = None,
        endpoint: str | None = None,
        response_body: str | None = None,
        request_method: str | None = None,
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
        if request_method is not None:
            context["request_method"] = request_method

        super().__init__(
            f"Oracle OIC API: {message}",
            details=context,
        )


# ===============================================================================
# ERROR DETAILS VALUE OBJECT
# ===============================================================================


class FlextTargetOracleOicErrorDetails(FlextCore.Models):
    """Structured error details using flext-core patterns."""

    error_code: str
    error_type: str
    context: FlextCore.Types.Dict
    timestamp: str
    source_component: str
    integration_name: str | None = None
    oic_instance: str | None = None

    def validate_domain_rules(self: object) -> FlextCore.Result[None]:
        """Validate domain-specific business rules."""
        try:
            # Validate error code format
            if not self.error_code or not self.error_code.startswith("ORACLE_OIC"):
                return FlextCore.Result[None].fail(
                    "Error code must start with 'ORACLE_OIC'"
                )

            # Validate error type is not empty
            if not self.error_type:
                return FlextCore.Result[None].fail("Error type cannot be empty")

            # Validate source component is valid
            valid_components = {
                "target_config",
                "target_client",
                "target_models",
                "target_exceptions",
                "connection",
                "patterns",
                "singer",
                "application",
                "infrastructure",
            }
            if self.source_component not in valid_components:
                return FlextCore.Result[None].fail(
                    f"Invalid source component: {self.source_component}",
                )

            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(f"Domain validation failed: {e}")


# ===============================================================================
# EXCEPTION FACTORY FUNCTIONS
# ===============================================================================


def create_authentication_error(
    message: str,
    *,
    auth_method: str | None = None,
    endpoint: str | None = None,
    oic_instance: str | None = None,
) -> FlextTargetOracleOicAuthenticationError:
    """Create authentication errors."""
    return FlextTargetOracleOicAuthenticationError(
        message,
        auth_method=auth_method,
        endpoint=endpoint,
        oic_instance=oic_instance,
    )


def create_connection_error(
    message: str,
    *,
    oic_instance: str | None = None,
    endpoint: str | None = None,
    connection_type: str | None = None,
) -> FlextTargetOracleOicConnectionError:
    """Create connection errors."""
    return FlextTargetOracleOicConnectionError(
        message,
        oic_instance=oic_instance,
        endpoint=endpoint,
        connection_type=connection_type,
    )


def create_processing_error(
    message: str,
    *,
    integration_name: str | None = None,
    processing_stage: str | None = None,
    record_count: int | None = None,
) -> FlextTargetOracleOicProcessingError:
    """Create processing errors."""
    return FlextTargetOracleOicProcessingError(
        message,
        integration_name=integration_name,
        processing_stage=processing_stage,
        record_count=record_count,
    )


def create_validation_error(
    message: str,
    *,
    field: str | None = None,
    value: object = None,
    integration_name: str | None = None,
    entity_type: str | None = None,
) -> FlextTargetOracleOicValidationError:
    """Create validation errors."""
    return FlextTargetOracleOicValidationError(
        message,
        field=field,
        value=value,
        integration_name=integration_name,
        entity_type=entity_type,
    )


def create_configuration_error(
    message: str,
    *,
    config_key: str | None = None,
    config_section: str | None = None,
    integration_name: str | None = None,
) -> FlextTargetOracleOicConfigurationError:
    """Create configuration errors."""
    return FlextTargetOracleOicConfigurationError(
        message,
        config_key=config_key,
        config_section=config_section,
        integration_name=integration_name,
    )


def create_api_error(
    message: str,
    *,
    status_code: int | None = None,
    endpoint: str | None = None,
    response_body: str | None = None,
    request_method: str | None = None,
) -> FlextTargetOracleOicAPIError:
    """Create API errors."""
    return FlextTargetOracleOicAPIError(
        message,
        status_code=status_code,
        endpoint=endpoint,
        response_body=response_body,
        request_method=request_method,
    )


# ===============================================================================
# ERROR RESULT FACTORY FUNCTIONS
# ===============================================================================


def create_auth_error_result(
    message: str,
    *,
    auth_method: str | None = None,
    endpoint: str | None = None,
    oic_instance: str | None = None,
) -> FlextCore.Result[None]:
    """Create authentication error result."""
    error = create_authentication_error(
        message,
        auth_method=auth_method,
        endpoint=endpoint,
        oic_instance=oic_instance,
    )
    return FlextCore.Result[None].fail(str(error))


def create_connection_error_result(
    message: str,
    *,
    oic_instance: str | None = None,
    endpoint: str | None = None,
    connection_type: str | None = None,
) -> FlextCore.Result[None]:
    """Create connection error result."""
    error = create_connection_error(
        message,
        oic_instance=oic_instance,
        endpoint=endpoint,
        connection_type=connection_type,
    )
    return FlextCore.Result[None].fail(str(error))


def create_processing_error_result(
    message: str,
    *,
    integration_name: str | None = None,
    processing_stage: str | None = None,
    record_count: int | None = None,
) -> FlextCore.Result[None]:
    """Create processing error result."""
    error = create_processing_error(
        message,
        integration_name=integration_name,
        processing_stage=processing_stage,
        record_count=record_count,
    )
    return FlextCore.Result[None].fail(str(error))


def create_validation_error_result(
    message: str,
    *,
    field: str | None = None,
    value: object = None,
    integration_name: str | None = None,
    entity_type: str | None = None,
) -> FlextCore.Result[None]:
    """Create validation error result."""
    error = create_validation_error(
        message,
        field=field,
        value=value,
        integration_name=integration_name,
        entity_type=entity_type,
    )
    return FlextCore.Result[None].fail(str(error))


# ===============================================================================
# EXPORTS
# ===============================================================================

__all__: FlextCore.Types.StringList = [
    "FlextTargetOracleOicAPIError",
    "FlextTargetOracleOicAuthenticationError",
    "FlextTargetOracleOicConfigurationError",
    "FlextTargetOracleOicConnectionError",
    "FlextTargetOracleOicError",
    "FlextTargetOracleOicErrorDetails",
    "FlextTargetOracleOicInfrastructureError",
    "FlextTargetOracleOicProcessingError",
    "FlextTargetOracleOicTransformationError",
    "FlextTargetOracleOicValidationError",
    "create_api_error",
    "create_auth_error_result",
    "create_authentication_error",
    "create_configuration_error",
    "create_connection_error",
    "create_connection_error_result",
    "create_processing_error",
    "create_processing_error_result",
    "create_validation_error",
    "create_validation_error_result",
]
