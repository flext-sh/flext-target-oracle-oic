# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Oic package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports
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
from flext_target_oracle_oic._exports import FLEXT_TARGET_ORACLE_OIC_LAZY_IMPORTS

if TYPE_CHECKING:
    from flext_core._root_typing_parts import (
        d as d,
        e as e,
        h as h,
        r as r,
        s as s,
        x as x,
    )
    from flext_target_oracle_oic.api import (
        FlextTargetOracleOicService as FlextTargetOracleOicService,
        target_oracle_oic as target_oracle_oic,
    )
    from flext_target_oracle_oic.cli import (
        FlextTargetOracleOicCli as FlextTargetOracleOicCli,
        main as main,
    )
    from flext_target_oracle_oic.constants import (
        FlextTargetOracleOicConstants as FlextTargetOracleOicConstants,
        c as c,
    )
    from flext_target_oracle_oic.models import (
        FlextTargetOracleOicModels as FlextTargetOracleOicModels,
        m as m,
    )
    from flext_target_oracle_oic.protocols import (
        FlextTargetOracleOicProtocols as FlextTargetOracleOicProtocols,
        p as p,
    )
    from flext_target_oracle_oic.settings import (
        FlextTargetOracleOicSettings as FlextTargetOracleOicSettings,
    )
    from flext_target_oracle_oic.typings import (
        FlextTargetOracleOicTypes as FlextTargetOracleOicTypes,
        t as t,
    )
    from flext_target_oracle_oic.utilities import (
        FlextTargetOracleOicUtilities as FlextTargetOracleOicUtilities,
        u as u,
    )


_LAZY_IMPORTS = FLEXT_TARGET_ORACLE_OIC_LAZY_IMPORTS


_EAGER_EXPORTS = (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)


_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextTargetOracleOicCli",
    "FlextTargetOracleOicConstants",
    "FlextTargetOracleOicModels",
    "FlextTargetOracleOicProtocols",
    "FlextTargetOracleOicService",
    "FlextTargetOracleOicSettings",
    "FlextTargetOracleOicTypes",
    "FlextTargetOracleOicUtilities",
    "target_oracle_oic",
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
    "u",
    "x",
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
    public_exports=_PUBLIC_EXPORTS,
)
