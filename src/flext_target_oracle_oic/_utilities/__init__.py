# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_target_oracle_oic._utilities import service_runtime
    from flext_target_oracle_oic._utilities.service_runtime import (
        FlextTargetOracleOicServiceRuntime,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextTargetOracleOicServiceRuntime": "flext_target_oracle_oic._utilities.service_runtime",
    "service_runtime": "flext_target_oracle_oic._utilities.service_runtime",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
