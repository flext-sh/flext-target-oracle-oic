# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_target_oracle_oic import (
        constants,
        models,
        protocols,
        test_cli_entrypoint,
        test_e2e,
        test_target,
        typings,
        utilities,
    )
    from flext_target_oracle_oic.constants import (
        FlextTargetOracleOicTestConstants,
        FlextTargetOracleOicTestConstants as c,
    )
    from flext_target_oracle_oic.models import (
        FlextTargetOracleOicTestModels,
        FlextTargetOracleOicTestModels as m,
        tm,
    )
    from flext_target_oracle_oic.protocols import (
        FlextTargetOracleOicTestProtocols,
        FlextTargetOracleOicTestProtocols as p,
    )
    from flext_target_oracle_oic.test_cli_entrypoint import (
        test_main_entrypoint_returns_none,
    )
    from flext_target_oracle_oic.test_e2e import DummySingerTarget, target, test_config
    from flext_target_oracle_oic.test_target import (
        AuthTestConfig,
        InvalidTokenResponse,
        authenticator,
        config,
        singer_target,
        test_oic_authenticator_builds_payload,
    )
    from flext_target_oracle_oic.typings import (
        FlextTargetOracleOicTestTypes,
        FlextTargetOracleOicTestTypes as t,
    )
    from flext_target_oracle_oic.utilities import (
        FlextTargetOracleOicTestUtilities,
        FlextTargetOracleOicTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "AuthTestConfig": "flext_target_oracle_oic.test_target",
    "DummySingerTarget": "flext_target_oracle_oic.test_e2e",
    "FlextTargetOracleOicTestConstants": "flext_target_oracle_oic.constants",
    "FlextTargetOracleOicTestModels": "flext_target_oracle_oic.models",
    "FlextTargetOracleOicTestProtocols": "flext_target_oracle_oic.protocols",
    "FlextTargetOracleOicTestTypes": "flext_target_oracle_oic.typings",
    "FlextTargetOracleOicTestUtilities": "flext_target_oracle_oic.utilities",
    "InvalidTokenResponse": "flext_target_oracle_oic.test_target",
    "authenticator": "flext_target_oracle_oic.test_target",
    "c": ("flext_target_oracle_oic.constants", "FlextTargetOracleOicTestConstants"),
    "config": "flext_target_oracle_oic.test_target",
    "constants": "flext_target_oracle_oic.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("flext_target_oracle_oic.models", "FlextTargetOracleOicTestModels"),
    "models": "flext_target_oracle_oic.models",
    "p": ("flext_target_oracle_oic.protocols", "FlextTargetOracleOicTestProtocols"),
    "protocols": "flext_target_oracle_oic.protocols",
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "singer_target": "flext_target_oracle_oic.test_target",
    "t": ("flext_target_oracle_oic.typings", "FlextTargetOracleOicTestTypes"),
    "target": "flext_target_oracle_oic.test_e2e",
    "test_cli_entrypoint": "flext_target_oracle_oic.test_cli_entrypoint",
    "test_config": "flext_target_oracle_oic.test_e2e",
    "test_e2e": "flext_target_oracle_oic.test_e2e",
    "test_main_entrypoint_returns_none": "flext_target_oracle_oic.test_cli_entrypoint",
    "test_oic_authenticator_builds_payload": "flext_target_oracle_oic.test_target",
    "test_target": "flext_target_oracle_oic.test_target",
    "tm": "flext_target_oracle_oic.models",
    "typings": "flext_target_oracle_oic.typings",
    "u": ("flext_target_oracle_oic.utilities", "FlextTargetOracleOicTestUtilities"),
    "utilities": "flext_target_oracle_oic.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
