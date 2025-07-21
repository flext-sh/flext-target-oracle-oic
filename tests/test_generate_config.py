"""Tests for generate_config module."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING
from unittest.mock import patch

from generate_config import generate_config, main

if TYPE_CHECKING:
    from pathlib import Path

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
            assert "base_url" in config
            assert "oauth_client_id" in config
            assert "oauth_client_secret" in config
            assert "oauth_token_url" in config

            # Verify values
            assert config["base_url"] == "https://test.integration.ocp.oraclecloud.com"
            assert config["oauth_client_id"] == "test_client_id"
            assert config["oauth_client_secret"] == "test_secret"

    def test_generate_config_defaults(self) -> None:
        """Test default values in config."""
        with patch.dict(os.environ, {}, clear=True):
            config = generate_config()

            # Check defaults
            assert config.get("import_mode") == "create_or_update"
            assert config.get("activate_integrations") is False
            assert config.get("batch_size") == 10

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
        assert config_file.read_text() == "{}"
