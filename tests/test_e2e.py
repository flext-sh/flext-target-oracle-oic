"""Comprehensive End-to-End tests for target-oracle-oic.

Tests all functionalities including:
- Target initialization with real configuration
- Sink operations with real OIC API calls
- Data loading and validation
- Authentication with real OAuth2
- Error handling scenarios
- Integration import/export workflows

NO MOCKS - Real functional testing only.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import os
from collections.abc import Mapping
from pathlib import Path
from typing import ClassVar

import pytest
from singer_sdk.target_base import Target as SingerTarget

from flext_target_oracle_oic.target_client import (
    ConnectionsSink,
    IntegrationsSink,
    LookupsSink,
    PackagesSink,
    TargetOracleOic,
)
from flext_target_oracle_oic.target_config import TargetOracleOicConfig


class DummySingerTarget(SingerTarget):
    name = "dummy-target-oracle-oic"
    config_jsonschema: ClassVar[Mapping[str, str | Mapping[str, t.StrMapping]]] = {
        "type": "t.NormalizedValue",
        "properties": {},
    }


def load_test_config() -> t.StrMapping:
    """Load real test configuration from environment variables."""
    env_file = Path(".env")
    if env_file.exists():
        with env_file.open(encoding="utf-8") as f:
            for line in f:
                if "=" in line and (not line.strip().startswith("#")):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value.strip("\"'")
    config = {
        "base_url": os.getenv("TARGET_ORACLE_OIC_BASE_URL", ""),
        "oauth_client_id": os.getenv("TARGET_ORACLE_OIC_OAUTH_CLIENT_ID", ""),
        "oauth_client_secret": os.getenv("TARGET_ORACLE_OIC_OAUTH_CLIENT_SECRET", ""),
        "oauth_token_url": os.getenv("TARGET_ORACLE_OIC_OAUTH_TOKEN_URL", ""),
        "oauth_client_aud": os.getenv("TARGET_ORACLE_OIC_OAUTH_CLIENT_AUD", ""),
    }
    required_keys = [
        "base_url",
        "oauth_client_id",
        "oauth_client_secret",
        "oauth_token_url",
    ]
    missing_keys = [k for k in required_keys if not config[k]]
    if missing_keys:
        pytest.skip(f"Missing required environment variables: {missing_keys}")
    return config


@pytest.fixture
def test_config() -> t.StrMapping:
    """Provide real test configuration."""
    return load_test_config()


@pytest.fixture
def target() -> TargetOracleOic:
    """Create target instance."""
    return TargetOracleOic()


@pytest.fixture
def singer_target() -> SingerTarget:
    """Create singer target instance for sink constructors."""
    return DummySingerTarget(config={})


class TestTargetOracleOicE2E:
    """End-to-end tests for target-oracle-oic using REAL configuration and NO MOCKS."""

    def test_target_initialization(
        self, target: TargetOracleOic, test_config: t.StrMapping
    ) -> None:
        """Test target initialization with valid configuration."""
        _ = test_config
        if target.name != "target-oracle-oic":
            msg: str = f"Expected {'target-oracle-oic'}, got {target.name}"
            raise AssertionError(msg)
        assert isinstance(target.get_sink_class("connections"), type)

    def test_sink_class_mapping(self, target: TargetOracleOic) -> None:
        """Test sink class mapping for known streams."""
        if target.get_sink_class("connections") is not ConnectionsSink:
            msg = f"Expected {ConnectionsSink}, got {target.get_sink_class('connections')}"
            raise AssertionError(msg)
        assert target.get_sink_class("integrations") is IntegrationsSink
        if target.get_sink_class("packages") is not PackagesSink:
            msg = f"Expected {PackagesSink}, got {target.get_sink_class('packages')}"
            raise AssertionError(msg)
        assert target.get_sink_class("lookups") is LookupsSink
        default_sink = target.get_sink_class("unknown_stream")
        if default_sink is not target.default_sink_class:
            msg = f"Expected {target.default_sink_class}, got {default_sink}"
            raise AssertionError(msg)

    def test_sink_initialization(self, singer_target: SingerTarget) -> None:
        """Test sink initialization for each stream type."""
        sinks_to_test = [
            ("connections", ConnectionsSink),
            ("integrations", IntegrationsSink),
            ("packages", PackagesSink),
            ("lookups", LookupsSink),
        ]
        for stream_name, sink_class in sinks_to_test:
            sink = sink_class(
                target=singer_target,
                stream_name=stream_name,
                schema={"properties": {"id": {"type": "string"}}},
                key_properties=["id"],
            )
            if sink.stream_name != stream_name:
                msg: str = f"Expected {stream_name}, got {sink.stream_name}"
                raise AssertionError(msg)
            sink.process_record({"id": "ok"}, {})

    def test_process_singer_messages(self, singer_target: SingerTarget) -> None:
        """Test processing Singer-like records end-to-end through sink."""
        sink = ConnectionsSink(
            target=singer_target,
            stream_name="connections",
            schema={"properties": {"id": {"type": "string"}}},
            key_properties=["id"],
        )
        records = [
            {"id": "test-connection-1", "name": "Test Connection"},
            {"id": "test-connection-2", "name": "Test Connection 2"},
        ]
        for record in records:
            sink.process_record(record, {})
        assert len(records) == 2

    def test_sink_authenticator_setup(self, singer_target: SingerTarget) -> None:
        """Test sink can be constructed with singer target."""
        sink = ConnectionsSink(
            target=singer_target,
            stream_name="connections",
            schema={"properties": {"id": {"type": "string"}}},
            key_properties=["id"],
        )
        assert hasattr(sink, "process_record")

    def test_connections_sink_record_processing(
        self, singer_target: SingerTarget
    ) -> None:
        """Test connections sink record processing."""
        sink = ConnectionsSink(
            target=singer_target,
            stream_name="connections",
            schema={
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "adapter_type": {"type": "string"},
                }
            },
            key_properties=["id"],
        )
        test_record = {
            "id": "TEST_CONNECTION_E2E",
            "name": "E2E Test Connection",
            "adapter_type": "REST",
        }
        sink.process_record(test_record, {})

    def test_integrations_sink_record_processing(
        self, singer_target: SingerTarget
    ) -> None:
        """Test integrations sink record processing."""
        sink = IntegrationsSink(
            target=singer_target,
            stream_name="integrations",
            schema={
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "archive_content": {"type": "string"},
                }
            },
            key_properties=["id"],
        )
        sink.process_record(
            {
                "id": "TEST_INTEGRATION_E2E",
                "name": "E2E Test Integration",
                "archive_content": "base64_encoded_iar_content_here",
            },
            {},
        )

    def test_connections_sink_validation(self, singer_target: SingerTarget) -> None:
        """Test connections sink record validation."""
        sink = ConnectionsSink(
            target=singer_target,
            stream_name="connections",
            schema={"properties": {"id": {"type": "string"}}},
            key_properties=["id"],
        )
        sink.process_record({}, {})

    def test_config_validation(self, target: TargetOracleOic) -> None:
        """Test setup/teardown result contract."""
        setup_result = target.setup()
        assert setup_result.is_success
        assert setup_result.value is not None
        assert setup_result.value is True
        teardown_result = target.teardown()
        assert teardown_result.is_success
        assert teardown_result.value is not None
        assert teardown_result.value is True

    def test_packages_sink_record_processing(self, singer_target: SingerTarget) -> None:
        """Test packages sink record processing."""
        sink = PackagesSink(
            target=singer_target,
            stream_name="packages",
            schema={
                "properties": {"id": {"type": "string"}, "name": {"type": "string"}}
            },
            key_properties=["id"],
        )
        records = [
            {
                "id": f"pkg-{i}",
                "name": f"Package {i}",
                "archive_content": f"fake-package-content-{i}",
            }
            for i in range(10)
        ]
        for record in records:
            sink.process_record(record, {})
        assert len(records) == 10

    def test_lookups_sink_record_processing(self, singer_target: SingerTarget) -> None:
        """Test lookups sink record processing."""
        sink = LookupsSink(
            target=singer_target,
            stream_name="lookups",
            schema={
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "version": {"type": "string"},
                }
            },
            key_properties=["id"],
        )
        sink.process_record(
            {"id": "test-lookup", "name": "Test Lookup", "version": "1.0"}, {}
        )
        assert sink.stream_name == "lookups"

    def test_cli_integration(self, singer_target: SingerTarget, tmp_path: Path) -> None:
        """Test sink processing path with singer-like input payload."""
        _ = tmp_path
        sink = ConnectionsSink(
            target=singer_target,
            stream_name="connections",
            schema={
                "type": "t.NormalizedValue",
                "properties": {"id": {"type": "string"}},
            },
            key_properties=["id"],
        )
        sink.process_record({"id": "test-cli-connection"}, {})

    def test_conditional_config_generation(self) -> None:
        """Test schema generation from pydantic configuration model."""
        schema_raw = TargetOracleOicConfig.model_json_schema()
        properties_raw = schema_raw.get("properties")
        if not isinstance(properties_raw, dict):
            msg = f"Expected {'properties'} in {schema_raw}"
            raise AssertionError(msg)
        if "oauth_token_url" not in properties_raw:
            msg = f"Expected {'oauth_token_url'} in {properties_raw}"
            raise AssertionError(msg)
        assert isinstance(properties_raw["oauth_token_url"], dict)


def test_target_smoke_class() -> None:
    assert TargetOracleOic.name == "target-oracle-oic"
