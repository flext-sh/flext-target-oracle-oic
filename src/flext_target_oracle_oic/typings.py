"""FLEXT Target Oracle OIC Types - Domain-specific Singer Oracle OIC target type definitions.

This module provides Singer Oracle OIC target-specific type definitions extending t.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends t properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes as _t

# =============================================================================
# TARGET ORACLE OIC-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer Oracle OIC target operations
# =============================================================================


# Singer Oracle OIC target domain TypeVars
class FlextTargetOracleOicTypes(_t):
    """Singer Oracle OIC target-specific type definitions extending t.

    Domain-specific type system for Singer Oracle OIC target operations.
    Contains ONLY complex Oracle OIC target-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # SINGER TARGET TYPES - Complex Singer target protocol types
    # =========================================================================

    class TargetOracleOic:
        """Singer target protocol complex types."""

        type TargetConfiguration = dict[
            str, str | int | bool | dict[str, _t.Types.GeneralValueType]
        ]
        type StreamConfiguration = dict[
            str,
            str | bool | dict[str, _t.Types.JsonValue],
        ]
        type MessageProcessing = dict[str, str | list[dict[str, _t.Types.JsonValue]]]
        type RecordHandling = dict[str, str | dict[str, _t.Types.JsonValue] | bool]
        type StateManagement = dict[str, str | dict[str, _t.Types.JsonValue]]
        type BatchProcessing = dict[str, str | int | dict[str, _t.Types.JsonValue]]

    # =========================================================================
    # ORACLE OIC INTEGRATION TYPES - Complex Oracle OIC integration types
    # =========================================================================

    class OicIntegration:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[
            str, str | int | bool | dict[str, _t.Types.GeneralValueType]
        ]
        type IntegrationDefinition = dict[
            str,
            str | list[str] | dict[str, _t.Types.JsonValue],
        ]
        type IntegrationFlow = dict[str, str | dict[str, _t.Types.JsonValue]]
        type IntegrationMapping = dict[str, str | dict[str, _t.Types.GeneralValueType]]
        type IntegrationMetadata = dict[str, str | dict[str, _t.Types.JsonValue]]
        type IntegrationStatus = dict[
            str, str | bool | dict[str, _t.Types.GeneralValueType]
        ]

    # =========================================================================
    # OIC CONNECTION TYPES - Complex Oracle OIC connection types
    # =========================================================================

    class OicConnection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str, str | int | bool | dict[str, _t.Types.GeneralValueType]
        ]
        type ConnectionCredentials = dict[str, str | dict[str, _t.Types.JsonValue]]
        type ConnectionSecurity = dict[
            str, str | bool | dict[str, _t.Types.GeneralValueType]
        ]
        type ConnectionValidation = dict[
            str, bool | str | dict[str, _t.Types.GeneralValueType]
        ]
        type ConnectionMetadata = dict[str, str | dict[str, _t.Types.JsonValue]]
        type ConnectionPool = dict[
            str, int | bool | dict[str, _t.Types.GeneralValueType]
        ]

    # =========================================================================
    # OIC AUTHENTICATION TYPES - Complex OAuth2/IDCS authentication types
    # =========================================================================

    class OicAuthentication:
        """Oracle OIC authentication complex types."""

        type OAuth2Configuration = dict[
            str, str | int | dict[str, _t.Types.GeneralValueType]
        ]
        type IdcsConfiguration = dict[str, str | bool | dict[str, _t.Types.JsonValue]]
        type TokenManagement = dict[
            str, str | int | dict[str, _t.Types.GeneralValueType]
        ]
        type AuthenticationFlow = dict[str, str | dict[str, _t.Types.JsonValue]]
        type SecuritySettings = dict[
            str, bool | str | dict[str, _t.Types.GeneralValueType]
        ]
        type AuthenticationCache = dict[
            str, str | int | dict[str, _t.Types.GeneralValueType]
        ]

    # =========================================================================
    # OIC DEPLOYMENT TYPES - Complex Oracle OIC deployment types
    # =========================================================================

    class OicDeployment:
        """Oracle OIC deployment complex types."""

        type DeploymentConfiguration = dict[
            str, str | bool | dict[str, _t.Types.GeneralValueType]
        ]
        type ArtifactManagement = dict[str, str | dict[str, _t.Types.JsonValue]]
        type DeploymentValidation = dict[
            str, bool | str | dict[str, _t.Types.GeneralValueType]
        ]
        type PackageDeployment = dict[str, str | dict[str, _t.Types.JsonValue]]
        type DeploymentStatus = dict[
            str, str | bool | dict[str, _t.Types.GeneralValueType]
        ]
        type RollbackStrategy = dict[str, str | dict[str, _t.Types.GeneralValueType]]

    # =========================================================================
    # DATA TRANSFORMATION TYPES - Complex data transformation types
    # =========================================================================

    class DataTransformation:
        """Data transformation complex types."""

        type TransformationConfiguration = dict[
            str, str | bool | dict[str, _t.Types.GeneralValueType]
        ]
        type FieldMapping = dict[
            str, str | list[str] | dict[str, _t.Types.GeneralValueType]
        ]
        type DataValidation = dict[str, str | dict[str, _t.Types.JsonValue]]
        type TypeConversion = dict[
            str, bool | str | dict[str, _t.Types.GeneralValueType]
        ]
        type FilteringRules = dict[str, str | dict[str, _t.Types.JsonValue]]
        type TransformationResult = dict[str, dict[str, _t.Types.JsonValue]]

    # =========================================================================
    # STREAM PROCESSING TYPES - Complex stream handling types
    # =========================================================================

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str, str | bool | int | dict[str, _t.Types.GeneralValueType]
        ]
        type StreamMetadata = dict[str, str | dict[str, _t.Types.JsonValue]]
        type StreamRecord = dict[
            str, _t.Types.JsonValue | dict[str, _t.Types.GeneralValueType]
        ]
        type StreamState = dict[str, str | int | dict[str, _t.Types.JsonValue]]
        type StreamBookmark = dict[
            str, str | int | dict[str, _t.Types.GeneralValueType]
        ]
        type StreamSchema = dict[str, str | dict[str, _t.Types.JsonValue] | bool]

    # =========================================================================
    # ERROR HANDLING TYPES - Complex error management types
    # =========================================================================

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str, bool | str | int | dict[str, _t.Types.GeneralValueType]
        ]
        type ErrorRecovery = dict[
            str, str | bool | dict[str, _t.Types.GeneralValueType]
        ]
        type ErrorReporting = dict[str, str | int | dict[str, _t.Types.JsonValue]]
        type ErrorClassification = dict[
            str, str | int | dict[str, _t.Types.GeneralValueType]
        ]
        type ErrorMetrics = dict[str, int | float | dict[str, _t.Types.JsonValue]]
        type ErrorTracking = list[dict[str, str | int | dict[str, _t.Types.JsonValue]]]

    # =========================================================================
    # SINGER TARGET ORACLE OIC PROJECT TYPES - Domain-specific project types extending t
    # =========================================================================

    class Project:
        """Singer Target Oracle OIC-specific project types.

        Adds Singer target Oracle OIC-specific project types.
        Follows domain separation principle:
        Singer target Oracle OIC domain owns OIC loading and Singer protocol-specific types.
        """

        # Singer target Oracle OIC-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from t
            "library",
            "application",
            "service",
            # Singer target Oracle OIC-specific types
            "singer-target",
            "oic-loader",
            "integration-loader",
            "singer-target-oracle-oic",
            "target-oracle-oic",
            "oic-connector",
            "integration-connector",
            "singer-protocol",
            "oic-integration",
            "oracle-oic",
            "cloud-integration",
            "singer-stream",
            "etl-target",
            "data-pipeline",
            "oic-sink",
            "singer-integration",
        ]

        # Singer target Oracle OIC-specific Literal type aliases (referencing constants.py StrEnums)
        type AuthMethodLiteral = Literal["oauth2"]
        type IntegrationStatusLiteral = Literal[
            "active", "inactive", "error", "configured", "activated"
        ]
        type IntegrationPatternLiteral = Literal[
            "ORCHESTRATION",
            "MAP_MY_DATA",
            "PUBLISH_TO_OIC",
            "SUBSCRIBE_TO_OIC",
        ]
        type ScheduleTypeLiteral = Literal["ONCE", "RECURRING", "CRON"]
        type IntegrationActionLiteral = Literal[
            "activate", "deactivate", "test", "clone"
        ]
        type MetadataActionLiteral = Literal["test", "refresh_metadata"]
        type DataOperationLiteral = Literal[
            "create_only", "update_only", "create_or_update"
        ]
        type ErrorTypeLiteral = Literal["AUTHENTICATION", "AUTHORIZATION", "NETWORK"]

        # Singer target Oracle OIC-specific project configurations
        type SingerTargetOracleOicProjectConfig = dict[str, _t.Types.GeneralValueType]
        type OicLoaderConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[
            str, bool | str | dict[str, _t.Types.GeneralValueType]
        ]
        type TargetOracleOicPipelineConfig = dict[str, _t.Types.GeneralValueType]


# Alias for simplified usage
t = FlextTargetOracleOicTypes

# Namespace composition via class inheritance
# TargetOracleOic namespace provides access to nested classes through inheritance
# Access patterns:
# - t.TargetOracleOic.* for Target Oracle OIC-specific types
# - t.Project.* for project types
# - t.Core.* for core types (inherited from parent)

# =============================================================================
# PUBLIC API EXPORTS - Singer Oracle OIC target TypeVars and types
# =============================================================================

__all__ = [
    "FlextTargetOracleOicTypes",
    "t",
]
