"""Tests for generate_config module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import patch

import pytest

from flext_target_oracle_oic import generate_config, main


class TestGenerateConfig:
    """Test generate_config functionality."""

    def test_generate_config_basic(self) -> None:
        """Test method."""
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
                msg: str = f"Expected {'base_url'} in {config}"
                raise AssertionError(msg)
            assert "oauth_client_id" in config
            if "oauth_client_secret" not in config:
                msg: str = f"Expected {'oauth_client_secret'} in {config}"
                raise AssertionError(msg)
            assert "oauth_token_url" in config
            # Verify values
            if config["base_url"] != "https://test.integration.ocp.oraclecloud.com":
                msg: str = f"Expected {'https://test.integration.ocp.oraclecloud.com'}, got {config['base_url']}"
                raise AssertionError(
                    msg,
                )
            assert config["oauth_client_id"] == "test_client_id"
            if config["oauth_client_secret"] != "test_secret":
                msg: str = (
                    f"Expected {'test_secret'}, got {config['oauth_client_secret']}"
                )
                raise AssertionError(
                    msg,
                )

    def test_generate_config_defaults(self) -> None:
        """Test method."""
        """Test default values in config."""
        with patch.dict(os.environ, {}, clear=True):
            config = generate_config()
            # Check defaults
            if config.get("import_mode") != "create_or_update":
                msg: str = (
                    f"Expected {'create_or_update'}, got {config.get('import_mode')}"
                )
                raise AssertionError(
                    msg,
                )
            if config.get("activate_integrations"):
                msg: str = f"Expected False, got {config.get('activate_integrations')}"
                raise AssertionError(
                    msg,
                )
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
        if config_file.read_text() != "{}":
            msg: str = f"Expected {'{}'}, got {config_file.read_text()}"
            raise AssertionError(msg)
