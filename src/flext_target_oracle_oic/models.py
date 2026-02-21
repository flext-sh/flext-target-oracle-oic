"""Domain models for target Oracle OIC."""

from __future__ import annotations

from enum import StrEnum

from flext_core import FlextModels, FlextResult, t
from pydantic import Field


class OICConnectionAction(StrEnum):
    """Supported connection actions."""

    CREATE = "create"
    UPDATE = "update"


class OICIntegrationAction(StrEnum):
    """Supported integration actions."""

    IMPORT = "import"
    ACTIVATE = "activate"


class OICConnection(FlextModels.ArbitraryTypesModel):
    """Connection payload model."""

    id: str
    name: str
    adapter_type: str
    properties: dict[str, t.GeneralValueType] = Field(default_factory=dict)


class OICIntegration(FlextModels.ArbitraryTypesModel):
    """Integration payload model."""

    id: str
    name: str
    version: str = "01.00.0000"
    pattern: str = "ORCHESTRATION"


class OICPackage(FlextModels.ArbitraryTypesModel):
    """Package payload model."""

    id: str
    name: str
    version: str = "01.00.0000"


class OICLookup(FlextModels.ArbitraryTypesModel):
    """Lookup payload model."""

    name: str
    columns: list[dict[str, t.GeneralValueType]] = Field(default_factory=list)
    rows: list[dict[str, t.GeneralValueType]] = Field(default_factory=list)


class OICProject(FlextModels.ArbitraryTypesModel):
    """Project payload model."""

    id: str
    name: str


class OICSchedule(FlextModels.ArbitraryTypesModel):
    """Schedule payload model."""

    name: str
    schedule_type: str = "ONCE"


class OICDataTransformation(FlextModels.ArbitraryTypesModel):
    """Transformation payload model."""

    source_stream: str
    target_entity: str
    mapping: dict[str, str] = Field(default_factory=dict)


class OICSchemaMapping(FlextModels.ArbitraryTypesModel):
    """Schema mapping payload model."""

    stream_name: str
    schema_mapping: dict[str, t.GeneralValueType] = Field(default_factory=dict)


class FlextTargetOracleOicModels(FlextModels):
    """Namespace class for OIC target models."""

    @staticmethod
    def validate_connection(connection: OICConnection) -> FlextResult[bool]:
        """Validate minimal connection invariants."""
        if not connection.id.strip() or not connection.name.strip():
            return FlextResult[bool].fail("Connection id/name cannot be empty")
        return FlextResult[bool].ok(value=True)


m = FlextTargetOracleOicModels

__all__ = [
    "FlextTargetOracleOicModels",
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
    "m",
]
