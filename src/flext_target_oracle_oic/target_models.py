"""Target Oracle OIC Models - Centralized data models using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import re
from datetime import datetime

from flext_oracle_oic_ext.ext_models import (
    OICConnectionInfo as ConnectionBase,
    OICIntegrationInfo as IntegrationBase,
)
from pydantic import Field

from flext_core import FlextModels, FlextResult, FlextTypes

LookupBase = FlextModels  # These models don't exist in ext_models
PackageBase = FlextModels


# ===============================================================================
# CORE OIC ENTITY MODELS
# ===============================================================================


class OICConnection(ConnectionBase):
    """Oracle Integration Cloud connection model using flext-core patterns."""

    id: str = Field(
        ...,
        description="Connection identifier",
        min_length=1,
    )
    name: str = Field(
        ...,
        description="Connection display name",
        min_length=1,
    )
    description: str = Field(
        default="",
        description="Connection description",
    )
    adapter_type: str = Field(
        ...,
        description="Connection adapter type",
        min_length=1,
    )
    properties: FlextTypes.Core.Dict = Field(
        default_factory=dict,
        description="Connection properties",
    )
    status: str = Field(
        default="active",
        description="Connection status",
        pattern="^(active | inactive | error)$",
    )
    created_at: datetime | None = Field(
        None,
        description="Creation timestamp",
    )
    updated_at: datetime | None = Field(
        None,
        description="Last update timestamp",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate connection business rules."""
        try:
            if not self.id.strip():
                return FlextResult[None].fail("Connection ID cannot be empty")
            if not self.name.strip():
                return FlextResult[None].fail("Connection name cannot be empty")
            if not self.adapter_type.strip():
                return FlextResult[None].fail("Adapter type cannot be empty")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Connection validation failed: {e}")


