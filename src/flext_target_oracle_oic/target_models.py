"""Factory helpers for OIC model instances."""

from __future__ import annotations

from collections.abc import Mapping

from .models import OICConnection, OICIntegration, OICLookup, OICPackage


def create_oic_connection(data: Mapping[str, object]) -> OICConnection:
    """Create an OICConnection model from generic payload via Pydantic validation."""
    return OICConnection.model_validate({**data, "properties": data})


def create_oic_integration(data: Mapping[str, object]) -> OICIntegration:
    """Create an OICIntegration model from generic payload via Pydantic validation."""
    return OICIntegration.model_validate(data)


def create_oic_package(data: Mapping[str, object]) -> OICPackage:
    """Create an OICPackage model from generic payload via Pydantic validation."""
    return OICPackage.model_validate(data)


def create_oic_lookup(data: Mapping[str, object]) -> OICLookup:
    """Create an OICLookup model from generic payload via Pydantic validation."""
    return OICLookup.model_validate(data)


__all__ = [
    "create_oic_connection",
    "create_oic_integration",
    "create_oic_lookup",
    "create_oic_package",
]
