"""Oracle OIC connection management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_oic.connection.config import OICConnectionSettings
from flext_target_oracle_oic.connection.connection import OICConnection
from flext_target_oracle_oic.typings import FlextTargetOracleOicTypes

__all__: FlextTargetOracleOicTypes.Core.StringList = [
    "OICConnection",
    "OICConnectionSettings",
]
