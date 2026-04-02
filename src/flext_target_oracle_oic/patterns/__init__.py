# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Patterns package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_target_oracle_oic.patterns import oic_patterns
    from flext_target_oracle_oic.patterns.oic_patterns import (
        FlextTargetOracleOicDataTransformer,
        FlextTargetOracleOicEntryManager,
        FlextTargetOracleOicSchemaMapper,
        FlextTargetOracleOicTypeConverter,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextTargetOracleOicDataTransformer": "flext_target_oracle_oic.patterns.oic_patterns",
    "FlextTargetOracleOicEntryManager": "flext_target_oracle_oic.patterns.oic_patterns",
    "FlextTargetOracleOicSchemaMapper": "flext_target_oracle_oic.patterns.oic_patterns",
    "FlextTargetOracleOicTypeConverter": "flext_target_oracle_oic.patterns.oic_patterns",
    "oic_patterns": "flext_target_oracle_oic.patterns.oic_patterns",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
