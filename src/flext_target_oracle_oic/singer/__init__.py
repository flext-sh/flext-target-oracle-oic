"""Oracle OIC Singer integration module using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes

from flext_target_oracle_oic.singer.processors import OICRecordProcessor

__all__: FlextTypes.Core.StringList = [
    "OICRecordProcessor",
]
