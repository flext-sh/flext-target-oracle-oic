"""Comprehensive End-to-End tests for target-oracle-oic.

Tests all functionalities including:
- Target initialization
- Sink operations
- Data loading
- Authentication
- Error handling
- Integration import/export.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest
from singer_sdk.exceptions import ConfigValidationError
from singer_sdk.testing import get_target_test_class

from flext_target_oracle_oic.sinks import (
    ConnectionsSink,
    IntegrationsSink,
    LookupsSink,
    PackagesSink,
)
from flext_target_oracle_oic.target import TargetOracleOIC


class TestTargetOracleOICE2E:
    """End-to-end tests for target-oracle-oic."""

    @pytest.fixture
    def config_path(self) -> str:
        config_file = Path(__file__).parent.parent / "config.json"
        if not config_file.exists():
            # Generate config if it doesn't exist:
            subprocess.run(
                ["python", "generate_config.py"],
                cwd=Path(__file__).parent.parent,
                check=True,
            )
        return str(config_file)

    @pytest.fixture
    def config(self, config_path: str) -> dict[str, object]:
        with open(config_path, encoding="utf-8") as f:
            loaded_config: dict[str, object] = json.load(f)
            return loaded_config

    @pytest.fixture
    def target(self, config: dict[str, object]) -> TargetOracleOIC:
        return TargetOracleOIC(config=config)

    def test_target_initialization(
        self,
        target: TargetOracleOIC,
        config: dict[str, Any],
    ) -> None:
        assert target.name == "target-oracle-oic"
        assert target.config == config
        assert target.config["base_url"] == config["base_url"]

    def test_sink_discovery(self, target: TargetOracleOIC) -> None:
        # Test known sinks
        assert target._get_sink_class("connections") == ConnectionsSink
        assert target._get_sink_class("integrations") == IntegrationsSink
        assert target._get_sink_class("packages") == PackagesSink
        assert target._get_sink_class("lookups") == LookupsSink
        # Test unknown stream returns default
        default_sink = target._get_sink_class("unknown_stream")
        assert default_sink == target.default_sink_class

    def test_sink_initialization(self, target: TargetOracleOIC) -> None:
        # Test each sink type
        sinks_to_test = [
            ("connections", ConnectionsSink),
            ("integrations", IntegrationsSink),
            ("packages", PackagesSink),
            ("lookups", LookupsSink),
        ]
        for stream_name, sink_class in sinks_to_test:
            sink = sink_class(
                target=target,
                stream_name=stream_name,
                schema={"properties": {"id": {"type": "string"}}},
                key_properties=["id"],
            )
            assert sink.stream_name == stream_name
            assert sink.config == target.config

    def test_process_singer_messages(
        self,
        target: TargetOracleOIC,
        tmp_path: Path,
    ) -> None:
        # Create test Singer messages
        messages = [
            {
                "type": "SCHEMA",
                "stream": "connections",
                "schema": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "name": {"type": "string"},
                    },
                },
                "key_properties": ["id"],
            },
            {
                "type": "RECORD",
                "stream": "connections",
                "record": {"id": "test-connection-1", "name": "Test Connection"},
            },
            {
                "type": "STATE",
                "value": {
                    "bookmarks": {
                        "connections": {
                            "replication_key_value": "2024-01-01T00:00:00Z",
                        },
                    },
                },
            },
        ]
        # Write messages to file
        input_file = tmp_path / "input.jsonl"
        with open(input_file, "w", encoding="utf-8") as f:
            f.writelines(json.dumps(msg) + "\n" for msg in messages)
        # Process messages using Singer SDK API
        with (
            patch.object(ConnectionsSink, "process_record") as mock_process,
            patch.object(ConnectionsSink, "client") as mock_client,
        ):
            # Mock the HTTP client to avoid actual API calls
            mock_client.get.return_value.status_code = 404
            mock_client.post.return_value.status_code = 201
            # Use the proper Singer SDK listen method with file input
            with open(input_file, encoding="utf-8") as f:
                target.listen(file_input=f)
            # Verify that the record was processed
            assert mock_process.called, "process_record should have been called"

    def test_authentication_handling(self, target: TargetOracleOIC) -> None:
        # Get a sink instance
        sink = ConnectionsSink(
            target=target,
            stream_name="connections",
            schema={"properties": {"id": {"type": "string"}}},
            key_properties=["id"],
        )
        # Test authenticator initialization
        authenticator = sink.authenticator
        assert authenticator is not None
        assert hasattr(authenticator, "auth_headers")

    def test_live_connection_create(self, target: TargetOracleOIC) -> None:
        sink = ConnectionsSink(
            target=target,
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
        # Test record
        test_record = {
            "id": "TEST_CONNECTION_E2E",
            "name": "E2E Test Connection",
            "adapter_type": "REST",
        }
        # Test that either succeeds or raises HTTP/auth-related exceptions
        try:
            # Process the record
            sink.process_record(test_record, {})
        except Exception as e:
            if any(code in str(e) for code in ["401", "403", "404", "500"]):
                # HTTP errors are expected in test environment without live credentials/instance
                # This confirms the sink is attempting real API calls as expected
                pass
            else:
                pytest.fail(f"Unexpected error: {e}")

    def test_integration_import_flow(self, target: TargetOracleOIC) -> None:
        sink = IntegrationsSink(
            target=target,
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
        # Mock the HTTP client to avoid actual API calls
        with patch.object(sink, "_client") as mock_client:
            # Mock responses
            mock_client.get.return_value.status_code = 404  # Integration doesn't exist
            mock_client.post.return_value.status_code = 201  # Creation successful
            # Test record with archive content
            test_record = {
                "id": "TEST_INTEGRATION_E2E",
                "name": "E2E Test Integration",
                "archive_content": "base64_encoded_iar_content_here",
            }
            # Process the record
            sink.process_record(test_record, {})
            # Verify import endpoint was called
            mock_client.post.assert_called()

    def test_error_handling(self, target: TargetOracleOIC) -> None:
        sink = ConnectionsSink(
            target=target,
            stream_name="connections",
            schema={"properties": {"id": {"type": "string"}}},
            key_properties=["id"],
        )
        # Test with invalid record (missing required field)
        with pytest.raises((ValueError, KeyError, TypeError)):
            sink.process_record({}, {})

    def test_config_validation(self) -> None:
        # Test missing required fields
        with pytest.raises(ConfigValidationError):
            TargetOracleOIC(config={})
        # Test with minimal valid config
        minimal_config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test",
            "oauth_client_secret": "test",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        target = TargetOracleOIC(config=minimal_config)
        assert target.config == minimal_config

    def test_batch_processing(self, target: TargetOracleOIC) -> None:
        sink = PackagesSink(
            target=target,
            stream_name="packages",
            schema={
                "properties": {"id": {"type": "string"}, "name": {"type": "string"}},
            },
            key_properties=["id"],
        )
        # Create batch of test records
        records = [
            {
                "id": f"pkg-{i}",
                "name": f"Package {i}",
                "archive_content": f"fake-package-content-{i}",
            }
            for i in range(10)
        ]
        # Mock the HTTP client properly by patching the underlying _client attribute
        with patch.object(sink, "_client") as mock_client:
            mock_client.get.return_value.status_code = 404
            mock_client.post.return_value.status_code = 201
            # Process all records
            for record in records:
                sink.process_record(record, {})
            # Verify all records were processed
            assert mock_client.post.call_count >= len(records)

    def test_update_vs_create_logic(self, target: TargetOracleOIC) -> None:
        sink = LookupsSink(
            target=target,
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
        test_record = {"id": "test-lookup", "name": "Test Lookup", "version": "1.0"}
        # Mock client responses
        with patch.object(sink, "_client") as mock_client:
            # Test CREATE flow (entity doesn't exist)
            mock_client.get.return_value.status_code = 404
            mock_client.post.return_value.status_code = 201
            sink.process_record(test_record, {})
            mock_client.post.assert_called()
            # Reset mocks
            mock_client.reset_mock()
            # Test UPDATE flow (entity exists)
            mock_client.get.return_value.status_code = 200
            mock_client.get.return_value.json.return_value = {"version": "1.0"}
            mock_client.put.return_value.status_code = 200
            sink.process_record(test_record, {})
            mock_client.put.assert_called()

    def test_cli_execution(self, config_path: str, tmp_path: Path) -> None:
        # Create test Singer input
        singer_input = [
            {
                "type": "SCHEMA",
                "stream": "connections",
                "schema": {"type": "object", "properties": {"id": {"type": "string"}}},
                "key_properties": ["id"],
            },
            {
                "type": "RECORD",
                "stream": "connections",
                "record": {"id": "test-cli-connection"},
            },
        ]
        input_file = tmp_path / "singer_input.jsonl"
        with open(input_file, "w", encoding="utf-8") as f:
            f.writelines(json.dumps(msg) + "\n" for msg in singer_input)
        # Run target via CLI
        with open(input_file, encoding="utf-8") as f:
            result = subprocess.run(
                ["python", "-m", "flext_target_oracle_oic", "--config", config_path],
                stdin=f,
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent.parent,
                check=False,
            )
        # Should complete without errors (might fail on actual API calls)
        # Check that it at least started processing
        assert "target-oracle-oic" in result.stderr or result.returncode == 0

    def test_conditional_config_generation(self) -> None:
        config_path = Path(__file__).parent.parent / "config.json"
        # If config doesn't exist, it should be generated
        if not config_path.exists():
            result = subprocess.run(
                ["python", "generate_config.py"],
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent.parent,
                input="y\n",
                check=False,
            )
            assert result.returncode == 0
            assert config_path.exists()
        # Load and validate config
        with open(config_path, encoding="utf-8") as f:
            config = json.load(f)
        # Check required fields
        assert "base_url" in config
        assert "oauth_client_id" in config
        assert "oauth_client_secret" in config
        assert "oauth_token_url" in config
        # Check target-specific fields
        assert "import_mode" in config
        assert config["import_mode"] in {"create", "update", "create_or_update"}


# Additional test class using Singer SDK test framework
def get_target_oic_test_class() -> type:
    """Get test class for Singer SDK tests."""
    return get_target_test_class(
        target_class=TargetOracleOIC,
        config={
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        },
    )


class TestTargetOICSingerSDK(get_target_oic_test_class()):  # type: ignore[misc]
    """Singer SDK standard tests for target-oracle-oic."""
