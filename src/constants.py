"""Enhanced Oracle OIC Target constants extending FlextConstants.

Contains comprehensive constants for Oracle OIC target operations with
enhanced organization, validation limits, and security considerations.
"""

from __future__ import annotations

from typing import Any, Final

from flext_core import FlextConstants

# Re-export for convenience
__all__ = ["FlextTargetOracleOICConstants"]


class FlextTargetOracleOICConstants(FlextConstants):
    """Enhanced Oracle OIC Target constants extending FlextConstants.

    Contains comprehensive constants for Oracle OIC target operations with
    enhanced organization, validation limits, and security considerations.
    """

    # Project identification
    PROJECT_PREFIX: Final[str] = "FLEXT_TARGET_ORACLE_OIC"
    PROJECT_NAME: Final[str] = "FLEXT Oracle OIC Target"
    PROJECT_VERSION: Final[str] = "1.0.0"
    PROJECT_DESCRIPTION: Final[str] = "Oracle OIC target for FLEXT data pipeline"

    # Oracle OIC Connection Configuration
    class OracleOIC:
        """Oracle OIC specific constants with comprehensive configuration."""

        # Connection defaults
        DEFAULT_TIMEOUT: Final[int] = 30
        DEFAULT_MAX_RETRIES: Final[int] = 3
        DEFAULT_BATCH_SIZE: Final[int] = 100
        DEFAULT_CONNECTION_POOL_SIZE: Final[int] = 10
        DEFAULT_CONNECTION_POOL_MAX: Final[int] = 20

        # Connection limits
        MIN_TIMEOUT: Final[int] = 1
        MAX_TIMEOUT: Final[int] = 3600
        MIN_MAX_RETRIES: Final[int] = 0
        MAX_MAX_RETRIES: Final[int] = 10
        MIN_BATCH_SIZE: Final[int] = 1
        MAX_BATCH_SIZE: Final[int] = 10000
        MIN_CONNECTION_POOL_SIZE: Final[int] = 1
        MAX_CONNECTION_POOL_SIZE: Final[int] = 100
        MIN_CONNECTION_POOL_MAX: Final[int] = 1
        MAX_CONNECTION_POOL_MAX: Final[int] = 100

        # String length limits
        MAX_BASE_URL_LENGTH: Final[int] = 500
        MAX_CLIENT_ID_LENGTH: Final[int] = 255
        MAX_CLIENT_SECRET_LENGTH: Final[int] = 255
        MAX_TOKEN_URL_LENGTH: Final[int] = 500
        MAX_SCOPE_LENGTH: Final[int] = 500

        # API configuration
        DEFAULT_API_VERSION: Final[str] = "v1"
        SUPPORTED_API_VERSIONS: Final[list[str]] = ["v1", "v2"]

        # SSL configuration
        DEFAULT_SSL_VERIFY: Final[bool] = True
        DEFAULT_SSL_TIMEOUT: Final[int] = 30

    # OAuth Configuration
    class OAuth:
        """OAuth configuration constants."""

        # Grant types
        GRANT_TYPE_CLIENT_CREDENTIALS: Final[str] = "client_credentials"
        GRANT_TYPE_AUTHORIZATION_CODE: Final[str] = "authorization_code"
        GRANT_TYPE_PASSWORD: Final[str] = "password"
        GRANT_TYPE_REFRESH_TOKEN: Final[str] = "refresh_token"

        # Valid grant types
        VALID_GRANT_TYPES: Final[set[str]] = {
            GRANT_TYPE_CLIENT_CREDENTIALS,
            GRANT_TYPE_AUTHORIZATION_CODE,
            GRANT_TYPE_PASSWORD,
            GRANT_TYPE_REFRESH_TOKEN,
        }

        # Default grant type
        DEFAULT_GRANT_TYPE: Final[str] = GRANT_TYPE_CLIENT_CREDENTIALS

        # Token configuration
        DEFAULT_TOKEN_EXPIRY_BUFFER: Final[int] = 300  # 5 minutes
        MIN_TOKEN_EXPIRY_BUFFER: Final[int] = 0
        MAX_TOKEN_EXPIRY_BUFFER: Final[int] = 3600  # 1 hour

        # OAuth endpoints
        DEFAULT_TOKEN_ENDPOINT: Final[str] = "/oauth2/v1/token"
        DEFAULT_AUTHORIZATION_ENDPOINT: Final[str] = "/oauth2/v1/authorize"

        # OAuth headers
        CONTENT_TYPE_FORM_URLENCODED: Final[str] = "application/x-www-form-urlencoded"
        CONTENT_TYPE_JSON: Final[str] = "application/json"
        ACCEPT_JSON: Final[str] = "application/json"

    # OIC Entity Types
    class EntityTypes:
        """OIC entity type constants."""

        # Entity types
        INTEGRATION: Final[str] = "integration"
        CONNECTION: Final[str] = "connection"
        LOOKUP: Final[str] = "lookup"
        PACKAGE: Final[str] = "package"
        FLOW: Final[str] = "flow"
        SCHEDULE: Final[str] = "schedule"
        TRIGGER: Final[str] = "trigger"

        # Valid entity types
        VALID_ENTITY_TYPES: Final[set[str]] = {
            INTEGRATION,
            CONNECTION,
            LOOKUP,
            PACKAGE,
            FLOW,
            SCHEDULE,
            TRIGGER,
        }

        # Entity type descriptions
        ENTITY_TYPE_DESCRIPTIONS: Final[dict[str, str]] = {
            INTEGRATION: "Oracle Integration Cloud integration",
            CONNECTION: "Oracle Integration Cloud connection",
            LOOKUP: "Oracle Integration Cloud lookup",
            PACKAGE: "Oracle Integration Cloud package",
            FLOW: "Oracle Integration Cloud flow",
            SCHEDULE: "Oracle Integration Cloud schedule",
            TRIGGER: "Oracle Integration Cloud trigger",
        }

    # Import Modes
    class ImportModes:
        """Import mode constants."""

        # Import modes
        CREATE: Final[str] = "create"
        UPDATE: Final[str] = "update"
        CREATE_OR_UPDATE: Final[str] = "create_or_update"
        REPLACE: Final[str] = "replace"

        # Valid import modes
        VALID_IMPORT_MODES: Final[set[str]] = {
            CREATE,
            UPDATE,
            CREATE_OR_UPDATE,
            REPLACE,
        }

        # Default import mode
        DEFAULT_IMPORT_MODE: Final[str] = CREATE_OR_UPDATE

        # Import mode descriptions
        IMPORT_MODE_DESCRIPTIONS: Final[dict[str, str]] = {
            CREATE: "Create new entities only",
            UPDATE: "Update existing entities only",
            CREATE_OR_UPDATE: "Create new or update existing entities",
            REPLACE: "Replace all entities",
        }

    # Operation Types
    class OperationTypes:
        """Operation type constants."""

        # Operation types
        DEPLOY: Final[str] = "DEPLOY"
        SYNC: Final[str] = "SYNC"
        VALIDATE: Final[str] = "VALIDATE"
        CLEANUP: Final[str] = "CLEANUP"

        # Valid operation types
        VALID_OPERATION_TYPES: Final[set[str]] = {
            DEPLOY,
            SYNC,
            VALIDATE,
            CLEANUP,
        }

        # Operation status
        STATUS_PENDING: Final[str] = "PENDING"
        STATUS_RUNNING: Final[str] = "RUNNING"
        STATUS_COMPLETED: Final[str] = "COMPLETED"
        STATUS_FAILED: Final[str] = "FAILED"
        STATUS_CANCELLED: Final[str] = "CANCELLED"

        # Valid operation statuses
        VALID_OPERATION_STATUSES: Final[set[str]] = {
            STATUS_PENDING,
            STATUS_RUNNING,
            STATUS_COMPLETED,
            STATUS_FAILED,
            STATUS_CANCELLED,
        }

        # Operation timeouts
        DEFAULT_OPERATION_TIMEOUT: Final[int] = 1800  # 30 minutes
        MIN_OPERATION_TIMEOUT: Final[int] = 60  # 1 minute
        MAX_OPERATION_TIMEOUT: Final[int] = 7200  # 2 hours

    # Record Operations
    class RecordOperations:
        """Record operation constants."""

        # Record operation types
        CREATE: Final[str] = "CREATE"
        UPDATE: Final[str] = "UPDATE"
        DELETE: Final[str] = "DELETE"
        UPSERT: Final[str] = "UPSERT"

        # Valid record operations
        VALID_RECORD_OPERATIONS: Final[set[str]] = {
            CREATE,
            UPDATE,
            DELETE,
            UPSERT,
        }

        # Default record operation
        DEFAULT_RECORD_OPERATION: Final[str] = CREATE

        # Record operation descriptions
        RECORD_OPERATION_DESCRIPTIONS: Final[dict[str, str]] = {
            CREATE: "Create new record",
            UPDATE: "Update existing record",
            DELETE: "Delete record",
            UPSERT: "Create or update record",
        }

    # Batch Processing Configuration
    class BatchProcessing:
        """Batch processing specific constants."""

        # Batch status
        BATCH_STATUS_PENDING: Final[str] = "PENDING"
        BATCH_STATUS_PROCESSING: Final[str] = "PROCESSING"
        BATCH_STATUS_COMPLETED: Final[str] = "COMPLETED"
        BATCH_STATUS_FAILED: Final[str] = "FAILED"
        BATCH_STATUS_CANCELLED: Final[str] = "CANCELLED"

        # Valid batch statuses
        VALID_BATCH_STATUSES: Final[set[str]] = {
            BATCH_STATUS_PENDING,
            BATCH_STATUS_PROCESSING,
            BATCH_STATUS_COMPLETED,
            BATCH_STATUS_FAILED,
            BATCH_STATUS_CANCELLED,
        }

        # Batch size limits
        MIN_BATCH_SIZE: Final[int] = 1
        MAX_BATCH_SIZE: Final[int] = 10000
        DEFAULT_BATCH_SIZE: Final[int] = 100
        OPTIMAL_BATCH_SIZE: Final[int] = 500

        # Batch processing timeouts
        DEFAULT_BATCH_TIMEOUT: Final[int] = 300  # 5 minutes
        MIN_BATCH_TIMEOUT: Final[int] = 30  # 30 seconds
        MAX_BATCH_TIMEOUT: Final[int] = 3600  # 1 hour

        # Batch retry configuration
        DEFAULT_BATCH_RETRIES: Final[int] = 3
        MAX_BATCH_RETRIES: Final[int] = 10
        BATCH_RETRY_DELAY: Final[float] = 5.0  # seconds

    # Performance Configuration
    class Performance:
        """Performance configuration constants."""

        # Throughput limits
        DEFAULT_RECORDS_PER_SECOND: Final[int] = 10
        MAX_RECORDS_PER_SECOND: Final[int] = 1000
        MIN_RECORDS_PER_SECOND: Final[int] = 1

        # Memory limits
        DEFAULT_MEMORY_LIMIT_MB: Final[int] = 512
        MAX_MEMORY_LIMIT_MB: Final[int] = 4096
        MIN_MEMORY_LIMIT_MB: Final[int] = 128

        # CPU limits
        DEFAULT_CPU_LIMIT_PERCENT: Final[int] = 80
        MAX_CPU_LIMIT_PERCENT: Final[int] = 100
        MIN_CPU_LIMIT_PERCENT: Final[int] = 10

        # Connection limits
        DEFAULT_MAX_CONNECTIONS: Final[int] = 50
        MAX_MAX_CONNECTIONS: Final[int] = 500
        MIN_MAX_CONNECTIONS: Final[int] = 1

        # Parallel processing
        DEFAULT_MAX_WORKERS: Final[int] = 4
        MAX_MAX_WORKERS: Final[int] = 16
        MIN_MAX_WORKERS: Final[int] = 1

        # Performance thresholds
        PERFORMANCE_WARNING_THRESHOLD: Final[float] = 2000.0  # milliseconds
        PERFORMANCE_CRITICAL_THRESHOLD: Final[float] = 10000.0  # milliseconds
        MEMORY_WARNING_THRESHOLD: Final[float] = 80.0  # percentage
        MEMORY_CRITICAL_THRESHOLD: Final[float] = 95.0  # percentage

    # Security Configuration
    class Security:
        """Security configuration constants."""

        # SSL/TLS
        DEFAULT_SSL_VERIFY: Final[bool] = True
        DEFAULT_SSL_TIMEOUT: Final[int] = 30
        SUPPORTED_SSL_PROTOCOLS: Final[list[str]] = ["TLSv1.2", "TLSv1.3"]

        # Authentication
        DEFAULT_AUTH_TIMEOUT: Final[int] = 300  # 5 minutes
        MAX_AUTH_ATTEMPTS: Final[int] = 5
        AUTH_LOCKOUT_DURATION: Final[int] = 900  # 15 minutes

        # Token security
        DEFAULT_TOKEN_EXPIRY_BUFFER: Final[int] = 300  # 5 minutes
        MIN_TOKEN_EXPIRY_BUFFER: Final[int] = 0
        MAX_TOKEN_EXPIRY_BUFFER: Final[int] = 3600  # 1 hour

        # Audit logging
        DEFAULT_AUDIT_LOGGING: Final[bool] = True
        AUDIT_LOG_RETENTION_DAYS: Final[int] = 90

        # Data masking
        DEFAULT_DATA_MASKING: Final[bool] = True
        SENSITIVE_FIELD_PATTERNS: Final[list[str]] = [
            "password",
            "secret",
            "key",
            "token",
            "credential",
            "client_secret",
        ]

    # Error Handling Configuration
    class ErrorHandling:
        """Error handling configuration constants."""

        # Error types
        ERROR_TYPE_VALIDATION: Final[str] = "VALIDATION_ERROR"
        ERROR_TYPE_CONNECTION: Final[str] = "CONNECTION_ERROR"
        ERROR_TYPE_TIMEOUT: Final[str] = "TIMEOUT_ERROR"
        ERROR_TYPE_AUTHENTICATION: Final[str] = "AUTHENTICATION_ERROR"
        ERROR_TYPE_AUTHORIZATION: Final[str] = "AUTHORIZATION_ERROR"
        ERROR_TYPE_DATA: Final[str] = "DATA_ERROR"
        ERROR_TYPE_SYSTEM: Final[str] = "SYSTEM_ERROR"
        ERROR_TYPE_DEPLOYMENT: Final[str] = "DEPLOYMENT_ERROR"

        # Valid error types
        VALID_ERROR_TYPES: Final[set[str]] = {
            ERROR_TYPE_VALIDATION,
            ERROR_TYPE_CONNECTION,
            ERROR_TYPE_TIMEOUT,
            ERROR_TYPE_AUTHENTICATION,
            ERROR_TYPE_AUTHORIZATION,
            ERROR_TYPE_DATA,
            ERROR_TYPE_SYSTEM,
            ERROR_TYPE_DEPLOYMENT,
        }

        # Error retry configuration
        DEFAULT_ERROR_RETRIES: Final[int] = 3
        MAX_ERROR_RETRIES: Final[int] = 10
        ERROR_RETRY_DELAY: Final[float] = 5.0  # seconds
        ERROR_RETRY_BACKOFF_MULTIPLIER: Final[float] = 2.0

        # Error logging
        DEFAULT_ERROR_LOGGING: Final[bool] = True
        MAX_ERROR_MESSAGE_LENGTH: Final[int] = 1000
        ERROR_LOG_RETENTION_DAYS: Final[int] = 30

    # Monitoring Configuration
    class Monitoring:
        """Monitoring configuration constants."""

        # Metrics collection
        DEFAULT_METRICS_INTERVAL: Final[int] = 60  # seconds
        MIN_METRICS_INTERVAL: Final[int] = 10  # seconds
        MAX_METRICS_INTERVAL: Final[int] = 3600  # 1 hour

        # Health checks
        DEFAULT_HEALTH_CHECK_INTERVAL: Final[int] = 30  # seconds
        HEALTH_CHECK_TIMEOUT: Final[int] = 5  # seconds
        HEALTH_CHECK_RETRIES: Final[int] = 3

        # Performance monitoring
        DEFAULT_PERFORMANCE_MONITORING: Final[bool] = True
        PERFORMANCE_METRICS_RETENTION_DAYS: Final[int] = 30

        # Alert thresholds
        DEFAULT_ALERT_THRESHOLD: Final[float] = 2000.0  # milliseconds
        CRITICAL_ALERT_THRESHOLD: Final[float] = 10000.0  # milliseconds
        ERROR_RATE_THRESHOLD: Final[float] = 5.0  # percentage

    # Validation Configuration
    class Validation:
        """Validation configuration constants."""

        # String length limits
        MIN_NAME_LENGTH: Final[int] = 1
        MAX_NAME_LENGTH: Final[int] = 255
        MIN_DESCRIPTION_LENGTH: Final[int] = 0
        MAX_DESCRIPTION_LENGTH: Final[int] = 1000

        # Numeric limits
        MIN_PERCENTAGE: Final[float] = 0.0
        MAX_PERCENTAGE: Final[float] = 100.0
        MIN_COUNT: Final[int] = 0
        MAX_COUNT: Final[int] = 1000000

        # URL validation
        MIN_URL_LENGTH: Final[int] = 1
        MAX_URL_LENGTH: Final[int] = 500

        # Entity validation
        MIN_ENTITY_ID_LENGTH: Final[int] = 1
        MAX_ENTITY_ID_LENGTH: Final[int] = 255
        MIN_ENTITY_TYPE_LENGTH: Final[int] = 1
        MAX_ENTITY_TYPE_LENGTH: Final[int] = 100

        # Validation patterns
        ENTITY_TYPE_PATTERN: Final[str] = r"^[a-zA-Z][a-zA-Z0-9_]*$"
        ENTITY_ID_PATTERN: Final[str] = r"^[a-zA-Z0-9][a-zA-Z0-9_-]*$"
        URL_PATTERN: Final[str] = r"^https?://[a-zA-Z0-9.-]+(:[0-9]+)?(/.*)?$"

    # Environment Configuration
    class Environment:
        """Environment configuration constants."""

        # Environment types
        ENV_DEVELOPMENT: Final[str] = "development"
        ENV_STAGING: Final[str] = "staging"
        ENV_PRODUCTION: Final[str] = "production"
        ENV_TESTING: Final[str] = "testing"
        ENV_LOCAL: Final[str] = "local"

        # Valid environments
        VALID_ENVIRONMENTS: Final[set[str]] = {
            ENV_DEVELOPMENT,
            ENV_STAGING,
            ENV_PRODUCTION,
            ENV_TESTING,
            ENV_LOCAL,
        }

        # Environment-specific defaults
        ENV_DEFAULTS: Final[dict[str, dict[str, Any]]] = {
            ENV_DEVELOPMENT: {
                "debug_mode": True,
                "verify_ssl": False,
                "enable_logging": True,
                "batch_size": 10,
                "timeout": 30,
                "max_retries": 3,
                "dry_run_mode": False,
            },
            ENV_STAGING: {
                "debug_mode": False,
                "verify_ssl": True,
                "enable_logging": True,
                "batch_size": 50,
                "timeout": 60,
                "max_retries": 5,
                "dry_run_mode": False,
            },
            ENV_PRODUCTION: {
                "debug_mode": False,
                "verify_ssl": True,
                "enable_logging": True,
                "batch_size": 100,
                "timeout": 120,
                "max_retries": 10,
                "dry_run_mode": False,
            },
            ENV_TESTING: {
                "debug_mode": True,
                "verify_ssl": False,
                "enable_logging": False,
                "batch_size": 5,
                "timeout": 15,
                "max_retries": 1,
                "dry_run_mode": True,
            },
            ENV_LOCAL: {
                "debug_mode": True,
                "verify_ssl": False,
                "enable_logging": True,
                "batch_size": 10,
                "timeout": 30,
                "max_retries": 2,
                "dry_run_mode": False,
            },
        }

    # Error Messages
    class ErrorMessages:
        """Error message constants."""

        # Connection errors
        CONNECTION_FAILED = "Failed to connect to Oracle OIC"
        CONNECTION_TIMEOUT = "Connection to Oracle OIC timed out"
        CONNECTION_REFUSED = "Connection to Oracle OIC was refused"
        CONNECTION_LOST = "Connection to Oracle OIC was lost"

        # Authentication errors
        AUTHENTICATION_FAILED = "Authentication to Oracle OIC failed"
        AUTHENTICATION_TIMEOUT = "Authentication to Oracle OIC timed out"
        INVALID_CREDENTIALS = "Invalid Oracle OIC credentials"
        TOKEN_EXPIRED = "Oracle OIC token has expired"

        # Data errors
        DATA_VALIDATION_FAILED = "Data validation failed"
        DATA_TRANSFORMATION_FAILED = "Data transformation failed"
        DATA_DEPLOYMENT_FAILED = "Data deployment to Oracle OIC failed"

        # Configuration errors
        CONFIGURATION_INVALID = "Invalid Oracle OIC target configuration"
        CONFIGURATION_MISSING = "Required Oracle OIC configuration missing"
        CONFIGURATION_TYPE_ERROR = "Oracle OIC configuration type error"

        # Operation errors
        OPERATION_FAILED = "Oracle OIC target operation failed"
        OPERATION_TIMEOUT = "Oracle OIC target operation timed out"
        OPERATION_CANCELLED = "Oracle OIC target operation was cancelled"

        # Deployment errors
        DEPLOYMENT_FAILED = "Oracle OIC deployment failed"
        DEPLOYMENT_VALIDATION_FAILED = "Oracle OIC deployment validation failed"
        DEPLOYMENT_TIMEOUT = "Oracle OIC deployment timed out"

        # Entity errors
        ENTITY_VALIDATION_FAILED = "Entity validation failed"
        ENTITY_TRANSFORMATION_FAILED = "Entity transformation failed"
        ENTITY_DEPLOYMENT_FAILED = "Entity deployment failed"

        # General errors
        UNKNOWN_ERROR = "Unknown error occurred in Oracle OIC target"
        INTERNAL_ERROR = "Internal error in Oracle OIC target"
        EXTERNAL_SERVICE_ERROR = "External service error"
        NETWORK_ERROR = "Network error occurred"
