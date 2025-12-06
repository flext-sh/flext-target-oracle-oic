"""Singer Oracle OIC target protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextResult, p


class FlextTargetOracleOicProtocols:
    """Singer Target Oracle OIC protocols with explicit re-exports from p foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TargetOracleOic namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    # ============================================================================
    # SINGER TARGET ORACLE OIC-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class TargetOracleOic:
        """Singer Target Oracle OIC domain protocols for Oracle OIC loading."""

        @runtime_checkable
        class OicIntegrationProtocol(p.Service, Protocol):
            """Protocol for Oracle OIC integration."""

            def integrate(self, data: dict[str, object]) -> FlextResult[None]:
                """Integrate data with Oracle OIC."""

            def transform_to_oic(
                self,
                record: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Transform Singer record to OIC format."""

            def invoke_integration(
                self,
                payload: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Invoke OIC integration with payload."""

            def process_batch(
                self,
                records: list[dict[str, object]],
            ) -> FlextResult[None]:
                """Process batch of records for OIC."""

            def validate_payload(self, payload: dict[str, object]) -> FlextResult[bool]:
                """Validate payload for OIC compatibility."""

            def optimize_throughput(
                self,
                config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Optimize OIC throughput settings."""

            def track_integration_status(
                self,
                integration_id: str,
            ) -> FlextResult[dict[str, object]]:
                """Track integration execution status."""

    # ============================================================================
    # BACKWARD COMPATIBILITY ALIASES (100% COMPATIBILITY)
    # ============================================================================

    @runtime_checkable
    class OicIntegrationProtocol(TargetOracleOic.OicIntegrationProtocol):
        """OicIntegrationProtocol - real inheritance."""

    @runtime_checkable
    class DataTransformationProtocol(TargetOracleOic.DataTransformationProtocol):
        """DataTransformationProtocol - real inheritance."""

    @runtime_checkable
    class CloudApiProtocol(TargetOracleOic.CloudApiProtocol):
        """CloudApiProtocol - real inheritance."""

    @runtime_checkable
    class BatchProcessingProtocol(TargetOracleOic.BatchProcessingProtocol):
        """BatchProcessingProtocol - real inheritance."""

    @runtime_checkable
    class ValidationProtocol(TargetOracleOic.ValidationProtocol):
        """ValidationProtocol - real inheritance."""

    @runtime_checkable
    class PerformanceProtocol(TargetOracleOic.PerformanceProtocol):
        """PerformanceProtocol - real inheritance."""

    @runtime_checkable
    class MonitoringProtocol(TargetOracleOic.MonitoringProtocol):
        """MonitoringProtocol - real inheritance."""

    @runtime_checkable
    class TargetOracleOicIntegrationProtocol(TargetOracleOic.OicIntegrationProtocol):
        """TargetOracleOicIntegrationProtocol - real inheritance."""

    @runtime_checkable
    class TargetOracleOicDataTransformationProtocol(
        TargetOracleOic.DataTransformationProtocol,
    ):
        """TargetOracleOicDataTransformationProtocol - real inheritance.

        Exposes DataTransformationProtocol through real inheritance.
        """

    @runtime_checkable
    class TargetOracleOicCloudApiProtocol(TargetOracleOic.CloudApiProtocol):
        """TargetOracleOicCloudApiProtocol - real inheritance."""

    @runtime_checkable
    class TargetOracleOicBatchProcessingProtocol(
        TargetOracleOic.BatchProcessingProtocol,
    ):
        """TargetOracleOicBatchProcessingProtocol - real inheritance."""

    @runtime_checkable
    class TargetOracleOicValidationProtocol(TargetOracleOic.ValidationProtocol):
        """TargetOracleOicValidationProtocol - real inheritance."""

    @runtime_checkable
    class TargetOracleOicPerformanceProtocol(TargetOracleOic.PerformanceProtocol):
        """TargetOracleOicPerformanceProtocol - real inheritance."""

    @runtime_checkable
    class TargetOracleOicMonitoringProtocol(TargetOracleOic.MonitoringProtocol):
        """TargetOracleOicMonitoringProtocol - real inheritance."""


__all__ = [
    "FlextTargetOracleOicProtocols",
]
