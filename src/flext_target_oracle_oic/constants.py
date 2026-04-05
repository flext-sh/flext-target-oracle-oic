"""Constants for target Oracle OIC."""

from __future__ import annotations

from enum import StrEnum, unique

from flext_meltano import FlextMeltanoConstants
from flext_oracle_oic import FlextOracleOicConstants


class FlextTargetOracleOicConstants(FlextMeltanoConstants, FlextOracleOicConstants):
    """Namespace class for OIC target constants."""

    class TargetOracleOic:
        """Target Oracle OIC domain constants."""

        STREAM_CONNECTIONS: str = "connections"
        STREAM_INTEGRATIONS: str = "integrations"
        STREAM_PACKAGES: str = "packages"
        STREAM_LOOKUPS: str = "lookups"
        TARGET_NAME: str = "target-oracle-oic"
        AUTH_SCHEME_BEARER: str = "Bearer"
        DEFAULT_OAUTH_SCOPE: str = "oic_instance"
        HEADER_CONTENT_TYPE: str = "Content-Type"
        HEADER_CONTENT_TYPE_FORM: str = "application/x-www-form-urlencoded"
        HEADER_CONTENT_TYPE_JSON: str = "application/json"
        HEADER_ACCEPT: str = "Accept"
        HEADER_AUTHORIZATION: str = "Authorization"
        API_PATH_OAUTH_TOKEN: str = "/oauth2/v1/token"
        API_PATH_INTEGRATION: str = "/ic/api/integration/v1"
        DEFAULT_VERSION: str = "01.00.0000"
        DEFAULT_PATTERN: str = "ORCHESTRATION"
        DEFAULT_SCHEDULE_TYPE: str = "ONCE"
        DEFAULT_USE_OAUTH2: bool = True
        DEFAULT_VERIFY_SSL: bool = True

        @unique
        class OICConnectionAction(StrEnum):
            """Supported connection actions."""

            CREATE = "create"
            UPDATE = "update"

        @unique
        class OICIntegrationAction(StrEnum):
            """Supported integration actions."""

            IMPORT = "import"
            ACTIVATE = "activate"


c = FlextTargetOracleOicConstants
__all__ = ["FlextTargetOracleOicConstants", "c"]
