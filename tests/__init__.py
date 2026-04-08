# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        TestsFlextTargetOracleOicConstants,
        TestsFlextTargetOracleOicConstants as c,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import (
        TestsFlextTargetOracleOicModels,
        TestsFlextTargetOracleOicModels as m,
    )

    protocols = _tests_protocols
    import tests.test_cli_entrypoint as _tests_test_cli_entrypoint
    from tests.protocols import (
        TestsFlextTargetOracleOicProtocols,
        TestsFlextTargetOracleOicProtocols as p,
    )

    test_cli_entrypoint = _tests_test_cli_entrypoint
    import tests.test_e2e as _tests_test_e2e

    test_e2e = _tests_test_e2e
    import tests.test_module_governance as _tests_test_module_governance

    test_module_governance = _tests_test_module_governance
    import tests.test_target as _tests_test_target

    test_target = _tests_test_target
    import tests.typings as _tests_typings

    typings = _tests_typings
    import tests.utilities as _tests_utilities
    from tests.typings import (
        TestsFlextTargetOracleOicTypes,
        TestsFlextTargetOracleOicTypes as t,
    )

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.utilities import (
        TestsFlextTargetOracleOicUtilities,
        TestsFlextTargetOracleOicUtilities as u,
    )
_LAZY_IMPORTS = {
    "TestsFlextTargetOracleOicConstants": (
        "tests.constants",
        "TestsFlextTargetOracleOicConstants",
    ),
    "TestsFlextTargetOracleOicModels": (
        "tests.models",
        "TestsFlextTargetOracleOicModels",
    ),
    "TestsFlextTargetOracleOicProtocols": (
        "tests.protocols",
        "TestsFlextTargetOracleOicProtocols",
    ),
    "TestsFlextTargetOracleOicTypes": (
        "tests.typings",
        "TestsFlextTargetOracleOicTypes",
    ),
    "TestsFlextTargetOracleOicUtilities": (
        "tests.utilities",
        "TestsFlextTargetOracleOicUtilities",
    ),
    "c": ("tests.constants", "TestsFlextTargetOracleOicConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("tests.models", "TestsFlextTargetOracleOicModels"),
    "models": "tests.models",
    "p": ("tests.protocols", "TestsFlextTargetOracleOicProtocols"),
    "protocols": "tests.protocols",
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("tests.typings", "TestsFlextTargetOracleOicTypes"),
    "test_cli_entrypoint": "tests.test_cli_entrypoint",
    "test_e2e": "tests.test_e2e",
    "test_module_governance": "tests.test_module_governance",
    "test_target": "tests.test_target",
    "typings": "tests.typings",
    "u": ("tests.utilities", "TestsFlextTargetOracleOicUtilities"),
    "utilities": "tests.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "TestsFlextTargetOracleOicConstants",
    "TestsFlextTargetOracleOicModels",
    "TestsFlextTargetOracleOicProtocols",
    "TestsFlextTargetOracleOicTypes",
    "TestsFlextTargetOracleOicUtilities",
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "t",
    "test_cli_entrypoint",
    "test_e2e",
    "test_module_governance",
    "test_target",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
