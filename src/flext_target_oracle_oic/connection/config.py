"""Oracle OIC connection configuration using flext-core patterns."""

from __future__ import annotations

from flext_core import FlextResult, FlextValueObject, get_logger
from pydantic import Field

logger = get_logger(__name__)


class OICConnectionSettings(FlextValueObject):
    """Oracle OIC connection settings using flext-core patterns."""

    base_url: str = Field(..., description="Oracle OIC base URL")
    client_id: str = Field(..., description="OAuth2 client ID")
    client_secret: str = Field(..., description="OAuth2 client secret", repr=False)
    scope: str = Field(default="oic_instance", description="OAuth2 scope")
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
    timeout: int = Field(default=30, description="Request timeout in seconds", gt=0)
    max_retries: int = Field(default=3, description="Maximum number of retries", ge=0)
    verify_ssl: bool = Field(default=True, description="Verify SSL certificates")

    def build_auth_url(self) -> str:
        """Build OAuth2 authentication URL."""
        url = self.base_url.rstrip("/")
        return f"{url}/oauth2/v1/token"

    def build_api_base_url(self) -> str:
        """Build OIC API base URL."""
        url = self.base_url.rstrip("/")
        return f"{url}/ic/api/integration/v1"

    def get_auth_headers(self) -> dict[str, str]:
        """Get authentication headers."""
        return {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }

    def get_api_headers(self, access_token: str) -> dict[str, str]:
        """Get API request headers with authentication."""
        return {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> OICConnectionSettings:
        """Create configuration from dictionary using modern Pydantic patterns."""
        try:
            return cls.model_validate(data)
        except Exception:
            logger.exception("Failed to create OICConnectionSettings from dict")
            raise

    def validate_business_rules(self) -> FlextResult[None]:
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
            return FlextResult[None].fail(
                f"OIC connection config validation failed: {'; '.join(errors)}",
            )

        return FlextResult[None].ok(None)
