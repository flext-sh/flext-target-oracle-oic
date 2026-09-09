"""Governance checks for Oracle OIC module structure."""

from __future__ import annotations

from flext_tests.utilities import ModuleGovernanceMixin

from tests import c


class TestsFlextTargetOracleOicModuleGovernance(ModuleGovernanceMixin):
    """Behavior contract for test_module_governance."""

    _test_file = __file__
    _tests_config = c.TargetOracleOic.Tests
    _warn_on_import_error = False


__all__: list[str] = ["TestsFlextTargetOracleOicModuleGovernance"]
