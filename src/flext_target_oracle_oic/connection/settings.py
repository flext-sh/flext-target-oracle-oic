"""Oracle OIC connection configuration using flext-core patterns.

Copyright (m) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import MutableSequence
from typing import Annotated, ClassVar, Self

from flext_core import FlextSettings
from flext_target_oracle_oic import c, m, p, r, t, u


@FlextSettings.auto_register("target-oracle-oic-connection")
class FlextTargetOracleOicConnectionSettings(FlextSettings):
    """Oracle OIC connection settings using flext-core patterns."""

    _logger: ClassVar[p.Logger] = u.fetch_logger(__name__)

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_TARGET_ORACLE_OIC_",
        extra="ignore",
    )

    base_url: Annotated[t.NonEmptyStr, u.Field(..., description="Oracle OIC base URL")]
    client_id: Annotated[t.NonEmptyStr, u.Field(..., description="OAuth2 client ID")]
    client_secret: Annotated[
        t.NonEmptyStr,
        u.Field(..., description="OAuth2 client secret", repr=False),
    ]
    scope: Annotated[
        str,
        u.Field(
            description="OAuth2 scope",
        ),
    ] = c.TargetOracleOic.DEFAULT_OAUTH_SCOPE
    username: Annotated[
        str | None, u.Field(description="Optional username for basic auth")
    ] = None
    password: Annotated[
        str | None, u.Field(description="Optional password for basic auth", repr=False)
    ] = None
    use_oauth2: Annotated[
        bool,
        u.Field(
            description="Use OAuth2 authentication",
        ),
    ] = c.TargetOracleOic.DEFAULT_USE_OAUTH2
    timeout: Annotated[
        t.PositiveInt,
        u.Field(
            description="Request timeout in seconds",
        ),
    ] = c.DEFAULT_TIMEOUT_SECONDS
    max_retries: Annotated[
        t.RetryCount,
        u.Field(
            description="Maximum number of retries",
        ),
    ] = c.MAX_RETRY_ATTEMPTS
    verify_ssl: Annotated[
        bool,
        u.Field(
            description="Verify SSL certificates",
        ),
    ] = c.TargetOracleOic.DEFAULT_VERIFY_SSL

    @classmethod
    def from_dict(
        cls,
        data: t.ConfigurationMapping,
    ) -> Self:
        """Create configuration from dictionary using modern Pydantic patterns."""
        try:
            return cls.model_validate(data)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS:
            cls._logger.exception(
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

    def validate_business_rules(self) -> p.Result[bool]:
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
                f"OIC connection settings validation failed: {'; '.join(errors)}",
            )
        return r[bool].ok(value=True)
