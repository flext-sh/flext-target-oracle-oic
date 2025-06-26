"""Tests for target-oracle-oic with enterprise-grade validation."""

from __future__ import annotations

import pytest

from target_oracle_oic.sinks import ConnectionsSink, IntegrationsSink
from target_oracle_oic.target import TargetOracleOIC


class TestTargetOracleOIC:
    """Test cases for TargetOracleOIC with proper enterprise validation."""

    @pytest.fixture
    def valid_config(self) -> dict[str, str]:
        """Provide a valid configuration for testing."""
        return {
            "base_url": "https://test-instance-region.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id_12345",
            "oauth_client_secret": "test_secret_67890",
            "oauth_token_url": "https://test-idcs.identity.oraclecloud.com/oauth2/v1/token",
            "oauth_client_aud": "https://test-idcs.identity.oraclecloud.com",
        }

    def test_target_initialization_with_valid_config(
        self, valid_config: dict[str, str],
    ) -> None:
        """Test target can be initialized with proper enterprise config."""
        target = TargetOracleOIC(config=valid_config)
        assert target.name == "target-oracle-oic"
        assert target.config == valid_config

    def test_target_initialization_fails_with_invalid_config(self) -> None:
        """Test target initialization fails with missing required config."""
        invalid_config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            # Missing required OAuth2 credentials
        }
        with pytest.raises((KeyError, ValueError)):
            TargetOracleOIC(config=invalid_config)

    def test_get_sink_mapping(self) -> None:
        """Test sink mapping for different streams."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        target = TargetOracleOIC(config=config)

        # Test known streams
        assert target._get_sink_class("connections") == ConnectionsSink
        assert target._get_sink_class("integrations") == IntegrationsSink

        # Test unknown stream returns default
        assert target._get_sink_class("unknown_stream") == target.default_sink_class

    def test_config_schema(self) -> None:
        """Test configuration schema is valid."""
        schema = TargetOracleOIC.config_jsonschema
        assert isinstance(schema, dict)
        assert "properties" in schema

        # Check required properties
        properties = schema["properties"]
        assert "base_url" in properties
        assert "oauth_client_id" in properties
        assert "oauth_client_secret" in properties
        assert "oauth_token_url" in properties

        # Check target-specific properties
        assert "import_mode" in properties
        assert "activate_integrations" in properties
