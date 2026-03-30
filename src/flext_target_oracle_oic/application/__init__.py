# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Oracle OIC application module using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_target_oracle_oic.application.orchestrator import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextTargetOracleOicOrchestrator": "flext_target_oracle_oic.application.orchestrator",
    "orchestrator": "flext_target_oracle_oic.application.orchestrator",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
