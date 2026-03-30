# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Test package initialization module.

This module is part of the FLEXT ecosystem. Docstrings follow PEP 257 and Google style.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import d, e, h, r, s, x

    from tests import (
        constants as constants,
        models as models,
        protocols as protocols,
        test_cli_entrypoint as test_cli_entrypoint,
        test_e2e as test_e2e,
        test_target as test_target,
        typings as typings,
        utilities as utilities,
    )
    from tests.constants import (
        FlextTargetOracleOicTestConstants as FlextTargetOracleOicTestConstants,
        FlextTargetOracleOicTestConstants as c,
    )
    from tests.models import (
        FlextTargetOracleOicTestModels as FlextTargetOracleOicTestModels,
        FlextTargetOracleOicTestModels as m,
        tm as tm,
    )
    from tests.protocols import (
        FlextTargetOracleOicTestProtocols as FlextTargetOracleOicTestProtocols,
        FlextTargetOracleOicTestProtocols as p,
    )
    from tests.test_cli_entrypoint import (
        test_main_entrypoint_returns_none as test_main_entrypoint_returns_none,
    )
    from tests.test_e2e import (
        TestTargetOracleOicE2E as TestTargetOracleOicE2E,
        load_test_config as load_test_config,
        target as target,
        test_config as test_config,
        test_target_smoke_class as test_target_smoke_class,
    )
    from tests.test_target import (
        AuthTestConfig as AuthTestConfig,
        DummySingerTarget as DummySingerTarget,
        TestTargetOracleOic as TestTargetOracleOic,
        singer_target as singer_target,
        test_oic_authenticator_builds_payload as test_oic_authenticator_builds_payload,
        test_oic_authenticator_omits_optional_scope_and_audience as test_oic_authenticator_omits_optional_scope_and_audience,
        test_oic_authenticator_rejects_invalid_token_response as test_oic_authenticator_rejects_invalid_token_response,
    )
    from tests.typings import (
        FlextTargetOracleOicTestTypes as FlextTargetOracleOicTestTypes,
        FlextTargetOracleOicTestTypes as t,
    )
    from tests.utilities import (
        FlextTargetOracleOicTestUtilities as FlextTargetOracleOicTestUtilities,
        FlextTargetOracleOicTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "AuthTestConfig": ["tests.test_target", "AuthTestConfig"],
    "DummySingerTarget": ["tests.test_target", "DummySingerTarget"],
    "FlextTargetOracleOicTestConstants": ["tests.constants", "FlextTargetOracleOicTestConstants"],
    "FlextTargetOracleOicTestModels": ["tests.models", "FlextTargetOracleOicTestModels"],
    "FlextTargetOracleOicTestProtocols": ["tests.protocols", "FlextTargetOracleOicTestProtocols"],
    "FlextTargetOracleOicTestTypes": ["tests.typings", "FlextTargetOracleOicTestTypes"],
    "FlextTargetOracleOicTestUtilities": ["tests.utilities", "FlextTargetOracleOicTestUtilities"],
    "TestTargetOracleOic": ["tests.test_target", "TestTargetOracleOic"],
    "TestTargetOracleOicE2E": ["tests.test_e2e", "TestTargetOracleOicE2E"],
    "c": ["tests.constants", "FlextTargetOracleOicTestConstants"],
    "constants": ["tests.constants", ""],
    "d": ["flext_tests", "d"],
    "e": ["flext_tests", "e"],
    "h": ["flext_tests", "h"],
    "load_test_config": ["tests.test_e2e", "load_test_config"],
    "m": ["tests.models", "FlextTargetOracleOicTestModels"],
    "models": ["tests.models", ""],
    "p": ["tests.protocols", "FlextTargetOracleOicTestProtocols"],
    "protocols": ["tests.protocols", ""],
    "r": ["flext_tests", "r"],
    "s": ["flext_tests", "s"],
    "singer_target": ["tests.test_target", "singer_target"],
    "t": ["tests.typings", "FlextTargetOracleOicTestTypes"],
    "target": ["tests.test_e2e", "target"],
    "test_cli_entrypoint": ["tests.test_cli_entrypoint", ""],
    "test_config": ["tests.test_e2e", "test_config"],
    "test_e2e": ["tests.test_e2e", ""],
    "test_main_entrypoint_returns_none": ["tests.test_cli_entrypoint", "test_main_entrypoint_returns_none"],
    "test_oic_authenticator_builds_payload": ["tests.test_target", "test_oic_authenticator_builds_payload"],
    "test_oic_authenticator_omits_optional_scope_and_audience": ["tests.test_target", "test_oic_authenticator_omits_optional_scope_and_audience"],
    "test_oic_authenticator_rejects_invalid_token_response": ["tests.test_target", "test_oic_authenticator_rejects_invalid_token_response"],
    "test_target": ["tests.test_target", ""],
    "test_target_smoke_class": ["tests.test_e2e", "test_target_smoke_class"],
    "tm": ["tests.models", "tm"],
    "typings": ["tests.typings", ""],
    "u": ["tests.utilities", "FlextTargetOracleOicTestUtilities"],
    "utilities": ["tests.utilities", ""],
    "x": ["flext_tests", "x"],
}

_EXPORTS: Sequence[str] = [
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
    "constants",
    "d",
    "e",
    "h",
    "load_test_config",
    "m",
    "models",
    "p",
    "protocols",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
