"""Singer Oracle OIC target protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextCore


class FlextTargetOracleOicProtocols:
    """Singer Target Oracle OIC protocols with explicit re-exports from FlextCore.Protocols foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TargetOracleOic namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    Foundation = FlextCore.Protocols.Foundation
    Domain = FlextCore.Protocols.Domain
    Application = FlextCore.Protocols.Application
    Infrastructure = FlextCore.Protocols.Infrastructure
    Extensions = FlextCore.Protocols.Extensions
    Commands = FlextCore.Protocols.Commands

    # ============================================================================
    # SINGER TARGET ORACLE OIC-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class TargetOracleOic:
        """Singer Target Oracle OIC domain protocols for Oracle OIC loading."""

        @runtime_checkable
        class OicIntegrationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Oracle OIC integration."""

            def integrate(
                self, data: FlextCore.Types.Dict
            ) -> FlextCore.Result[None]: ...

        @runtime_checkable
        class DataTransformationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Singer to OIC transformation."""

            def transform_to_oic(
                self, record: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]: ...

        @runtime_checkable
        class CloudApiProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for OIC cloud API operations."""

            def invoke_integration(
                self, payload: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]: ...

        @runtime_checkable
        class BatchProcessingProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for OIC batch processing."""

            def process_batch(
                self, records: list[FlextCore.Types.Dict]
            ) -> FlextCore.Result[None]: ...

        @runtime_checkable
        class ValidationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for OIC payload validation."""

            def validate_payload(
                self, payload: FlextCore.Types.Dict
            ) -> FlextCore.Result[bool]: ...

        @runtime_checkable
        class PerformanceProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for OIC performance optimization."""

            def optimize_throughput(
                self, config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]: ...

        @runtime_checkable
        class MonitoringProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for OIC loading monitoring."""

            def track_integration_status(
                self, integration_id: str
            ) -> FlextCore.Result[FlextCore.Types.Dict]: ...

    # ============================================================================
    # BACKWARD COMPATIBILITY ALIASES (100% COMPATIBILITY)
    # ============================================================================

    OicIntegrationProtocol = TargetOracleOic.OicIntegrationProtocol
    DataTransformationProtocol = TargetOracleOic.DataTransformationProtocol
    CloudApiProtocol = TargetOracleOic.CloudApiProtocol
    BatchProcessingProtocol = TargetOracleOic.BatchProcessingProtocol
    ValidationProtocol = TargetOracleOic.ValidationProtocol
    PerformanceProtocol = TargetOracleOic.PerformanceProtocol
    MonitoringProtocol = TargetOracleOic.MonitoringProtocol

    TargetOracleOicIntegrationProtocol = TargetOracleOic.OicIntegrationProtocol
    TargetOracleOicDataTransformationProtocol = (
        TargetOracleOic.DataTransformationProtocol
    )
    TargetOracleOicCloudApiProtocol = TargetOracleOic.CloudApiProtocol
    TargetOracleOicBatchProcessingProtocol = TargetOracleOic.BatchProcessingProtocol
    TargetOracleOicValidationProtocol = TargetOracleOic.ValidationProtocol
    TargetOracleOicPerformanceProtocol = TargetOracleOic.PerformanceProtocol
    TargetOracleOicMonitoringProtocol = TargetOracleOic.MonitoringProtocol


__all__ = [
    "FlextTargetOracleOicProtocols",
]
