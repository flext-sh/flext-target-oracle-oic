"""Utilities for Oracle OIC Singer payload handling."""

from __future__ import annotations

from flext_core import FlextResult, t


class FlextTargetOracleOicUtilities:
    """Namespace for message-building and validation helpers."""

    class TargetOracleOic:
        """Singer message helper functions."""

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: dict[str, t.GeneralValueType],
            key_properties: list[str] | None = None,
        ) -> dict[str, t.GeneralValueType]:
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
            record: dict[str, t.GeneralValueType],
        ) -> dict[str, t.GeneralValueType]:
            """Build a Singer RECORD message payload."""
            return {"type": "RECORD", "stream": stream_name, "record": record}

    class Validation:
        """Runtime configuration validation helper functions."""

        @staticmethod
        def validate_config(
            config: dict[str, t.GeneralValueType],
        ) -> FlextResult[bool]:
            """Validate required OIC target configuration keys."""
            required = {"base_url", "oauth_client_id", "oauth_client_secret"}
            missing = sorted(key for key in required if key not in config)
            if missing:
                return FlextResult[bool].fail(
                    f"Missing required config fields: {missing}"
                )
            return FlextResult[bool].ok(value=True)


__all__ = ["FlextTargetOracleOicUtilities"]
