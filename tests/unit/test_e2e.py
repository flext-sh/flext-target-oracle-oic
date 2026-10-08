"""End-to-end tests for target-oracle-oic.

Tests target initialization, sink resolution, setup/teardown, and the settings
schema through the public target surface. NO MOCKS - real functional testing only.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from flext_tests import tm

from flext_target_oracle_oic import FlextTargetOracleOicSettings
from flext_target_oracle_oic.target import FlextTargetOracleOic
from tests import c, t


@pytest.fixture
def target() -> FlextTargetOracleOic:
    """Provide ``target``.

    Returns:
        The resulting ``FlextTargetOracleOic``.
    """
    return FlextTargetOracleOic()


class TestsFlextTargetOracleOicE2e:
    """Tests for ``FlextTargetOracleOicE2e``."""

    @staticmethod
    def test_target_initialization(target: FlextTargetOracleOic) -> None:
        """The target carries its declared name and a sink class."""
        tm.that(target.name, eq=c.TargetOracleOic.TARGET_NAME)
        tm.that(target.default_sink_class, is_=type)

    @staticmethod
    def test_config_validation(target: FlextTargetOracleOic) -> None:
        """Test setup/teardown result contract."""
        setup_result = target.setup()
        tm.ok(setup_result)
        tm.that(setup_result.value, none=False)
        tm.that(setup_result.value, eq=True)
        teardown_result = target.teardown()
        tm.ok(teardown_result)
        tm.that(teardown_result.value, none=False)
        tm.that(teardown_result.value, eq=True)

    @staticmethod
    def test_conditional_config_generation() -> None:
        """Test schema generation from pydantic configuration model.

        Raises:
            TypeError: If the schema carries no properties mapping.
        """
        schema_raw = t.json_mapping_adapter().validate_python(
            FlextTargetOracleOicSettings.model_json_schema(),
        )
        properties_raw = schema_raw.get("properties")
        if not isinstance(properties_raw, dict):
            msg = f"Expected {'properties'} in {schema_raw}"
            raise TypeError(msg)
        tm.that(properties_raw, has="TargetOracleOic")
        tm.that(properties_raw["TargetOracleOic"], is_=dict)

    @staticmethod
    def test_target_smoke_class() -> None:
        """Test target smoke class."""
        tm.that(FlextTargetOracleOic.name, eq=c.TargetOracleOic.TARGET_NAME)
