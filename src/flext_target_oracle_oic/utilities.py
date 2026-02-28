"""Utilities for Oracle OIC Singer payload handling."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextResult, t
from flext_meltano import FlextMeltanoUtilities
from flext_oracle_oic import FlextOracleOicUtilities


class FlextTargetOracleOicUtilities(FlextMeltanoUtilities, FlextOracleOicUtilities):
    """Namespace for message-building and validation helpers."""

    class TargetOracleOic:
        """Singer message helper functions."""

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: Mapping[str, t.JsonValue],
            key_properties: list[str] | None = None,
        ) -> Mapping[str, t.JsonValue]:
            """Build a Singer SCHEMA message payload."""
            return {
                "type": "SCHEMA",
                "stream": stream_name,
                "schema": schema,
                "key_properties": key_properties or [],
            }

        @staticmethod
        def create_record_message(
            stream_name: str,
            record: Mapping[str, t.JsonValue],
        ) -> Mapping[str, t.JsonValue]:
            """Build a Singer RECORD message payload."""
            return {"type": "RECORD", "stream": stream_name, "record": record}

    class Validation:
        """Runtime configuration validation helper functions."""

        @staticmethod
        def validate_config(
            config: Mapping[str, t.JsonValue],
        ) -> FlextResult[bool]:
            """Validate required OIC target configuration keys."""
            required = {"base_url", "oauth_client_id", "oauth_client_secret"}
            missing = sorted(key for key in required if key not in config)
            if missing:
                return FlextResult[bool].fail(
                    f"Missing required config fields: {missing}"
                )
            return FlextResult[bool].ok(value=True)


u = FlextTargetOracleOicUtilities

__all__ = ["FlextTargetOracleOicUtilities", "u"]
