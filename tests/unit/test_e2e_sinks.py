"""End-to-end sink tests for target-oracle-oic.

Tests Singer sink construction and record processing paths without mocks.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import ClassVar

import pytest
from flext_tests import tm
from singer_sdk.target_base import Target as SingerTarget

from flext_target_oracle_oic.target import FlextTargetOracleOic
from tests import c, t


class TestsFlextTargetOracleOicE2eSinks:
    """Tests for the Oracle OIC Singer sink."""

    class DummySingerTarget(SingerTarget):
        """Minimal Singer target hosting the sink under test."""

        name = "dummy-target-oracle-oic"
        config_jsonschema: ClassVar[dict[str, str | t.MappingKV[str, t.StrMapping]]] = {
            "type": "object",
            "properties": dict[str, t.StrMapping](),
        }

    @staticmethod
    @pytest.fixture
    def singer_target() -> SingerTarget:
        """Provide ``singer_target``.

        Returns:
            The resulting ``SingerTarget``.
        """
        return TestsFlextTargetOracleOicE2eSinks.DummySingerTarget(config={})

    @staticmethod
    @pytest.mark.parametrize("stream_name", c.TargetOracleOic.Tests.STREAM_NAMES)
    def test_sink_processes_records_per_stream(
        singer_target: SingerTarget,
        stream_name: str,
    ) -> None:
        """The target sink binds to each stream and processes its records."""
        sink = FlextTargetOracleOic.default_sink_class(
            target=singer_target,
            stream_name=stream_name,
            schema={
                "properties": {"id": {"type": "string"}, "name": {"type": "string"}},
            },
            key_properties=["id"],
        )
        tm.that(sink.stream_name, eq=stream_name)
        records: list[t.MutableJsonMapping] = [
            {"id": f"{stream_name}-{i}", "name": f"Record {i}"} for i in range(3)
        ]
        for record in records:
            sink.process_record(record, {})
        sink.process_batch({})

    @staticmethod
    def test_sink_accepts_empty_record(singer_target: SingerTarget) -> None:
        """An empty record passes through the sink record hook."""
        sink = FlextTargetOracleOic.default_sink_class(
            target=singer_target,
            stream_name=c.TargetOracleOic.Tests.STREAM_NAMES[0],
            schema={"properties": {"id": {"type": "string"}}},
            key_properties=["id"],
        )
        sink.process_record({}, {})
        tm.that(sink.stream_name, eq=c.TargetOracleOic.Tests.STREAM_NAMES[0])
