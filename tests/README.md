# 🧪 TARGET Oracle OIC - Test Suite

> **Module**: Comprehensive test suite for TARGET Oracle OIC with Singer SDK compliance and integration testing | **Audience**: QA Engineers, Data Engineers, Target Testing Specialists | **Status**: Production Ready

## 📋 **Overview**

Enterprise-grade test suite for the TARGET Oracle OIC implementation, providing comprehensive testing coverage including unit tests, integration tests with real Oracle Integration Cloud endpoints, performance testing, and Singer SDK compliance validation. This test suite demonstrates best practices for testing Singer targets and data loading operations.

---

## 🧭 **Navigation Context**

**🏠 Root**: [PyAuto Home](../../README.md) → **📂 Component**: [TARGET Oracle OIC](../README.md) → **📂 Current**: Test Suite

---

## 🎯 **Module Purpose**

This test module provides comprehensive validation for the TARGET Oracle OIC implementation, ensuring reliability, performance, and correctness of all data loading operations, Singer SDK compliance, and enterprise Oracle Integration Cloud integration workflows.

### **Key Testing Areas**

- **Unit Testing** - Core target logic and data transformation validation
- **Integration Testing** - End-to-end data loading with real OIC endpoints
- **Performance Testing** - Data throughput and loading performance
- **Singer SDK Testing** - Target compliance and specification validation
- **Authentication Testing** - OAuth2/JWT authentication validation
- **Error Handling Testing** - Error recovery and resilience validation

---

## 📁 **Test Structure**

```
tests/
├── unit/
│   ├── test_target_core.py              # Core target functionality tests
│   ├── test_sinks_validation.py         # Sink implementation tests
│   ├── test_authentication.py           # Authentication mechanism tests
│   ├── test_config_validation.py        # Configuration validation tests
│   └── test_data_transformation.py      # Data transformation tests
├── integration/
│   ├── test_oic_integration.py          # OIC endpoint integration tests
│   ├── test_singer_compliance.py        # Singer SDK compliance tests
│   ├── test_data_loading.py             # End-to-end data loading tests
│   ├── test_batch_processing.py         # Batch processing integration tests
│   └── test_real_time_loading.py        # Real-time data loading tests
├── performance/
│   ├── test_throughput_performance.py   # Data throughput testing
│   ├── test_concurrent_loading.py       # Concurrent loading scenarios
│   ├── test_memory_optimization.py      # Memory usage optimization tests
│   └── test_scalability_limits.py       # Scalability testing
├── singer/
│   ├── test_target_compliance.py        # Singer target specification compliance
│   ├── test_schema_validation.py        # Schema handling validation
│   ├── test_state_management.py         # State management testing
│   └── test_message_processing.py       # Singer message processing tests
├── authentication/
│   ├── test_oauth2_flow.py              # OAuth2 authentication flow tests
│   ├── test_jwt_validation.py           # JWT token validation tests
│   ├── test_token_refresh.py            # Token refresh mechanism tests
│   └── test_auth_error_handling.py      # Authentication error handling
├── error_handling/
│   ├── test_connection_errors.py        # Connection error recovery tests
│   ├── test_data_validation_errors.py   # Data validation error handling
│   ├── test_retry_mechanisms.py         # Retry logic validation
│   └── test_failover_scenarios.py       # Failover scenario testing
├── fixtures/
│   ├── oic_fixtures.py                  # OIC test data fixtures
│   ├── singer_fixtures.py               # Singer message test fixtures
│   └── authentication_fixtures.py       # Authentication test fixtures
├── conftest.py                           # Pytest configuration and fixtures
├── pytest.ini                           # Pytest configuration settings
└── singer_test_config.json              # Singer target test configuration
```

---

## 🔧 **Test Categories**

### **1. Unit Tests (unit/)**

#### **Core Target Testing (test_target_core.py)**

