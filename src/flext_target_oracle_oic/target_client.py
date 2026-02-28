"""Singer target client and sink definitions for Oracle OIC."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import override

from flext_core import FlextLogger, FlextResult, t
from flext_meltano import FlextMeltanoTarget as Target
from flext_target_oracle_oic.constants import c
from singer_sdk import Sink

logger = FlextLogger(__name__)


class OICBaseSink(Sink):
    """Base sink implementation used by OIC stream sinks."""

    def __init__(
        self,
        target: Target,
        stream_name: str,
        schema: Mapping[str, t.JsonValue],
        key_properties: Sequence[str] | None = None,
    ) -> None:
        """Initialize sink metadata and source context."""
        super().__init__(target, stream_name, dict(schema), key_properties)

    @override
    def process_record(
        self,
        record: Mapping[str, t.JsonValue],
        context: Mapping[str, t.JsonValue],
    ) -> None:
        """Default sink behavior: log incoming record metadata."""
        _ = context
        logger.debug(
            "Processing OIC record",
            extra={"keys": list(record.keys())},
        )

    @override
    def process_batch(self, context: Mapping[str, t.JsonValue]) -> None:
        """Singer batch hook implementation."""
        _ = context


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

    name = c.TargetOracleOic.TARGET_NAME
    default_sink_class = OICBaseSink

    @override
    def get_sink_class(self, stream_name: str) -> type[OICBaseSink]:
        """Resolve sink class by stream name."""
        mapping: dict[str, type[OICBaseSink]] = {
            "connections": ConnectionsSink,
            "integrations": IntegrationsSink,
            "packages": PackagesSink,
            "lookups": LookupsSink,
        }
        return mapping.get(stream_name, OICBaseSink)

    def setup(self) -> FlextResult[bool]:
        """Setup target resources."""
        return FlextResult[bool].ok(value=True)

    def teardown(self) -> FlextResult[bool]:
        """Teardown target resources."""
        return FlextResult[bool].ok(value=True)


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
