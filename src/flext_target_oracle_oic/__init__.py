# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Oic package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports
from flext_target_oracle_oic.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_oracle_oic import d, e, h, r, s, x
    from flext_target_oracle_oic.api import (
        FlextTargetOracleOicService,
        target_oracle_oic,
    )
    from flext_target_oracle_oic.cli import FlextTargetOracleOicCli, main
    from flext_target_oracle_oic.constants import FlextTargetOracleOicConstants, c
    from flext_target_oracle_oic.models import FlextTargetOracleOicModels, m
    from flext_target_oracle_oic.protocols import FlextTargetOracleOicProtocols, p
    from flext_target_oracle_oic.settings import FlextTargetOracleOicSettings
    from flext_target_oracle_oic.typings import FlextTargetOracleOicTypes, t
    from flext_target_oracle_oic.utilities import FlextTargetOracleOicUtilities, u
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".api": (
            "FlextTargetOracleOicService",
            "target_oracle_oic",
        ),
        ".cli": (
            "FlextTargetOracleOicCli",
            "main",
        ),
        ".constants": (
            "FlextTargetOracleOicConstants",
            "c",
        ),
        ".models": (
            "FlextTargetOracleOicModels",
            "m",
        ),
        ".protocols": (
            "FlextTargetOracleOicProtocols",
            "p",
        ),
        ".settings": ("FlextTargetOracleOicSettings",),
        ".typings": (
            "FlextTargetOracleOicTypes",
            "t",
        ),
        ".utilities": (
            "FlextTargetOracleOicUtilities",
            "u",
        ),
        "flext_oracle_oic": (
            "d",
            "e",
            "h",
            "r",
            "s",
            "x",
        ),
    },
)


__all__: tuple[str, ...] = (
    "FlextTargetOracleOicCli",
    "FlextTargetOracleOicConstants",
    "FlextTargetOracleOicModels",
    "FlextTargetOracleOicProtocols",
    "FlextTargetOracleOicService",
    "FlextTargetOracleOicSettings",
    "FlextTargetOracleOicTypes",
    "FlextTargetOracleOicUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "target_oracle_oic",
    "u",
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=__all__,
)
