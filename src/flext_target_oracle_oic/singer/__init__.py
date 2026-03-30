# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Oracle OIC Singer integration module using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_oic.singer import processors as processors
    from flext_target_oracle_oic.singer.processors import (
        FlextTargetOracleOicProcessedRecord as FlextTargetOracleOicProcessedRecord,
        FlextTargetOracleOicRecordProcessor as FlextTargetOracleOicRecordProcessor,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTargetOracleOicProcessedRecord": [
        "flext_target_oracle_oic.singer.processors",
        "FlextTargetOracleOicProcessedRecord",
    ],
    "FlextTargetOracleOicRecordProcessor": [
        "flext_target_oracle_oic.singer.processors",
        "FlextTargetOracleOicRecordProcessor",
    ],
    "processors": ["flext_target_oracle_oic.singer.processors", ""],
}

_EXPORTS: Sequence[str] = [
    "FlextTargetOracleOicProcessedRecord",
    "FlextTargetOracleOicRecordProcessor",
    "processors",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
