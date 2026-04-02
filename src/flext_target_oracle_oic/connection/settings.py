"""Oracle OIC connection configuration using flext-core patterns.

Copyright (m) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import MutableSequence
from typing import Annotated

from pydantic import Field

from flext_core import FlextLogger, r
from flext_target_oracle_oic import c, m, t

logger = FlextLogger(__name__)


class FlextTargetOracleOicConnectionSettings(m):
    """Oracle OIC connection settings using flext-core patterns."""

    base_url: Annotated[t.NonEmptyStr, Field(..., description="Oracle OIC base URL")]
    client_id: Annotated[t.NonEmptyStr, Field(..., description="OAuth2 client ID")]
    client_secret: Annotated[
        t.NonEmptyStr,
        Field(..., description="OAuth2 client secret", repr=False),
    ]
    scope: Annotated[
        str,
        Field(
            default=c.TargetOracleOic.DEFAULT_OAUTH_SCOPE,
            description="OAuth2 scope",
        ),
    ]
    username: Annotated[
        str | None,
        Field(default=None, description="Optional username for basic auth"),
    ]
    password: Annotated[
        str | None,
        Field(default=None, description="Optional password for basic auth", repr=False),
    ]
    use_oauth2: Annotated[
        bool,
        Field(default=True, description="Use OAuth2 authentication"),
    ]
    timeout: Annotated[
        t.PositiveInt,
        Field(
            default=c.DEFAULT_TIMEOUT_SECONDS,
            description="Request timeout in seconds",
        ),
    ]
    max_retries: Annotated[
        t.RetryCount,
        Field(
            default=c.MAX_RETRY_ATTEMPTS,
            description="Maximum number of retries",
        ),
    ]
    verify_ssl: Annotated[
        bool,
        Field(default=True, description="Verify SSL certificates"),
    ]

    @classmethod
    def from_dict(
        cls,
        data: t.ConfigurationMapping,
    ) -> FlextTargetOracleOicConnectionSettings:
        """Create configuration from dictionary using modern Pydantic patterns."""
        try:
            return cls(**data)
        except c.Meltano.Singer.SAFE_EXCEPTIONS:
            logger.exception(
                "Failed to create FlextTargetOracleOicConnectionSettings from dict",
            )
            raise

    def build_api_base_url(self) -> str:
        """Build OIC API base URL."""
        url = self.base_url.rstrip("/")
        return f"{url}{c.TargetOracleOic.API_PATH_INTEGRATION}"

    def build_auth_url(self) -> str:
        """Build OAuth2 authentication URL."""
        url = self.base_url.rstrip("/")
        return f"{url}{c.TargetOracleOic.API_PATH_OAUTH_TOKEN}"

    def get_api_headers(self, access_token: str) -> t.StrMapping:
        """Get API request headers with authentication."""
        return {
            c.TargetOracleOic.HEADER_AUTHORIZATION: f"{c.TargetOracleOic.AUTH_SCHEME_BEARER} {access_token}",
            c.TargetOracleOic.HEADER_CONTENT_TYPE: c.TargetOracleOic.HEADER_CONTENT_TYPE_JSON,
            c.TargetOracleOic.HEADER_ACCEPT: c.TargetOracleOic.HEADER_CONTENT_TYPE_JSON,
        }

    def get_auth_headers(self) -> t.StrMapping:
        """Get authentication headers."""
        return {
            c.TargetOracleOic.HEADER_CONTENT_TYPE: c.TargetOracleOic.HEADER_CONTENT_TYPE_FORM,
            c.TargetOracleOic.HEADER_ACCEPT: c.TargetOracleOic.HEADER_CONTENT_TYPE_JSON,
        }

    def validate_business_rules(self) -> r[bool]:
        """Validate OIC connection configuration business rules."""
        errors: MutableSequence[str] = []
        if not self.base_url:
            errors.append("base_url is required")
        elif not self.base_url.startswith(("http://", "https://")):
            errors.append("base_url must be a valid URL")
        if not self.client_id:
            errors.append("client_id is required")
        if not self.client_secret:
            errors.append("client_secret is required")
        if errors:
            return r[bool].fail(
                f"OIC connection config validation failed: {'; '.join(errors)}",
            )
        return r[bool].ok(value=True)
