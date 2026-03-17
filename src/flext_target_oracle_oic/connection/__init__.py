# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Oracle OIC connection management using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from flext_target_oracle_oic.connection.connection import OICConnection
    from flext_target_oracle_oic.connection.settings import (
        OICConnectionSettings,
        logger,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "OICConnection": ("flext_target_oracle_oic.connection.connection", "OICConnection"),
    "OICConnectionSettings": (
        "flext_target_oracle_oic.connection.settings",
        "OICConnectionSettings",
    ),
    "logger": ("flext_target_oracle_oic.connection.settings", "logger"),
}

__all__ = [
    "OICConnection",
    "OICConnectionSettings",
    "logger",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
