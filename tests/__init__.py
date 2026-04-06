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
    from tests.conftest import pytest_plugins

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        FlextTargetOracleOicTestConstants,
        FlextTargetOracleOicTestConstants as c,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import (
        FlextTargetOracleOicTestModels,
        FlextTargetOracleOicTestModels as m,
        tm,
    )

    protocols = _tests_protocols
    import tests.test_cli_entrypoint as _tests_test_cli_entrypoint
    from tests.protocols import (
        FlextTargetOracleOicTestProtocols,
        FlextTargetOracleOicTestProtocols as p,
    )

    test_cli_entrypoint = _tests_test_cli_entrypoint
    import tests.test_e2e as _tests_test_e2e
    from tests.test_cli_entrypoint import test_main_entrypoint_returns_none

    test_e2e = _tests_test_e2e
    import tests.test_target as _tests_test_target
    from tests.test_e2e import (
        TestTargetOracleOicE2E,
        load_test_config,
        target,
        test_config,
        test_target_smoke_class,
    )

    test_target = _tests_test_target
    import tests.typings as _tests_typings
    from tests.test_target import (
        AuthTestConfig,
        DummySingerTarget,
        TestTargetOracleOic,
        singer_target,
        test_oic_authenticator_builds_payload,
        test_oic_authenticator_omits_optional_scope_and_audience,
        test_oic_authenticator_rejects_invalid_token_response,
    )

    typings = _tests_typings
    import tests.utilities as _tests_utilities
    from tests.typings import (
        FlextTargetOracleOicTestTypes,
        FlextTargetOracleOicTestTypes as t,
    )

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.utilities import (
        FlextTargetOracleOicTestUtilities,
        FlextTargetOracleOicTestUtilities as u,
    )
_LAZY_IMPORTS = {
    "AuthTestConfig": ("tests.test_target", "AuthTestConfig"),
    "DummySingerTarget": ("tests.test_target", "DummySingerTarget"),
    "FlextTargetOracleOicTestConstants": (
        "tests.constants",
        "FlextTargetOracleOicTestConstants",
    ),
    "FlextTargetOracleOicTestModels": (
        "tests.models",
        "FlextTargetOracleOicTestModels",
    ),
    "FlextTargetOracleOicTestProtocols": (
        "tests.protocols",
        "FlextTargetOracleOicTestProtocols",
    ),
    "FlextTargetOracleOicTestTypes": ("tests.typings", "FlextTargetOracleOicTestTypes"),
    "FlextTargetOracleOicTestUtilities": (
        "tests.utilities",
        "FlextTargetOracleOicTestUtilities",
    ),
    "TestTargetOracleOic": ("tests.test_target", "TestTargetOracleOic"),
    "TestTargetOracleOicE2E": ("tests.test_e2e", "TestTargetOracleOicE2E"),
    "c": ("tests.constants", "FlextTargetOracleOicTestConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "load_test_config": ("tests.test_e2e", "load_test_config"),
    "m": ("tests.models", "FlextTargetOracleOicTestModels"),
    "models": "tests.models",
    "p": ("tests.protocols", "FlextTargetOracleOicTestProtocols"),
    "protocols": "tests.protocols",
    "pytest_plugins": ("tests.conftest", "pytest_plugins"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "singer_target": ("tests.test_target", "singer_target"),
    "t": ("tests.typings", "FlextTargetOracleOicTestTypes"),
    "target": ("tests.test_e2e", "target"),
    "test_cli_entrypoint": "tests.test_cli_entrypoint",
    "test_config": ("tests.test_e2e", "test_config"),
    "test_e2e": "tests.test_e2e",
    "test_main_entrypoint_returns_none": (
        "tests.test_cli_entrypoint",
        "test_main_entrypoint_returns_none",
    ),
    "test_oic_authenticator_builds_payload": (
        "tests.test_target",
        "test_oic_authenticator_builds_payload",
    ),
    "test_oic_authenticator_omits_optional_scope_and_audience": (
        "tests.test_target",
        "test_oic_authenticator_omits_optional_scope_and_audience",
    ),
    "test_oic_authenticator_rejects_invalid_token_response": (
        "tests.test_target",
        "test_oic_authenticator_rejects_invalid_token_response",
    ),
    "test_target": "tests.test_target",
    "test_target_smoke_class": ("tests.test_e2e", "test_target_smoke_class"),
    "tm": ("tests.models", "tm"),
    "typings": "tests.typings",
    "u": ("tests.utilities", "FlextTargetOracleOicTestUtilities"),
    "utilities": "tests.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "AuthTestConfig",
    "DummySingerTarget",
    "FlextTargetOracleOicTestConstants",
    "FlextTargetOracleOicTestModels",
    "FlextTargetOracleOicTestProtocols",
    "FlextTargetOracleOicTestTypes",
    "FlextTargetOracleOicTestUtilities",
    "TestTargetOracleOic",
    "TestTargetOracleOicE2E",
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "h",
    "load_test_config",
    "m",
    "models",
    "p",
    "protocols",
    "pytest_plugins",
    "r",
    "s",
    "singer_target",
    "t",
    "target",
    "test_cli_entrypoint",
    "test_config",
    "test_e2e",
    "test_main_entrypoint_returns_none",
    "test_oic_authenticator_builds_payload",
    "test_oic_authenticator_omits_optional_scope_and_audience",
    "test_oic_authenticator_rejects_invalid_token_response",
    "test_target",
    "test_target_smoke_class",
    "tm",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
