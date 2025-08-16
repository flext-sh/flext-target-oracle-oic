"""Oracle OIC connection management using flext-core patterns."""

from __future__ import annotations

from flext_target_oracle_oic.connection.config import OICConnectionSettings
from flext_target_oracle_oic.connection.connection import OICConnection

__all__: list[str] = [
    "OICConnection",
    "OICConnectionSettings",
]
