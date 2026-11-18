# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Oic. Utilities package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_oic._utilities.service_runtime import (
        FlextTargetOracleOicUtilitiesServiceRuntime,
    )
    from flext_target_oracle_oic._utilities.sink import (
        FlextTargetOracleOicUtilitiesSink,
    )


__all__: tuple[str, ...] = (
    "FlextTargetOracleOicUtilitiesServiceRuntime",
    "FlextTargetOracleOicUtilitiesSink",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextTargetOracleOicUtilitiesServiceRuntime": ".service_runtime",
        "FlextTargetOracleOicUtilitiesSink": ".sink",
    },
    public_exports=__all__,
    deferred_members=("FlextTargetOracleOicUtilitiesServiceRuntime",),
)
