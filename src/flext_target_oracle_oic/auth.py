"""Oracle Integration Cloud authentication - PEP8 compliant with maximum composition.

This module provides backward compatibility while directing to the new unified configuration.
For new development, use flext_target_oracle_oic.target_config directly.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_oic.target_config import (
    OICAuthConfig,
    OICOAuth2Authenticator,
)

# Note: This module is maintained for backward compatibility only.
# New code should import directly from flext_target_oracle_oic.target_config

__all__: list[str] = ["OICAuthConfig", "OICOAuth2Authenticator"]
