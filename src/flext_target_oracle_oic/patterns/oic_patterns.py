"""Oracle OIC patterns using flext-core patterns."""

from __future__ import annotations

import json

from flext_core import FlextResult, get_logger

logger = get_logger(__name__)


class OICTypeConverter:
    """Convert data types for OIC storage using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize OIC type converter."""

    def convert_singer_to_oic(
        self,
        singer_type: str,
        value: object,
    ) -> FlextResult[object]:
        """Convert Singer type to OIC-compatible type."""
        try:
            if value is None:
                return FlextResult[object].ok(None)

            # Handle complex types first
            if singer_type in {"object", "array"}:
                if isinstance(value, (dict, list)):
                    return FlextResult[object].ok(value)
                parsed_value: object
                parsed_value = json.loads(value) if isinstance(value, str) else value
                return FlextResult[object].ok(parsed_value)

            # Handle simple types with mapping
            type_converters = {
                "string": str,
                "text": str,
                "boolean": bool,
                "integer": lambda x: x,  # OIC handles numbers natively
                "number": lambda x: x,  # OIC handles numbers natively
            }

            if singer_type in type_converters:
                converter = type_converters[singer_type]
                if callable(converter):
                    return FlextResult[object].ok(converter(value))
                return FlextResult[object].ok(value)

            # Default fallback
            return FlextResult[object].ok(value)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.warning("Type conversion failed for %s: %s", singer_type, e)
            return FlextResult[object].ok(str(value))  # Fallback to string


