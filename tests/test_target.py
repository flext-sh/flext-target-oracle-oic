"""Tests for target-oracle-oic with enterprise-grade validation."""

from __future__ import annotations

import pytest
# MIGRATED: from singer_sdk.exceptions import ConfigValidationError -> use flext_meltano
from flext_meltano import ConfigValidationError

from flext_target_oracle_oic.sinks import ConnectionsSink, IntegrationsSink
from flext_target_oracle_oic.target import TargetOracleOIC


class TestTargetOracleOIC:
    """Test cases for TargetOracleOIC with proper enterprise validation."""

    @pytest.fixture
    def valid_config(self) -> dict[str, str]:
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
        target = TargetOracleOIC(config=valid_config)
        if target.name != "target-oracle-oic":
            raise AssertionError(f"Expected {"target-oracle-oic"}, got {target.name}")
        assert target.config == valid_config

    def test_target_initialization_fails_with_invalid_config(self) -> None:
        invalid_config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            # Missing required OAuth2 credentials
        }
        with pytest.raises(ConfigValidationError):
            TargetOracleOIC(config=invalid_config)

    def test_get_sink_mapping(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        target = TargetOracleOIC(config=config)

        # Test known streams
        if target._get_sink_class("connections") != ConnectionsSink:
            raise AssertionError(f"Expected {ConnectionsSink}, got {target._get_sink_class("connections")}")
        assert target._get_sink_class("integrations") == IntegrationsSink

        # Test unknown stream returns default
        if target._get_sink_class("unknown_stream") != target.default_sink_class:
            raise AssertionError(f"Expected {target.default_sink_class}, got {target._get_sink_class("unknown_stream")}")

    def test_config_schema(self) -> None:
        schema = TargetOracleOIC.config_jsonschema
        assert isinstance(schema, dict)
        if "properties" not in schema:
            raise AssertionError(f"Expected {"properties"} in {schema}")

        # Check required properties
        properties = schema["properties"]
        assert isinstance(properties, dict)
        if "base_url" not in properties:
            raise AssertionError(f"Expected {"base_url"} in {properties}")
        assert "oauth_client_id" in properties
        if "oauth_client_secret" not in properties:
            raise AssertionError(f"Expected {"oauth_client_secret"} in {properties}")
        assert "oauth_token_url" in properties

        # Check target-specific properties
        if "import_mode" not in properties:
            raise AssertionError(f"Expected {"import_mode"} in {properties}")
        assert "activate_integrations" in properties
