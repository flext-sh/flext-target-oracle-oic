# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Connection package."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "FlextTargetOracleOicConnection": (
        "flext_target_oracle_oic.connection.connection",
        "FlextTargetOracleOicConnection",
    ),
    "FlextTargetOracleOicConnectionSettings": (
        "flext_target_oracle_oic.connection.settings",
        "FlextTargetOracleOicConnectionSettings",
    ),
    "c": ("flext_core.constants", "FlextConstants"),
    "connection": "flext_target_oracle_oic.connection.connection",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("flext_core.models", "FlextModels"),
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "settings": "flext_target_oracle_oic.connection.settings",
    "t": ("flext_core.typings", "FlextTypes"),
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
