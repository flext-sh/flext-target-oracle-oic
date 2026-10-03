"""FLEXT Target Oracle OIC base constants — OIC target domain constants.

All constants are flat with descriptive prefixes to explain their usage.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextTargetOracleOicConstantsBase:
    """Base Oracle OIC target constants: streams, auth, headers, defaults."""

    # Streams
    STREAM_CONNECTIONS: Final[str] = "connections"
    STREAM_INTEGRATIONS: Final[str] = "integrations"
    STREAM_PACKAGES: Final[str] = "packages"
    STREAM_LOOKUPS: Final[str] = "lookups"
    TARGET_NAME: Final[str] = "target-oracle-oic"

    # Auth
    AUTH_SCHEME_BEARER: Final[str] = "Bearer"
    DEFAULT_OAUTH_SCOPE: Final[str] = "oic_instance"
    HEADER_CONTENT_TYPE: Final[str] = "Content-Type"
    HEADER_CONTENT_TYPE_FORM: Final[str] = "application/x-www-form-urlencoded"
    HEADER_CONTENT_TYPE_JSON: Final[str] = "application/json"
    HEADER_ACCEPT: Final[str] = "Accept"
    HEADER_AUTHORIZATION: Final[str] = "Authorization"

    # Defaults
    API_PATH_INTEGRATION: Final[str] = "/ic/api/integration/v1"
    DEFAULT_VERSION: Final[str] = "01.00.0000"
    DEFAULT_PATTERN: Final[str] = "ORCHESTRATION"
    DEFAULT_SCHEDULE_TYPE: Final[str] = "ONCE"
    DEFAULT_USE_OAUTH2: Final[bool] = True
    DEFAULT_VERIFY_SSL: Final[bool] = True
