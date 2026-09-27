"""Governance checks for Oracle OIC module structure."""

from __future__ import annotations

from flext_tests import FlextTestsModuleGovernanceMixin

from tests import c


class TestsFlextTargetOracleOicModuleGovernance(FlextTestsModuleGovernanceMixin):
    """Behavior contract for test_module_governance."""

    _test_file = __file__
    _tests_config = c.TargetOracleOic.Tests
    _warn_on_import_error = False
