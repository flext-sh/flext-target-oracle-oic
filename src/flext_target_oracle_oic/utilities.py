"""Utilities for Oracle OIC Singer payload handling."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_core import r
from flext_meltano import FlextMeltanoUtilities
from flext_oracle_oic import FlextOracleOicUtilities

from flext_target_oracle_oic import m, t


class FlextTargetOracleOicUtilities(FlextMeltanoUtilities, FlextOracleOicUtilities):
    """Namespace for message-building and validation helpers."""

    class TargetOracleOic:
        """Singer message helper functions."""

        @staticmethod
        def create_record_message(
            stream_name: str, record: Mapping[str, t.Scalar]
        ) -> Mapping[str, str | Mapping[str, t.Scalar]]:
            """Build a Singer RECORD message payload."""
            return {"type": "RECORD", "stream": stream_name, "record": record}

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: Mapping[str, t.Container],
            key_properties: Sequence[str] | None = None,
        ) -> Mapping[str, str | Mapping[str, t.Container] | Sequence[str]]:
            """Build a Singer SCHEMA message payload."""
            return {
                "type": "SCHEMA",
                "stream": stream_name,
                "schema": schema,
                "key_properties": key_properties or [],
            }

        class Validation:
            """Runtime configuration validation helper functions."""

            @staticmethod
            def validate_config(config: Mapping[str, t.Scalar]) -> r[bool]:
                """Validate required OIC target configuration keys."""
                required = {"base_url", "oauth_client_id", "oauth_client_secret"}
                missing = sorted(key for key in required if key not in config)
                if missing:
                    return r[bool].fail(f"Missing required config fields: {missing}")
                return r[bool].ok(value=True)

        class Factories:
            """Factory helpers for OIC model instances."""

            @staticmethod
            def create_oic_connection(
                data: Mapping[str, t.Container],
            ) -> m.TargetOracleOic.OICConnection:
                """Create an OICConnection model from generic payload via Pydantic validation."""
                return m.TargetOracleOic.OICConnection.model_validate({
                    **data,
                    "properties": data,
                })

            @staticmethod
            def create_oic_integration(
                data: Mapping[str, t.Container],
            ) -> m.TargetOracleOic.OICIntegration:
                """Create an OICIntegration model from generic payload via Pydantic validation."""
                return m.TargetOracleOic.OICIntegration.model_validate(data)

            @staticmethod
            def create_oic_package(
                data: Mapping[str, t.Container],
            ) -> m.TargetOracleOic.OICPackage:
                """Create an OICPackage model from generic payload via Pydantic validation."""
                return m.TargetOracleOic.OICPackage.model_validate(data)

            @staticmethod
            def create_oic_lookup(
                data: Mapping[str, t.Container],
            ) -> m.TargetOracleOic.OICLookup:
                """Create an OICLookup model from generic payload via Pydantic validation."""
                return m.TargetOracleOic.OICLookup.model_validate(data)


u = FlextTargetOracleOicUtilities
__all__ = [
    "FlextTargetOracleOicUtilities",
    "u",
]