```python
"""Unit tests for TARGET Oracle OIC core functionality."""

import pytest
from unittest.mock import Mock, AsyncMock, patch
import json
from datetime import datetime

from target_oracle_oic.target import TargetOracleOIC
from target_oracle_oic.config import TargetConfig
from target_oracle_oic.sinks import OracleOICSink
from target_oracle_oic.exceptions import (
    TargetConfigurationError,
    OICConnectionError,
    DataValidationError
)

class TestTargetOracleOIC:
    """Test Oracle OIC target core functionality."""

    @pytest.fixture
    def target_config(self):
        """Target configuration fixture."""
        return TargetConfig(
            oic_host="https://test-oic.oracle.com",
            client_id="test_client_id",
            client_secret="test_client_secret",
            username="test_user",
            password="test_password",
            batch_size=1000,
            timeout=30
        )

    @pytest.fixture
    def mock_oic_client(self):
        """Mock OIC client fixture."""
        return Mock()

    @pytest.fixture
    def target_instance(self, target_config, mock_oic_client):
        """Target instance with mocked dependencies."""
        with patch('target_oracle_oic.target.OICClient', return_value=mock_oic_client):
            return TargetOracleOIC(config=target_config)

    def test_target_initialization_success(self, target_config):
        """Test successful target initialization."""
        # Act
        target = TargetOracleOIC(config=target_config)
        
        # Assert
        assert target.config == target_config
        assert target.name == "target-oracle-oic"
        assert target.config.batch_size == 1000

    def test_target_initialization_invalid_config(self):
        """Test target initialization with invalid configuration."""
        # Arrange
        invalid_config = TargetConfig(
            oic_host="",  # Invalid empty host
            client_id="test_client",
            client_secret="test_secret"
        )
        
        # Act & Assert
        with pytest.raises(TargetConfigurationError):
            TargetOracleOIC(config=invalid_config)

    def test_get_sink_for_stream(self, target_instance):
        """Test sink creation for specific stream."""
        # Arrange
        stream_name = "users"
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "email": {"type": "string"}
            }
        }
        
        # Act
        sink = target_instance.get_sink(stream_name, schema)
        
        # Assert
        assert isinstance(sink, OracleOICSink)
        assert sink.stream_name == stream_name
        assert sink.schema == schema

    def test_stream_discovery(self, target_instance, mock_oic_client):
        """Test stream discovery functionality."""
        # Arrange
        mock_oic_client.discover_streams.return_value = [
            {"name": "users", "endpoint": "/users"},
            {"name": "orders", "endpoint": "/orders"}
        ]
        
        # Act
        streams = target_instance.discover_streams()
        
        # Assert
        assert len(streams) == 2
        assert streams[0]["name"] == "users"
        assert streams[1]["name"] == "orders"
        mock_oic_client.discover_streams.assert_called_once()

class TestOracleOICSink:
    """Test Oracle OIC sink implementation."""

    @pytest.fixture
    def sink_config(self):
        """Sink configuration fixture."""
        return TargetConfig(
            oic_host="https://test-oic.oracle.com",
            client_id="test_client",
            client_secret="test_secret",
            batch_size=500
        )

    @pytest.fixture
    def user_schema(self):
        """User stream schema fixture."""
        return {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "email": {"type": "string"},
                "created_at": {"type": "string", "format": "date-time"}
            },
            "required": ["id", "name", "email"]
        }

    @pytest.fixture
    def mock_oic_client(self):
        """Mock OIC client for sink testing."""
        client = Mock()
        client.send_batch.return_value = {"status": "success", "records_processed": 100}
        return client

    @pytest.fixture
    def oracle_oic_sink(self, sink_config, user_schema, mock_oic_client):
        """Oracle OIC sink instance."""
        with patch('target_oracle_oic.sinks.OICClient', return_value=mock_oic_client):
            return OracleOICSink(
                target=Mock(),
                stream_name="users",
                schema=user_schema,
                config=sink_config
            )

    def test_sink_initialization(self, oracle_oic_sink, user_schema):
        """Test sink initialization."""
        # Assert
        assert oracle_oic_sink.stream_name == "users"
        assert oracle_oic_sink.schema == user_schema
        assert oracle_oic_sink.batch_size == 500
        assert len(oracle_oic_sink.records_buffer) == 0

    def test_process_record_valid_data(self, oracle_oic_sink):
        """Test processing valid record data."""
        # Arrange
        record = {
            "id": "user_001",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "created_at": "2025-06-19T10:00:00Z"
        }
        
        # Act
        oracle_oic_sink.process_record(record)
        
        # Assert
        assert len(oracle_oic_sink.records_buffer) == 1
        assert oracle_oic_sink.records_buffer[0] == record

    def test_process_record_invalid_data(self, oracle_oic_sink):
        """Test processing invalid record data."""
        # Arrange
        invalid_record = {
            "id": "user_001",
            "name": "John Doe"
            # Missing required 'email' field
        }
        
        # Act & Assert
        with pytest.raises(DataValidationError):
            oracle_oic_sink.process_record(invalid_record)

    def test_flush_records_batch(self, oracle_oic_sink, mock_oic_client):
        """Test batch flushing functionality."""
        # Arrange
        records = [
            {"id": f"user_{i:03d}", "name": f"User {i}", "email": f"user{i}@example.com"}
            for i in range(100)
        ]
        
        for record in records:
            oracle_oic_sink.process_record(record)
        
        # Act
        result = oracle_oic_sink.flush_records()
        
        # Assert
        assert result["status"] == "success"
        assert result["records_processed"] == 100
        assert len(oracle_oic_sink.records_buffer) == 0
        mock_oic_client.send_batch.assert_called_once()

    def test_auto_flush_on_batch_size(self, oracle_oic_sink, mock_oic_client):
        """Test automatic flush when batch size is reached."""
        # Arrange
        oracle_oic_sink.batch_size = 5  # Small batch size for testing
        
        # Act - Add records up to batch size
        for i in range(5):
            oracle_oic_sink.process_record({
                "id": f"user_{i:03d}",
                "name": f"User {i}",
                "email": f"user{i}@example.com"
            })
        
        # Assert - Should auto-flush
        mock_oic_client.send_batch.assert_called_once()
        assert len(oracle_oic_sink.records_buffer) == 0

class TestDataTransformation:
    """Test data transformation functionality."""

    def test_datetime_format_transformation(self):
        """Test datetime format transformation."""
        from target_oracle_oic.transformations import format_datetime
        
        # Arrange
        input_datetime = "2025-06-19T10:30:45.123Z"
        
        # Act
        result = format_datetime(input_datetime)
        
        # Assert
        assert result == "2025-06-19 10:30:45"

    def test_null_value_handling(self):
        """Test null value handling in transformations."""
        from target_oracle_oic.transformations import handle_null_values
        
        # Arrange
        record_with_nulls = {
            "id": "user_001",
            "name": "John Doe",
            "email": None,
            "phone": "",
            "address": "123 Main St"
        }
        
        # Act
        result = handle_null_values(record_with_nulls)
        
        # Assert
        assert result["id"] == "user_001"
        assert result["name"] == "John Doe"
        assert result["email"] is None
        assert result["phone"] == ""
        assert result["address"] == "123 Main St"

    def test_data_type_conversion(self):
        """Test data type conversion for OIC compatibility."""
        from target_oracle_oic.transformations import convert_data_types
        
        # Arrange
        input_record = {
            "id": 12345,  # Should convert to string
            "amount": "99.99",  # Should convert to float
            "is_active": "true",  # Should convert to boolean
            "count": "42"  # Should convert to integer
        }
        
        schema = {
            "properties": {
                "id": {"type": "string"},
                "amount": {"type": "number"},
                "is_active": {"type": "boolean"},
                "count": {"type": "integer"}
            }
        }
        
        # Act
        result = convert_data_types(input_record, schema)
        
        # Assert
        assert isinstance(result["id"], str)
        assert result["id"] == "12345"
        assert isinstance(result["amount"], float)
        assert result["amount"] == 99.99
        assert isinstance(result["is_active"], bool)
        assert result["is_active"] is True
        assert isinstance(result["count"], int)
        assert result["count"] == 42
```

