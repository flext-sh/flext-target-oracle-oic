"""Singer target client and sink definitions for Oracle OIC."""

from __future__ import annotations

from collections.abc import Mapping
from typing import ClassVar, override

from flext_core import FlextLogger, r, t
from flext_meltano import FlextMeltanoTargetAbstractions as Target
from singer_sdk import Sink

from flext_target_oracle_oic.constants import c

logger = FlextLogger(__name__)


class OICBaseSink(Sink):
    """Base sink implementation used by OIC stream sinks."""

    @override
    def process_batch(self, context: Mapping[str, object None:
        """Singer batch hook implementation."""
        _ = context

    @override
    def process_record(
        self, record: Mapping[str, objectntext: Mapping[str, objecobject
    ) -> None:
        """Default sink behavior: log incoming record metadata."""
        _ = context
        logger.debug("Processing OIC record", extra={"keys": list(record.keys())})


class ConnectionsSink(OICBaseSink):
    """Sink for OIC connections stream."""

    name = c.TargetOracleOic.STREAM_CONNECTIONS


class IntegrationsSink(OICBaseSink):
    """Sink for OIC integrations stream."""

    name = c.TargetOracleOic.STREAM_INTEGRATIONS


class PackagesSink(OICBaseSink):
    """Sink for OIC packages stream."""

    name = c.TargetOracleOic.STREAM_PACKAGES


class LookupsSink(OICBaseSink):
    """Sink for OIC lookups stream."""

    name = c.TargetOracleOic.STREAM_LOOKUPS


class TargetOracleOic(Target):
    """Singer target entry point for Oracle OIC."""

    name: ClassVar[str] = c.TargetOracleOic.TARGET_NAME
    default_sink_class: ClassVar[type[OICBaseSink]] = OICBaseSink

    def get_sink_class(self, stream_name: str) -> type[OICBaseSink]:
        """Resolve sink class by stream name."""
        mapping: dict[str, type[OICBaseSink]] = {
            "connections": ConnectionsSink,
            "integrations": IntegrationsSink,
            "packages": PackagesSink,
            "lookups": LookupsSink,
        }
        return mapping.get(stream_name, OICBaseSink)

    def setup(self) -> r[bool]:
        """Setup target resources."""
        return r[bool].ok(value=True)

    def teardown(self) -> r[bool]:
        """Teardown target resources."""
        return r[bool].ok(value=True)


def main() -> None:
    """CLI entry point wrapper for singer target runtime."""
    return


__all__ = [
    "ConnectionsSink",
    "IntegrationsSink",
    "LookupsSink",
    "OICBaseSink",
    "PackagesSink",
    "TargetOracleOic",
    "main",
]