class OICDataTransformer:
    """Transform data for OIC storage using flext-core patterns."""

    def __init__(self, type_converter: OICTypeConverter | None = None) -> None:
        """Initialize OIC data transformer."""
        self.type_converter = type_converter or OICTypeConverter()

    def transform_record(
        self,
        record: dict[str, object],
        schema: dict[str, object] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Transform Singer record for OIC storage."""
        try:
            transformed: dict[str, object] = {}

            for key, value in record.items():
                # OIC-specific attribute naming (camelCase convention)
                oic_key = self._normalize_oic_attribute_name(key)

                # Type conversion
                if schema and isinstance(schema, dict):
                    properties = schema.get("properties", {})
                    if isinstance(properties, dict):
                        prop_def = properties.get(key, {})
                    singer_type = prop_def.get("type", "string")

                    convert_result = self.type_converter.convert_singer_to_oic(
                        singer_type,
                        value,
                    )
                    if convert_result.success:
                        transformed[oic_key] = convert_result.data
                    else:
                        transformed[oic_key] = value
                else:
                    transformed[oic_key] = value

            return FlextResult[dict[str, object]].ok(transformed)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC record transformation failed")
            return FlextResult[dict[str, object]].fail(
                f"Record transformation failed: {e}"
            )

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
        record: dict[str, object],
        resource_type: str,
    ) -> FlextResult[dict[str, object]]:
        """Prepare payload for OIC API calls."""
        try:
            payload: dict[str, object] = {
                "resourceType": resource_type,
                "properties": record,
                "metadata": {
                    "createdBy": "flext-target-oracle-oic",
                    "version": "1.0",
                },
            }

            return FlextResult[dict[str, object]].ok(payload)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC payload preparation failed")
            return FlextResult[dict[str, object]].fail(
                f"Payload preparation failed: {e}"
            )


class OICSchemaMapper:
    """Map Singer schemas to OIC schemas using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize OIC schema mapper."""

    def map_singer_schema_to_oic(
        self,
        schema: dict[str, object],
        resource_type: str = "integration",
    ) -> FlextResult[dict[str, str]]:
        """Map Singer schema to OIC resource definitions."""
        try:
            oic_schema: dict[str, str] = {}
            properties = schema.get("properties", {})

            if isinstance(properties, dict):
                for prop_name, prop_def in properties.items():
                    if not isinstance(prop_name, str) or not isinstance(prop_def, dict):
                        continue
                    # Ensure prop_def is properly typed as dict[str, object]
                    typed_prop_def: dict[str, object] = prop_def
                    oic_name = self._normalize_attribute_name(prop_name)
                    oic_type_result = self._map_singer_type_to_oic(
                        typed_prop_def,
                        resource_type,
                    )

                    if oic_type_result.success:
                        # Ensure we have a string type
                        mapped_type = oic_type_result.data
                        oic_schema[oic_name] = mapped_type
                    else:
                        oic_schema[oic_name] = "string"  # Fallback

            return FlextResult[dict[str, str]].ok(oic_schema)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC schema mapping failed")
            return FlextResult[dict[str, str]].fail(f"Schema mapping failed: {e}")

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
        prop_def: dict[str, object],
        _resource_type: str,
    ) -> FlextResult[str]:
        """Map Singer property definition to OIC resource type."""
        try:
            prop_type = prop_def.get("type", "string")
            prop_format = prop_def.get("format")

            if prop_format in {"date-time", "date"}:
                return FlextResult[str].ok("datetime")
            if prop_type in {"integer", "number"}:
                return FlextResult[str].ok("number")
            if prop_type == "boolean":
                return FlextResult[str].ok("boolean")
            if prop_type in {"object", "array"}:
                return FlextResult[str].ok("object")
            return FlextResult[str].ok("string")

        except (RuntimeError, ValueError, TypeError) as e:
            logger.warning("OIC type mapping failed: %s", e)
            return FlextResult[str].ok("string")


class OICEntryManager:
    """Manage OIC entries using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize OIC entry manager."""

    def prepare_integration_entry(
        self,
        record: dict[str, object],
        integration_name: str,
    ) -> FlextResult[dict[str, object]]:
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

            return FlextResult[dict[str, object]].ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Integration entry preparation failed")
            return FlextResult[dict[str, object]].fail(
                f"Integration entry preparation failed: {e}"
            )

    def prepare_connection_entry(
        self,
        record: dict[str, object],
        connection_name: str,
    ) -> FlextResult[dict[str, object]]:
        """Prepare connection entry for OIC."""
        try:
            entry = {
                "name": connection_name,
                "identifier": record.get("identifier", connection_name),
                "adapterType": record.get("adapterType", "rest"),
                "connectionType": record.get("connectionType", "TRIGGER_CONNECTION"),
                "connectionProperties": record,
            }

            return FlextResult[dict[str, object]].ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Connection entry preparation failed")
            return FlextResult[dict[str, object]].fail(
                f"Connection entry preparation failed: {e}"
            )

    def prepare_package_entry(
        self,
        record: dict[str, object],
        package_name: str,
    ) -> FlextResult[dict[str, object]]:
        """Prepare package entry for OIC."""
        try:
            entry = {
                "name": package_name,
                "version": record.get("version", "1.0"),
                "description": record.get("description", f"Package: {package_name}"),
                "bundleType": record.get("bundleType", "INTEGRATION"),
                "contents": record,
            }

            return FlextResult[dict[str, object]].ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Package entry preparation failed")
            return FlextResult[dict[str, object]].fail(
                f"Package entry preparation failed: {e}"
            )

    def prepare_lookup_entry(
        self,
        record: dict[str, object],
        lookup_name: str,
    ) -> FlextResult[dict[str, object]]:
        """Prepare lookup entry for OIC."""
        try:
            entry = {
                "name": lookup_name,
                "description": record.get("description", f"Lookup: {lookup_name}"),
                "lookupType": record.get("lookupType", "DIRECT"),
                "lookupData": record,
            }

            return FlextResult[dict[str, object]].ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Lookup entry preparation failed")
            return FlextResult[dict[str, object]].fail(
                f"Lookup entry preparation failed: {e}"
            )

    def validate_entry_structure(
        self,
        entry: dict[str, object],
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
                return FlextResult[bool].fail(
                    f"Missing required fields: {missing_fields}"
                )

            return FlextResult[bool].ok(data=True)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Entry validation failed")
            return FlextResult[bool].fail(f"Entry validation failed: {e}")
