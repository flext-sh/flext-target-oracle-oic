"""Tests for target-oracle-oic with enterprise-grade validation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping
from typing import ClassVar

import pytest
from pydantic import SecretStr
from singer_sdk.target_base import Target as SingerTarget

from flext_target_oracle_oic.target_client import (
    FlextTargetOracleOic,
    FlextTargetOracleOicConnectionsSink,
    FlextTargetOracleOicIntegrationsSink,
)
from flext_target_oracle_oic.target_config import (
    FlextTargetOracleOicAuthenticator,
    FlextTargetOracleOicConfig,
)
from tests import t

_DEFAULT_PROPERTIES: Mapping[str, t.StrMapping] = {"id": {"type": "string"}}


class AuthTestConfig(FlextTargetOracleOicConfig):
    pass


class DummySingerTarget(SingerTarget):
    """Minimal Singer target implementation for sink tests."""

    name = "dummy-target-oracle-oic"
    config_jsonschema: ClassVar[Mapping[str, str | Mapping[str, t.StrMapping]]] = {
        "type": "t.NormalizedValue",
        "properties": _DEFAULT_PROPERTIES,
    }


class TestTargetOracleOic:
    """Test cases for FlextTargetOracleOic with proper enterprise validation."""

    @pytest.fixture
    def valid_config(self) -> t.StrMapping:
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
        valid_config: t.StrMapping,
    ) -> None:
        """Test target initialization with valid configuration."""
        _ = valid_config
        target = FlextTargetOracleOic()
        if target.name != "target-oracle-oic":
            msg: str = f"Expected {'target-oracle-oic'}, got {target.name}"
            raise AssertionError(msg)
        assert isinstance(target.get_sink_class("connections"), type)

    def test_target_initialization_with_minimal_config(self) -> None:
        """Test method."""
        target = FlextTargetOracleOic()
        if target.name != "target-oracle-oic":
            msg: str = f"Expected {'target-oracle-oic'}, got {target.name}"
            raise AssertionError(msg)

    def test_get_sink_mapping(self) -> None:
        """Test method."""
        target = FlextTargetOracleOic()
        if (
            target.get_sink_class("connections")
            is not FlextTargetOracleOicConnectionsSink
        ):
            msg: str = f"Expected {FlextTargetOracleOicConnectionsSink}, got {target.get_sink_class('connections')}"
            raise AssertionError(msg)
        assert (
            target.get_sink_class("integrations")
            is FlextTargetOracleOicIntegrationsSink
        )
        if target.get_sink_class("unknown_stream") is not target.default_sink_class:
            msg = f"Expected {target.default_sink_class}, got {target.get_sink_class('unknown_stream')}"
            raise AssertionError(msg)

    def test_config_schema(self) -> None:
        """Test method."""
        schema = FlextTargetOracleOicConfig.model_json_schema()
        assert isinstance(schema, dict)
        if "properties" not in schema:
            msg = f"Expected {'properties'} in {schema}"
            raise AssertionError(msg)
        properties = schema["properties"]
        assert isinstance(properties, dict)
        assert "oauth_client_id" in properties


@pytest.fixture
def singer_target() -> SingerTarget:
    """Provide a Singer target accepted by singer-sdk Sink constructors."""
    return DummySingerTarget(config={})


def _build_auth_config(
    *,
    oauth_scope: str | None = "urn:opc:resource:consumer:all",
    oauth_client_aud: str | None = "https://idcs.example.com",
) -> FlextTargetOracleOicConfig:
    config = AuthTestConfig.__new__(AuthTestConfig)
    object.__setattr__(config, "oauth_client_id", "client-id")
    object.__setattr__(config, "oauth_client_secret", SecretStr("client-secret"))
    object.__setattr__(
        config,
        "oauth_token_url",
        "https://idcs.example.com/oauth2/v1/token",
    )
    object.__setattr__(config, "oauth_scope", oauth_scope)
    object.__setattr__(config, "oauth_client_aud", oauth_client_aud)
    object.__setattr__(config, "timeout", 30)
    return config


def test_oic_authenticator_builds_payload() -> None:
    authenticator = FlextTargetOracleOicAuthenticator(_build_auth_config())
    payload = authenticator.build_token_request_data()
    assert payload["grant_type"] == "client_credentials"
    assert payload["client_id"] == "client-id"
    assert payload["client_secret"] == "client-secret"
    assert payload["scope"] == "urn:opc:resource:consumer:all"
    assert payload["audience"] == "https://idcs.example.com"


def test_oic_authenticator_omits_optional_scope_and_audience() -> None:
    authenticator = FlextTargetOracleOicAuthenticator(
        _build_auth_config(oauth_scope="", oauth_client_aud=None),
    )
    payload = authenticator.build_token_request_data()
    assert "scope" not in payload
    assert "audience" not in payload


def test_oic_authenticator_rejects_invalid_token_response(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    authenticator = FlextTargetOracleOicAuthenticator(_build_auth_config())

    class InvalidTokenResponse:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> t.StrMapping:
            return {"token_type": "Bearer"}

    def fake_post(*_args: t.Scalar, **_kwargs: t.Scalar) -> InvalidTokenResponse:
        return InvalidTokenResponse()

    monkeypatch.setattr(
        f"{FlextTargetOracleOicAuthenticator.__module__}.requests.post",
        fake_post,
    )
    with pytest.raises(RuntimeError, match="access_token"):
        authenticator.get_access_token()
