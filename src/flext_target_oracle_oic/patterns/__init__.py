# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Patterns package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_oic.patterns import oic_patterns as oic_patterns
    from flext_target_oracle_oic.patterns.oic_patterns import (
        FlextTargetOracleOicDataTransformer as FlextTargetOracleOicDataTransformer,
        FlextTargetOracleOicEntryManager as FlextTargetOracleOicEntryManager,
        FlextTargetOracleOicSchemaMapper as FlextTargetOracleOicSchemaMapper,
        FlextTargetOracleOicTypeConverter as FlextTargetOracleOicTypeConverter,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTargetOracleOicDataTransformer": [
        "flext_target_oracle_oic.patterns.oic_patterns",
        "FlextTargetOracleOicDataTransformer",
    ],
    "FlextTargetOracleOicEntryManager": [
        "flext_target_oracle_oic.patterns.oic_patterns",
        "FlextTargetOracleOicEntryManager",
    ],
    "FlextTargetOracleOicSchemaMapper": [
        "flext_target_oracle_oic.patterns.oic_patterns",
        "FlextTargetOracleOicSchemaMapper",
    ],
    "FlextTargetOracleOicTypeConverter": [
        "flext_target_oracle_oic.patterns.oic_patterns",
        "FlextTargetOracleOicTypeConverter",
    ],
    "oic_patterns": ["flext_target_oracle_oic.patterns.oic_patterns", ""],
}

_EXPORTS: Sequence[str] = [
    "FlextTargetOracleOicDataTransformer",
    "FlextTargetOracleOicEntryManager",
    "FlextTargetOracleOicSchemaMapper",
    "FlextTargetOracleOicTypeConverter",
    "oic_patterns",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