class OICIntegration(IntegrationBase):
    """Oracle Integration Cloud integration model using flext-core patterns."""

    id: str = Field(
        ...,
        description="Integration identifier",
        min_length=1,
    )
    name: str = Field(
        ...,
        description="Integration display name",
        min_length=1,
    )
    description: str = Field(
        default="",
        description="Integration description",
    )
    version: str = Field(
        default="01.00.0000",
        description="Integration version",
        pattern=r"^\d{2}\.\d{2}\.\d{4}$",
    )
    pattern: str = Field(
        default="ORCHESTRATION",
        description="Integration pattern",
        pattern="^(ORCHESTRATION | MAP_MY_DATA | PUBLISH_TO_OIC|SUBSCRIBE_TO_OIC)$",
    )
    status: str = Field(
        default="configured",
        description="Integration status",
        pattern="^(configured | activated | error)$",
    )
    archive_content: bytes | None = Field(
        None,
        description="Integration archive content",
    )
    connections: FlextTypes.Core.StringList = Field(
        default_factory=list,
        description="List of connection IDs used by this integration",
    )
    created_at: datetime | None = Field(
        None,
        description="Creation timestamp",
    )
    updated_at: datetime | None = Field(
        None,
        description="Last update timestamp",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate integration business rules."""
        try:
            if not self.id.strip():
                return FlextResult[None].fail("Integration ID cannot be empty")
            if not self.name.strip():
                return FlextResult[None].fail("Integration name cannot be empty")

            # Validate version format
            if not re.match(r"^\d{2}\.\d{2}\.\d{4}$", self.version):
                return FlextResult[None].fail(f"Invalid version format: {self.version}")

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Integration validation failed: {e}")


class OICPackage(PackageBase):
    """Oracle Integration Cloud package model using flext-core patterns."""

    id: str = Field(
        ...,
        description="Package identifier",
        min_length=1,
    )
    name: str = Field(
        ...,
        description="Package display name",
        min_length=1,
    )
    description: str = Field(
        default="",
        description="Package description",
    )
    version: str = Field(
        default="01.00.0000",
        description="Package version",
        pattern=r"^\d{2}\.\d{2}\.\d{4}$",
    )
    archive_content: bytes | None = Field(
        None,
        description="Package archive content",
    )
    integrations: FlextTypes.Core.StringList = Field(
        default_factory=list,
        description="List of integration IDs in this package",
    )
    connections: FlextTypes.Core.StringList = Field(
        default_factory=list,
        description="List of connection IDs in this package",
    )
    lookups: FlextTypes.Core.StringList = Field(
        default_factory=list,
        description="List of lookup names in this package",
    )
    created_at: datetime | None = Field(
        None,
        description="Creation timestamp",
    )
    updated_at: datetime | None = Field(
        None,
        description="Last update timestamp",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate package business rules."""
        try:
            if not self.id.strip():
                return FlextResult[None].fail("Package ID cannot be empty")
            if not self.name.strip():
                return FlextResult[None].fail("Package name cannot be empty")

            # Validate version format
            if not re.match(r"^\d{2}\.\d{2}\.\d{4}$", self.version):
                return FlextResult[None].fail(f"Invalid version format: {self.version}")

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Package validation failed: {e}")


class OICLookup(LookupBase):
    """Oracle Integration Cloud lookup model using flext-core patterns."""

    name: str = Field(
        ...,
        description="Lookup name (identifier)",
        min_length=1,
    )
    description: str = Field(
        default="",
        description="Lookup description",
    )
    columns: list[FlextTypes.Core.Headers] = Field(
        default_factory=list,
        description="Lookup column definitions",
    )
    rows: list[FlextTypes.Core.Dict] = Field(
        default_factory=list,
        description="Lookup row data",
    )
    created_at: datetime | None = Field(
        None,
        description="Creation timestamp",
    )
    updated_at: datetime | None = Field(
        None,
        description="Last update timestamp",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate lookup business rules."""
        try:
            # Check name
            if not self.name.strip():
                return FlextResult[None].fail("Lookup name cannot be empty")

            # Validate columns structure - columns are already validated by type hints as FlextTypes.Core.Headers
            validation_errors: list[str] = []
            validation_errors.extend(
                [
                    "Column must have a name"
                    for column in self.columns
                    if "name" not in column
                ],
            )

            # Validate rows have valid column references - rows are already validated by type hints as FlextTypes.Core.Dict
            if self.columns and self.rows:
                column_names = {col["name"] for col in self.columns}
                for row in self.rows:
                    validation_errors.extend(
                        f"Row contains unknown column: {key}"
                        for key in row
                        if key not in column_names
                    )

            if validation_errors:
                return FlextResult[None].fail("; ".join(validation_errors))

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Lookup validation failed: {e}")


# ===============================================================================
# EXTENDED OIC MODELS (FROM PATTERNS)
# ===============================================================================


class OICProject(FlextModels):
    """Oracle Integration Cloud project model using flext-core patterns."""

    id: str = Field(
        ...,
        description="Project identifier",
        min_length=1,
    )
    name: str = Field(
        ...,
        description="Project display name",
        min_length=1,
    )
    description: str = Field(
        default="",
        description="Project description",
    )
    folders: list[FlextTypes.Core.Dict] = Field(
        default_factory=list,
        description="Project folders",
    )
    created_at: datetime | None = Field(
        None,
        description="Creation timestamp",
    )
    updated_at: datetime | None = Field(
        None,
        description="Last update timestamp",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate project business rules."""
        try:
            if not self.id.strip():
                return FlextResult[None].fail("Project ID cannot be empty")
            if not self.name.strip():
                return FlextResult[None].fail("Project name cannot be empty")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Project validation failed: {e}")


class OICSchedule(FlextModels):
    """Oracle Integration Cloud schedule model using flext-core patterns."""

    integration_id: str = Field(
        ...,
        description="Integration identifier",
        min_length=1,
    )
    schedule_type: str = Field(
        default=ONCE,
        description="Schedule type",
        pattern="^(ONCE | RECURRING | CRON)$",
    )
    schedule_expression: str = Field(
        default="",
        description="Schedule expression (cron format for CRON type)",
    )
    timezone: str = Field(
        default=UTC,
        description="Schedule timezone",
    )
    start_time: datetime | None = Field(
        None,
        description="Schedule start time",
    )
    end_time: datetime | None = Field(
        None,
        description="Schedule end time",
    )
    enabled: bool = Field(
        default=True,
        description="Schedule enabled status",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate schedule business rules."""
        try:
            if not self.integration_id.strip():
                return FlextResult[None].fail("Integration ID cannot be empty")

            # Validate cron expression if CRON type
            if self.schedule_type == "CRON" and not self.schedule_expression:
                return FlextResult[None].fail(
                    "CRON schedule type requires schedule expression",
                )

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Schedule validation failed: {e}")


class OICIntegrationAction(FlextModels):
    """Oracle Integration Cloud integration action model using flext-core patterns."""

    integration_id: str = Field(
        ...,
        description="Integration identifier",
        min_length=1,
    )
    version: str = Field(
        default="01.00.0000",
        description="Integration version",
        pattern=r"^\d{2}\.\d{2}\.\d{4}$",
    )
    action: str = Field(
        ...,
        description="Action to perform",
        pattern="^(activate | deactivate | test|clone)$",
    )
    parameters: FlextTypes.Core.Dict = Field(
        default_factory=dict,
        description="Action parameters",
    )
    executed_at: datetime | None = Field(
        None,
        description="Action execution timestamp",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate integration action business rules."""
        try:
            if not self.integration_id.strip():
                return FlextResult[None].fail("Integration ID cannot be empty")
            if not self.action.strip():
                return FlextResult[None].fail("Action cannot be empty")

            # Validate version format
            if not re.match(r"^\d{2}\.\d{2}\.\d{4}$", self.version):
                return FlextResult[None].fail(f"Invalid version format: {self.version}")

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Integration action validation failed: {e}")


class OICConnectionAction(FlextModels):
    """Oracle Integration Cloud connection action model using flext-core patterns."""

    connection_id: str = Field(
        ...,
        description="Connection identifier",
        min_length=1,
    )
    action: str = Field(
        ...,
        description="Action to perform",
        pattern="^(test | refresh_metadata)$",
    )
    parameters: FlextTypes.Core.Dict = Field(
        default_factory=dict,
        description="Action parameters",
    )
    executed_at: datetime | None = Field(
        None,
        description="Action execution timestamp",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate connection action business rules."""
        try:
            if not self.connection_id.strip():
                return FlextResult[None].fail("Connection ID cannot be empty")
            if not self.action.strip():
                return FlextResult[None].fail("Action cannot be empty")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Connection action validation failed: {e}")


# ===============================================================================
# DATA TRANSFORMATION MODELS
# ===============================================================================


class OICDataTransformation(FlextModels):
    """Data transformation model for OIC records using flext-core patterns."""

    source_data: FlextTypes.Core.Dict = Field(
        ...,
        description="Source data to transform",
    )
    target_schema: FlextTypes.Core.Dict = Field(
        ...,
        description="Target OIC schema",
    )
    transformation_rules: list[FlextTypes.Core.Dict] = Field(
        default_factory=list,
        description="Transformation rules to apply",
    )
    transformed_data: FlextTypes.Core.Dict = Field(
        default_factory=dict,
        description="Transformed data result",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate transformation business rules."""
        try:
            if not self.source_data:
                return FlextResult[None].fail("Source data cannot be empty")
            if not self.target_schema:
                return FlextResult[None].fail("Target schema cannot be empty")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Transformation validation failed: {e}")


class OICSchemaMapping(FlextModels):
    """Schema mapping model for Singer to OIC transformation using flext-core patterns."""

    singer_schema: FlextTypes.Core.Dict = Field(
        ...,
        description="Singer schema definition",
    )
    oic_schema: FlextTypes.Core.Dict = Field(
        ...,
        description="OIC schema definition",
    )
    field_mappings: FlextTypes.Core.Headers = Field(
        default_factory=dict,
        description="Field mappings from Singer to OIC",
    )
    type_conversions: FlextTypes.Core.Headers = Field(
        default_factory=dict,
        description="Type conversions from Singer to OIC",
    )

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate schema mapping business rules."""
        try:
            if not self.singer_schema:
                return FlextResult[None].fail("Singer schema cannot be empty")
            if not self.oic_schema:
                return FlextResult[None].fail("OIC schema cannot be empty")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Schema mapping validation failed: {e}")


# ===============================================================================
# MODEL FACTORY FUNCTIONS
# ===============================================================================


def create_oic_connection(data: FlextTypes.Core.Dict) -> FlextResult[OICConnection]:
    """Create OIC connection from data dictionary."""
    try:
        connection = OICConnection(**data)
        validation = connection.validate_business_rules()
        if not validation.success:
            return FlextResult[OICConnection].fail(
                f"Connection validation failed: {validation.error}",
            )
        return FlextResult[OICConnection].ok(connection)
    except Exception as e:
        return FlextResult[OICConnection].fail(f"Failed to create connection: {e}")


def create_oic_integration(data: FlextTypes.Core.Dict) -> FlextResult[OICIntegration]:
    """Create OIC integration from data dictionary."""
    try:
        integration = OICIntegration(**data)
        validation = integration.validate_business_rules()
        if not validation.success:
            return FlextResult[OICIntegration].fail(
                f"Integration validation failed: {validation.error}",
            )
        return FlextResult[OICIntegration].ok(integration)
    except Exception as e:
        return FlextResult[OICIntegration].fail(f"Failed to create integration: {e}")


def create_oic_package(data: FlextTypes.Core.Dict) -> FlextResult[OICPackage]:
    """Create OIC package from data dictionary."""
    try:
        package = OICPackage(**data)
        validation = package.validate_business_rules()
        if not validation.success:
            return FlextResult[OICPackage].fail(
                f"Package validation failed: {validation.error}",
            )
        return FlextResult[OICPackage].ok(package)
    except Exception as e:
        return FlextResult[OICPackage].fail(f"Failed to create package: {e}")


def create_oic_lookup(data: FlextTypes.Core.Dict) -> FlextResult[OICLookup]:
    """Create OIC lookup from data dictionary."""
    try:
        lookup = OICLookup(**data)
        validation = lookup.validate_business_rules()
        if not validation.success:
            return FlextResult[OICLookup].fail(
                f"Lookup validation failed: {validation.error}",
            )
        return FlextResult[OICLookup].ok(lookup)
    except Exception as e:
        return FlextResult[OICLookup].fail(f"Failed to create lookup: {e}")


# ===============================================================================
# EXPORTS
# ===============================================================================

__all__: FlextTypes.Core.StringList = [
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
    "create_oic_connection",
    "create_oic_integration",
    "create_oic_lookup",
    "create_oic_package",
]
