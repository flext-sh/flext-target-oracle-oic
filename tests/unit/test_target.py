"""Tests for target-oracle-oic with enterprise-grade validation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import ClassVar
from unittest.mock import Mock, patch

import pytest
from flext_tests import r as result_type
from singer_sdk.target_base import Target as SingerTarget

from flext_target_oracle_oic import FlextTargetOracleOicSettings, u
from flext_target_oracle_oic.target import (
    FlextTargetOracleOic,
    FlextTargetOracleOicConnectionsSink,
    FlextTargetOracleOicIntegrationsSink,
)
from tests.constants import c
from tests.typings import t


class AuthTestSettings(FlextTargetOracleOicSettings):
    pass


class DummySingerTarget(SingerTarget):
    """Minimal Singer target implementation for sink tests."""

    name = "dummy-target-oracle-oic"
    config_jsonschema: ClassVar[dict[str, str | t.MappingKV[str, t.StrMapping]]] = {
        "type": "object",
        "properties": c.TargetOracleOic.Tests.DEFAULT_PROPERTIES,
    }


class TestsFlextTargetOracleOicTarget:
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
        assert isinstance(target.fetch_sink_class("connections"), type)

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
            target.fetch_sink_class("connections")
            is not FlextTargetOracleOicConnectionsSink
        ):
            msg: str = f"Expected {FlextTargetOracleOicConnectionsSink}, got {target.fetch_sink_class('connections')}"
            raise AssertionError(msg)
        assert (
            target.fetch_sink_class("integrations")
            is FlextTargetOracleOicIntegrationsSink
        )
        if target.fetch_sink_class("unknown_stream") is not target.default_sink_class:
            msg = f"Expected {target.default_sink_class}, got {target.fetch_sink_class('unknown_stream')}"
            raise AssertionError(msg)

    def test_config_schema(self) -> None:
        """Test method."""
        schema = FlextTargetOracleOicSettings.model_json_schema()
        assert isinstance(schema, dict)
        if "properties" not in schema:
            msg = f"Expected {'properties'} in {schema}"
            raise AssertionError(msg)
        properties = schema["properties"]
        assert isinstance(properties, dict)
        assert "TargetOracleOic" in properties

    def test_oic_authenticator_builds_payload(self) -> None:
        authenticator = u.TargetOracleOic.Authenticator(_build_auth_config())
        payload = authenticator.build_token_request_data()
        assert payload["grant_type"] == "client_credentials"
        assert payload["client_id"] == "client-id"
        assert payload["client_secret"] == "client-secret"
        assert payload["scope"] == "urn:opc:resource:consumer:all"
        assert payload["audience"] == "https://idcs.example.com"

    def test_oic_authenticator_omits_optional_scope_and_audience(self) -> None:
        authenticator = u.TargetOracleOic.Authenticator(
            _build_auth_config(oauth_scope="", oauth_client_aud=None),
        )
        payload = authenticator.build_token_request_data()
        assert "scope" not in payload
        assert "audience" not in payload

    def test_oic_authenticator_rejects_invalid_token_response(self) -> None:

        authenticator = u.TargetOracleOic.Authenticator(_build_auth_config())

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.body = {"token_type": "Bearer"}

        with patch(
            "flext_api.FlextApi.post",
            return_value=result_type[Mock].ok(mock_response),
        ):
            with pytest.raises(RuntimeError, match="access_token"):
                authenticator.get_access_token()


@pytest.fixture
def singer_target() -> SingerTarget:
    return DummySingerTarget(config={})


def _build_auth_config(
    *,
    oauth_scope: str | None = "urn:opc:resource:consumer:all",
    oauth_client_aud: str | None = "https://idcs.example.com",
) -> FlextTargetOracleOicSettings:
    # Build via __new__ to avoid touching the flext-core settings singleton;
    # oauth fields live under the TargetOracleOic namespace (ADR-005).
    settings = AuthTestSettings.__new__(AuthTestSettings)
    namespace = FlextTargetOracleOicSettings._TargetOracleOic.model_validate({
        "oauth_client_id": "client-id",
        "oauth_client_secret": "client-secret",
        "oauth_token_url": "https://idcs.example.com/oauth2/v1/token",
        "oauth_scope": oauth_scope,
        "oauth_client_aud": oauth_client_aud,
        "timeout": 30,
    })
    object.__setattr__(settings, "TargetOracleOic", namespace)
    return settings
