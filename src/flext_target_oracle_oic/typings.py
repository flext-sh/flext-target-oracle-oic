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

from flext_core import t

# =============================================================================
# TARGET ORACLE OIC-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer Oracle OIC target operations
# =============================================================================


# Singer Oracle OIC target domain TypeVars
class FlextTargetOracleOicTypes(t):
    """Singer Oracle OIC target-specific type definitions extending t.

    Domain-specific type system for Singer Oracle OIC target operations.
    Contains ONLY complex Oracle OIC target-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # SINGER TARGET TYPES - Complex Singer target protocol types
    # =========================================================================

    class SingerTarget:
        """Singer target protocol complex types."""

        type TargetConfiguration = dict[str, str | int | bool | dict[str, object]]
        type StreamConfiguration = dict[str, str | bool | dict[str, t.JsonValue]]
        type MessageProcessing = dict[str, str | list[dict[str, t.JsonValue]]]
        type RecordHandling = dict[str, str | dict[str, t.JsonValue] | bool]
        type StateManagement = dict[str, str | dict[str, t.JsonValue]]
        type BatchProcessing = dict[str, str | int | dict[str, t.JsonValue]]

    # =========================================================================
    # ORACLE OIC INTEGRATION TYPES - Complex Oracle OIC integration types
    # =========================================================================

    class OicIntegration:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[str, str | int | bool | dict[str, object]]
        type IntegrationDefinition = dict[str, str | list[str] | dict[str, t.JsonValue]]
        type IntegrationFlow = dict[str, str | dict[str, t.JsonValue]]
        type IntegrationMapping = dict[str, str | dict[str, object]]
        type IntegrationMetadata = dict[str, str | dict[str, t.JsonValue]]
        type IntegrationStatus = dict[str, str | bool | dict[str, object]]

    # =========================================================================
    # OIC CONNECTION TYPES - Complex Oracle OIC connection types
    # =========================================================================

    class OicConnection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[str, str | int | bool | dict[str, object]]
        type ConnectionCredentials = dict[str, str | dict[str, t.JsonValue]]
        type ConnectionSecurity = dict[str, str | bool | dict[str, object]]
        type ConnectionValidation = dict[str, bool | str | dict[str, object]]
        type ConnectionMetadata = dict[str, str | dict[str, t.JsonValue]]
        type ConnectionPool = dict[str, int | bool | dict[str, object]]

    # =========================================================================
    # OIC AUTHENTICATION TYPES - Complex OAuth2/IDCS authentication types
    # =========================================================================

    class OicAuthentication:
        """Oracle OIC authentication complex types."""

        type OAuth2Configuration = dict[str, str | int | dict[str, object]]
        type IdcsConfiguration = dict[str, str | bool | dict[str, t.JsonValue]]
        type TokenManagement = dict[str, str | int | dict[str, object]]
        type AuthenticationFlow = dict[str, str | dict[str, t.JsonValue]]
        type SecuritySettings = dict[str, bool | str | dict[str, object]]
        type AuthenticationCache = dict[str, str | int | dict[str, object]]

    # =========================================================================
    # OIC DEPLOYMENT TYPES - Complex Oracle OIC deployment types
    # =========================================================================

    class OicDeployment:
        """Oracle OIC deployment complex types."""

        type DeploymentConfiguration = dict[str, str | bool | dict[str, object]]
        type ArtifactManagement = dict[str, str | dict[str, t.JsonValue]]
        type DeploymentValidation = dict[str, bool | str | dict[str, object]]
        type PackageDeployment = dict[str, str | dict[str, t.JsonValue]]
        type DeploymentStatus = dict[str, str | bool | dict[str, object]]
        type RollbackStrategy = dict[str, str | dict[str, object]]

    # =========================================================================
    # DATA TRANSFORMATION TYPES - Complex data transformation types
    # =========================================================================

    class DataTransformation:
        """Data transformation complex types."""

        type TransformationConfiguration = dict[str, str | bool | dict[str, object]]
        type FieldMapping = dict[str, str | list[str] | dict[str, object]]
        type DataValidation = dict[str, str | dict[str, t.JsonValue]]
        type TypeConversion = dict[str, bool | str | dict[str, object]]
        type FilteringRules = dict[str, str | dict[str, t.JsonValue]]
        type TransformationResult = dict[str, dict[str, t.JsonValue]]

    # =========================================================================
    # STREAM PROCESSING TYPES - Complex stream handling types
    # =========================================================================

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[str, str | bool | int | dict[str, object]]
        type StreamMetadata = dict[str, str | dict[str, t.JsonValue]]
        type StreamRecord = dict[str, t.JsonValue | dict[str, object]]
        type StreamState = dict[str, str | int | dict[str, t.JsonValue]]
        type StreamBookmark = dict[str, str | int | dict[str, object]]
        type StreamSchema = dict[str, str | dict[str, t.JsonValue] | bool]

    # =========================================================================
    # ERROR HANDLING TYPES - Complex error management types
    # =========================================================================

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[str, bool | str | int | dict[str, object]]
        type ErrorRecovery = dict[str, str | bool | dict[str, object]]
        type ErrorReporting = dict[str, str | int | dict[str, t.JsonValue]]
        type ErrorClassification = dict[str, str | int | dict[str, object]]
        type ErrorMetrics = dict[str, int | float | dict[str, t.JsonValue]]
        type ErrorTracking = list[dict[str, str | int | dict[str, t.JsonValue]]]

    # =========================================================================
    # SINGER TARGET ORACLE OIC PROJECT TYPES - Domain-specific project types extending t
    # =========================================================================

    class Project(t):
        """Singer Target Oracle OIC-specific project types extending t.

        Adds Singer target Oracle OIC-specific project types while inheriting
        generic types from t. Follows domain separation principle:
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

        # Singer target Oracle OIC-specific project configurations
        type SingerTargetOracleOicProjectConfig = dict[str, object]
        type OicLoaderConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[str, bool | str | dict[str, object]]
        type TargetOracleOicPipelineConfig = dict[str, object]


# =============================================================================
# PUBLIC API EXPORTS - Singer Oracle OIC target TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextTargetOracleOicTypes",
]
