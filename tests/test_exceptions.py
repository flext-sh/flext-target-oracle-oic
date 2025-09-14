"""Test exception hierarchy for FlextTargetOracleOic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

import pytest
from pydantic_core import ValidationError

from flext_target_oracle_oic import (
    FlextTargetOracleOicAPIError,
    FlextTargetOracleOicAuthenticationError,
    FlextTargetOracleOicConfigurationError,
    FlextTargetOracleOicConnectionError,
    FlextTargetOracleOicError,
    FlextTargetOracleOicErrorDetails,
    FlextTargetOracleOicInfrastructureError,
    FlextTargetOracleOicProcessingError,
    FlextTargetOracleOicTransformationError,
    FlextTargetOracleOicValidationError,
)


class TestFlextTargetOracleOicError:
    """Test base exception class."""

    def test_basic_exception(self) -> None:
        """Test method."""
        """Test basic exception creation."""
        exception = FlextTargetOracleOicError("Test error")
        if str(exception) != "Test error":
            msg: str = f"Expected {'Test error'}, got {exception!s}"
            raise AssertionError(msg)
        assert exception.message == "Test error"
        if exception.details != {}:
            msg: str = f"Expected {{}}, got {exception.details}"
            raise AssertionError(msg)

    def test_exception_with_details(self) -> None:
        """Test method."""
        """Test exception with details."""
        details = {"component": "connection", "operation": "authenticate"}
        exception = FlextTargetOracleOicError("Test error", details)
        if exception.details != details:
            msg: str = f"Expected {details}, got {exception.details}"
            raise AssertionError(msg)

    def test_exception_inheritance(self) -> None:
        """Test method."""
        """Test exception inheritance from Exception."""
        exception = FlextTargetOracleOicError("Test error")
        assert isinstance(exception, Exception)


class TestSpecificExceptions:
    """Test specific exception classes."""

    def test_connection_error(self) -> None:
        """Test method."""
        """Test connection error."""
        error = FlextTargetOracleOicConnectionError("Connection failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Connection failed":
            msg: str = f"Expected {'Connection failed'}, got {error!s}"
            raise AssertionError(msg)

    def test_authentication_error(self) -> None:
        """Test method."""
        """Test authentication error."""
        error = FlextTargetOracleOicAuthenticationError("Auth failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Auth failed":
            msg: str = f"Expected {'Auth failed'}, got {error!s}"
            raise AssertionError(msg)

    def test_validation_error(self) -> None:
        """Test method."""
        """Test validation error."""
        error = FlextTargetOracleOicValidationError("Validation failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Validation failed":
            msg: str = f"Expected {'Validation failed'}, got {error!s}"
            raise AssertionError(msg)

    def test_transformation_error(self) -> None:
        """Test method."""
        """Test transformation error."""
        error = FlextTargetOracleOicTransformationError("Transform failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Transform failed":
            msg: str = f"Expected {'Transform failed'}, got {error!s}"
            raise AssertionError(msg)

    def test_processing_error(self) -> None:
        """Test method."""
        """Test processing error."""
        error = FlextTargetOracleOicProcessingError("Processing failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Processing failed":
            msg: str = f"Expected {'Processing failed'}, got {error!s}"
            raise AssertionError(msg)

    def test_configuration_error(self) -> None:
        """Test method."""
        """Test configuration error."""
        error = FlextTargetOracleOicConfigurationError("Config failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Config failed":
            msg: str = f"Expected {'Config failed'}, got {error!s}"
            raise AssertionError(msg)

    def test_infrastructure_error(self) -> None:
        """Test method."""
        """Test infrastructure error."""
        error = FlextTargetOracleOicInfrastructureError("Infrastructure failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Infrastructure failed":
            msg: str = f"Expected {'Infrastructure failed'}, got {error!s}"
            raise AssertionError(msg)

    def test_api_error(self) -> None:
        """Test method."""
        """Test API error."""
        error = FlextTargetOracleOicAPIError("API failed", 500)
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "API failed":
            msg: str = f"Expected {'API failed'}, got {error!s}"
            raise AssertionError(msg)
        assert error.status_code == 500

    def test_api_error_without_status_code(self) -> None:
        """Test method."""
        """Test API error without status code."""
        error = FlextTargetOracleOicAPIError("API failed")
        assert error.status_code is None


class TestFlextTargetOracleOicErrorDetails:
    """Test error details value object."""

    def test_error_details_creation(self) -> None:
        """Test method."""
        """Test error details creation."""
        details = FlextTargetOracleOicErrorDetails(
            error_code="OIC001",
            error_type="ConnectionError",
            context={"server": "oic.example.com"},
            timestamp="2025-01-20T10:00:00Z",
            source_component="connection",
        )

        if details.error_code != "OIC001":
            msg: str = f"Expected {'OIC001'}, got {details.error_code}"
            raise AssertionError(msg)
        assert details.error_type == "ConnectionError"
        if details.context != {"server": "oic.example.com"}:
            msg: str = (
                f"Expected {{'server': 'oic.example.com'}}, got {details.context}"
            )
            raise AssertionError(msg)
        assert details.timestamp == "2025-01-20T10:00:00Z"
        if details.source_component != "connection":
            msg: str = f"Expected {'connection'}, got {details.source_component}"
            raise AssertionError(msg)

    def test_error_details_immutability(self) -> None:
        """Test method."""
        """Test that error details are immutable."""
        details = FlextTargetOracleOicErrorDetails(
            error_code="OIC001",
            error_type="ConnectionError",
            context={},
            timestamp="2025-01-20T10:00:00Z",
            source_component="connection",
        )

        with pytest.raises(ValidationError):
            details.error_code = "OIC002"

    def test_error_details_validation_success(self) -> None:
        """Test method."""
        """Test successful validation."""
        details = FlextTargetOracleOicErrorDetails(
            error_code="OIC001",
            error_type="ConnectionError",
            context={"server": "oic.example.com"},
            timestamp="2025-01-20T10:00:00Z",
            source_component="connection",
        )

        # Should not raise any exception
        details.validate_domain_rules()

    def test_error_details_validation_invalid_error_code(self) -> None:
        """Test method."""
        """Test validation with invalid error code."""
        details = FlextTargetOracleOicErrorDetails(
            error_code="INVALID",
            error_type="ConnectionError",
            context={},
            timestamp="2025-01-20T10:00:00Z",
            source_component="connection",
        )

        with pytest.raises(ValueError, match="Error code must start with 'OIC'"):
            details.validate_domain_rules()

    def test_error_details_validation_empty_error_type(self) -> None:
        """Test method."""
        """Test validation with empty error type."""
        details = FlextTargetOracleOicErrorDetails(
            error_code="OIC001",
            error_type="",
            context={},
            timestamp="2025-01-20T10:00:00Z",
            source_component="connection",
        )

        with pytest.raises(ValueError, match="Error type cannot be empty"):
            details.validate_domain_rules()

    def test_error_details_validation_invalid_source_component(self) -> None:
        """Test method."""
        """Test validation with invalid source component."""
        details = FlextTargetOracleOicErrorDetails(
            error_code="OIC001",
            error_type="ConnectionError",
            context={},
            timestamp="2025-01-20T10:00:00Z",
            source_component="invalid_component",
        )

        with pytest.raises(
            ValueError,
            match="Invalid source component: invalid_component",
        ):
            details.validate_domain_rules()
