"""Tests for generate_config module."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import patch

# Add scripts directory to Python path for import
scripts_path = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_path))

# Import after path modification - required due to dynamic path modification
from generate_config import (
    generate_config,
    main,
)

if TYPE_CHECKING:
    import pytest


class TestGenerateConfig:
    """Test generate_config functionality."""

    def test_generate_config_basic(self) -> None:
        """Test basic config generation."""
        # Set required environment variables
        env_vars = {
            "OIC_IDCS_CLIENT_AUD": "https://test.integration.ocp.oraclecloud.com",
            "OIC_IDCS_CLIENT_ID": "test_client_id",
            "OIC_IDCS_CLIENT_SECRET": "test_secret",
            "OIC_IDCS_URL": "https://test.identity.oraclecloud.com",
        }
        with patch.dict(os.environ, env_vars):
            config = generate_config()
            # Check required fields
            if "base_url" not in config:
                raise AssertionError(f"Expected {"base_url"} in {config}")
            assert "oauth_client_id" in config
            if "oauth_client_secret" not in config:
                raise AssertionError(f"Expected {"oauth_client_secret"} in {config}")
            assert "oauth_token_url" in config
            # Verify values
            if config["base_url"] != "https://test.integration.ocp.oraclecloud.com":
                raise AssertionError(f"Expected {"https://test.integration.ocp.oraclecloud.com"}, got {config["base_url"]}")
            assert config["oauth_client_id"] == "test_client_id"
            if config["oauth_client_secret"] != "test_secret":
                raise AssertionError(f"Expected {"test_secret"}, got {config["oauth_client_secret"]}")

    def test_generate_config_defaults(self) -> None:
        """Test default values in config."""
        with patch.dict(os.environ, {}, clear=True):
            config = generate_config()
            # Check defaults
            if config.get("import_mode") != "create_or_update":
                raise AssertionError(f"Expected {"create_or_update"}, got {config.get("import_mode")}")
            if config.get("activate_integrations"):
                raise AssertionError(f"Expected False, got {config.get("activate_integrations")}")\ n            assert config.get("batch_size") == 10

    def test_main_creates_file(
        self,
        tmp_path: Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Test main function creates config.json."""
        # Change to temp directory
        monkeypatch.chdir(tmp_path)
        # Mock input to confirm overwrite
        with patch("builtins.input", return_value="y"):
            main()
        # Check file was created
        config_file = tmp_path / "config.json"
        assert config_file.exists()

    def test_main_skip_existing(
        self,
        tmp_path: Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Test main function skips existing file when user says no."""
        # Change to temp directory
        monkeypatch.chdir(tmp_path)
        # Create existing file
        config_file = tmp_path / "config.json"
        config_file.write_text("{}")
        # Mock input to skip overwrite
        with patch("builtins.input", return_value="n"):
            main()
        # Check file was not modified
        if config_file.read_text() != "{}":
            raise AssertionError(f"Expected {"{}"}, got {config_file.read_text()}")
