"""Oracle Integration Cloud authentication - ELIMINATES DUPLICATION.

Re-exports OAuth from tap-oracle-oic to eliminate exact code duplication.
This eliminates the 42-line identical OAuth2 authenticator implementation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

# CONSOLIDATION: Import OAuth from tap to eliminate duplication
from flext_tap_oracle_oic.auth import OICAuthConfig, OICOAuth2Authenticator

# Compatibility - no need to reimplement identical functionality


__all__: list[str] = ["OICAuthConfig", "OICOAuth2Authenticator"]
