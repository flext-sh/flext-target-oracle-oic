# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Oracle OIC application module using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_oic.application import orchestrator as orchestrator
    from flext_target_oracle_oic.application.orchestrator import (
        FlextTargetOracleOicOrchestrator as FlextTargetOracleOicOrchestrator,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTargetOracleOicOrchestrator": [
        "flext_target_oracle_oic.application.orchestrator",
        "FlextTargetOracleOicOrchestrator",
    ],
    "orchestrator": ["flext_target_oracle_oic.application.orchestrator", ""],
}

_EXPORTS: Sequence[str] = [
    "FlextTargetOracleOicOrchestrator",
    "orchestrator",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
