"""FLEXT Target Oracle OIC Types - Domain-specific Singer Oracle OIC target type definitions.

This module provides Singer Oracle OIC target-specific type definitions extending FlextTypes.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextTypes properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes

# =============================================================================
# TARGET ORACLE OIC-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer Oracle OIC target operations
# =============================================================================


# Singer Oracle OIC target domain TypeVars
class FlextTargetOracleOicTypes(FlextTypes):
    """Singer Oracle OIC target-specific type definitions extending FlextTypes.

    Domain-specific type system for Singer Oracle OIC target operations.
    Contains ONLY complex Oracle OIC target-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # SINGER TARGET TYPES - Complex Singer target protocol types
    # =========================================================================

    class SingerTarget:
        """Singer target protocol complex types."""

        type TargetConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type StreamConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.Core.JsonValue]
        ]
        type MessageProcessing = dict[
            str, str | list[dict[str, FlextTypes.Core.JsonValue]]
        ]
        type RecordHandling = dict[
            str, str | dict[str, FlextTypes.Core.JsonValue] | bool
        ]
        type StateManagement = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type BatchProcessing = dict[
            str, str | int | dict[str, FlextTypes.Core.JsonValue]
        ]

    # =========================================================================
    # ORACLE OIC INTEGRATION TYPES - Complex Oracle OIC integration types
    # =========================================================================

    class OicIntegration:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type IntegrationDefinition = dict[
            str, str | list[str] | dict[str, FlextTypes.Core.JsonValue]
        ]
        type IntegrationFlow = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type IntegrationMapping = dict[str, str | dict[str, object]]
        type IntegrationMetadata = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type IntegrationStatus = dict[str, str | bool | dict[str, object]]

    # =========================================================================
    # OIC CONNECTION TYPES - Complex Oracle OIC connection types
    # =========================================================================

    class OicConnection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type ConnectionCredentials = dict[
            str, str | dict[str, FlextTypes.Core.JsonValue]
        ]
        type ConnectionSecurity = dict[
            str, str | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type ConnectionValidation = dict[str, bool | str | dict[str, object]]
        type ConnectionMetadata = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type ConnectionPool = dict[str, int | bool | dict[str, object]]

    # =========================================================================
    # OIC AUTHENTICATION TYPES - Complex OAuth2/IDCS authentication types
    # =========================================================================

    class OicAuthentication:
        """Oracle OIC authentication complex types."""

        type OAuth2Configuration = dict[
            str, str | int | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type IdcsConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.Core.JsonValue]
        ]
        type TokenManagement = dict[str, str | int | dict[str, object]]
        type AuthenticationFlow = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type SecuritySettings = dict[
            str, bool | str | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type AuthenticationCache = dict[str, str | int | dict[str, object]]

    # =========================================================================
    # OIC DEPLOYMENT TYPES - Complex Oracle OIC deployment types
    # =========================================================================

    class OicDeployment:
        """Oracle OIC deployment complex types."""

        type DeploymentConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type ArtifactManagement = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type DeploymentValidation = dict[str, bool | str | dict[str, object]]
        type PackageDeployment = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type DeploymentStatus = dict[
            str, str | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type RollbackStrategy = dict[str, str | dict[str, object]]

    # =========================================================================
    # DATA TRANSFORMATION TYPES - Complex data transformation types
    # =========================================================================

    class DataTransformation:
        """Data transformation complex types."""

        type TransformationConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type FieldMapping = dict[str, str | list[str] | dict[str, object]]
        type DataValidation = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type TypeConversion = dict[str, bool | str | dict[str, object]]
        type FilteringRules = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type TransformationResult = dict[str, dict[str, FlextTypes.Core.JsonValue]]

    # =========================================================================
    # STREAM PROCESSING TYPES - Complex stream handling types
    # =========================================================================

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str, str | bool | int | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type StreamMetadata = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type StreamRecord = dict[str, FlextTypes.Core.JsonValue | dict[str, object]]
        type StreamState = dict[str, str | int | dict[str, FlextTypes.Core.JsonValue]]
        type StreamBookmark = dict[str, str | int | dict[str, object]]
        type StreamSchema = dict[str, str | dict[str, FlextTypes.Core.JsonValue] | bool]

    # =========================================================================
    # ERROR HANDLING TYPES - Complex error management types
    # =========================================================================

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str, bool | str | int | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type ErrorRecovery = dict[str, str | bool | dict[str, object]]
        type ErrorReporting = dict[
            str, str | int | dict[str, FlextTypes.Core.JsonValue]
        ]
        type ErrorClassification = dict[str, str | int | dict[str, object]]
        type ErrorMetrics = dict[
            str, int | float | dict[str, FlextTypes.Core.JsonValue]
        ]
        type ErrorTracking = list[
            dict[str, str | int | dict[str, FlextTypes.Core.JsonValue]]
        ]

    # =========================================================================
    # SINGER TARGET ORACLE OIC PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes.Project):
        """Singer Target Oracle OIC-specific project types extending FlextTypes.Project.

        Adds Singer target Oracle OIC-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        Singer target Oracle OIC domain owns OIC loading and Singer protocol-specific types.
        """

        # Singer target Oracle OIC-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextTypes.Project
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

        # Singer target Oracle OIC-specific project configurations
        type SingerTargetOracleOicProjectConfig = dict[
            str, FlextTypes.Core.ConfigValue | object
        ]
        type OicLoaderConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[str, bool | str | dict[str, object]]
        type TargetOracleOicPipelineConfig = dict[
            str, FlextTypes.Core.ConfigValue | object
        ]


# =============================================================================
# PUBLIC API EXPORTS - Singer Oracle OIC target TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextTargetOracleOicTypes",
]
