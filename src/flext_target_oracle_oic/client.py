"""Oracle OIC client re-export module.

This module provides a consistent import path for OIC client functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes

from flext_target_oracle_oic.connection.connection import OICConnection as OICClient

__all__: FlextTypes.Core.StringList = ["OICClient"]
