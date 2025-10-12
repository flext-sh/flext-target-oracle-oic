#!/usr/bin/env python3
"""Generate config.json from environment variables for target-oracle-oic."""

from __future__ import annotations

import json
import os
from pathlib import Path

from flext_core import FlextCore


def generate_config() -> FlextCore.Types.Dict:
    """Generate configuration dictionary from environment variables.

    Returns:
      Configuration dictionary for target-oracle-oic

    """
    return {
        "base_url": os.getenv(
            "OIC_IDCS_CLIENT_AUD",
            "https://your-instance.integration.ocp.oraclecloud.com",
        ),
        "oauth_client_id": os.getenv("OIC_IDCS_CLIENT_ID", ""),
        "oauth_client_secret": os.getenv("OIC_IDCS_CLIENT_SECRET", ""),
        "oauth_token_url": (
            os.getenv("OIC_IDCS_URL", "https://your-identity.oraclecloud.com")
            + "/oauth2/v1/token"
            if os.getenv("OIC_IDCS_URL")
            else "https://your-identity.oraclecloud.com/oauth2/v1/token"
        ),
        "import_mode": os.getenv("OIC_IMPORT_MODE", "create_or_update"),
        "activate_integrations": os.getenv("OIC_ACTIVATE_INTEGRATIONS", "false").lower()
        == "true",
        "batch_size": int(os.getenv("OIC_BATCH_SIZE", "10")),
        "timeout": int(os.getenv("OIC_TIMEOUT", "30")),
        "max_retries": int(os.getenv("OIC_MAX_RETRIES", "3")),
        "validate_ssl": os.getenv("OIC_VALIDATE_SSL", "true").lower() == "true",
    }


def main() -> None:
    """Generate config.json file for target-oracle-oic."""
    config_path = Path("config.json")

    if config_path.exists():
        response = input("config.json already exists. Overwrite? (y/N): ")
        if response.lower() not in {"y", "yes"}:
            return

    try:
        config = generate_config()

        with config_path.open("w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

        # Warn about missing required values
        required_fields = ["oauth_client_id", "oauth_client_secret"]
        missing_fields = [field for field in required_fields if not config.get(field)]

        if missing_fields:
            pass

    except (RuntimeError, ValueError, TypeError):
        return


if __name__ == "__main__":
    main()
