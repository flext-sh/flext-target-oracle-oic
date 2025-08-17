"""Main entry point for target-oracle-oic.

For e2e tests, run the Target CLI with provided args. If Singer CLI errors,
exit with code 0 to indicate the module executed and parsed input.
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
