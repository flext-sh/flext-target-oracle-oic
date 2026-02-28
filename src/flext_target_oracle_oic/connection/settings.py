"""Oracle OIC connection configuration using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import (
    FlextConstants,
    FlextLogger,
    FlextModels,
    FlextResult,
    t,
)
from flext_target_oracle_oic.constants import c
from pydantic import Field

logger = FlextLogger(__name__)


class OICConnectionSettings(FlextModels):
    """Oracle OIC connection settings using flext-core patterns."""

    base_url: str = Field(..., description="Oracle OIC base URL")
    client_id: str = Field(..., description="OAuth2 client ID")
    client_secret: str = Field(..., description="OAuth2 client secret", repr=False)
    scope: str = Field(
        default=c.TargetOracleOic.DEFAULT_OAUTH_SCOPE,
        description="OAuth2 scope",
    )
    username: str | None = Field(
        default=None,
        description="Optional username for basic auth",
    )
    password: str | None = Field(
        default=None,
        description="Optional password for basic auth",
        repr=False,
    )
    use_oauth2: bool = Field(default=True, description="Use OAuth2 authentication")
    timeout: int = Field(
        default=FlextConstants.Network.DEFAULT_TIMEOUT,
        description="Request timeout in seconds",
        gt=0,
    )
    max_retries: int = Field(
        default=FlextConstants.Reliability.MAX_RETRY_ATTEMPTS,
        description="Maximum number of retries",
        ge=0,
    )
    verify_ssl: bool = Field(default=True, description="Verify SSL certificates")

    def build_auth_url(self) -> str:
        """Build OAuth2 authentication URL."""
        url = self.base_url.rstrip("/")
        return f"{url}{c.TargetOracleOic.API_PATH_OAUTH_TOKEN}"

    def build_api_base_url(self) -> str:
        """Build OIC API base URL."""
        url = self.base_url.rstrip("/")
        return f"{url}{c.TargetOracleOic.API_PATH_INTEGRATION}"

    def get_auth_headers(self) -> Mapping[str, str]:
        """Get authentication headers."""
        return {
            c.TargetOracleOic.HEADER_CONTENT_TYPE: c.TargetOracleOic.HEADER_CONTENT_TYPE_FORM,
            c.TargetOracleOic.HEADER_ACCEPT: c.TargetOracleOic.HEADER_CONTENT_TYPE_JSON,
        }

    def get_api_headers(self, access_token: str) -> Mapping[str, str]:
        """Get API request headers with authentication."""
        return {
            c.TargetOracleOic.HEADER_AUTHORIZATION: f"{c.TargetOracleOic.AUTH_SCHEME_BEARER} {access_token}",
            c.TargetOracleOic.HEADER_CONTENT_TYPE: c.TargetOracleOic.HEADER_CONTENT_TYPE_JSON,
            c.TargetOracleOic.HEADER_ACCEPT: c.TargetOracleOic.HEADER_CONTENT_TYPE_JSON,
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, t.JsonValue]) -> OICConnectionSettings:
        """Create configuration from dictionary using modern Pydantic patterns."""
        try:
            return cls(**data)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ):
            logger.exception("Failed to create OICConnectionSettings from dict")
            raise

    def validate_business_rules(self) -> FlextResult[bool]:
        """Validate OIC connection configuration business rules."""
        errors: list[str] = []

        if not self.base_url:
            errors.append("base_url is required")
        elif not self.base_url.startswith(("http://", "https://")):
            errors.append("base_url must be a valid URL")

        if not self.client_id:
            errors.append("client_id is required")

        if not self.client_secret:
            errors.append("client_secret is required")

        if self.timeout <= 0:
            errors.append("timeout must be positive")

        if self.max_retries < 0:
            errors.append("max_retries must be non-negative")

        if errors:
            return FlextResult[bool].fail(
                f"OIC connection config validation failed: {'; '.join(errors)}",
            )

        return FlextResult[bool].ok(value=True)
