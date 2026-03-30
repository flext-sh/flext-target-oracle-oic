# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Oracle OIC connection management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_oic.connection import (
        connection as connection,
        settings as settings,
    )
    from flext_target_oracle_oic.connection.connection import (
        FlextTargetOracleOicConnection as FlextTargetOracleOicConnection,
    )
    from flext_target_oracle_oic.connection.settings import (
        FlextTargetOracleOicConnectionSettings as FlextTargetOracleOicConnectionSettings,
        logger as logger,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTargetOracleOicConnection": [
        "flext_target_oracle_oic.connection.connection",
        "FlextTargetOracleOicConnection",
    ],
    "FlextTargetOracleOicConnectionSettings": [
        "flext_target_oracle_oic.connection.settings",
        "FlextTargetOracleOicConnectionSettings",
    ],
    "connection": ["flext_target_oracle_oic.connection.connection", ""],
    "logger": ["flext_target_oracle_oic.connection.settings", "logger"],
    "settings": ["flext_target_oracle_oic.connection.settings", ""],
}

_EXPORTS: Sequence[str] = [
    "FlextTargetOracleOicConnection",
    "FlextTargetOracleOicConnectionSettings",
    "connection",
    "logger",
    "settings",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
