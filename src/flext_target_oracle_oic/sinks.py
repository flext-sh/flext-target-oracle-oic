"""Sink exports for target Oracle OIC streams."""

from __future__ import annotations

from .target_client import (
    ConnectionsSink,
    IntegrationsSink,
    LookupsSink,
    OICBaseSink,
    PackagesSink,
)

__all__ = [
    "ConnectionsSink",
    "IntegrationsSink",
    "LookupsSink",
    "OICBaseSink",
    "PackagesSink",
]
