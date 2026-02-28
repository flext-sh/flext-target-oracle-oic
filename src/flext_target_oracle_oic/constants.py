"""Constants for target Oracle OIC."""

from __future__ import annotations

from flext_meltano import FlextMeltanoConstants
from flext_oracle_oic import FlextOracleOicConstants


class FlextTargetOracleOicConstants(FlextMeltanoConstants, FlextOracleOicConstants):
    """Namespace class for OIC target constants."""

    class TargetOracleOic:
        """Target Oracle OIC domain constants."""

        # Stream names
        STREAM_CONNECTIONS: str = "connections"
        STREAM_INTEGRATIONS: str = "integrations"
        STREAM_PACKAGES: str = "packages"
        STREAM_LOOKUPS: str = "lookups"

        # Target identifier
        TARGET_NAME: str = "target-oracle-oic"

        # Authentication
        AUTH_SCHEME_BEARER: str = "Bearer"
        DEFAULT_OAUTH_SCOPE: str = "oic_instance"

        # HTTP Headers
        HEADER_CONTENT_TYPE: str = "Content-Type"
        HEADER_CONTENT_TYPE_FORM: str = "application/x-www-form-urlencoded"
        HEADER_CONTENT_TYPE_JSON: str = "application/json"
        HEADER_ACCEPT: str = "Accept"
        HEADER_AUTHORIZATION: str = "Authorization"

        # API Paths
        API_PATH_OAUTH_TOKEN: str = "/oauth2/v1/token"
        API_PATH_INTEGRATION: str = "/ic/api/integration/v1"

        # Default model values
        DEFAULT_VERSION: str = "01.00.0000"
        DEFAULT_PATTERN: str = "ORCHESTRATION"
        DEFAULT_SCHEDULE_TYPE: str = "ONCE"


c = FlextTargetOracleOicConstants

__all__ = ["FlextTargetOracleOicConstants", "c"]