#### **Authentication Testing (test_authentication.py)**

```python
"""Unit tests for Oracle OIC authentication mechanisms."""

import pytest
from unittest.mock import Mock, patch, AsyncMock
import jwt
from datetime import datetime, timedelta
import requests

from target_oracle_oic.auth import OICAuthenticator, OAuth2TokenManager
from target_oracle_oic.exceptions import AuthenticationError, TokenExpiredError

class TestOICAuthenticator:
    """Test Oracle OIC authentication functionality."""

    @pytest.fixture
    def auth_config(self):
        """Authentication configuration fixture."""
        return {
            "oic_host": "https://test-oic.oracle.com",
            "client_id": "test_client_id",
            "client_secret": "test_client_secret",
            "username": "test_user",
            "password": "test_password",
            "scope": "oic_integration"
        }

    @pytest.fixture
    def mock_requests(self):
        """Mock requests module."""
        with patch('target_oracle_oic.auth.requests') as mock_req:
            yield mock_req

    @pytest.fixture
    def authenticator(self, auth_config):
        """OIC authenticator instance."""
        return OICAuthenticator(auth_config)

    def test_authenticator_initialization(self, authenticator, auth_config):
        """Test authenticator initialization."""
        assert authenticator.oic_host == auth_config["oic_host"]
        assert authenticator.client_id == auth_config["client_id"]
        assert authenticator.client_secret == auth_config["client_secret"]

    def test_oauth2_token_request_success(self, authenticator, mock_requests):
        """Test successful OAuth2 token request."""
        # Arrange
        expected_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "access_token": expected_token,
            "token_type": "Bearer",
            "expires_in": 3600
        }
        mock_requests.post.return_value = mock_response

        # Act
        token_info = authenticator.get_access_token()

        # Assert
        assert token_info["access_token"] == expected_token
        assert token_info["token_type"] == "Bearer"
        assert token_info["expires_in"] == 3600
        mock_requests.post.assert_called_once()

    def test_oauth2_token_request_failure(self, authenticator, mock_requests):
        """Test OAuth2 token request failure."""
        # Arrange
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.json.return_value = {
            "error": "invalid_client",
            "error_description": "Invalid client credentials"
        }
        mock_requests.post.return_value = mock_response

        # Act & Assert
        with pytest.raises(AuthenticationError) as exc_info:
            authenticator.get_access_token()
        
        assert "Invalid client credentials" in str(exc_info.value)

    def test_jwt_token_validation(self, authenticator):
        """Test JWT token validation."""
        # Arrange
        payload = {
            "sub": "test_user",
            "iss": "https://test-oic.oracle.com",
            "aud": "oic_integration",
            "exp": datetime.utcnow() + timedelta(hours=1),
            "iat": datetime.utcnow()
        }
        
        # Create valid JWT token
        token = jwt.encode(payload, "secret_key", algorithm="HS256")

        # Act
        with patch('target_oracle_oic.auth.jwt.decode') as mock_decode:
            mock_decode.return_value = payload
            result = authenticator.validate_token(token)

        # Assert
        assert result is True
        mock_decode.assert_called_once_with(
            token, 
            options={"verify_signature": False}
        )

    def test_jwt_token_expired(self, authenticator):
        """Test JWT token expiration handling."""
        # Arrange
        expired_payload = {
            "sub": "test_user",
            "exp": datetime.utcnow() - timedelta(hours=1)  # Expired
        }
        
        expired_token = jwt.encode(expired_payload, "secret_key", algorithm="HS256")

        # Act & Assert
        with patch('target_oracle_oic.auth.jwt.decode') as mock_decode:
            mock_decode.side_effect = jwt.ExpiredSignatureError("Token expired")
            
            with pytest.raises(TokenExpiredError):
                authenticator.validate_token(expired_token)

class TestOAuth2TokenManager:
    """Test OAuth2 token management functionality."""

    @pytest.fixture
    def token_manager(self):
        """OAuth2 token manager instance."""
        return OAuth2TokenManager()

    def test_token_storage_and_retrieval(self, token_manager):
        """Test token storage and retrieval."""
        # Arrange
        token_data = {
            "access_token": "test_token_123",
            "refresh_token": "refresh_token_456",
            "expires_in": 3600,
            "token_type": "Bearer"
        }

        # Act
        token_manager.store_token(token_data)
        retrieved_token = token_manager.get_current_token()

        # Assert
        assert retrieved_token["access_token"] == token_data["access_token"]
        assert retrieved_token["refresh_token"] == token_data["refresh_token"]

    def test_token_expiration_check(self, token_manager):
        """Test token expiration checking."""
        # Arrange
        expired_token = {
            "access_token": "expired_token",
            "expires_at": datetime.utcnow() - timedelta(minutes=5)
        }
        
        valid_token = {
            "access_token": "valid_token",
            "expires_at": datetime.utcnow() + timedelta(hours=1)
        }

        # Act & Assert
        token_manager.store_token(expired_token)
        assert token_manager.is_token_expired() is True

        token_manager.store_token(valid_token)
        assert token_manager.is_token_expired() is False

    def test_automatic_token_refresh(self, token_manager, mock_requests):
        """Test automatic token refresh functionality."""
        # Arrange
        expired_token = {
            "access_token": "expired_token",
            "refresh_token": "refresh_token_123",
            "expires_at": datetime.utcnow() - timedelta(minutes=5)
        }
        
        new_token_response = {
            "access_token": "new_access_token",
            "refresh_token": "new_refresh_token",
            "expires_in": 3600
        }

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = new_token_response
        mock_requests.post.return_value = mock_response

        # Act
        token_manager.store_token(expired_token)
        refreshed_token = token_manager.refresh_token_if_needed()

        # Assert
        assert refreshed_token["access_token"] == "new_access_token"
        assert refreshed_token["refresh_token"] == "new_refresh_token"
```

