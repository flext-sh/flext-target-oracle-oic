"""Tests for Oracle OIC target CLI entrypoint.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_oic import main


class TestsFlextTargetOracleOicCliEntrypoint:
    """Behavior contract for test_cli_entrypoint."""

    def test_main_entrypoint_returns_zero(self) -> None:
        assert main() == 0
