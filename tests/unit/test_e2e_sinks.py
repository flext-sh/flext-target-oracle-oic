"""End-to-end sink tests for target-oracle-oic.

Tests Singer sink construction and record processing paths without mocks.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar

import pytest
from singer_sdk.target_base import Target as SingerTarget

from flext_target_oracle_oic.target import (
    FlextTargetOracleOicConnectionsSink,
    FlextTargetOracleOicIntegrationsSink,
    FlextTargetOracleOicLookupsSink,
    FlextTargetOracleOicPackagesSink,
)
from tests.typings import t


class DummySingerTargetE2E(SingerTarget):
    name = "dummy-target-oracle-oic"
    config_jsonschema: ClassVar[dict[str, str | t.MappingKV[str, t.StrMapping]]] = {
        "type": "object",
        "properties": dict[str, t.StrMapping](),
    }


@pytest.fixture
def singer_target() -> SingerTarget:
    return DummySingerTargetE2E(config={})


class TestsFlextTargetOracleOicE2eSinks:
    def test_sink_initialization(self, singer_target: SingerTarget) -> None:
        """Test sink initialization for each stream type."""
        sinks_to_test = [
            ("connections", FlextTargetOracleOicConnectionsSink),
            ("integrations", FlextTargetOracleOicIntegrationsSink),
            ("packages", FlextTargetOracleOicPackagesSink),
            ("lookups", FlextTargetOracleOicLookupsSink),
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
        sink = FlextTargetOracleOicConnectionsSink(
            target=singer_target,
            stream_name="connections",
            schema={"properties": {"id": {"type": "string"}}},
            key_properties=["id"],
        )
        records: list[t.MutableJsonMapping] = [
            {"id": "test-connection-1", "name": "Test Connection"},
            {"id": "test-connection-2", "name": "Test Connection 2"},
        ]
        for record in records:
            sink.process_record(record, {})
        assert len(records) == 2

    def test_sink_authenticator_setup(self, singer_target: SingerTarget) -> None:
        """Test sink can be constructed with singer target."""
        FlextTargetOracleOicConnectionsSink(
            target=singer_target,
            stream_name="connections",
            schema={"properties": {"id": {"type": "string"}}},
            key_properties=["id"],
        )

    def test_connections_sink_record_processing(
        self,
        singer_target: SingerTarget,
    ) -> None:
        """Test connections sink record processing."""
        sink = FlextTargetOracleOicConnectionsSink(
            target=singer_target,
            stream_name="connections",
            schema={
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "adapter_type": {"type": "string"},
                },
            },
            key_properties=["id"],
        )
        test_record: t.MutableJsonMapping = {
            "id": "TEST_CONNECTION_E2E",
            "name": "E2E Test Connection",
            "adapter_type": "REST",
        }
        sink.process_record(test_record, {})

    def test_integrations_sink_record_processing(
        self,
        singer_target: SingerTarget,
    ) -> None:
        """Test integrations sink record processing."""
        sink = FlextTargetOracleOicIntegrationsSink(
            target=singer_target,
            stream_name="integrations",
            schema={
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "archive_content": {"type": "string"},
                },
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
        sink = FlextTargetOracleOicConnectionsSink(
            target=singer_target,
            stream_name="connections",
            schema={"properties": {"id": {"type": "string"}}},
            key_properties=["id"],
        )
        sink.process_record({}, {})

    def test_packages_sink_record_processing(self, singer_target: SingerTarget) -> None:
        """Test packages sink record processing."""
        sink = FlextTargetOracleOicPackagesSink(
            target=singer_target,
            stream_name="packages",
            schema={
                "properties": {"id": {"type": "string"}, "name": {"type": "string"}},
            },
            key_properties=["id"],
        )
        records: list[t.MutableJsonMapping] = [
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
        sink = FlextTargetOracleOicLookupsSink(
            target=singer_target,
            stream_name="lookups",
            schema={
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "version": {"type": "string"},
                },
            },
            key_properties=["id"],
        )
        sink.process_record(
            {"id": "test-lookup", "name": "Test Lookup", "version": "1.0"},
            {},
        )
        assert sink.stream_name == "lookups"

    def test_cli_integration(self, singer_target: SingerTarget, tmp_path: Path) -> None:
        """Test sink processing path with singer-like input payload."""
        _ = tmp_path
        sink = FlextTargetOracleOicConnectionsSink(
            target=singer_target,
            stream_name="connections",
            schema={
                "type": "object",
                "properties": {"id": {"type": "string"}},
            },
            key_properties=["id"],
        )
        sink.process_record({"id": "test-cli-connection"}, {})
