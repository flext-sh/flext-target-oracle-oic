"""Oracle OIC patterns using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_target_oracle_oic.patterns.oic_patterns import (
    OICDataTransformer,
    OICEntryManager,
    OICSchemaMapper,
    OICTypeConverter,
)
from flext_target_oracle_oic.typings import FlextTargetOracleOicTypes

__all__: FlextTargetOracleOicTypes.Core.StringList = [
    "OICDataTransformer",
    "OICEntryManager",
    "OICSchemaMapper",
    "OICTypeConverter",
]
