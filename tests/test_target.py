"""Tests for target-oracle-oic with enterprise-grade validation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from flext_meltano import ConfigValidationError

from flext_target_oracle_oic import ConnectionsSink, IntegrationsSink, TargetOracleOic


class TestTargetOracleOic:
    """Test cases for TargetOracleOic with proper enterprise validation."""

    @pytest.fixture
    def valid_config(self) -> dict[str, str]:
        """Create valid configuration for testing."""
        return {
            "base_url": "https://test-instance-region.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id_12345",
            "oauth_client_secret": "test_secret_67890",
            "oauth_token_url": "https://test-idcs.identity.oraclecloud.com/oauth2/v1/token",
            "oauth_client_aud": "https://test-idcs.identity.oraclecloud.com",
        }

    def test_target_initialization_with_valid_config(
        self,
        valid_config: dict[str, str],
    ) -> None:
        """Test target initialization with valid configuration."""
        target = TargetOracleOic(config=valid_config)
        if target.name != "target-oracle-oic":
            msg: str = f"Expected {'target-oracle-oic'}, got {target.name}"
            raise AssertionError(msg)
        assert target.config == valid_config

    def test_target_initialization_fails_with_invalid_config(self) -> None:
        """Test method."""
        invalid_config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            # Missing required OAuth2 credentials
        }
        with pytest.raises(ConfigValidationError):
            TargetOracleOic(config=invalid_config)

    def test_get_sink_mapping(self) -> None:
        """Test method."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        target = TargetOracleOic(config=config)

        # Test known streams
        if target._get_sink_class("connections") != ConnectionsSink:
            msg: str = f"Expected {ConnectionsSink}, got {target._get_sink_class('connections')}"
            raise AssertionError(msg)
        assert target._get_sink_class("integrations") == IntegrationsSink

        # Test unknown stream returns default
        if target._get_sink_class("unknown_stream") != target.default_sink_class:
            msg: str = f"Expected {target.default_sink_class}, got {target._get_sink_class('unknown_stream')}"
            raise AssertionError(msg)

    def test_config_schema(self) -> None:
        """Test method."""
        schema = TargetOracleOic.config_jsonschema
        assert isinstance(schema, dict)
        if "properties" not in schema:
            msg: str = f"Expected {'properties'} in {schema}"
            raise AssertionError(msg)

        # Check required properties
        properties = schema["properties"]
        assert isinstance(properties, dict)
        if "base_url" not in properties:
            msg: str = f"Expected {'base_url'} in {properties}"
            raise AssertionError(msg)
        assert "oauth_client_id" in properties
        if "oauth_client_secret" not in properties:
            msg: str = f"Expected {'oauth_client_secret'} in {properties}"
            raise AssertionError(msg)
        assert "oauth_token_url" in properties

        # Check target-specific properties
        if "import_mode" not in properties:
            msg: str = f"Expected {'import_mode'} in {properties}"
            raise AssertionError(msg)
        assert "activate_integrations" in properties
