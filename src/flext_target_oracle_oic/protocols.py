"""Singer Oracle OIC target protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextResult


class FlextTargetOracleOicProtocols(FlextProtocols):
    """Singer Oracle OIC target protocols extending FlextProtocols with Oracle Integration Cloud target interfaces.

    This class provides protocol definitions for Singer Oracle OIC target operations including
    OIC data integration, service invocation, cloud resource management, and performance optimization.
    """

    @runtime_checkable
    class OicIntegrationProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle Integration Cloud integration operations."""

        def send_to_oic_integration(
            self,
            records: list[dict[str, object]],
            integration_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Send Singer records to Oracle Integration Cloud integration.

            Args:
                records: Singer records to send to OIC
                integration_config: OIC integration configuration

            Returns:
                FlextResult[dict[str, object]]: Integration response or error

            """
            ...

        def invoke_oic_service(
            self,
            service_endpoint: str,
            payload: dict[str, object],
            invocation_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Invoke Oracle Integration Cloud service endpoint.

            Args:
                service_endpoint: OIC service endpoint URL
                payload: Request payload data
                invocation_config: Service invocation configuration

            Returns:
                FlextResult[dict[str, object]]: Service response or error

            """
            ...

        def manage_oic_connection(
            self,
            connection_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Manage Oracle Integration Cloud connection lifecycle.

            Args:
                connection_config: OIC connection configuration

            Returns:
                FlextResult[dict[str, object]]: Connection status or error

            """
            ...

        def monitor_integration_flow(
            self,
            flow_id: str,
            monitoring_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Monitor Oracle Integration Cloud flow execution.

            Args:
                flow_id: OIC integration flow identifier
                monitoring_config: Flow monitoring configuration

            Returns:
                FlextResult[dict[str, object]]: Flow status or error

            """
            ...

    @runtime_checkable
    class DataTransformationProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Singer to OIC data transformation operations."""

        def transform_singer_to_oic(
            self,
            singer_record: dict[str, object],
            transformation_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Transform Singer record to OIC-compatible format.

            Args:
                singer_record: Singer record to transform
                transformation_config: Transformation configuration

            Returns:
                FlextResult[dict[str, object]]: OIC-compatible record or error

            """
            ...

        def map_stream_to_service(
            self,
            stream_name: str,
            mapping_config: dict[str, object],
        ) -> FlextResult[str]:
            """Map Singer stream to OIC service endpoint.

            Args:
                stream_name: Singer stream name
                mapping_config: Stream to service mapping configuration

            Returns:
                FlextResult[str]: OIC service endpoint or error

            """
            ...

        def handle_nested_structures(
            self,
            nested_data: dict[str, object],
            structure_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Handle nested data structures for OIC integration.

            Args:
                nested_data: Nested data structure
                structure_config: Structure handling configuration

            Returns:
                FlextResult[dict[str, object]]: Flattened OIC data or error

            """
            ...

        def validate_oic_payload(
            self,
            payload: dict[str, object],
            validation_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Validate payload for OIC service compatibility.

            Args:
                payload: Payload to validate
                validation_config: Validation configuration

            Returns:
                FlextResult[dict[str, object]]: Validation results or error

            """
            ...

    @runtime_checkable
    class CloudApiProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle Integration Cloud API operations."""

        def authenticate_with_oic(
            self,
            auth_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Authenticate with Oracle Integration Cloud.

            Args:
                auth_config: OIC authentication configuration

            Returns:
                FlextResult[dict[str, object]]: Authentication tokens or error

            """
            ...

        def call_oic_api(
            self,
            endpoint: str,
            method: str,
            data: dict[str, object],
            api_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Call Oracle Integration Cloud API endpoints.

            Args:
                endpoint: API endpoint path
                method: HTTP method
                data: Request data
                api_config: API call configuration

            Returns:
                FlextResult[dict[str, object]]: API response or error

            """
            ...

        def handle_api_rate_limiting(
            self,
            request_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Handle OIC API rate limiting and throttling.

            Args:
                request_config: Request configuration for rate limiting

            Returns:
                FlextResult[dict[str, object]]: Rate limiting status or error

            """
            ...

        def manage_api_pagination(
            self,
            pagination_config: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Manage API response pagination for large datasets.

            Args:
                pagination_config: API pagination configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Paginated results or error

            """
            ...

    @runtime_checkable
    class BatchProcessingProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for OIC batch processing operations."""

        def process_record_batch(
            self,
            records: list[dict[str, object]],
            batch_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Process batch of Singer records for OIC integration.

            Args:
                records: Batch of Singer records
                batch_config: Batch processing configuration

            Returns:
                FlextResult[dict[str, object]]: Batch processing results or error

            """
            ...

        def optimize_batch_size(
            self,
            stream_name: str,
            optimization_config: dict[str, object],
        ) -> FlextResult[int]:
            """Optimize batch size for OIC service performance.

            Args:
                stream_name: Singer stream name
                optimization_config: Batch optimization configuration

            Returns:
                FlextResult[int]: Optimal batch size or error

            """
            ...

        def handle_batch_failures(
            self,
            failed_records: list[dict[str, object]],
            failure_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Handle failed records in batch processing.

            Args:
                failed_records: Records that failed processing
                failure_config: Failure handling configuration

            Returns:
                FlextResult[dict[str, object]]: Failure handling results or error

            """
            ...

        def monitor_batch_progress(
            self,
            batch_id: str,
            monitoring_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Monitor batch processing progress.

            Args:
                batch_id: Batch processing identifier
                monitoring_config: Progress monitoring configuration

            Returns:
                FlextResult[dict[str, object]]: Progress status or error

            """
            ...

    @runtime_checkable
    class ValidationProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for OIC target validation operations."""

        def validate_integration_config(
            self,
            config: dict[str, object],
            validation_rules: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Validate OIC integration configuration.

            Args:
                config: Integration configuration to validate
                validation_rules: Configuration validation rules

            Returns:
                FlextResult[dict[str, object]]: Validation results or error

            """
            ...

        def check_service_availability(
            self,
            service_endpoint: str,
            availability_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Check OIC service endpoint availability.

            Args:
                service_endpoint: OIC service endpoint
                availability_config: Availability check configuration

            Returns:
                FlextResult[dict[str, object]]: Service availability status or error

            """
            ...

        def validate_data_schema(
            self,
            data: dict[str, object],
            schema_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Validate data against OIC service schema.

            Args:
                data: Data to validate
                schema_config: Schema validation configuration

            Returns:
                FlextResult[dict[str, object]]: Schema validation results or error

            """
            ...

        def check_authentication_status(
            self,
            auth_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Check OIC authentication status and token validity.

            Args:
                auth_config: Authentication configuration

            Returns:
                FlextResult[dict[str, object]]: Authentication status or error

            """
            ...

    @runtime_checkable
    class PerformanceProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for OIC target performance optimization operations."""

        def optimize_cloud_performance(
            self, performance_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Optimize performance for OIC cloud operations.

            Args:
                performance_config: Performance optimization configuration

            Returns:
                FlextResult[dict[str, object]]: Optimization results or error

            """
            ...

        def configure_connection_pooling(
            self, pool_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Configure connection pooling for OIC API calls.

            Args:
                pool_config: Connection pooling configuration

            Returns:
                FlextResult[dict[str, object]]: Pool configuration result or error

            """
            ...

        def monitor_target_performance(
            self, performance_metrics: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Monitor OIC target performance metrics.

            Args:
                performance_metrics: Performance monitoring data

            Returns:
                FlextResult[dict[str, object]]: Performance analysis or error

            """
            ...

        def optimize_data_transfer(
            self, transfer_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Optimize data transfer to OIC cloud services.

            Args:
                transfer_config: Data transfer optimization configuration

            Returns:
                FlextResult[dict[str, object]]: Transfer optimization results or error

            """
            ...

    @runtime_checkable
    class MonitoringProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for OIC target monitoring operations."""

        def track_target_metrics(
            self, target_id: str, metrics: dict[str, object]
        ) -> FlextResult[bool]:
            """Track OIC target operation metrics.

            Args:
                target_id: Target operation identifier
                metrics: Target metrics data

            Returns:
                FlextResult[bool]: Metric tracking success status

            """
            ...

        def monitor_cloud_health(
            self, health_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Monitor OIC cloud service health status.

            Args:
                health_config: Health monitoring configuration

            Returns:
                FlextResult[dict[str, object]]: Health status or error

            """
            ...

        def get_integration_status(
            self, integration_id: str
        ) -> FlextResult[dict[str, object]]:
            """Get OIC integration operation status.

            Args:
                integration_id: Integration identifier

            Returns:
                FlextResult[dict[str, object]]: Integration status or error

            """
            ...

        def create_monitoring_dashboard(
            self, dashboard_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Create monitoring dashboard for OIC target operations.

            Args:
                dashboard_config: Dashboard configuration

            Returns:
                FlextResult[dict[str, object]]: Dashboard creation result or error

            """
            ...

    # Convenience aliases for easier downstream usage
    TargetOracleOicIntegrationProtocol = OicIntegrationProtocol
    TargetOracleOicDataTransformationProtocol = DataTransformationProtocol
    TargetOracleOicCloudApiProtocol = CloudApiProtocol
    TargetOracleOicBatchProcessingProtocol = BatchProcessingProtocol
    TargetOracleOicValidationProtocol = ValidationProtocol
    TargetOracleOicPerformanceProtocol = PerformanceProtocol
    TargetOracleOicMonitoringProtocol = MonitoringProtocol


__all__ = [
    "FlextTargetOracleOicProtocols",
]
