"""Oracle Integration Cloud Singer Target.

A Singer-compatible target for Oracle Integration Cloud (OIC) that supports
OAuth2 authentication and comprehensive integration management.

This target provides:
- OAuth2 authentication with Oracle Identity Cloud Service (IDCS)
- Support for connections, integrations, packages, and lookups
- Batch processing for efficient data loading
- Enterprise-grade error handling and logging
- Archive-based integration deployment

Example:
            ```bash
    # Install the target
    pip install target-oracle-oic

    # Configure the target
    export OAUTH_CLIENT_ID="your-client-id"
    export OAUTH_CLIENT_SECRET="your-client-secret"
    export OAUTH_TOKEN_URL="https://your-idcs.identity.oraclecloud.com/oauth2/v1/token"
    export BASE_URL="https://your-instance.integration.ocp.oraclecloud.com"

    # Run with Singer data
    cat data.jsonl | target-oracle-oic --config config.json
    ```

"""

from __future__ import annotations

from flext_target_oracle_oic.__version__ import __version__
from flext_target_oracle_oic.target import TargetOracleOIC

__all__ = ["TargetOracleOIC", "__version__", "main"]


def main() -> None:
        TargetOracleOIC.cli()


if __name__ == "__main__":
            main()
