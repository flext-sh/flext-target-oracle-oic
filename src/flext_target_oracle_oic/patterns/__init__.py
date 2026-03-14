# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Oracle OIC patterns using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from flext_target_oracle_oic.patterns.oic_patterns import (
        OICDataTransformer,
        OICEntryManager,
        OICSchemaMapper,
        OICTypeConverter,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "OICDataTransformer": (
        "flext_target_oracle_oic.patterns.oic_patterns",
        "OICDataTransformer",
    ),
    "OICEntryManager": (
        "flext_target_oracle_oic.patterns.oic_patterns",
        "OICEntryManager",
    ),
    "OICSchemaMapper": (
        "flext_target_oracle_oic.patterns.oic_patterns",
        "OICSchemaMapper",
    ),
    "OICTypeConverter": (
        "flext_target_oracle_oic.patterns.oic_patterns",
        "OICTypeConverter",
    ),
}

__all__ = [
    "OICDataTransformer",
    "OICEntryManager",
    "OICSchemaMapper",
    "OICTypeConverter",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
