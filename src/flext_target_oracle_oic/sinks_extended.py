"""Additional sink classes for non-core Oracle OIC streams."""

from __future__ import annotations

from flext_core import FlextTypes as t

from .target_client import OICBaseSink


class LibrariesSink(OICBaseSink):
    """Sink for OIC libraries stream."""

    name = "libraries"


class CertificatesSink(OICBaseSink):
    """Sink for OIC certificates stream."""

    name = "certificates"


class ProjectsSink(OICBaseSink):
    """Sink for OIC projects stream."""

    name = "projects"


class SchedulesSink(OICBaseSink):
    """Sink for OIC schedules stream."""

    name = "schedules"


class ConnectivityAgentSink(OICBaseSink):
    """Sink for OIC connectivity agents stream."""

    name = "connectivity_agents"


class GenericOICEntitySink(OICBaseSink):
    """Sink used for generic OIC stream handling."""

    name = "generic"

    def process_record(
        self,
        record: dict[str, t.GeneralValueType],
        context: dict[str, t.GeneralValueType],
    ) -> None:
        """No-op processing for unsupported generic entities."""
        _ = context
        _ = record


__all__ = [
    "CertificatesSink",
    "ConnectivityAgentSink",
    "GenericOICEntitySink",
    "LibrariesSink",
    "ProjectsSink",
    "SchedulesSink",
]
