# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Test package initialization module.

This module is part of the FLEXT ecosystem. Docstrings follow PEP 257 and Google style.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tests import d, e, h, r, s, x

    from tests.constants import (
        FlextTargetOracleOicTestConstants,
        FlextTargetOracleOicTestConstants as c,
    )
    from tests.models import (
        FlextTargetOracleOicTestModels,
        FlextTargetOracleOicTestModels as m,
        tm,
    )
    from tests.protocols import (
        FlextTargetOracleOicTestProtocols,
        FlextTargetOracleOicTestProtocols as p,
    )
    from tests.test_cli_entrypoint import test_main_entrypoint_returns_none
    from tests.test_e2e import (
        TestTargetOracleOicE2E,
        load_test_config,
        target,
        test_config,
        test_target_smoke_class,
    )
    from tests.test_target import (
        AuthTestConfig,
        DummySingerTarget,
        TestTargetOracleOic,
        singer_target,
        test_oic_authenticator_builds_payload,
        test_oic_authenticator_omits_optional_scope_and_audience,
        test_oic_authenticator_rejects_invalid_token_response,
    )
    from tests.typings import (
        FlextTargetOracleOicTestTypes,
        FlextTargetOracleOicTestTypes as t,
    )
    from tests.utilities import (
        FlextTargetOracleOicTestUtilities,
        FlextTargetOracleOicTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "AuthTestConfig": ["tests.test_target", "AuthTestConfig"],
    "DummySingerTarget": ["tests.test_target", "DummySingerTarget"],
    "FlextTargetOracleOicTestConstants": [
        "tests.constants",
        "FlextTargetOracleOicTestConstants",
    ],
    "FlextTargetOracleOicTestModels": [
        "tests.models",
        "FlextTargetOracleOicTestModels",
    ],
    "FlextTargetOracleOicTestProtocols": [
        "tests.protocols",
        "FlextTargetOracleOicTestProtocols",
    ],
    "FlextTargetOracleOicTestTypes": ["tests.typings", "FlextTargetOracleOicTestTypes"],
    "FlextTargetOracleOicTestUtilities": [
        "tests.utilities",
        "FlextTargetOracleOicTestUtilities",
    ],
    "TestTargetOracleOic": ["tests.test_target", "TestTargetOracleOic"],
    "TestTargetOracleOicE2E": ["tests.test_e2e", "TestTargetOracleOicE2E"],
    "c": ["tests.constants", "FlextTargetOracleOicTestConstants"],
    "d": ["flext_tests", "d"],
    "e": ["flext_tests", "e"],
    "h": ["flext_tests", "h"],
    "load_test_config": ["tests.test_e2e", "load_test_config"],
    "m": ["tests.models", "FlextTargetOracleOicTestModels"],
    "p": ["tests.protocols", "FlextTargetOracleOicTestProtocols"],
    "r": ["flext_tests", "r"],
    "s": ["flext_tests", "s"],
    "singer_target": ["tests.test_target", "singer_target"],
    "t": ["tests.typings", "FlextTargetOracleOicTestTypes"],
    "target": ["tests.test_e2e", "target"],
    "test_config": ["tests.test_e2e", "test_config"],
    "test_main_entrypoint_returns_none": [
        "tests.test_cli_entrypoint",
        "test_main_entrypoint_returns_none",
    ],
    "test_oic_authenticator_builds_payload": [
        "tests.test_target",
        "test_oic_authenticator_builds_payload",
    ],
    "test_oic_authenticator_omits_optional_scope_and_audience": [
        "tests.test_target",
        "test_oic_authenticator_omits_optional_scope_and_audience",
    ],
    "test_oic_authenticator_rejects_invalid_token_response": [
        "tests.test_target",
        "test_oic_authenticator_rejects_invalid_token_response",
    ],
    "test_target_smoke_class": ["tests.test_e2e", "test_target_smoke_class"],
    "tm": ["tests.models", "tm"],
    "u": ["tests.utilities", "FlextTargetOracleOicTestUtilities"],
    "x": ["flext_tests", "x"],
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
    "d",
    "e",
    "h",
    "load_test_config",
    "m",
    "p",
    "r",
    "s",
    "singer_target",
    "t",
    "target",
    "test_config",
    "test_main_entrypoint_returns_none",
    "test_oic_authenticator_builds_payload",
    "test_oic_authenticator_omits_optional_scope_and_audience",
    "test_oic_authenticator_rejects_invalid_token_response",
    "test_target_smoke_class",
    "tm",
    "u",
    "x",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
