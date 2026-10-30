"""End-to-end sink tests for target-oracle-oic.

Exercises the real Singer sink construction and record processing paths
through the public service surface, without mocks.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_target_oracle_oic import FlextTargetOracleOicService
from tests import c, tm


class TestsFlextTargetOracleOicE2eSinks:
    """Tests for the Oracle OIC Singer sink through the service facade."""

    @staticmethod
    @pytest.mark.parametrize("stream_name", c.TargetOracleOic.Tests.STREAM_NAMES)
    def test_service_processes_records_per_stream(stream_name: str) -> None:
        """The service binds a sink per stream and drains its records."""
        service = FlextTargetOracleOicService()
        schema = {"properties": c.TargetOracleOic.Tests.DEFAULT_PROPERTIES}
        for index in range(3):
            record = {
                "id": f"{stream_name}-{index}",
                "name": f"Record {index}",
            }
            tm.ok(service.process_record(stream_name, record, schema))
        tm.ok(
            service.process_record(stream_name, {"id": c.ProcessingMode.BATCH}, schema)
        )
        tm.ok(service.flush(stream_name))

    @staticmethod
    def test_service_accepts_empty_record() -> None:
        """An empty record passes through the sink record hook."""
        service = FlextTargetOracleOicService()
        stream_name = c.TargetOracleOic.Tests.STREAM_NAMES[0]
        schema = {"properties": c.TargetOracleOic.Tests.DEFAULT_PROPERTIES}
        tm.ok(service.process_record(stream_name, {}, schema))
