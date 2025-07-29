"""Oracle Integration Cloud target implementation."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar

# MIGRATED: Singer SDK imports centralized via flext-meltano
from flext_meltano.singer import FlextMeltanoTarget as Target

from flext_target_oracle_oic.application import OICTargetOrchestrator
from flext_target_oracle_oic.sinks import (
    ConnectionsSink,
    IntegrationsSink,
    LookupsSink,
    OICBaseSink,
    PackagesSink,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

    from flext_meltano import Sink


class TargetOracleOIC(Target):
    """Oracle Integration Cloud (OIC) target for Singer.

    This target handles data integration with Oracle Integration Cloud,
    supporting OAuth2 authentication and integration artifact management.

    Key features:
    - OAuth2 authentication with OIC
    - Secure integration artifact upload
    - Configurable import modes (create, update, create_or_update)
    - Automatic integration activation
    - Comprehensive error handling and retry logic

    Configuration:
    - base_url: OIC instance base URL
    - oauth_client_id: OAuth2 client ID
    - oauth_client_secret: OAuth2 client secret
    - oauth_token_url: OAuth2 token endpoint URL
    - oauth_client_aud: OAuth2 client audience (optional)
    - import_mode: Integration import mode
    - activate_integrations: Auto-activate after import

    Usage:
        target = TargetOracleOIC(config={
            "base_url": "https://your-oic-instance.com",
            "oauth_client_id": "your_client_id",
            "oauth_client_secret": "your_client_secret",
            "oauth_token_url": "https://identity.oraclecloud.com/oauth2/v1/token"
        })
    """

    name = "target-oracle-oic"
    # Use Singer SDK default configuration (will define custom later if needed)
    default_sink_class = OICBaseSink

    config_jsonschema: ClassVar[dict[str, object]] = {
        "type": "object",
        "properties": {
            "base_url": {
                "type": "string",
                "description": "OIC instance base URL",
            },
            "oauth_client_id": {
                "type": "string",
                "description": "OAuth2 client ID",
            },
            "oauth_client_secret": {
                "type": "string",
                "description": "OAuth2 client secret",
                "secret": True,
            },
            "oauth_token_url": {
                "type": "string",
                "description": "OAuth2 token endpoint URL",
            },
            "oauth_client_aud": {
                "type": ["string", "null"],
                "description": "OAuth2 client audience",
            },
            "import_mode": {
                "type": "string",
                "enum": ["create", "update", "create_or_update"],
                "default": "create_or_update",
                "description": "Import mode for integrations",
            },
            "activate_integrations": {
                "type": "boolean",
                "default": False,
                "description": "Automatically activate integrations after import",
            },
        },
        "required": [
            "base_url",
            "oauth_client_id",
            "oauth_client_secret",
            "oauth_token_url",
        ],
    }

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
        # Initialize the orchestrator for modular architecture
        self._orchestrator: OICTargetOrchestrator | None = None

    def setup(self) -> None:
        """Setup the target orchestrator."""
        if self._orchestrator is None:
            self._orchestrator = OICTargetOrchestrator(self.config)
            setup_result = self._orchestrator.setup()
            if not setup_result.is_success:
                self.logger.error(f"Orchestrator setup failed: {setup_result.error}")

    def teardown(self) -> None:
        """Teardown the target orchestrator."""
        if self._orchestrator:
            teardown_result = self._orchestrator.teardown()
            if not teardown_result.is_success:
                self.logger.warning(
                    f"Orchestrator teardown failed: {teardown_result.error}",
                )
            self._orchestrator = None

    def _process_schema_message(self, message_dict: dict[str, Any]) -> None:
        """Process a schema message by creating and registering the appropriate sink.

        Args:
            message_dict: The schema message dictionary.

        """
        # Call parent implementation first
        super()._process_schema_message(message_dict)

        # Ensure sink is created and registered for this stream
        stream_name = message_dict["stream"]
        schema = message_dict["schema"]
        key_properties = message_dict.get("key_properties", [])

        # Add sink if it doesn't exist yet
        if not self.sink_exists(stream_name):
            self.add_sink(stream_name, schema, key_properties)

    def get_sink(
        self,
        stream_name: str,
        *,
        record: dict[str, Any] | None = None,
        schema: dict[str, Any] | None = None,
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
        # Return existing sink if it exists
        if self.sink_exists(stream_name):
            return self._sinks_active[stream_name]

        # Create new sink only if we have a valid schema
        if schema and "properties" in schema:
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
            "connections": ConnectionsSink,
            "integrations": IntegrationsSink,
            "packages": PackagesSink,
            "lookups": LookupsSink,
        }
        return sink_mapping.get(stream_name, self.default_sink_class)

    def _get_sink_class(self, stream_name: str) -> type[OICBaseSink]:
        """Private method - delegates to public get_sink_class."""
        return self.get_sink_class(stream_name)


def main() -> None:
    TargetOracleOIC.cli()


if __name__ == "__main__":
    main()
