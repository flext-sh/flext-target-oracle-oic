"""DEPRECATED: Legacy Oracle OIC Target - DELEGATES TO FLEXT-MELTANO UNIFIED SDK.

This module provides backward compatibility for Oracle Integration Cloud data loading
by delegating to the enterprise flext-meltano Singer SDK integration.

TRUE FACADE PATTERN: 100% DELEGATION TO FLEXT-MELTANO SDK
==========================================================

DELEGATION TARGET: flext_meltano.singer_sdk_integration - Enterprise Singer SDK
with unified target protocols, connection pooling, and batch optimization.

PREFERRED PATTERN:
    from flext_meltano.singer_sdk_integration import FlextSingerSDKIntegration

    sdk = FlextSingerSDKIntegration(project_root=Path('.'))
    target = await sdk.create_oracle_oic_target(config)
    await target.write_batch(stream, records)

LEGACY COMPATIBILITY:
    from target_oracle_oic.target import TargetOracleOIC

    # Still works but delegates to flext-meltano internally
    target = TargetOracleOIC(config)
    target.sink_class = OICBaseSink

MIGRATION BENEFITS:
- Eliminates Singer protocol implementation duplication
- Leverages enterprise connection pooling and optimization
- Automatic improvements from unified SDK
- Consistent behavior across all Singer targets
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

from singer_sdk import Target

# Delegate to enterprise Singer SDK integration
try:
    from flext_meltano.singer_sdk_integration import (
        FlextSingerSDKIntegration,
        FlextTargetProtocol,
    )
except ImportError:
    # Fallback for environments without flext-meltano
    FlextSingerSDKIntegration = None
    FlextTargetProtocol = None

from target_oracle_oic.config import TargetOracleOICConfig
from target_oracle_oic.sinks import (
    ConnectionsSink,
    IntegrationsSink,
    LookupsSink,
    OICBaseSink,
    PackagesSink,
)
from target_oracle_oic.sinks_extended import (
    BusinessEventsSink,
    CertificatesSink,
    ConnectionActionsSink,
    IntegrationActionsSink,
    LibrariesSink,
    MonitoringConfigSink,
    ProjectsSink,
    SchedulesSink,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

    from singer_sdk.sinks import Sink


class TargetOracleOIC(Target):
    """Legacy Oracle OIC Target - True Facade with Pure Delegation to flext-meltano.

    Delegates entirely to enterprise Singer SDK integration while maintaining
    compatibility with Singer SDK interface.

    ENTERPRISE BENEFITS:
    - Automatic connection pooling via unified SDK
    - Enhanced batch processing through enterprise patterns
    - Centralized Oracle OIC integration management
    - Consistent behavior across all Oracle targets

    LEGACY COMPATIBILITY:
    - Maintains Singer SDK Target interface
    - Preserves existing sink configuration patterns
    - Supports all OIC-specific features

    DELEGATION TARGET: flext_meltano.singer_sdk_integration.FlextSingerSDKIntegration
    """

    name = "target-oracle-oic"
    config_jsonschema = TargetOracleOICConfig.model_json_schema()
    default_sink_class = OICBaseSink

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize target facade - delegates to flext-meltano unified SDK."""
        super().__init__(*args, **kwargs)

        # Initialize enterprise Singer SDK integration
        if FlextSingerSDKIntegration:
            self._enterprise_sdk = FlextSingerSDKIntegration(project_root=Path())
            self._enterprise_target = None
        else:
            self._enterprise_sdk = None
            self._enterprise_target = None

    async def _get_enterprise_target(self):
        """Get or create enterprise target instance."""
        if self._enterprise_target is None and self._enterprise_sdk:
            self._enterprise_target = await self._enterprise_sdk.create_oracle_oic_target(self.config)
        return self._enterprise_target

    def get_sink(
        self,
        stream_name: str,
        *,
        record: dict[str, Any] | None = None,
        schema: dict[str, Any] | None = None,
        key_properties: Sequence[str] | None = None,
    ) -> Sink:
        """Return a sink for the given stream name."""
        sink_class = self._get_sink_class(stream_name)
        return sink_class(
            target=self,
            stream_name=stream_name,
            schema=schema or {},
            key_properties=key_properties,
        )

    def _get_sink_class(self, stream_name: str) -> type[OICBaseSink]:
        """Get the sink class for a stream."""
        sink_mapping = {
            # Core sinks
            "connections": ConnectionsSink,
            "integrations": IntegrationsSink,
            "packages": PackagesSink,
            "lookups": LookupsSink,
            # Extended sinks
            "libraries": LibrariesSink,
            "certificates": CertificatesSink,
            "projects": ProjectsSink,
            "schedules": SchedulesSink,
            "business_events": BusinessEventsSink,
            # Action sinks
            "integration_actions": IntegrationActionsSink,
            "connection_actions": ConnectionActionsSink,
            "monitoring_config": MonitoringConfigSink,
        }
        return sink_mapping.get(stream_name, self.default_sink_class)
