"""Test exception hierarchy for FlextTargetOracleOic."""

from pydantic_core import ValidationError


import pytest

from flext_target_oracle_oic.exceptions import (
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
        """Test basic exception creation."""
        exception = FlextTargetOracleOicError("Test error")
        if str(exception) != "Test error":
            raise AssertionError(f"Expected {"Test error"}, got {str(exception)}")
        assert exception.message == "Test error"
        if exception.details != {}:
            raise AssertionError(f"Expected {{}}, got {exception.details}")

    def test_exception_with_details(self) -> None:
        """Test exception with details."""
        details = {"component": "connection", "operation": "authenticate"}
        exception = FlextTargetOracleOicError("Test error", details)
        if exception.details != details:
            raise AssertionError(f"Expected {details}, got {exception.details}")

    def test_exception_inheritance(self) -> None:
        """Test exception inheritance from Exception."""
        exception = FlextTargetOracleOicError("Test error")
        assert isinstance(exception, Exception)


class TestSpecificExceptions:
    """Test specific exception classes."""

    def test_connection_error(self) -> None:
        """Test connection error."""
        error = FlextTargetOracleOicConnectionError("Connection failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Connection failed":
            raise AssertionError(f"Expected {"Connection failed"}, got {str(error)}")

    def test_authentication_error(self) -> None:
        """Test authentication error."""
        error = FlextTargetOracleOicAuthenticationError("Auth failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Auth failed":
            raise AssertionError(f"Expected {"Auth failed"}, got {str(error)}")

    def test_validation_error(self) -> None:
        """Test validation error."""
        error = FlextTargetOracleOicValidationError("Validation failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Validation failed":
            raise AssertionError(f"Expected {"Validation failed"}, got {str(error)}")

    def test_transformation_error(self) -> None:
        """Test transformation error."""
        error = FlextTargetOracleOicTransformationError("Transform failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Transform failed":
            raise AssertionError(f"Expected {"Transform failed"}, got {str(error)}")

    def test_processing_error(self) -> None:
        """Test processing error."""
        error = FlextTargetOracleOicProcessingError("Processing failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Processing failed":
            raise AssertionError(f"Expected {"Processing failed"}, got {str(error)}")

    def test_configuration_error(self) -> None:
        """Test configuration error."""
        error = FlextTargetOracleOicConfigurationError("Config failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Config failed":
            raise AssertionError(f"Expected {"Config failed"}, got {str(error)}")

    def test_infrastructure_error(self) -> None:
        """Test infrastructure error."""
        error = FlextTargetOracleOicInfrastructureError("Infrastructure failed")
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "Infrastructure failed":
            raise AssertionError(f"Expected {"Infrastructure failed"}, got {str(error)}")

    def test_api_error(self) -> None:
        """Test API error."""
        error = FlextTargetOracleOicAPIError("API failed", 500)
        assert isinstance(error, FlextTargetOracleOicError)
        if str(error) != "API failed":
            raise AssertionError(f"Expected {"API failed"}, got {str(error)}")
        assert error.status_code == 500

    def test_api_error_without_status_code(self) -> None:
        """Test API error without status code."""
        error = FlextTargetOracleOicAPIError("API failed")
        assert error.status_code is None


class TestFlextTargetOracleOicErrorDetails:
    """Test error details value object."""

    def test_error_details_creation(self) -> None:
        """Test error details creation."""
        details = FlextTargetOracleOicErrorDetails(
            error_code="OIC001",
            error_type="ConnectionError",
            context={"server": "oic.example.com"},
            timestamp="2025-01-20T10:00:00Z",
            source_component="connection",
        )

        if details.error_code != "OIC001":

            raise AssertionError(f"Expected {"OIC001"}, got {details.error_code}")
        assert details.error_type == "ConnectionError"
        if details.context != {"server": "oic.example.com"}:
            raise AssertionError(f"Expected {{'server': 'oic.example.com'}}, got {details.context}")
        assert details.timestamp == "2025-01-20T10:00:00Z"
        if details.source_component != "connection":
            raise AssertionError(f"Expected {"connection"}, got {details.source_component}")

    def test_error_details_immutability(self) -> None:
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
        """Test validation with invalid source component."""
        details = FlextTargetOracleOicErrorDetails(
            error_code="OIC001",
            error_type="ConnectionError",
            context={},
            timestamp="2025-01-20T10:00:00Z",
            source_component="invalid_component",
        )

        with pytest.raises(
            ValueError, match="Invalid source component: invalid_component",
        ):
            details.validate_domain_rules()
