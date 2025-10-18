"""FLEXT Target Oracle OIC Constants - Oracle OIC target loading constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Final

from flext_core import FlextConstants
from flext_oracle_oic import FlextOracleOicConstants


class FlextTargetOracleOicConstants(FlextConstants):
    """Oracle OIC target loading-specific constants following flext-core patterns.

    Enhanced Oracle OIC Target constants extending FlextConstants with
    comprehensive organization, validation limits, and security considerations.

    Composes with FlextOracleOicConstants to avoid duplication and ensure consistency.
    """

    # Project identification (Final attributes inherited from FlextConstants)
    PROJECT_VERSION: Final[str] = "1.0.0"
    PROJECT_DESCRIPTION: Final[str] = "Oracle OIC target for FLEXT data pipeline"

    class OracleOic:
        """Oracle OIC specific constants with comprehensive configuration."""

        # Connection defaults from FlextOracleOicConstants
        DEFAULT_TIMEOUT: Final[int] = FlextOracleOicConstants.OIC.DEFAULT_TIMEOUT
        DEFAULT_MAX_RETRIES: Final[int] = (
            FlextOracleOicConstants.OIC.DEFAULT_MAX_RETRIES
        )
        DEFAULT_BATCH_SIZE: Final[int] = FlextOracleOicConstants.OIC.DEFAULT_PAGE_SIZE
        DEFAULT_CONNECTION_POOL_SIZE: Final[int] = 10
        DEFAULT_CONNECTION_POOL_MAX: Final[int] = 20

        # Connection limits
        MIN_TIMEOUT: Final[int] = FlextOracleOicConstants.OIC.MIN_REQUEST_TIMEOUT
        MAX_TIMEOUT: Final[int] = FlextOracleOicConstants.OIC.MAX_REQUEST_TIMEOUT
        MIN_MAX_RETRIES: Final[int] = FlextOracleOicConstants.OIC.MIN_MAX_RETRIES
        MAX_MAX_RETRIES: Final[int] = FlextOracleOicConstants.OIC.MAX_MAX_RETRIES
        MIN_BATCH_SIZE: Final[int] = FlextOracleOicConstants.OIC.MIN_PAGE_SIZE
        MAX_BATCH_SIZE: Final[int] = FlextOracleOicConstants.OIC.MAX_PAGE_SIZE
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

        # API configuration from FlextOracleOicConstants
        DEFAULT_API_VERSION: Final[str] = (
            FlextOracleOicConstants.OIC.DEFAULT_API_VERSION
        )
        SUPPORTED_API_VERSIONS: Final[list[str]] = (
            FlextOracleOicConstants.OIC.SUPPORTED_API_VERSIONS
        )

        # SSL configuration
        DEFAULT_SSL_VERIFY: Final[bool] = FlextOracleOicConstants.OIC.DEFAULT_VERIFY_SSL
        DEFAULT_SSL_TIMEOUT: Final[int] = FlextOracleOicConstants.OIC.DEFAULT_TIMEOUT

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

        # Token configuration from FlextOracleOicConstants
        DEFAULT_TOKEN_EXPIRY_BUFFER: Final[int] = 300  # 5 minutes
        MIN_TOKEN_EXPIRY_BUFFER: Final[int] = (
            FlextOracleOicConstants.Auth.MIN_TOKEN_EXPIRY_SECONDS
        )
        MAX_TOKEN_EXPIRY_BUFFER: Final[int] = (
            FlextOracleOicConstants.Auth.MAX_TOKEN_EXPIRY_SECONDS
        )

        # OAuth endpoints
        DEFAULT_TOKEN_ENDPOINT: Final[str] = "/oauth2/v1/token"
        DEFAULT_AUTHORIZATION_ENDPOINT: Final[str] = "/oauth2/v1/authorize"

        # OAuth headers from FlextOracleOicConstants
        CONTENT_TYPE_FORM_URLENCODED: Final[str] = (
            FlextOracleOicConstants.API.CONTENT_TYPE_FORM
        )
        CONTENT_TYPE_JSON: Final[str] = FlextOracleOicConstants.API.CONTENT_TYPE_JSON
        ACCEPT_JSON: Final[str] = FlextOracleOicConstants.API.CONTENT_TYPE_JSON

        # HTTP status codes
        HTTP_NOT_FOUND: Final[int] = 404
        HTTP_BAD_REQUEST: Final[int] = 400
        HTTP_ERROR_STATUS_THRESHOLD: Final[int] = 400

        # MIME types
        JSON_MIME: Final[str] = "application/json"

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

        # Operation status from FlextOracleOicConstants
        STATUS_PENDING: Final[str] = "PENDING"
        STATUS_RUNNING: Final[str] = FlextOracleOicConstants.Integration.STATUS_RUNNING
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

        # General errors
        UNKNOWN_ERROR = "Unknown error occurred in Oracle OIC target"
        INTERNAL_ERROR = "Internal error in Oracle OIC target"
        EXTERNAL_SERVICE_ERROR = "External service error"
        NETWORK_ERROR = "Network error occurred"


__all__ = ["FlextTargetOracleOicConstants"]
