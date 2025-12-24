"""Oracle Integration Cloud target implementation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from typing import ClassVar, override

# Use FLEXT Meltano wrappers instead of direct singer_sdk imports (domain separation)
from flext_meltano import FlextSink as Sink, FlextTarget as Target, typing as th

from flext import FlextResult
from flext_target_oracle_oic.application import OICTargetOrchestrator
from flext_target_oracle_oic.sinks import (
    OICBaseSink,
)


class TargetOracleOic(Target):
    """Oracle Integration Cloud (OIC) target for Singer."""

    name = "target-oracle-oic"
    # Use Singer SDK default configuration (will define custom later if needed)
    default_sink_class = OICBaseSink
    # Create additional target-specific configuration properties
    _additional_properties = th.PropertiesList(
        th.Property(
            "oauth_client_aud",
            th.StringType,
            description="OAuth2 client audience",
        ),
        th.Property(
            "import_mode",
            th.StringType,
            allowed_values=["create", "update", "create_or_update"],
            default="create_or_update",
            description="Import mode for integrations",
        ),
        th.Property(
            "activate_integrations",
            th.BooleanType,
            default=False,
            description="Automatically activate integrations after import",
        ),
    )
    config_jsonschema: ClassVar = th.PropertiesList(
        th.Property(
            "base_url",
            th.StringType,
            required=True,
            description="Oracle OIC base URL",
        ),
        th.Property(
            "oauth_client_id",
            th.StringType,
            required=True,
            description="OAuth2 client ID",
        ),
        th.Property(
            "oauth_client_secret",
            th.StringType,
            required=True,
            secret=True,
            description="OAuth2 client secret",
        ),
        th.Property(
            "oauth_token_url",
            th.StringType,
            required=True,
            description="OAuth2 token URL",
        ),
        th.Property(
            "oauth_client_aud",
            th.StringType,
            description="OAuth2 client audience",
        ),
        *_additional_properties,
    ).to_dict()

    @override
    def __init__(
        self,
        *,
        config: dict[str, object] | None = None,
        parse_env_config: bool = False,
        validate_config: bool = True,
        **_kwargs: object,
    ) -> None:
        """Initialize target with configuration and options."""
        super().__init__(
            config=config,
            parse_env_config=parse_env_config,
            validate_config=validate_config,
            # Do not forward arbitrary kwargs; Singer Target expects fixed signature
        )
        # Initialize the orchestrator for modular architecture
        self._orchestrator: OICTargetOrchestrator | None = None

    def setup(self: object) -> None:
        """Set up the target orchestrator."""
        if self._orchestrator is None:
            self._orchestrator = OICTargetOrchestrator(
                dict[str, object](self.config) if self.config else None,
            )
            setup_result: FlextResult[object] = self._orchestrator.setup()
            if not setup_result.success:
                self.logger.error("Orchestrator setup failed: %s", setup_result.error)

    def teardown(self: object) -> None:
        """Teardown the target orchestrator."""
        if self._orchestrator:
            teardown_result: FlextResult[object] = self._orchestrator.teardown()
            if not teardown_result.success:
                self.logger.warning(
                    "Orchestrator teardown failed: %s",
                    teardown_result.error,
                )
            self._orchestrator = None

    def _process_schema_message(self, message_dict: dict[str, object]) -> None:
        """Process a schema message by creating and registering the appropriate sink.

        Args:
        message_dict: The schema message dictionary.

        Returns:
        object: Description of return value.

        """
        # Ensure sink is created and registered for this stream
        stream_name = str(message_dict["stream"])  # Ensure str for typing
        schema_obj = message_dict["schema"]
        if not isinstance(schema_obj, dict):
            return
        schema: dict[str, object] = schema_obj
        key_properties_obj: list[object] = message_dict.get("key_properties", [])
        key_properties: Sequence[str] | None = (
            key_properties_obj if isinstance(key_properties_obj, list) else None
        )
        # Add sink if it doesn't exist yet
        if not self.sink_exists(stream_name):
            self.add_sink(stream_name, schema, key_properties)

    def get_sink(
        self,
        stream_name: str,
        *,
        record: dict[str, object]
        | None = None,  # kept for interface compatibility, not used
        schema: dict[str, object] | None = None,
        key_properties: Sequence[str] | None = None,
    ) -> Sink:
        """Get appropriate sink for the given stream.

        Args:
        stream_name: Name of the data stream to process.
        record: Optional record for context.
        schema: Optional schema for validation.
        key_properties: Optional key properties for the stream.

        Returns:
        Sink instance for processing the stream data.

        """
        _ = record
        # Return existing sink if it exists
        if self.sink_exists(stream_name):
            return self._sinks_active[stream_name]
        # Create new sink only if we have a valid schema
        if schema and isinstance(schema, dict) and "properties" in schema:
            sink_class = self._get_sink_class(stream_name)
            return sink_class(
                target=self,
                stream_name=stream_name,
                schema=schema,
                key_properties=key_properties,
            )
        # If no schema provided and no existing sink, raise an error
        msg = (
            f"Cannot create sink for stream '{stream_name}' without a valid schema. "
            "Ensure a SCHEMA message is sent before any RECORD messages."
        )
        raise ValueError(msg)

    def get_sink_class(self, stream_name: str) -> type[OICBaseSink]:
        """Get sink class for the given stream name.

        Args:
        stream_name: Name of the stream.

        Returns:
        Appropriate sink class for the stream.

        """
        sink_mapping = {
            "connections": "ConnectionsSink",
            "integrations": "IntegrationsSink",
            "packages": "PackagesSink",
            "lookups": "LookupsSink",
        }
        return sink_mapping.get(stream_name, self.default_sink_class)

    def _get_sink_class(self, stream_name: str) -> type[OICBaseSink]:
        """Private method - delegates to public get_sink_class."""
        return self.get_sink_class(stream_name)


def main() -> None:
    """Entry point for target-oracle-oic CLI."""
    TargetOracleOic.cli()


if __name__ == "__main__":
    main()
