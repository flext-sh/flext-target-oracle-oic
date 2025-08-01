"""Oracle OIC connection configuration using flext-core patterns."""

from __future__ import annotations

from typing import Any

# Import from flext-core for foundational patterns
from flext_core import FlextValueObject, get_logger

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
        return cls(**data)
