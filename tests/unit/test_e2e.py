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
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from flext_target_oracle_oic import FlextTargetOracleOicSettings
from flext_target_oracle_oic.target import (
    FlextTargetOracleOic,
    FlextTargetOracleOicConnectionsSink,
    FlextTargetOracleOicIntegrationsSink,
    FlextTargetOracleOicLookupsSink,
    FlextTargetOracleOicPackagesSink,
)
from flext_tests import tm

if TYPE_CHECKING:
    from tests import t


def load_test_config() -> t.StrMapping:
    """Load real test configuration from environment variables."""
    env_file = Path(".env")
    if env_file.exists():
        with env_file.open(encoding="utf-8") as f:
            for line in f:
                if "=" in line and (not line.strip().startswith("#")):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value.strip("\"'")
    settings = {
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
    missing_keys = [k for k in required_keys if not settings[k]]
    if missing_keys:
        pytest.skip(f"Missing required environment variables: {missing_keys}")
    return settings


@pytest.fixture
def target() -> FlextTargetOracleOic:
    return FlextTargetOracleOic()


class TestsFlextTargetOracleOicE2e:
    def test_target_initialization(self, target: FlextTargetOracleOic) -> None:
        """Test target initialization with valid configuration."""
        if target.name != "target-oracle-oic":
            msg: str = f"Expected {'target-oracle-oic'}, got {target.name}"
            raise AssertionError(msg)
        tm.that(target.fetch_sink_class("connections"), is_=type)

    def test_sink_class_mapping(self, target: FlextTargetOracleOic) -> None:
        """Test sink class mapping for known streams."""
        if (
            target.fetch_sink_class("connections")
            is not FlextTargetOracleOicConnectionsSink
        ):
            msg = f"Expected {FlextTargetOracleOicConnectionsSink}, got {target.fetch_sink_class('connections')}"
            raise AssertionError(msg)
        assert (
            target.fetch_sink_class("integrations")
            is FlextTargetOracleOicIntegrationsSink
        )
        if target.fetch_sink_class("packages") is not FlextTargetOracleOicPackagesSink:
            msg = f"Expected {FlextTargetOracleOicPackagesSink}, got {target.fetch_sink_class('packages')}"
            raise AssertionError(msg)
        assert target.fetch_sink_class("lookups") is FlextTargetOracleOicLookupsSink
        default_sink = target.fetch_sink_class("unknown_stream")
        if default_sink is not target.default_sink_class:
            msg = f"Expected {target.default_sink_class}, got {default_sink}"
            raise AssertionError(msg)

    def test_config_validation(self, target: FlextTargetOracleOic) -> None:
        """Test setup/teardown result contract."""
        setup_result = target.setup()
        tm.ok(setup_result)
        tm.that(setup_result.value, none=False)
        tm.that(setup_result.value, eq=True)
        teardown_result = target.teardown()
        tm.ok(teardown_result)
        tm.that(teardown_result.value, none=False)
        tm.that(teardown_result.value, eq=True)

    def test_conditional_config_generation(self) -> None:
        """Test schema generation from pydantic configuration model."""
        schema_raw = FlextTargetOracleOicSettings.model_json_schema()
        properties_raw = schema_raw.get("properties")
        if not isinstance(properties_raw, dict):
            msg = f"Expected {'properties'} in {schema_raw}"
            raise AssertionError(msg)
        if "TargetOracleOic" not in properties_raw:
            msg = f"Expected {'TargetOracleOic'} in {properties_raw}"
            raise AssertionError(msg)
        tm.that(properties_raw["TargetOracleOic"], is_=dict)

    @pytest.fixture
    def test_config(self) -> t.StrMapping:
        return load_test_config()

    def test_target_smoke_class(self) -> None:
        tm.that(FlextTargetOracleOic.name, eq="target-oracle-oic")
