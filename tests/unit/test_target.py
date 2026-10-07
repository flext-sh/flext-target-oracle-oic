"""Tests for target-oracle-oic with enterprise-grade validation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import ClassVar

import pytest
from flext_tests import tm
from singer_sdk.target_base import Target as SingerTarget

from flext_target_oracle_oic import FlextTargetOracleOicSettings
from flext_target_oracle_oic.target import (
    FlextTargetOracleOic,
    FlextTargetOracleOicConnectionsSink,
    FlextTargetOracleOicIntegrationsSink,
)
from tests import c, t


class DummySingerTarget(SingerTarget):
    """Minimal Singer target implementation for sink tests."""

    name = "dummy-target-oracle-oic"
    config_jsonschema: ClassVar[dict[str, str | t.MappingKV[str, t.StrMapping]]] = {
        "type": "object",
        "properties": c.TargetOracleOic.Tests.DEFAULT_PROPERTIES,
    }


class TestsFlextTargetOracleOicTarget:
    """Tests for ``FlextTargetOracleOicTarget``."""

    @staticmethod
    @pytest.fixture
    def valid_config() -> t.StrMapping:
        """Create valid configuration for testing.

        Returns:
            The resulting ``t.StrMapping``.
        """
        return {
            "base_url": "https://test-instance-region.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id_12345",
            "oauth_client_secret": "s" + "0" * 14,
            "oauth_token_url": "https://test-idcs.identity.oraclecloud.com/oauth2/v1/token",
            "oauth_client_aud": "https://test-idcs.identity.oraclecloud.com",
        }

    @staticmethod
    def test_target_initialization_with_valid_config(
        valid_config: t.StrMapping,
    ) -> None:
        """Test target initialization with valid configuration.

        Raises:
            AssertionError: If ``target.name != 'target-oracle-oic'``.
        """
        _ = valid_config
        target = FlextTargetOracleOic()
        if target.name != "target-oracle-oic":
            msg: str = f"Expected {'target-oracle-oic'}, got {target.name}"
            raise AssertionError(msg)
        tm.that(target.fetch_sink_class("connections"), is_=type)

    @staticmethod
    def test_target_initialization_with_minimal_config() -> None:
        """Test method.

        Raises:
            AssertionError: If ``target.name != 'target-oracle-oic'``.
        """
        target = FlextTargetOracleOic()
        if target.name != "target-oracle-oic":
            msg: str = f"Expected {'target-oracle-oic'}, got {target.name}"
            raise AssertionError(msg)

    @staticmethod
    def test_get_sink_mapping() -> None:
        """Test method.

        Raises:
            AssertionError: If ``target.fetch_sink_class('connections') is not
                FlextTargetOracleOicConnectionsSink``; or if Expected.
        """
        target = FlextTargetOracleOic()
        if (
            target.fetch_sink_class("connections")
            is not FlextTargetOracleOicConnectionsSink
        ):
            expected = FlextTargetOracleOicConnectionsSink
            got = target.fetch_sink_class("connections")
            msg: str = f"Expected {expected}, got {got}"
            raise AssertionError(msg)
        assert (
            target.fetch_sink_class("integrations")
            is FlextTargetOracleOicIntegrationsSink
        )
        if target.fetch_sink_class("unknown_stream") is not target.default_sink_class:
            expected = target.default_sink_class
            got = target.fetch_sink_class("unknown_stream")
            msg = f"Expected {expected}, got {got}"
            raise AssertionError(msg)

    @staticmethod
    def test_config_schema() -> None:
        """Test method.

        Raises:
            AssertionError: If Expected.
        """
        schema = FlextTargetOracleOicSettings.model_json_schema()
        tm.that(schema, is_=dict)
        if "properties" not in schema:
            msg = f"Expected {'properties'} in {schema}"
            raise AssertionError(msg)
        properties = schema["properties"]
        tm.that(properties, is_=dict)
        tm.that(properties, has="TargetOracleOic")


@pytest.fixture
def singer_target() -> SingerTarget:
    """Provide ``singer_target``.

    Returns:
        The resulting ``SingerTarget``.
    """
    return DummySingerTarget(config={})
