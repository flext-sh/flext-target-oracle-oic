"""Oracle Integration Cloud Singer Target using flext-core patterns.

ReFACTORED: Uses flext-core configuration patterns and clean architecture.
Zero tolerance for code duplication.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from singer_sdk import Target

from flext_observability.logging import get_logger
from flext_target_oracle_oic.config import TargetOracleOICConfig
from flext_target_oracle_oic.sinks import (
    ConnectionsSink,
    IntegrationsSink,
    LookupsSink,
    OICBaseSink,
    PackagesSink,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

    from singer_sdk.sinks import Sink

logger = get_logger(__name__)


class TargetOracleOIC(Target):
    """Oracle OIC Singer Target using flext-core patterns.

    Clean architecture implementation for Oracle Integration Cloud.
    Uses flext-core configuration and logging patterns.
    """

    name = "target-oracle-oic"
    # Use flext-core configuration class
    config_class = TargetOracleOICConfig
    default_sink_class = OICBaseSink

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.logger = logger

    def get_sink(self, stream_name: str, *, record: dict[str, Any] | None = None, schema: dict[str, Any] | None = None, key_properties: Sequence[str] | None = None) -> Sink:
        """Get appropriate sink for the given stream.

        Args:
            stream_name: Name of the data stream to process.
            record: Optional record for context.
            schema: Optional schema for validation.
            key_properties: Optional key properties for the stream.

        Returns:
            Sink instance for processing the stream data.

        """
        sink_class = self._get_sink_class(stream_name)
        return sink_class(target=self,
            stream_name=stream_name,
            schema=schema or {},
            key_properties=key_properties,
        )

    def _get_sink_class(self, stream_name: str) -> type[OICBaseSink]:
        sink_mapping = {
            "connections": ConnectionsSink,
            "integrations": IntegrationsSink,
            "packages": PackagesSink,
            "lookups": LookupsSink,
        }
        return sink_mapping.get(stream_name, self.default_sink_class)


def main() -> None:
        TargetOracleOIC.cli()


if __name__ == "__main__":
            main()
