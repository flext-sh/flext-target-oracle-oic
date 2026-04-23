"""Singer target sink definitions for Oracle OIC."""

from __future__ import annotations

from collections.abc import (
    Mapping,
)
from typing import ClassVar, override

from flext_meltano import (
    FlextMeltanoTargetAbstractions,
)

from flext_target_oracle_oic import c, m, p, r, t, u


class FlextTargetOracleOicBaseSink(m.Meltano.SingerSinkBase):
    """Base sink implementation used by OIC stream sinks."""

    _logger: ClassVar[p.Logger] = u.fetch_logger(__name__)

    @override
    def process_batch(self, context: t.MutableJsonMapping) -> None:
        """Singer batch hook implementation."""
        _ = context

    @override
    def process_record(
        self,
        record: t.MutableJsonMapping,
        context: t.MutableJsonMapping,
    ) -> None:
        """Default sink behavior: log incoming record metadata."""
        _ = context
        self._logger.debug("Processing OIC record", keys=str(list(record.keys())))


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
    _sink_classes: ClassVar[Mapping[str, type[FlextTargetOracleOicBaseSink]]] = {
        c.TargetOracleOic.STREAM_CONNECTIONS: FlextTargetOracleOicConnectionsSink,
        c.TargetOracleOic.STREAM_INTEGRATIONS: FlextTargetOracleOicIntegrationsSink,
        c.TargetOracleOic.STREAM_PACKAGES: FlextTargetOracleOicPackagesSink,
        c.TargetOracleOic.STREAM_LOOKUPS: FlextTargetOracleOicLookupsSink,
    }

    def fetch_sink_class(self, stream_name: str) -> type[FlextTargetOracleOicBaseSink]:
        """Resolve sink class by stream name."""
        return self._sink_classes.get(stream_name, self.default_sink_class)

    def setup(self) -> p.Result[bool]:
        """Setup target resources."""
        return r[bool].ok(value=True)

    def teardown(self) -> p.Result[bool]:
        """Teardown target resources."""
        return r[bool].ok(value=True)


__all__: list[str] = [
    "FlextTargetOracleOic",
    "FlextTargetOracleOicBaseSink",
    "FlextTargetOracleOicConnectionsSink",
    "FlextTargetOracleOicIntegrationsSink",
    "FlextTargetOracleOicLookupsSink",
    "FlextTargetOracleOicPackagesSink",
]
