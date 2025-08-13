"""Oracle OIC connection configuration using flext-core patterns."""

from __future__ import annotations

from flext_core import FlextResult, FlextValueObject, get_logger

logger = get_logger(__name__)


class OICConnectionConfig(FlextValueObject):
    """Oracle OIC connection configuration using flext-core patterns."""

    server_url: str
    client_id: str
    client_secret: str
    scope: str = "oic_instance"
    username: str | None = None
    password: str | None = None
    use_oauth2: bool = True
    timeout: int = 30
    max_retries: int = 3
    verify_ssl: bool = True

    def build_auth_url(self) -> str:
        """Build OAuth2 authentication URL."""
        base_url = self.server_url.rstrip("/")
        return f"{base_url}/oauth2/v1/token"

    def build_api_base_url(self) -> str:
        """Build OIC API base URL."""
        base_url = self.server_url.rstrip("/")
        return f"{base_url}/ic/api/integration/v1"

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

    def to_dict(self) -> dict[str, object]:
        """Convert configuration to dictionary."""
        return self.model_dump()

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> OICConnectionConfig:
        """Create configuration from dictionary."""
        try:
            return cls(
                server_url=str(data.get("server_url", "")),
                client_id=str(data.get("client_id", "")),
                client_secret=str(data.get("client_secret", "")),
                scope=str(data.get("scope", "oic_instance")),
                username=str(data["username"]) if data.get("username") else None,
                password=str(data["password"]) if data.get("password") else None,
                use_oauth2=bool(data.get("use_oauth2", True)),
                timeout=int(str(data.get("timeout", 30))),
                max_retries=int(str(data.get("max_retries", 3))),
                verify_ssl=bool(data.get("verify_ssl", True)),
            )
        except (ValueError, TypeError, KeyError):
            logger.exception("Failed to create OICConnectionConfig from dict")
            raise

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate OIC connection configuration business rules."""
        errors = []

        if not self.server_url:
            errors.append("server_url is required")
        elif not self.server_url.startswith(("http://", "https://")):
            errors.append("server_url must be a valid URL")

        if not self.client_id:
            errors.append("client_id is required")

        if not self.client_secret:
            errors.append("client_secret is required")

        if self.timeout <= 0:
            errors.append("timeout must be positive")

        if self.max_retries < 0:
            errors.append("max_retries must be non-negative")

        if errors:
            return FlextResult.fail(
                f"OIC connection config validation failed: {'; '.join(errors)}",
            )

        return FlextResult.ok(None)
