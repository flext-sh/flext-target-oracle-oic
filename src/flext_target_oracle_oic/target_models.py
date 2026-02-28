"""Factory helpers for OIC model instances."""

from __future__ import annotations

from collections.abc import Mapping

from flext_target_oracle_oic.models import m


def create_oic_connection(
    data: Mapping[str, object],
) -> m.TargetOracleOic.OICConnection:
    """Create an OICConnection model from generic payload via Pydantic validation."""
    return m.TargetOracleOic.OICConnection.model_validate({**data, "properties": data})


def create_oic_integration(
    data: Mapping[str, object],
) -> m.TargetOracleOic.OICIntegration:
    """Create an OICIntegration model from generic payload via Pydantic validation."""
    return m.TargetOracleOic.OICIntegration.model_validate(data)


def create_oic_package(data: Mapping[str, object]) -> m.TargetOracleOic.OICPackage:
    """Create an OICPackage model from generic payload via Pydantic validation."""
    return m.TargetOracleOic.OICPackage.model_validate(data)


def create_oic_lookup(data: Mapping[str, object]) -> m.TargetOracleOic.OICLookup:
    """Create an OICLookup model from generic payload via Pydantic validation."""
    return m.TargetOracleOic.OICLookup.model_validate(data)


__all__ = [
    "create_oic_connection",
    "create_oic_integration",
    "create_oic_lookup",
    "create_oic_package",
]
