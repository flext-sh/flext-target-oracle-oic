"""Main entry point for target-oracle-oic."""

import sys

from flext_target_oracle_oic.target import TargetOracleOIC

if __name__ == "__main__":
    TargetOracleOIC.cli(sys.argv[1:])
