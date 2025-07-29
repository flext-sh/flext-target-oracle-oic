"""Oracle OIC patterns using flext-core patterns."""

from __future__ import annotations

import json
from typing import Any

# Import from flext-core for foundational patterns
from flext_core import FlextResult, get_logger

logger = get_logger(__name__)


class OICTypeConverter:
    """Convert data types for OIC storage using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize OIC type converter."""

    def convert_singer_to_oic(self, singer_type: str, value: Any) -> FlextResult[Any]:
        """Convert Singer type to OIC-compatible type."""
        try:
            if value is None:
                return FlextResult.ok(None)

            if singer_type in {"string", "text"}:
                return FlextResult.ok(str(value))
            if singer_type in {"integer", "number"}:
                return FlextResult.ok(value)  # OIC handles numbers natively
            if singer_type == "boolean":
                return FlextResult.ok(bool(value))
            if singer_type in {"object", "array"}:
                if isinstance(value, (dict, list)):
                    return FlextResult.ok(value)
                return FlextResult.ok(
                    json.loads(str(value)) if isinstance(value, str) else value,
                )
            return FlextResult.ok(value)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.warning(f"Type conversion failed for {singer_type}: {e}")
            return FlextResult.ok(str(value))  # Fallback to string


class OICDataTransformer:
    """Transform data for OIC storage using flext-core patterns."""

    def __init__(self, type_converter: OICTypeConverter | None = None) -> None:
        """Initialize OIC data transformer."""
        self.type_converter = type_converter or OICTypeConverter()

    def transform_record(
        self,
        record: dict[str, Any],
        schema: dict[str, Any] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Transform Singer record for OIC storage."""
        try:
            transformed = {}

            for key, value in record.items():
                # OIC-specific attribute naming (camelCase convention)
                oic_key = self._normalize_oic_attribute_name(key)

                # Type conversion
                if schema:
                    properties = schema.get("properties", {})
                    prop_def = properties.get(key, {})
                    singer_type = prop_def.get("type", "string")

                    convert_result = self.type_converter.convert_singer_to_oic(
                        singer_type,
                        value,
                    )
                    if convert_result.is_success:
                        transformed[oic_key] = convert_result.data
                    else:
                        transformed[oic_key] = value
                else:
                    transformed[oic_key] = value

            return FlextResult.ok(transformed)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC record transformation failed")
            return FlextResult.fail(f"Record transformation failed: {e}")

    def _normalize_oic_attribute_name(self, name: str) -> str:
        """Normalize attribute name for OIC conventions."""
        # OIC uses camelCase convention
        if "_" in name or "-" in name:
            parts = name.replace("-", "_").split("_")
            normalized = parts[0].lower() + "".join(
                word.capitalize() for word in parts[1:]
            )
        else:
            normalized = name

        return normalized

    def prepare_oic_payload(
        self,
        record: dict[str, Any],
        resource_type: str,
    ) -> FlextResult[dict[str, Any]]:
        """Prepare payload for OIC API calls."""
        try:
            payload = {
                "resourceType": resource_type,
                "properties": record,
                "metadata": {
                    "createdBy": "flext-target-oracle-oic",
                    "version": "1.0",
                },
            }

            return FlextResult.ok(payload)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC payload preparation failed")
            return FlextResult.fail(f"Payload preparation failed: {e}")


class OICSchemaMapper:
    """Map Singer schemas to OIC schemas using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize OIC schema mapper."""

    def map_singer_schema_to_oic(
        self,
        schema: dict[str, Any],
        resource_type: str = "integration",
    ) -> FlextResult[dict[str, str]]:
        """Map Singer schema to OIC resource definitions."""
        try:
            oic_schema: dict[str, str] = {}
            properties = schema.get("properties", {})

            for prop_name, prop_def in properties.items():
                oic_name = self._normalize_attribute_name(prop_name)
                oic_type_result = self._map_singer_type_to_oic(prop_def, resource_type)

                if oic_type_result.is_success:
                    # Ensure we have a string type
                    mapped_type = oic_type_result.data
                    oic_schema[oic_name] = (
                        mapped_type if isinstance(mapped_type, str) else "string"
                    )
                else:
                    oic_schema[oic_name] = "string"  # Fallback

            return FlextResult.ok(oic_schema)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC schema mapping failed")
            return FlextResult.fail(f"Schema mapping failed: {e}")

    def _normalize_attribute_name(self, name: str) -> str:
        """Normalize attribute name for OIC."""
        # Convert to camelCase for OIC resources
        if "_" in name or "-" in name:
            parts = name.replace("-", "_").split("_")
            normalized = parts[0].lower() + "".join(
                word.capitalize() for word in parts[1:]
            )
        else:
            normalized = name.lower()

        return normalized

    def _map_singer_type_to_oic(
        self,
        prop_def: dict[str, Any],
        resource_type: str,
    ) -> FlextResult[str]:
        """Map Singer property definition to OIC resource type."""
        try:
            prop_type = prop_def.get("type", "string")
            prop_format = prop_def.get("format")

            if prop_format in {"date-time", "date"}:
                return FlextResult.ok("datetime")
            if prop_type in {"integer", "number"}:
                return FlextResult.ok("number")
            if prop_type == "boolean":
                return FlextResult.ok("boolean")
            if prop_type in {"object", "array"}:
                return FlextResult.ok("object")
            return FlextResult.ok("string")

        except (RuntimeError, ValueError, TypeError) as e:
            logger.warning(f"OIC type mapping failed: {e}")
            return FlextResult.ok("string")


class OICEntryManager:
    """Manage OIC entries using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize OIC entry manager."""

    def prepare_integration_entry(
        self,
        record: dict[str, Any],
        integration_name: str,
    ) -> FlextResult[dict[str, Any]]:
        """Prepare integration entry for OIC."""
        try:
            entry = {
                "name": integration_name,
                "version": record.get("version", "01.00.0000"),
                "description": record.get(
                    "description",
                    f"Integration: {integration_name}",
                ),
                "style": record.get("style", "ORCHESTRATION"),
                "pattern": record.get("pattern", "SYNCHRONOUS"),
                "properties": record,
            }

            return FlextResult.ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Integration entry preparation failed")
            return FlextResult.fail(f"Integration entry preparation failed: {e}")

    def prepare_connection_entry(
        self,
        record: dict[str, Any],
        connection_name: str,
    ) -> FlextResult[dict[str, Any]]:
        """Prepare connection entry for OIC."""
        try:
            entry = {
                "name": connection_name,
                "identifier": record.get("identifier", connection_name),
                "adapterType": record.get("adapterType", "rest"),
                "connectionType": record.get("connectionType", "TRIGGER_CONNECTION"),
                "connectionProperties": record,
            }

            return FlextResult.ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Connection entry preparation failed")
            return FlextResult.fail(f"Connection entry preparation failed: {e}")

    def prepare_package_entry(
        self,
        record: dict[str, Any],
        package_name: str,
    ) -> FlextResult[dict[str, Any]]:
        """Prepare package entry for OIC."""
        try:
            entry = {
                "name": package_name,
                "version": record.get("version", "1.0"),
                "description": record.get("description", f"Package: {package_name}"),
                "bundleType": record.get("bundleType", "INTEGRATION"),
                "contents": record,
            }

            return FlextResult.ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Package entry preparation failed")
            return FlextResult.fail(f"Package entry preparation failed: {e}")

    def prepare_lookup_entry(
        self,
        record: dict[str, Any],
        lookup_name: str,
    ) -> FlextResult[dict[str, Any]]:
        """Prepare lookup entry for OIC."""
        try:
            entry = {
                "name": lookup_name,
                "description": record.get("description", f"Lookup: {lookup_name}"),
                "lookupType": record.get("lookupType", "DIRECT"),
                "lookupData": record,
            }

            return FlextResult.ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Lookup entry preparation failed")
            return FlextResult.fail(f"Lookup entry preparation failed: {e}")

    def validate_entry_structure(
        self,
        entry: dict[str, Any],
        entry_type: str,
    ) -> FlextResult[bool]:
        """Validate OIC entry structure."""
        try:
            required_fields = {
                "integration": ["name", "version"],
                "connection": ["name", "identifier", "adapterType"],
                "package": ["name", "version", "bundleType"],
                "lookup": ["name", "lookupType"],
            }

            required = required_fields.get(entry_type, [])
            missing_fields = [field for field in required if field not in entry]

            if missing_fields:
                return FlextResult.fail(f"Missing required fields: {missing_fields}")

            return FlextResult.ok(True)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Entry validation failed")
            return FlextResult.fail(f"Entry validation failed: {e}")
