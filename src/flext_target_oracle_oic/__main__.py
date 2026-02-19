"""Main entry point for target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import sys

from flext_target_oracle_oic.cli import main

if __name__ == "__main__":
    try:
        _ = sys.argv[1:]
        main()
    except SystemExit:
        sys.exit(0)
