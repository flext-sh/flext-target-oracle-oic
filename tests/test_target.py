"""Tests for target-oracle-oic with enterprise-grade validation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from src.flext_target_oracle_oic.target_client import (
    ConnectionsSink,
    IntegrationsSink,
    TargetOracleOic,
)
from src.flext_target_oracle_oic.target_config import OICOAuth2Authenticator
from src.flext_target_oracle_oic.target_config import TargetOracleOicConfig


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

    def test_target_initialization_with_minimal_config(self) -> None:
        """Test method."""
        target = TargetOracleOic(config={})
        if target.name != "target-oracle-oic":
            msg: str = f"Expected {'target-oracle-oic'}, got {target.name}"
            raise AssertionError(msg)

    def test_get_sink_mapping(self) -> None:
        """Test method."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        target = TargetOracleOic(config=config)

        if target.get_sink_class("connections") is not ConnectionsSink:
            msg: str = f"Expected {ConnectionsSink}, got {target.get_sink_class('connections')}"
            raise AssertionError(msg)
        assert target.get_sink_class("integrations") is IntegrationsSink

        if target.get_sink_class("unknown_stream") is not target.default_sink_class:
            msg = f"Expected {target.default_sink_class}, got {target.get_sink_class('unknown_stream')}"
            raise AssertionError(msg)

    def test_config_schema(self) -> None:
        """Test method."""
        schema = TargetOracleOic.config_jsonschema
        assert isinstance(schema, dict)
        if "properties" not in schema:
            msg = f"Expected {'properties'} in {schema}"
            raise AssertionError(msg)

        # Check required properties
        properties = schema["properties"]
        assert isinstance(properties, dict)
        assert isinstance(properties, dict)


def _build_auth_config(**overrides: object) -> TargetOracleOicConfig:
    config: dict[str, object] = {
        "oauth_client_id": "client-id",
        "oauth_client_secret": "client-secret",
        "oauth_token_url": "https://idcs.example.com/oauth2/v1/token",
        "oauth_scope": "urn:opc:resource:consumer:all",
        "oauth_client_aud": "https://idcs.example.com",
        "base_url": "https://instance.integration.ocp.oraclecloud.com",
    }
    config.update(overrides)
    return TargetOracleOicConfig.model_validate(config)


def test_oic_authenticator_builds_payload() -> None:
    authenticator = OICOAuth2Authenticator(_build_auth_config())

    payload = authenticator.build_token_request_data()

    assert payload["grant_type"] == "client_credentials"
    assert payload["client_id"] == "client-id"
    assert payload["client_secret"] == "client-secret"
    assert payload["scope"] == "urn:opc:resource:consumer:all"
    assert payload["audience"] == "https://idcs.example.com"


def test_oic_authenticator_omits_optional_scope_and_audience() -> None:
    authenticator = OICOAuth2Authenticator(
        _build_auth_config(oauth_scope="", oauth_client_aud=None),
    )

    payload = authenticator.build_token_request_data()

    assert "scope" not in payload
    assert "audience" not in payload


def test_oic_authenticator_rejects_invalid_token_response(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    authenticator = OICOAuth2Authenticator(_build_auth_config())

    class InvalidTokenResponse:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict[str, str]:
            return {"token_type": "Bearer"}

    def fake_post(*_: object, **__: object) -> InvalidTokenResponse:
        return InvalidTokenResponse()

    monkeypatch.setattr(f"{OICOAuth2Authenticator.__module__}.requests.post", fake_post)

    with pytest.raises(RuntimeError, match="access_token"):
        authenticator.get_access_token()
