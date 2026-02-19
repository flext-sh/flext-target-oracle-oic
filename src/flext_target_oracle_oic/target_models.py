"""Factory helpers for OIC model instances."""

from __future__ import annotations

from flext_core import FlextTypes as t

from .models import OICConnection, OICIntegration, OICLookup, OICPackage


def create_oic_connection(data: dict[str, t.GeneralValueType]) -> OICConnection:
    """Create an OICConnection model from generic payload."""
    return OICConnection(
        id=str(data.get("id", "")),
        name=str(data.get("name", "")),
        adapter_type=str(data.get("adapter_type", "REST")),
        properties=data if isinstance(data, dict) else {},
    )


def create_oic_integration(data: dict[str, t.GeneralValueType]) -> OICIntegration:
    """Create an OICIntegration model from generic payload."""
    return OICIntegration(
        id=str(data.get("id", "")),
        name=str(data.get("name", "")),
        version=str(data.get("version", "01.00.0000")),
        pattern=str(data.get("pattern", "ORCHESTRATION")),
    )


def create_oic_package(data: dict[str, t.GeneralValueType]) -> OICPackage:
    """Create an OICPackage model from generic payload."""
    return OICPackage(
        id=str(data.get("id", "")),
        name=str(data.get("name", "")),
        version=str(data.get("version", "01.00.0000")),
    )


def create_oic_lookup(data: dict[str, t.GeneralValueType]) -> OICLookup:
    """Create an OICLookup model from generic payload."""
    rows_obj = data.get("rows", [])
    cols_obj = data.get("columns", [])
    rows = rows_obj if isinstance(rows_obj, list) else []
    cols = cols_obj if isinstance(cols_obj, list) else []
    return OICLookup(name=str(data.get("name", "")), columns=cols, rows=rows)


__all__ = [
    "create_oic_connection",
    "create_oic_integration",
    "create_oic_lookup",
    "create_oic_package",
]
