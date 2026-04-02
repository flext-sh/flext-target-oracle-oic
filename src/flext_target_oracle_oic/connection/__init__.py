# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Oracle OIC connection management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_target_oracle_oic.connection import connection, settings
    from flext_target_oracle_oic.connection.connection import (
        FlextTargetOracleOicConnection,
    )
    from flext_target_oracle_oic.connection.settings import (
        FlextTargetOracleOicConnectionSettings,
        logger,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextTargetOracleOicConnection": "flext_target_oracle_oic.connection.connection",
    "FlextTargetOracleOicConnectionSettings": "flext_target_oracle_oic.connection.settings",
    "connection": "flext_target_oracle_oic.connection.connection",
    "logger": "flext_target_oracle_oic.connection.settings",
    "settings": "flext_target_oracle_oic.connection.settings",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