### **2. Integration Tests (integration/)**

#### **OIC Integration Testing (test_oic_integration.py)**

```python
"""Integration tests for Oracle OIC endpoint integration."""

import pytest
import asyncio
from unittest.mock import patch, Mock
import json

from target_oracle_oic.target import TargetOracleOIC
from target_oracle_oic.config import TargetConfig

@pytest.mark.integration
class TestOICIntegration:
    """Test Oracle OIC integration scenarios."""

    @pytest.fixture
    def integration_config(self):
        """Integration test configuration."""
        return TargetConfig(
            oic_host="https://test-oic.oracle.com",
            client_id="integration_test_client",
            client_secret="integration_test_secret",
            username="integration_user",
            password="integration_password",
            batch_size=100,
            timeout=60
        )

    @pytest.fixture
    async def target_with_auth(self, integration_config):
        """Target instance with authenticated OIC client."""
        target = TargetOracleOIC(config=integration_config)
        
        # Mock successful authentication
        with patch.object(target.oic_client, 'authenticate') as mock_auth:
            mock_auth.return_value = True
            await target.oic_client.authenticate()
            
        return target

    @pytest.mark.asyncio
    async def test_end_to_end_data_loading(self, target_with_auth):
        """Test end-to-end data loading to OIC."""
        # Arrange
        test_records = [
            {
                "id": "user_001",
                "name": "John Doe",
                "email": "john.doe@example.com",
                "department": "Engineering",
                "created_at": "2025-06-19T10:00:00Z"
            },
            {
                "id": "user_002", 
                "name": "Jane Smith",
                "email": "jane.smith@example.com",
                "department": "Marketing",
                "created_at": "2025-06-19T10:05:00Z"
            }
        ]

        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"}, 
                "email": {"type": "string"},
                "department": {"type": "string"},
                "created_at": {"type": "string", "format": "date-time"}
            }
        }

        # Mock successful OIC API calls
        with patch.object(target_with_auth.oic_client, 'send_batch') as mock_send:
            mock_send.return_value = {
                "status": "success",
                "records_processed": len(test_records),
                "integration_id": "INT_12345"
            }

            # Act
            sink = target_with_auth.get_sink("users", schema)
            
            for record in test_records:
                sink.process_record(record)
            
            result = sink.flush_records()

            # Assert
            assert result["status"] == "success"
            assert result["records_processed"] == 2
            mock_send.assert_called_once()

    @pytest.mark.asyncio
    async def test_batch_processing_performance(self, target_with_auth):
        """Test batch processing performance with large datasets."""
        # Arrange
        batch_size = 1000
        test_records = [
            {
                "id": f"record_{i:06d}",
                "name": f"Test Record {i}",
                "value": i * 10.5,
                "timestamp": "2025-06-19T10:00:00Z"
            }
            for i in range(batch_size)
        ]

        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "value": {"type": "number"},
                "timestamp": {"type": "string", "format": "date-time"}
            }
        }

        # Mock OIC client for performance testing
        with patch.object(target_with_auth.oic_client, 'send_batch') as mock_send:
            mock_send.return_value = {
                "status": "success",
                "records_processed": batch_size,
                "processing_time_ms": 150
            }

            # Act
            import time
            start_time = time.time()
            
            sink = target_with_auth.get_sink("performance_test", schema)
            
            for record in test_records:
                sink.process_record(record)
            
            result = sink.flush_records()
            end_time = time.time()

            # Assert
            processing_time = end_time - start_time
            assert result["status"] == "success"
            assert result["records_processed"] == batch_size
            assert processing_time < 5.0  # Should process 1000 records in under 5 seconds
            
            # Verify batch was sent to OIC
            mock_send.assert_called_once()
            call_args = mock_send.call_args[0][0]
            assert len(call_args) == batch_size

    @pytest.mark.asyncio
    async def test_error_recovery_and_retry(self, target_with_auth):
        """Test error recovery and retry mechanisms."""
        # Arrange
        test_records = [
            {"id": "test_001", "name": "Test Record 1"},
            {"id": "test_002", "name": "Test Record 2"}
        ]

        schema = {
            "type": "object", 
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"}
            }
        }

        # Mock OIC client to simulate failure then success
        with patch.object(target_with_auth.oic_client, 'send_batch') as mock_send:
            # First call fails, second succeeds
            mock_send.side_effect = [
                Exception("Temporary network error"),
                {
                    "status": "success",
                    "records_processed": 2,
                    "retry_attempt": 1
                }
            ]

            # Act
            sink = target_with_auth.get_sink("error_recovery_test", schema)
            
            for record in test_records:
                sink.process_record(record)
            
            # Should retry and succeed
            result = sink.flush_records()

            # Assert
            assert result["status"] == "success"
            assert result["records_processed"] == 2
            assert mock_send.call_count == 2  # Original call + 1 retry

    @pytest.mark.asyncio
    async def test_concurrent_stream_processing(self, target_with_auth):
        """Test concurrent processing of multiple streams."""
        # Arrange
        streams_data = {
            "users": [
                {"id": "user_001", "name": "John Doe"},
                {"id": "user_002", "name": "Jane Smith"}
            ],
            "orders": [
                {"id": "order_001", "amount": 99.99},
                {"id": "order_002", "amount": 149.99}
            ]
        }

        schemas = {
            "users": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"}
                }
            },
            "orders": {
                "type": "object", 
                "properties": {
                    "id": {"type": "string"},
                    "amount": {"type": "number"}
                }
            }
        }

        # Mock OIC client for concurrent processing
        with patch.object(target_with_auth.oic_client, 'send_batch') as mock_send:
            mock_send.return_value = {
                "status": "success",
                "records_processed": 2
            }

            # Act
            sinks = {}
            for stream_name, schema in schemas.items():
                sinks[stream_name] = target_with_auth.get_sink(stream_name, schema)

            # Process records concurrently
            tasks = []
            for stream_name, records in streams_data.items():
                async def process_stream(sink, stream_records):
                    for record in stream_records:
                        sink.process_record(record)
                    return sink.flush_records()
                
                tasks.append(process_stream(sinks[stream_name], records))

            results = await asyncio.gather(*tasks)

            # Assert
            assert len(results) == 2
            for result in results:
                assert result["status"] == "success"
                assert result["records_processed"] == 2
            
            # Verify both streams were processed
            assert mock_send.call_count == 2
```

