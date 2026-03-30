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
    from tests.constants import *
    from tests.models import *
    from tests.protocols import *
    from tests.test_cli_entrypoint import *
    from tests.test_e2e import *
    from tests.test_target import *
    from tests.typings import *
    from tests.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "AuthTestConfig": "tests.test_target",
    "DummySingerTarget": "tests.test_target",
    "FlextTargetOracleOicTestConstants": "tests.constants",
    "FlextTargetOracleOicTestModels": "tests.models",
    "FlextTargetOracleOicTestProtocols": "tests.protocols",
    "FlextTargetOracleOicTestTypes": "tests.typings",
    "FlextTargetOracleOicTestUtilities": "tests.utilities",
    "TestTargetOracleOic": "tests.test_target",
    "TestTargetOracleOicE2E": "tests.test_e2e",
    "c": ["tests.constants", "FlextTargetOracleOicTestConstants"],
    "constants": "tests.constants",
    "d": "flext_tests",
    "e": "flext_tests",
    "h": "flext_tests",
    "load_test_config": "tests.test_e2e",
    "m": ["tests.models", "FlextTargetOracleOicTestModels"],
    "models": "tests.models",
    "p": ["tests.protocols", "FlextTargetOracleOicTestProtocols"],
    "protocols": "tests.protocols",
    "r": "flext_tests",
    "s": "flext_tests",
    "singer_target": "tests.test_target",
    "t": ["tests.typings", "FlextTargetOracleOicTestTypes"],
    "target": "tests.test_e2e",
    "test_cli_entrypoint": "tests.test_cli_entrypoint",
    "test_config": "tests.test_e2e",
    "test_e2e": "tests.test_e2e",
    "test_main_entrypoint_returns_none": "tests.test_cli_entrypoint",
    "test_oic_authenticator_builds_payload": "tests.test_target",
    "test_oic_authenticator_omits_optional_scope_and_audience": "tests.test_target",
    "test_oic_authenticator_rejects_invalid_token_response": "tests.test_target",
    "test_target": "tests.test_target",
    "test_target_smoke_class": "tests.test_e2e",
    "tm": "tests.models",
    "typings": "tests.typings",
    "u": ["tests.utilities", "FlextTargetOracleOicTestUtilities"],
    "utilities": "tests.utilities",
    "x": "flext_tests",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
