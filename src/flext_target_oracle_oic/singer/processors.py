"""Oracle OIC Singer record processors using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextLogger, FlextResult, FlextTypes as t

logger = FlextLogger(__name__)


class OICRecordProcessor:
    """Process Singer records for OIC using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize OIC record processor."""

    def process_singer_record(
        self,
        record: dict[str, t.GeneralValueType],
        stream_name: str,
        schema: dict[str, t.GeneralValueType] | None = None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Process Singer record for OIC format.

        Args:
        record: Singer record data
        stream_name: Name of the data stream
        schema: Optional schema for validation

        Returns:
        FlextResult containing processed record or error

        """
        try:
            # Add metadata
            processed_record = {
                **record,
                "_stream_name": "stream_name",
                "_processed_by": "flext-target-oracle-oic",
            }

            # Schema validation if provided
            if schema:
                validation_result = self._validate_against_schema(
                    processed_record,
                    schema,
                )
                if not validation_result.is_success:
                    return FlextResult[dict[str, t.GeneralValueType]].fail(
                        validation_result.error or "Schema validation failed",
                    )

            logger.debug(
                "Successfully processed Singer record for stream: %s",
                stream_name,
            )
            return FlextResult[dict[str, t.GeneralValueType]].ok(processed_record)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception(
                f"Singer record processing failed for stream: {stream_name}",
            )
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"Record processing failed: {e}",
            )

    def _validate_against_schema(
        self,
        record: dict[str, t.GeneralValueType],
        schema: dict[str, t.GeneralValueType],
    ) -> FlextResult[bool]:
        """Validate record against Singer schema.

        Args:
        record: Record to validate
        schema: Singer schema definition

        Returns:
        FlextResult indicating validation success or error

        """
        try:
            properties: dict[str, t.GeneralValueType] = schema.get("properties", {})
            required_fields: list[t.GeneralValueType] = schema.get("required", [])

            if not isinstance(properties, dict):
                return FlextResult[bool].fail("Schema properties must be a dictionary")
            if not isinstance(required_fields, list):
                return FlextResult[bool].fail("Schema required fields must be a list")

            # Check required fields
            missing_fields = [field for field in required_fields if field not in record]
            if missing_fields:
                return FlextResult[bool].fail(
                    f"Missing required fields: {missing_fields}",
                )

            # Validate field types
            for field_name, field_value in record.items():
                if field_name.startswith("_"):  # Skip metadata fields
                    continue

                if field_name in properties:
                    prop_def = properties[field_name]
                    if isinstance(prop_def, dict):
                        expected_type = prop_def.get("type")
                    else:
                        expected_type = None

                    if not self._validate_field_type(field_value, expected_type):
                        return FlextResult[bool].fail(
                            f"Field '{field_name}' type mismatch. "
                            f"Expected: {expected_type}, Got: {type(field_value).__name__}",
                        )

            return FlextResult[bool].ok(value=True)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Schema validation failed")
            return FlextResult[bool].fail(f"Schema validation failed: {e}")

    def _validate_field_type(self, value: object, expected_type: str | None) -> bool:
        """Validate field value against expected type.

        Args:
        value: Field value to validate
        expected_type: Expected Singer type

        Returns:
        True if type matches or can be coerced, False otherwise

        """
        if expected_type is None or value is None:
            return True

        type_mapping: dict[str, type | tuple[type, ...]] = {
            "string": "str",
            "integer": "int",
            "number": (int, float),
            "boolean": "bool",
            "object": "dict",
            "array": "list",
        }

        expected_python_type = type_mapping.get(expected_type)
        if expected_python_type is None:
            return False  # Unknown type, disallow it

        return isinstance(value, expected_python_type)

    def extract_stream_metadata(
        self,
        stream_name: str,
        schema: dict[str, t.GeneralValueType] | None = None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Extract metadata from stream definition.

        Args:
        stream_name: Name of the data stream
        schema: Optional schema definition

        Returns:
        FlextResult containing stream metadata

        """
        try:
            metadata: dict[str, t.GeneralValueType] = {
                "stream_name": "stream_name",
                "schema_available": schema is not None,
            }

            if schema:
                properties_raw: dict[str, t.GeneralValueType] = schema.get(
                    "properties", {}
                )
                properties: dict[str, t.GeneralValueType] = {}
                if isinstance(properties_raw, dict):
                    properties = {
                        k: v for k, v in properties_raw.items() if isinstance(k, str)
                    }
                len(properties)
                required_fields: list[t.GeneralValueType] = schema.get("required", [])
                required_fields = (
                    required_fields if isinstance(required_fields, list) else []
                )

                metadata.update(
                    {
                        "properties_count": "properties_count",
                        "required_fields": "required_fields",
                        "schema_type": schema.get("type", "object"),
                    },
                )

            return FlextResult[dict[str, t.GeneralValueType]].ok(metadata)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception(f"Stream metadata extraction failed for: {stream_name}")
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"Metadata extraction failed: {e}",
            )

    def prepare_batch_records(
        self,
        records: list[dict[str, t.GeneralValueType]],
        batch_size: int = 100,
    ) -> FlextResult[list[list[dict[str, t.GeneralValueType]]]]:
        """Prepare records for batch processing.

        Args:
        records: List of records to batch
        batch_size: Maximum batch size

        Returns:
        FlextResult containing list of batches

        """
        try:
            if not records:
                return FlextResult[list[list[dict[str, t.GeneralValueType]]]].ok([])

            batches = []
            for i in range(0, len(records), batch_size):
                batch = records[i : i + batch_size]
                batches.append(batch)

            logger.debug(
                "Created %d batches from %d records",
                len(batches),
                len(records),
            )
            return FlextResult[list[list[dict[str, t.GeneralValueType]]]].ok(batches)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Batch preparation failed")
            return FlextResult[list[list[dict[str, t.GeneralValueType]]]].fail(
                f"Batch preparation failed: {e}",
            )