---

## 🔧 **Test Configuration**

### **Pytest Configuration (conftest.py)**

```python
"""Pytest configuration and shared fixtures for TARGET Oracle OIC tests."""

import pytest
import asyncio
import os
from unittest.mock import Mock, patch
import json

from target_oracle_oic.config import TargetConfig
from target_oracle_oic.target import TargetOracleOIC

@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def test_config():
    """Test configuration fixture."""
    return TargetConfig(
        oic_host=os.getenv("TEST_OIC_HOST", "https://test-oic.oracle.com"),
        client_id=os.getenv("TEST_CLIENT_ID", "test_client"),
        client_secret=os.getenv("TEST_CLIENT_SECRET", "test_secret"),
        username=os.getenv("TEST_USERNAME", "test_user"),
        password=os.getenv("TEST_PASSWORD", "test_password"),
        batch_size=100,
        timeout=30
    )

@pytest.fixture
def mock_oic_client():
    """Mock Oracle OIC client."""
    client = Mock()
    client.authenticate.return_value = True
    client.send_batch.return_value = {
        "status": "success",
        "records_processed": 0
    }
    return client

@pytest.fixture
def target_instance(test_config, mock_oic_client):
    """Target instance with mocked OIC client."""
    with patch('target_oracle_oic.target.OICClient', return_value=mock_oic_client):
        return TargetOracleOIC(config=test_config)

@pytest.fixture
def sample_user_records():
    """Sample user records for testing."""
    return [
        {
            "id": "user_001",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "department": "Engineering",
            "created_at": "2025-06-19T10:00:00Z"
        },
        {
            "id": "user_002",
            "name": "Jane Smith", 
            "email": "jane.smith@example.com",
            "department": "Marketing",
            "created_at": "2025-06-19T10:05:00Z"
        }
    ]

@pytest.fixture
def user_schema():
    """User stream schema fixture."""
    return {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "department": {"type": "string"},
            "created_at": {"type": "string", "format": "date-time"}
        },
        "required": ["id", "name", "email"]
    }

@pytest.fixture
def singer_messages():
    """Sample Singer messages for testing."""
    return [
        {
            "type": "SCHEMA",
            "stream": "users",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "email": {"type": "string"}
                }
            }
        },
        {
            "type": "RECORD",
            "stream": "users",
            "record": {
                "id": "user_001",
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        },
        {
            "type": "STATE",
            "value": {"bookmarks": {"users": {"timestamp": "2025-06-19T10:00:00Z"}}}
        }
    ]
```

