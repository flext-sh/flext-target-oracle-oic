"""Oracle OIC Singer integration module using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_oic.singer.processors import OICRecordProcessor
from flext_target_oracle_oic.typings import FlextTargetOracleOicTypes

__all__: FlextTargetOracleOicTypes.Core.StringList = [
    "OICRecordProcessor",
]
