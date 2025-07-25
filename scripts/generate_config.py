#!/usr/bin/env python3
"""Generate config.json from environment variables for target-oracle-oic."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


def generate_config() -> dict[str, Any]:
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
            print("Configuration generation skipped.")
            return

    try:
        config = generate_config()

        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

        print("✅ Successfully generated target-oracle-oic configuration")
        print("📄 Configuration saved to: config.json")
        print(f"🔧 Configuration includes: {', '.join(config.keys())}")

        # Warn about missing required values
        required_fields = ["oauth_client_id", "oauth_client_secret"]
        missing_fields = [field for field in required_fields if not config.get(field)]

        if missing_fields:
            print(
                f"⚠️  Warning: Missing required environment variables for: {', '.join(missing_fields)}",
            )
            print("   Make sure to set OIC_IDCS_CLIENT_ID and OIC_IDCS_CLIENT_SECRET")

    except Exception as e:
        print(f"❌ Error generating configuration: {e}")
        return


if __name__ == "__main__":
    main()
