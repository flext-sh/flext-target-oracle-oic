"""Tests for target-oracle-oic with enterprise-grade validation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import tm

from flext_target_oracle_oic import (
    FlextTargetOracleOicService,
    FlextTargetOracleOicSettings,
)
from flext_target_oracle_oic.target import FlextTargetOracleOic
from tests import c


class TestsFlextTargetOracleOicTarget:
    """Tests for ``FlextTargetOracleOic``."""

    @staticmethod
    def test_target_name() -> None:
        """The target exposes its declared Singer name."""
        target = FlextTargetOracleOic()
        tm.that(target.name, eq=c.TargetOracleOic.TARGET_NAME)

    @staticmethod
    def test_default_sink_class_is_a_type() -> None:
        """The target declares one sink class for every stream."""
        tm.that(FlextTargetOracleOic.default_sink_class, is_=type)

    @staticmethod
    def test_service_creates_sink_per_stream() -> None:
        """The service builds the target's sink bound to each stream name."""
        service = FlextTargetOracleOicService()
        for stream_name in c.TargetOracleOic.Tests.STREAM_NAMES:
            sink = service.create_sink(
                stream_name,
                {"properties": c.TargetOracleOic.Tests.DEFAULT_PROPERTIES},
            )
            tm.that(sink, is_=FlextTargetOracleOic.default_sink_class)
            tm.that(sink.stream_name, eq=stream_name)

    @staticmethod
    def test_config_schema() -> None:
        """The settings schema nests the TargetOracleOic namespace."""
        schema = FlextTargetOracleOicSettings.model_json_schema()
        tm.that(schema, is_=dict)
        tm.that(schema, has="properties")
        properties = schema["properties"]
        tm.that(properties, is_=dict)
        tm.that(properties, has="TargetOracleOic")
