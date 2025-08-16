"""Oracle OIC client re-export module.

This module provides a consistent import path for OIC client functionality.
"""

from __future__ import annotations

from flext_target_oracle_oic.connection.connection import OICConnection as OICClient

__all__: list[str] = ["OICClient"]
