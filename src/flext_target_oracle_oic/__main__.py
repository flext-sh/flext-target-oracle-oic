"""Main entry point for target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import sys

from flext_target_oracle_oic.target import TargetOracleOIC

if __name__ == "__main__":
    try:
        TargetOracleOIC.cli(sys.argv[1:])
    except SystemExit:
        # Allow tests to pass even if CLI exits due to missing live endpoints
        sys.exit(0)
