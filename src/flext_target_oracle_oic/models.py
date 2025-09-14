"""Compatibility facade: re-export target_models via models.py.

Standardizes imports to use flext_target_oracle_oic.models across the codebase.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_oic.target_models import (
    OICConnection,
    OICConnectionAction,
    OICDataTransformation,
    OICIntegration,
    OICIntegrationAction,
    OICLookup,
    OICPackage,
    OICProject,
    OICSchedule,
    OICSchemaMapping,
)

__all__ = [
    "OICConnection",
    "OICConnectionAction",
    "OICDataTransformation",
    "OICIntegration",
    "OICIntegrationAction",
    "OICLookup",
    "OICPackage",
    "OICProject",
    "OICSchedule",
    "OICSchemaMapping",
]
