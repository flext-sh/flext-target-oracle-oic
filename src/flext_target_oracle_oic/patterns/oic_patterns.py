"""Oracle OIC patterns using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import json

from flext_core import FlextResult, FlextTypes as t
from flext_core.runtime import FlextRuntime

logger = FlextRuntime.get_logger(__name__)


class OICTypeConverter:
    """Convert data types for OIC storage using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize OIC type converter."""
        super().__init__()

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

            # Handle simple types - OIC handles numbers natively
            if singer_type in {"integer", "number"}:
                return FlextResult[object].ok(value)

            # Default: return value as-is for string, text, boolean, etc.
            return FlextResult[object].ok(value)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.warning("Type conversion failed for %s: %s", singer_type, e)
            return FlextResult[object].ok(str(value))  # Fallback to string


class OICDataTransformer:
    """Transform data for OIC storage using flext-core patterns."""

    def __init__(self, type_converter: OICTypeConverter | None = None) -> None:
        """Initialize OIC data transformer."""
        super().__init__()
        self.type_converter = type_converter or OICTypeConverter()

    def transform_record(
        self,
        record: dict[str, t.GeneralValueType],
        schema: dict[str, t.GeneralValueType] | None = None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Transform Singer record for OIC storage."""
        try:
            transformed: dict[str, t.GeneralValueType] = {}

            for key, value in record.items():
                # OIC-specific attribute naming (camelCase convention)
                oic_key = self._normalize_oic_attribute_name(key)

                if schema is not None:
                    properties_val = schema.get("properties", {})
                    if isinstance(properties_val, dict):
                        prop_def_val = properties_val.get(key, {})
                        if isinstance(prop_def_val, dict):
                            singer_type_val = prop_def_val.get("type", "string")
                            singer_type = (
                                str(singer_type_val) if singer_type_val else "string"
                            )

                            convert_result = self.type_converter.convert_singer_to_oic(
                                singer_type,
                                value,
                            )
                            if convert_result.is_success:
                                converted = convert_result.data
                                # Ensure we assign GeneralValueType
                                if (
                                    isinstance(
                                        converted, (str, int, float, bool, list, dict)
                                    )
                                    or converted is None
                                ):
                                    transformed[oic_key] = converted
                                else:
                                    transformed[oic_key] = str(converted)
                            else:
                                transformed[oic_key] = value
                        else:
                            transformed[oic_key] = value
                    else:
                        transformed[oic_key] = value
                else:
                    transformed[oic_key] = value

            return FlextResult[dict[str, t.GeneralValueType]].ok(transformed)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC record transformation failed")
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"Record transformation failed: {e}",
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
        _record: dict[str, t.GeneralValueType],
        _resource_type: str,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Prepare payload for OIC API calls."""
        try:
            payload: dict[str, t.GeneralValueType] = {
                "resourceType": _resource_type,
                "properties": _record,
                "metadata": {
                    "createdBy": "flext-target-oracle-oic",
                    "version": 1.0,
                },
            }

            return FlextResult[dict[str, t.GeneralValueType]].ok(payload)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC payload preparation failed")
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"Payload preparation failed: {e}",
            )


class OICSchemaMapper:
    """Map Singer schemas to OIC schemas using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize OIC schema mapper."""
        super().__init__()

    def map_singer_schema_to_oic(
        self,
        schema: dict[str, t.GeneralValueType],
        resource_type: str = "integration",
    ) -> FlextResult[dict[str, str]]:
        """Map Singer schema to OIC resource definitions."""
        try:
            oic_schema: dict[str, str] = {}
            properties_val = schema.get("properties", {})

            if isinstance(properties_val, dict):
                for prop_name, prop_def in properties_val.items():
                    if not isinstance(prop_def, dict):
                        continue
                    # Ensure prop_def is properly typed
                    typed_prop_def: dict[str, t.GeneralValueType] = {
                        str(k): v for k, v in prop_def.items()
                    }
                    oic_name = self._normalize_attribute_name(str(prop_name))
                    oic_type_result = self._map_singer_type_to_oic(
                        typed_prop_def,
                        resource_type,
                    )

                    if oic_type_result.is_success:
                        mapped_type = oic_type_result.data
                        oic_schema[oic_name] = mapped_type or "string"
                    else:
                        oic_schema[oic_name] = "string"

            return FlextResult[dict[str, str]].ok(oic_schema)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("OIC schema mapping failed")
            return FlextResult[dict[str, str]].fail(
                f"Schema mapping failed: {e}",
            )

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
        prop_def: dict[str, t.GeneralValueType],
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
        super().__init__()

    def prepare_integration_entry(
        self,
        record: dict[str, t.GeneralValueType],
        integration_name: str,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Prepare integration entry for OIC."""
        try:
            entry: dict[str, t.GeneralValueType] = {
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

            return FlextResult[dict[str, t.GeneralValueType]].ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Integration entry preparation failed")
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"Integration entry preparation failed: {e}",
            )

    def prepare_connection_entry(
        self,
        record: dict[str, t.GeneralValueType],
        connection_name: str,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Prepare connection entry for OIC."""
        try:
            entry: dict[str, t.GeneralValueType] = {
                "name": connection_name,
                "identifier": record.get("identifier", connection_name),
                "adapterType": record.get("adapterType", "rest"),
                "connectionType": record.get("connectionType", "TRIGGER_CONNECTION"),
                "connectionProperties": record,
            }

            return FlextResult[dict[str, t.GeneralValueType]].ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Connection entry preparation failed")
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"Connection entry preparation failed: {e}",
            )

    def prepare_package_entry(
        self,
        record: dict[str, t.GeneralValueType],
        package_name: str,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Prepare package entry for OIC."""
        try:
            entry: dict[str, t.GeneralValueType] = {
                "name": package_name,
                "version": record.get("version", "1.0"),
                "description": record.get("description", f"Package: {package_name}"),
                "bundleType": record.get("bundleType", "INTEGRATION"),
                "contents": record,
            }

            return FlextResult[dict[str, t.GeneralValueType]].ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Package entry preparation failed")
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"Package entry preparation failed: {e}",
            )

    def prepare_lookup_entry(
        self,
        record: dict[str, t.GeneralValueType],
        lookup_name: str,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Prepare lookup entry for OIC."""
        try:
            entry: dict[str, t.GeneralValueType] = {
                "name": lookup_name,
                "description": record.get("description", f"Lookup: {lookup_name}"),
                "lookupType": record.get("lookupType", "DIRECT"),
                "lookupData": record,
            }

            return FlextResult[dict[str, t.GeneralValueType]].ok(entry)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Lookup entry preparation failed")
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"Lookup entry preparation failed: {e}",
            )

    def validate_entry_structure(
        self,
        entry: dict[str, t.GeneralValueType],
        entry_type: str,
    ) -> FlextResult[bool]:
        """Validate OIC entry structure."""
        try:
            required_fields: dict[str, list[str]] = {
                "integration": ["name", "version"],
                "connection": ["name", "identifier", "adapterType"],
                "package": ["name", "version", "bundleType"],
                "lookup": ["name", "lookupType"],
            }

            required = required_fields.get(entry_type, [])
            missing_fields = [field for field in required if field not in entry]

            if missing_fields:
                return FlextResult[bool].fail(
                    f"Missing required fields: {missing_fields}",
                )

            return FlextResult[bool].ok(value=True)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Entry validation failed")
            return FlextResult[bool].fail(f"Entry validation failed: {e}")