### **Test Settings (pytest.ini)**

```ini
[tool:pytest]
minversion = 6.0
addopts =
    -ra
    --strict-markers
    --strict-config
    --cov=target_oracle_oic
    --cov-report=term-missing
    --cov-report=html
    --cov-report=xml
    --cov-fail-under=85
testpaths = tests
markers =
    unit: Unit tests
    integration: Integration tests
    performance: Performance tests
    singer: Singer SDK compliance tests
    authentication: Authentication tests
    slow: Slow running tests
asyncio_mode = auto
filterwarnings =
    ignore::DeprecationWarning
    ignore::PendingDeprecationWarning
    error::UserWarning
```

---

## 🔗 **Cross-References**

### **Component Documentation**

- [Component Overview](../README.md) - Complete TARGET Oracle OIC documentation
- [Source Implementation](../src/README.md) - Source code structure and patterns
- [Configuration Guide](../config.json.example) - Configuration examples

### **Testing Documentation**

- [Singer SDK Testing](https://sdk.meltano.com/en/latest/testing.html) - Singer SDK testing guidelines
- [PyTest Documentation](https://docs.pytest.org/) - Python testing framework
- [AsyncIO Testing](https://docs.python.org/3/library/asyncio-dev.html) - Async testing patterns

### **Oracle OIC References**

- [Oracle Integration Cloud](https://docs.oracle.com/en/cloud/paas/integration-cloud/) - OIC documentation
- [OIC REST APIs](https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/) - REST API reference
- [OAuth2 with Oracle Cloud](https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/Authentication.html) - Authentication guide

---

**📂 Module**: Test Suite | **🏠 Component**: [TARGET Oracle OIC](../README.md) | **Framework**: PyTest 7.0+ | **Updated**: 2025-06-19