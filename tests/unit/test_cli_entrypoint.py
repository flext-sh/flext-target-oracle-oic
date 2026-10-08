"""Tests for Oracle OIC target CLI entrypoint.

Runs the REAL installed console script through the flext-cli SSOT runner
(``u.Cli.capture``) with an empty Singer stream on stdin, exactly as an
orchestrator invokes the target.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import pytest
from flext_tests import m, tm, u

from tests import c


class TestsFlextTargetOracleOicCliEntrypoint:
    """Behavior contract for test_cli_entrypoint."""

    pytestmark = pytest.mark.slow

    @staticmethod
    def test_console_drains_empty_stream_with_exit_zero() -> None:
        """Test console drains empty stream with exit zero."""
        result = u.Cli.capture(
            [c.TargetOracleOic.TARGET_NAME],
            options=m.Cli.ProcessOptions(
                remove_env_keys=("PYTHONPATH",),
                input_data="",
            ),
        )
        tm.ok(result)
