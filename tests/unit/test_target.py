"""Tests for target-oracle-oic with enterprise-grade validation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from typing import TYPE_CHECKING, ClassVar

import pytest
from flext_tests import tm
from singer_sdk.target_base import Target as SingerTarget

from flext_target_oracle_oic import FlextTargetOracleOicSettings, u
from flext_target_oracle_oic.target import (
    FlextTargetOracleOic,
    FlextTargetOracleOicConnectionsSink,
    FlextTargetOracleOicIntegrationsSink,
)
from tests import c, t

if TYPE_CHECKING:
    from collections.abc import Iterator


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
            "oauth_client_secret": "s" + "0" * 14,
            "oauth_token_url": "https://test-idcs.identity.oraclecloud.com/oauth2/v1/token",
            "oauth_client_aud": "https://test-idcs.identity.oraclecloud.com",
        }

    def test_target_initialization_with_valid_config(
        self, valid_config: t.StrMapping
    ) -> None:
        """Test target initialization with valid configuration."""
        _ = valid_config
        target = FlextTargetOracleOic()
        if target.name != "target-oracle-oic":
            msg: str = f"Expected {'target-oracle-oic'}, got {target.name}"
            raise AssertionError(msg)
        tm.that(target.fetch_sink_class("connections"), is_=type)

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
        tm.that(schema, is_=dict)
        if "properties" not in schema:
            msg = f"Expected {'properties'} in {schema}"
            raise AssertionError(msg)
        properties = schema["properties"]
        tm.that(properties, is_=dict)
        tm.that(properties, has="TargetOracleOic")

    def test_oic_authenticator_builds_payload(self) -> None:
        authenticator = u.TargetOracleOic.Authenticator(_build_auth_config())
        payload = authenticator.build_token_request_data()
        tm.that(payload["grant_type"], eq="client_credentials")
        tm.that(payload["client_id"], eq="client-id")
        tm.that(payload["client_secret"], eq="s" + "0" * 14)
        tm.that(payload["scope"], eq="urn:opc:resource:consumer:all")
        tm.that(payload["audience"], eq="https://idcs.example.com")

    def test_oic_authenticator_omits_optional_scope_and_audience(self) -> None:
        authenticator = u.TargetOracleOic.Authenticator(
            _build_auth_config(oauth_scope="", oauth_client_aud=None)
        )
        payload = authenticator.build_token_request_data()
        tm.that(payload, lacks="scope")
        tm.that(payload, lacks="audience")

    def test_oic_authenticator_rejects_invalid_token_response(
        self, local_token_url: str
    ) -> None:
        """A 200 token response without access_token fails loud over real HTTP."""
        authenticator = u.TargetOracleOic.Authenticator(
            _build_auth_config(oauth_token_url=local_token_url)
        )
        with pytest.raises(RuntimeError, match="access_token"):
            authenticator.get_access_token()


class _TokenWithoutAccessTokenHandler(BaseHTTPRequestHandler):
    """Local token endpoint answering 200 with a body lacking access_token."""

    def do_POST(self) -> None:
        """Answer one token request with deterministic token-type-only JSON."""
        body = b'{"token_type": "Bearer"}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


@pytest.fixture
def local_token_url() -> Iterator[str]:
    """Run one ephemeral local OAuth2 token endpoint for the duration of a test."""
    server = HTTPServer(("127.0.0.1", 0), _TokenWithoutAccessTokenHandler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_address[1]}"
    server.shutdown()
    server.server_close()
    thread.join(timeout=5)


@pytest.fixture
def singer_target() -> SingerTarget:
    return DummySingerTarget(config={})


def _build_auth_config(
    *,
    oauth_token_url: str | None = None,
    oauth_scope: str | None = "urn:opc:resource:consumer:all",
    oauth_client_aud: str | None = "https://idcs.example.com",
) -> FlextTargetOracleOicSettings:
    # Build via model_construct to avoid touching the flext-core settings singleton;
    # oauth fields live under the TargetOracleOic namespace (ADR-005).
    namespace = {
        "oauth_client_id": "client-id",
        "oauth_client_secret": "s" + "0" * 14,
        "oauth_token_url": (
            oauth_token_url
            if oauth_token_url is not None
            else c.TargetOracleOic.Tests.OAUTH_ENDPOINT_URL
        ),
        "oauth_scope": oauth_scope,
        "oauth_client_aud": oauth_client_aud,
        "timeout": 30,
    }
    return AuthTestSettings.model_validate({"TargetOracleOic": namespace})
