# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Test package initialization module.

This module is part of the FLEXT ecosystem. Docstrings follow PEP 257 and Google style.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from tests.constants import (
        TestsFlextTargetOracleOicConstants,
        TestsFlextTargetOracleOicConstants as c,
    )
    from tests.models import TestsFlextTargetOracleOicModels, m, tm
    from tests.protocols import TestsFlextTargetOracleOicProtocols, p
    from tests.test_cli_entrypoint import test_main_entrypoint_returns_none
    from tests.test_e2e import (
        TestTargetOracleOicE2E,
        load_test_config,
        target,
        test_config,
        test_target_smoke_class,
    )
    from tests.test_target import (
        TestTargetOracleOic,
        test_oic_authenticator_builds_payload,
        test_oic_authenticator_omits_optional_scope_and_audience,
        test_oic_authenticator_rejects_invalid_token_response,
    )
    from tests.typings import (
        TestsFlextTargetOracleOicTypes,
        TestsFlextTargetOracleOicTypes as t,
    )
    from tests.utilities import (
        TestsFlextTargetOracleOicUtilities,
        TestsFlextTargetOracleOicUtilities as u,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "TestTargetOracleOic": ("tests.test_target", "TestTargetOracleOic"),
    "TestTargetOracleOicE2E": ("tests.test_e2e", "TestTargetOracleOicE2E"),
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
    "load_test_config": ("tests.test_e2e", "load_test_config"),
    "m": ("tests.models", "m"),
    "p": ("tests.protocols", "p"),
    "t": ("tests.typings", "TestsFlextTargetOracleOicTypes"),
    "target": ("tests.test_e2e", "target"),
    "test_config": ("tests.test_e2e", "test_config"),
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
    "test_target_smoke_class": ("tests.test_e2e", "test_target_smoke_class"),
    "tm": ("tests.models", "tm"),
    "u": ("tests.utilities", "TestsFlextTargetOracleOicUtilities"),
}

__all__ = [
    "TestTargetOracleOic",
    "TestTargetOracleOicE2E",
    "TestsFlextTargetOracleOicConstants",
    "TestsFlextTargetOracleOicModels",
    "TestsFlextTargetOracleOicProtocols",
    "TestsFlextTargetOracleOicTypes",
    "TestsFlextTargetOracleOicUtilities",
    "c",
    "load_test_config",
    "m",
    "p",
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
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
