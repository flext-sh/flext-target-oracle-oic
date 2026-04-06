"""Singer target entry point and sink definitions for Oracle OIC."""

from __future__ import annotations

from collections.abc import Mapping
from typing import ClassVar, override

from flext_core import FlextLogger, r
from flext_meltano import FlextMeltanoSingerSinkBase, FlextMeltanoTargetAbstractions
from flext_target_oracle_oic import c, t

logger = FlextLogger(__name__)


class FlextTargetOracleOicBaseSink(FlextMeltanoSingerSinkBase):
    """Base sink implementation used by OIC stream sinks."""

    @override
    def process_batch(self, context: t.MutableContainerValueMapping) -> None:
        """Singer batch hook implementation."""
        _ = context

    @override
    def process_record(
        self,
        record: t.MutableContainerValueMapping,
        context: t.MutableContainerValueMapping,
    ) -> None:
        """Default sink behavior: log incoming record metadata."""
        _ = context
        logger.debug("Processing OIC record", keys=str(list(record.keys())))


class FlextTargetOracleOicConnectionsSink(FlextTargetOracleOicBaseSink):
    """Sink for OIC connections stream."""

    name = c.TargetOracleOic.STREAM_CONNECTIONS


class FlextTargetOracleOicIntegrationsSink(FlextTargetOracleOicBaseSink):
    """Sink for OIC integrations stream."""

    name = c.TargetOracleOic.STREAM_INTEGRATIONS


class FlextTargetOracleOicPackagesSink(FlextTargetOracleOicBaseSink):
    """Sink for OIC packages stream."""

    name = c.TargetOracleOic.STREAM_PACKAGES


class FlextTargetOracleOicLookupsSink(FlextTargetOracleOicBaseSink):
    """Sink for OIC lookups stream."""

    name = c.TargetOracleOic.STREAM_LOOKUPS


class FlextTargetOracleOic(FlextMeltanoTargetAbstractions):
    """Singer target entry point for Oracle OIC."""

    name: ClassVar[str] = c.TargetOracleOic.TARGET_NAME
    default_sink_class: ClassVar[type[FlextTargetOracleOicBaseSink]] = (
        FlextTargetOracleOicBaseSink
    )

    def get_sink_class(self, stream_name: str) -> type[FlextTargetOracleOicBaseSink]:
        """Resolve sink class by stream name."""
        mapping: Mapping[str, type[FlextTargetOracleOicBaseSink]] = {
            "connections": FlextTargetOracleOicConnectionsSink,
            "integrations": FlextTargetOracleOicIntegrationsSink,
            "packages": FlextTargetOracleOicPackagesSink,
            "lookups": FlextTargetOracleOicLookupsSink,
        }
        return mapping.get(stream_name, FlextTargetOracleOicBaseSink)

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
    "FlextTargetOracleOic",
    "FlextTargetOracleOicBaseSink",
    "FlextTargetOracleOicConnectionsSink",
    "FlextTargetOracleOicIntegrationsSink",
    "FlextTargetOracleOicLookupsSink",
    "FlextTargetOracleOicPackagesSink",
    "main",
]
