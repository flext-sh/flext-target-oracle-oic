# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Oic. Utilities package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_oic._utilities.service_runtime import (
        FlextTargetOracleOicServiceRuntime,
    )
    from flext_target_oracle_oic._utilities.sink import FlextTargetOracleOicSink


__all__: tuple[str, ...] = (
    "FlextTargetOracleOicServiceRuntime",
    "FlextTargetOracleOicSink",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTargetOracleOicServiceRuntime": ".service_runtime",
        "FlextTargetOracleOicSink": ".sink",
    }),
    public_exports=__all__,
)
