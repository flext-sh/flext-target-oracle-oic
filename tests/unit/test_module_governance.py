"""Governance checks for Oracle OIC module structure.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_module_governance
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import u

from tests import c


class TestsFlextTargetOracleOicModuleGovernance(u.FlextTestsModuleGovernanceMixin):
    """Behavior contract for test_module_governance."""

    _test_file = __file__
    _tests_config = c.TargetOracleOic.Tests()
    _warn_on_import_error = False
