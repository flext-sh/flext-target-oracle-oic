"""FlextTargetOracleOicUtilities - Singer target utilities for Oracle Integration Cloud operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import ClassVar

from flext_core import FlextConstants, FlextResult, FlextTypes, FlextUtilities


class FlextTargetOracleOicUtilities(FlextUtilities):
    """Single unified utilities class for Singer target Oracle Integration Cloud operations.

    This class provides comprehensive Oracle OIC target functionality for Singer protocol
    integration, including OAuth2 authentication, integration artifact deployment,
    connection management, and API operations with comprehensive security patterns.

    Oracle OIC Domain Specialization:
    - Enterprise OAuth2/IDCS authentication with secure token management
    - Oracle Integration Cloud artifact deployment and lifecycle management
    - High-performance API operations with rate limiting and connection pooling
    - Singer protocol compliance with stream-to-integration mapping
    - OIC-specific error handling with comprehensive retry strategies
    - Enterprise security with OAuth2 token lifecycle management
    - OIC performance monitoring and optimization patterns

    Attributes:
        OIC_DEFAULT_API_TIMEOUT: Default API operation timeout (180 seconds)
        OIC_DEFAULT_BATCH_SIZE: Default batch size for bulk operations (25)
        OAUTH2_TOKEN_REFRESH_THRESHOLD: Threshold for token refresh (300 seconds)
        MAX_API_RETRIES: Maximum API retry attempts (5)
        DEFAULT_CONNECTION_POOL_SIZE: Default connection pool size (5)

    """

    OIC_DEFAULT_API_TIMEOUT: ClassVar[int] = 180
    OIC_DEFAULT_BATCH_SIZE: ClassVar[int] = 25
    OAUTH2_TOKEN_REFRESH_THRESHOLD: ClassVar[int] = 300
    MAX_API_RETRIES: ClassVar[int] = 5
    DEFAULT_CONNECTION_POOL_SIZE: ClassVar[int] = 5
    OIC_API_RATE_LIMIT_PER_MINUTE: ClassVar[int] = 100
    DEFAULT_CIRCUIT_BREAKER_THRESHOLD: ClassVar[int] = 10

    class SingerUtilities:
        """Singer protocol utilities for Oracle OIC target operations."""

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: dict[str, object],
            key_properties: list[str] | None = None,
        ) -> dict[str, object]:
            """Create Singer SCHEMA message for OIC integration definition.

            Args:
                stream_name: Name of the Singer stream
                schema: JSON schema definition for the stream
                key_properties: List of key property names

            Returns:
                Singer SCHEMA message dictionary

            """
            return {
                "type": "SCHEMA",
                "stream": stream_name,
                "schema": schema,
                "key_properties": key_properties or [],
                "bookmark_properties": [],
            }

        @staticmethod
        def create_record_message(
            stream_name: str,
            record: dict[str, object],
            time_extracted: str | None = None,
        ) -> dict[str, object]:
            """Create Singer RECORD message for OIC integration deployment.

            Args:
                stream_name: Name of the Singer stream
                record: Integration record to deploy
                time_extracted: Optional extraction timestamp

            Returns:
                Singer RECORD message dictionary

            """
            message = {
                "type": "RECORD",
                "stream": stream_name,
                "record": record,
            }
            if time_extracted:
                message["time_extracted"] = time_extracted
            return message

        @staticmethod
        def create_state_message(state: dict[str, object]) -> dict[str, object]:
            """Create Singer STATE message for OIC target checkpointing.

            Args:
                state: State data for checkpointing

            Returns:
                Singer STATE message dictionary

            """
            return {"type": "STATE", "value": state}

        @staticmethod
        def validate_singer_message(
            message: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Validate Singer message format and required fields.

            Args:
                message: Singer message to validate

            Returns:
                FlextResult containing validated message or error

            """
            if not isinstance(message, dict):
                return FlextResult[dict[str, object]].fail(
                    "Singer message must be a dictionary"
                )

            message_type = message.get("type")
            if message_type not in {"SCHEMA", "RECORD", "STATE"}:
                return FlextResult[dict[str, object]].fail(
                    f"Invalid Singer message type: {message_type}"
                )

            if message_type == "SCHEMA":
                required_fields = ["stream", "schema"]
                for field in required_fields:
                    if field not in message:
                        return FlextResult[dict[str, object]].fail(
                            f"Missing required field for SCHEMA: {field}"
                        )

            elif message_type == "RECORD":
                required_fields = ["stream", "record"]
                for field in required_fields:
                    if field not in message:
                        return FlextResult[dict[str, object]].fail(
                            f"Missing required field for RECORD: {field}"
                        )

            elif message_type == "STATE":
                if "value" not in message:
                    return FlextResult[dict[str, object]].fail(
                        "Missing required field for STATE: value"
                    )

            return FlextResult[dict[str, object]].ok(message)

    class OicIntegrationProcessing:
        """Oracle OIC integration-specific processing utilities."""

        @staticmethod
        def map_singer_stream_to_oic_integration(
            stream_name: str,
            schema: dict[str, object],
            oic_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Map Singer stream to Oracle OIC integration configuration.

            Args:
                stream_name: Name of the Singer stream
                schema: Singer stream schema
                oic_config: OIC-specific configuration

            Returns:
                FlextResult containing OIC integration mapping or error

            """
            try:
                integration_mapping = {
                    "integration_id": f"{stream_name.upper()}_INTEGRATION",
                    "integration_name": stream_name.replace("_", " ").title(),
                    "stream_name": stream_name,
                    "schema": schema,
                    "oic_configuration": oic_config,
                    "integration_type": oic_config.get("integration_type", "scheduled"),
                    "activation_mode": oic_config.get("activation_mode", "automatic"),
                }

                return FlextResult[dict[str, object]].ok(integration_mapping)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"Failed to map Singer stream to OIC integration: {e}"
                )

        @staticmethod
        def generate_oic_integration_package(
            integration_config: dict[str, object], artifacts: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Generate Oracle OIC integration package from Singer data.

            Args:
                integration_config: OIC integration configuration
                artifacts: Integration artifacts and components

            Returns:
                FlextResult containing OIC package information or error

            """
            try:
                package_info = {
                    "package_id": integration_config.get("integration_id"),
                    "package_name": f"{integration_config.get('integration_name', 'Integration')}.iar",
                    "package_version": "1.0.0",
                    "package_type": "INTEGRATION_ARCHIVE",
                    "components": artifacts.get("components", []),
                    "connections": artifacts.get("connections", []),
                    "lookups": artifacts.get("lookups", []),
                    "libraries": artifacts.get("libraries", []),
                    "certificates": artifacts.get("certificates", []),
                }

                # Validate package components
                if not package_info["components"]:
                    return FlextResult[dict[str, object]].fail(
                        "Integration package must have at least one component"
                    )

                return FlextResult[dict[str, object]].ok(package_info)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"Failed to generate OIC integration package: {e}"
                )

        @staticmethod
        def transform_record_for_oic_deployment(
            record: dict[str, object], deployment_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Transform Singer record for Oracle OIC deployment.

            Args:
                record: Singer record data
                deployment_config: OIC deployment configuration

            Returns:
                FlextResult containing transformed record or error

            """
            try:
                transformed = {
                    "deployment_target": deployment_config.get(
                        "target_environment", "production"
                    ),
                    "activation_mode": deployment_config.get(
                        "activation_mode", "automatic"
                    ),
                    "import_mode": deployment_config.get(
                        "import_mode", "create_or_update"
                    ),
                    "enable_tracing": deployment_config.get("enable_tracing", False),
                    "record_data": record,
                }

                # Transform specific OIC fields
                if "integration_id" in record:
                    transformed["oic_integration_id"] = record["integration_id"].upper()

                if "package_file" in record:
                    transformed["iar_file_path"] = record["package_file"]

                if "connections" in record:
                    transformed["connection_configs"] = record["connections"]

                return FlextResult[dict[str, object]].ok(transformed)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"Failed to transform record for OIC deployment: {e}"
                )

    class OAuth2Utilities:
        """OAuth2 authentication utilities for Oracle OIC operations."""

        @staticmethod
        def validate_oauth2_config(
            config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Validate OAuth2 configuration for Oracle OIC.

            Args:
                config: OAuth2 configuration

            Returns:
                FlextResult containing validated config or error

            """
            required_fields = ["client_id", "client_secret", "token_url", "audience"]
            for field in required_fields:
                if field not in config or not config[field]:
                    return FlextResult[dict[str, object]].fail(
                        f"Missing required OAuth2 config field: {field}"
                    )

            # Validate URLs
            token_url = config["token_url"]
            if not token_url.startswith(("https://", "http://")):
                return FlextResult[dict[str, object]].fail(
                    "OAuth2 token URL must be a valid HTTP/HTTPS URL"
                )

            return FlextResult[dict[str, object]].ok(config)

        @staticmethod
        def generate_oauth2_token_request(
            config: dict[str, object], grant_type: str = "client_credentials"
        ) -> FlextResult[dict[str, object]]:
            """Generate OAuth2 token request for Oracle IDCS.

            Args:
                config: OAuth2 configuration
                grant_type: OAuth2 grant type (default: client_credentials)

            Returns:
                FlextResult containing token request or error

            """
            try:
                token_request = {
                    "grant_type": grant_type,
                    "client_id": config["client_id"],
                    "client_secret": config["client_secret"],
                    "scope": config.get(
                        "scope", "https://oracle.com/cloud/integration/"
                    ),
                }

                if "audience" in config:
                    token_request["audience"] = config["audience"]

                return FlextResult[dict[str, object]].ok(token_request)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"Failed to generate OAuth2 token request: {e}"
                )

        @staticmethod
        def validate_oauth2_token_response(
            response: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Validate OAuth2 token response from Oracle IDCS.

            Args:
                response: OAuth2 token response

            Returns:
                FlextResult containing validated token info or error

            """
            try:
                required_fields = ["access_token", "token_type"]
                for field in required_fields:
                    if field not in response:
                        return FlextResult[dict[str, object]].fail(
                            f"Missing required token field: {field}"
                        )

                # Validate token type
                if response["token_type"].lower() != "bearer":
                    return FlextResult[dict[str, object]].fail(
                        "Invalid token type, expected 'Bearer'"
                    )

                # Extract token metadata
                token_info = {
                    "access_token": response["access_token"],
                    "token_type": response["token_type"],
                    "expires_in": response.get("expires_in", 3600),
                    "scope": response.get("scope", ""),
                }

                # Calculate expiration time
                expires_in = token_info["expires_in"]
                expiration_time = datetime.now(UTC) + timedelta(seconds=expires_in)
                token_info["expires_at"] = expiration_time.isoformat()

                return FlextResult[dict[str, object]].ok(token_info)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"Failed to validate OAuth2 token response: {e}"
                )

        @staticmethod
        def check_token_expiration(
            token_info: dict[str, object],
        ) -> FlextResult[bool]:
            """Check if OAuth2 token needs refresh.

            Args:
                token_info: Token information with expiration

            Returns:
                FlextResult containing boolean indicating if refresh needed

            """
            try:
                if "expires_at" not in token_info:
                    return FlextResult[bool].fail(
                        "Token expiration information not available"
                    )

                expiration_time = datetime.fromisoformat(token_info["expires_at"])
                current_time = datetime.now(UTC)

                # Check if token expires within threshold
                threshold_seconds = (
                    FlextTargetOracleOicUtilities.OAUTH2_TOKEN_REFRESH_THRESHOLD
                )
                time_until_expiry = (expiration_time - current_time).total_seconds()

                needs_refresh = time_until_expiry <= threshold_seconds
                return FlextResult[bool].ok(needs_refresh)

            except Exception as e:
                return FlextResult[bool].fail(f"Failed to check token expiration: {e}")

    class ApiUtilities:
        """Oracle OIC API utilities for operations and requests."""

        @staticmethod
        def create_oic_api_headers(
            access_token: str,
            additional_headers: dict[str, str] | None = None,
        ) -> FlextResult[dict[str, str]]:
            """Create headers for Oracle OIC API requests.

            Args:
                access_token: OAuth2 access token
                additional_headers: Optional additional headers

            Returns:
                FlextResult containing API headers or error

            """
            try:
                headers = {
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "User-Agent": "FLEXT-Target-Oracle-OIC/0.9.0",
                }

                if additional_headers:
                    headers.update(additional_headers)

                return FlextResult[dict[str, str]].ok(headers)

            except Exception as e:
                return FlextResult[dict[str, str]].fail(
                    f"Failed to create OIC API headers: {e}"
                )

        @staticmethod
        def validate_oic_api_response(
            response: dict[str, object],
            expected_status_codes: FlextTypes.IntList | None = None,
        ) -> FlextResult[dict[str, object]]:
            """Validate Oracle OIC API response.

            Args:
                response: API response data
                expected_status_codes: List of expected status codes

            Returns:
                FlextResult containing validated response or error

            """
            try:
                expected_codes = expected_status_codes or [200, 201, 202]

                # Check if response has status code
                status_code = response.get("status_code", 200)
                if status_code not in expected_codes:
                    error_message = response.get("error", {}).get(
                        "message", "Unknown API error"
                    )
                    return FlextResult[dict[str, object]].fail(
                        f"OIC API error (HTTP {status_code}): {error_message}"
                    )

                # Extract response data
                response_data = response.get("data", response)

                return FlextResult[dict[str, object]].ok(response_data)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"Failed to validate OIC API response: {e}"
                )

        @staticmethod
        def calculate_api_retry_delay(
            attempt: int, base_delay: float = 2.0, max_delay: float = 60.0
        ) -> FlextResult[float]:
            """Calculate exponential backoff delay for API retries.

            Args:
                attempt: Current retry attempt number (starting from 1)
                base_delay: Base delay in seconds
                max_delay: Maximum delay in seconds

            Returns:
                FlextResult containing calculated delay or error

            """
            try:
                if attempt <= 0:
                    return FlextResult[float].fail("Retry attempt must be positive")

                # Exponential backoff: base_delay * (2 ^ (attempt - 1))
                delay = base_delay * (2 ** (attempt - 1))

                # Cap at maximum delay
                actual_delay = min(delay, max_delay)

                return FlextResult[float].ok(actual_delay)

            except Exception as e:
                return FlextResult[float].fail(f"Failed to calculate retry delay: {e}")

    class StreamUtilities:
        """Singer stream processing utilities for Oracle OIC target."""

        @staticmethod
        def process_schema_stream(
            stream_name: str,
            schema_message: dict[str, object],
            oic_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Process Singer schema stream for OIC integration configuration.

            Args:
                stream_name: Name of the Singer stream
                schema_message: Singer SCHEMA message
                oic_config: OIC-specific configuration

            Returns:
                FlextResult containing processed schema information or error

            """
            try:
                schema = schema_message.get("schema", {})
                key_properties = schema_message.get("key_properties", [])

                # Map to OIC integration
                integration_result = FlextTargetOracleOicUtilities.OicIntegrationProcessing.map_singer_stream_to_oic_integration(
                    stream_name, schema, oic_config
                )
                if integration_result.is_failure:
                    return FlextResult[dict[str, object]].fail(
                        f"Integration mapping failed: {integration_result.error}"
                    )

                processed_schema = {
                    "stream_name": stream_name,
                    "oic_integration_config": integration_result.unwrap(),
                    "key_properties": key_properties,
                    "properties": schema.get("properties", {}),
                    "stream_metadata": {
                        "extraction_method": oic_config.get("extraction_method", "api"),
                        "replication_method": oic_config.get(
                            "replication_method", "full_table"
                        ),
                    },
                }

                return FlextResult[dict[str, object]].ok(processed_schema)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"Failed to process schema stream: {e}"
                )

        @staticmethod
        def batch_records_for_oic_deployment(
            records: list[dict[str, object]], batch_size: int | None = None
        ) -> FlextResult[list[list[dict[str, object]]]]:
            """Batch Singer records for efficient OIC deployment operations.

            Args:
                records: List of Singer records
                batch_size: Size of each batch (default: OIC_DEFAULT_BATCH_SIZE)

            Returns:
                FlextResult containing list of batches or error

            """
            actual_batch_size = (
                batch_size or FlextTargetOracleOicUtilities.OIC_DEFAULT_BATCH_SIZE
            )

            if actual_batch_size <= 0:
                return FlextResult[list[list[dict[str, object]]]].fail(
                    "Batch size must be positive"
                )

            try:
                batches = []
                for i in range(0, len(records), actual_batch_size):
                    batch = records[i : i + actual_batch_size]
                    batches.append(batch)

                return FlextResult[list[list[dict[str, object]]]].ok(batches)

            except Exception as e:
                return FlextResult[list[list[dict[str, object]]]].fail(
                    f"Failed to batch records: {e}"
                )

    class ConfigValidation:
        """Configuration validation utilities for Oracle OIC target."""

        @staticmethod
        def validate_oic_connection_config(
            config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Validate Oracle OIC connection configuration.

            Args:
                config: OIC connection configuration

            Returns:
                FlextResult containing validated config or error

            """
            required_fields = [
                "base_url",
                "oauth_client_id",
                "oauth_client_secret",
                "oauth_token_url",
            ]
            for field in required_fields:
                if field not in config or not config[field]:
                    return FlextResult[dict[str, object]].fail(
                        f"Missing required OIC config field: {field}"
                    )

            # Validate URLs
            base_url = config["base_url"]
            if not base_url.startswith("https://"):
                return FlextResult[dict[str, object]].fail(
                    "OIC base URL must use HTTPS"
                )

            token_url = config["oauth_token_url"]
            if not token_url.startswith(("https://", "http://")):
                return FlextResult[dict[str, object]].fail(
                    "OAuth token URL must be a valid HTTP/HTTPS URL"
                )

            return FlextResult[dict[str, object]].ok(config)

        @staticmethod
        def validate_oic_target_config(
            config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Validate Oracle OIC target-specific configuration.

            Args:
                config: OIC target configuration

            Returns:
                FlextResult containing validated config or error

            """
            # Validate batch size
            batch_size = config.get(
                "batch_size", FlextTargetOracleOicUtilities.OIC_DEFAULT_BATCH_SIZE
            )
            if batch_size <= 0 or batch_size > FlextConstants.Batch.DEFAULT_SIZE:
                return FlextResult[dict[str, object]].fail(
                    f"Batch size must be between 1 and {FlextConstants.Batch.DEFAULT_SIZE}"
                )

            # Validate timeout
            timeout = config.get(
                "request_timeout", FlextTargetOracleOicUtilities.OIC_DEFAULT_API_TIMEOUT
            )
            if timeout <= 0 or timeout > FlextConstants.Web.TOTAL_TIMEOUT:
                return FlextResult[dict[str, object]].fail(
                    f"Request timeout must be between 1 and {FlextConstants.Web.TOTAL_TIMEOUT} seconds"
                )

            # Validate retry configuration
            max_retries = config.get(
                "max_retries", FlextTargetOracleOicUtilities.MAX_API_RETRIES
            )
            if max_retries < 0 or max_retries > FlextConstants.Batch.SMALL_SIZE:
                return FlextResult[dict[str, object]].fail(
                    f"Max retries must be between 0 and {FlextConstants.Batch.SMALL_SIZE}"
                )

            return FlextResult[dict[str, object]].ok(config)

    class StateManagement:
        """Singer state management utilities for Oracle OIC target."""

        @staticmethod
        def create_oic_target_state(
            deployment_states: dict[str, object],
            target_metadata: dict[str, object] | None = None,
        ) -> FlextResult[dict[str, object]]:
            """Create Oracle OIC target state for Singer checkpointing.

            Args:
                deployment_states: Dictionary of deployment states
                target_metadata: Optional target-specific metadata

            Returns:
                FlextResult containing OIC target state or error

            """
            try:
                state = {
                    "deployments": deployment_states,
                    "target_type": "oracle_oic",
                    "last_updated": datetime.now(UTC).isoformat(),
                }

                if target_metadata:
                    state["target_metadata"] = target_metadata

                return FlextResult[dict[str, object]].ok(state)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"Failed to create OIC target state: {e}"
                )

        @staticmethod
        def update_deployment_state(
            current_state: dict[str, object],
            integration_id: str,
            deployment_result: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Update state for a specific integration deployment.

            Args:
                current_state: Current Singer state
                integration_id: ID of the integration
                deployment_result: Deployment result data

            Returns:
                FlextResult containing updated state or error

            """
            try:
                updated_state = current_state.copy()

                if "deployments" not in updated_state:
                    updated_state["deployments"] = {}

                updated_state["deployments"][integration_id] = {
                    "deployment_result": deployment_result,
                    "last_updated": datetime.now(UTC).isoformat(),
                    "deployment_status": deployment_result.get("status", "unknown"),
                }

                return FlextResult[dict[str, object]].ok(updated_state)

            except Exception as e:
                return FlextResult[dict[str, object]].fail(
                    f"Failed to update deployment state: {e}"
                )

    class PerformanceUtilities:
        """Oracle OIC performance optimization utilities."""

        @staticmethod
        def calculate_optimal_api_batch_size(
            integration_size_bytes: int,
            available_memory_mb: int = 50,
        ) -> FlextResult[int]:
            """Calculate optimal batch size for OIC API operations.

            Args:
                integration_size_bytes: Average size of integration artifact in bytes
                available_memory_mb: Available memory for batching in MB

            Returns:
                FlextResult containing optimal batch size or error

            """
            try:
                if integration_size_bytes <= 0:
                    return FlextResult[int].fail("Integration size must be positive")

                if available_memory_mb <= 0:
                    return FlextResult[int].fail("Available memory must be positive")

                available_memory_bytes = available_memory_mb * 1024 * 1024
                max_batch_size = available_memory_bytes // integration_size_bytes

                # Ensure batch size is within OIC API limits
                optimal_batch_size = max(
                    1,
                    min(
                        max_batch_size,
                        FlextTargetOracleOicUtilities.OIC_DEFAULT_BATCH_SIZE,
                    ),
                )

                return FlextResult[int].ok(optimal_batch_size)

            except Exception as e:
                return FlextResult[int].fail(
                    f"Failed to calculate optimal batch size: {e}"
                )

        @staticmethod
        def calculate_api_rate_limit_delay(
            requests_per_minute: int,
            _current_request_count: int,
        ) -> FlextResult[float]:
            """Calculate delay to respect OIC API rate limits.

            Args:
                requests_per_minute: API rate limit (requests per minute)
                _current_request_count: Current number of requests made

            Returns:
                FlextResult containing delay in seconds or error

            """
            try:
                if requests_per_minute <= 0:
                    return FlextResult[float].fail(
                        "Requests per minute must be positive"
                    )

                # Calculate delay to spread requests evenly across the minute
                delay_seconds = 60.0 / requests_per_minute

                # Add small deterministic jitter to avoid thundering herd
                jitter = (hash(str(_current_request_count)) % 10) / 100.0  # 0.0 to 0.1
                actual_delay = delay_seconds + jitter

                return FlextResult[float].ok(actual_delay)

            except Exception as e:
                return FlextResult[float].fail(
                    f"Failed to calculate rate limit delay: {e}"
                )

    # Proxy methods for backward compatibility (minimal)
    def validate_singer_message(
        self, message: dict[str, object]
    ) -> FlextResult[dict[str, object]]:
        """Proxy to SingerUtilities.validate_singer_message."""
        return self.SingerUtilities.validate_singer_message(message)

    def validate_oauth2_config(
        self, config: dict[str, object]
    ) -> FlextResult[dict[str, object]]:
        """Proxy to OAuth2Utilities.validate_oauth2_config."""
        return self.OAuth2Utilities.validate_oauth2_config(config)

    def validate_oic_connection_config(
        self, config: dict[str, object]
    ) -> FlextResult[dict[str, object]]:
        """Proxy to ConfigValidation.validate_oic_connection_config."""
        return self.ConfigValidation.validate_oic_connection_config(config)
