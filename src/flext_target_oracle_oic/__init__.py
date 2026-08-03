# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Oic package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import __author__ as __author__
from .__version__ import __author_email__ as __author_email__
from .__version__ import __description__ as __description__
from .__version__ import __license__ as __license__
from .__version__ import __title__ as __title__
from .__version__ import __url__ as __url__
from .__version__ import __version__ as __version__
from .__version__ import __version_info__ as __version_info__

if TYPE_CHECKING:
    from flext_oracle_oic import d as d
    from flext_oracle_oic import e as e
    from flext_oracle_oic import h as h
    from flext_oracle_oic import r as r
    from flext_oracle_oic import s as s
    from flext_oracle_oic import x as x

    from ._config import FlextTargetOracleOicConfig as FlextTargetOracleOicConfig
    from ._config import config as config
    from ._settings import FlextTargetOracleOicSettings as FlextTargetOracleOicSettings
    from ._settings import settings as settings
    from .api import FlextTargetOracleOicService as FlextTargetOracleOicService
    from .api import target_oracle_oic as target_oracle_oic
    from .cli import FlextTargetOracleOicCli as FlextTargetOracleOicCli
    from .cli import main as main
    from .constants import (
        FlextTargetOracleOicConstants as FlextTargetOracleOicConstants,
    )

    c: type[FlextTargetOracleOicConstants]
    from .models import FlextTargetOracleOicModels as FlextTargetOracleOicModels

    m: type[FlextTargetOracleOicModels]
    from .protocols import (
        FlextTargetOracleOicProtocols as FlextTargetOracleOicProtocols,
    )

    p: type[FlextTargetOracleOicProtocols]
    from .typings import FlextTargetOracleOicTypes as FlextTargetOracleOicTypes

    t: type[FlextTargetOracleOicTypes]
    from .utilities import (
        FlextTargetOracleOicUtilities as FlextTargetOracleOicUtilities,
    )

    u: type[FlextTargetOracleOicUtilities]

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._config": ("FlextTargetOracleOicConfig", "config"),
    "._settings": ("FlextTargetOracleOicSettings", "settings"),
    ".api": ("FlextTargetOracleOicService", "target_oracle_oic"),
    ".cli": ("FlextTargetOracleOicCli", "main"),
    ".constants": ("FlextTargetOracleOicConstants", "c"),
    ".models": ("FlextTargetOracleOicModels", "m"),
    ".protocols": ("FlextTargetOracleOicProtocols", "p"),
    ".typings": ("FlextTargetOracleOicTypes", "t"),
    ".utilities": ("FlextTargetOracleOicUtilities", "u"),
    "flext_oracle_oic": ("d", "e", "h", "r", "s", "x"),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextTargetOracleOicCli",
    "FlextTargetOracleOicConfig",
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
    "config",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "target_oracle_oic",
    "u",
    "x",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
