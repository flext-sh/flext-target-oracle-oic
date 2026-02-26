"""Tests for Oracle OIC target CLI entrypoint.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_oic.target_client import main


def test_main_entrypoint_returns_none() -> None:
    main()
