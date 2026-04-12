"""Internal runtime adapters for the target-oracle-oic service facade."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from pathlib import Path

from flext_meltano.services.singer_sdk import Target as FlextMeltanoSingerTargetBase
from flext_target_oracle_oic.target import (
    FlextTargetOracleOic,
    FlextTargetOracleOicBaseSink,
)
from flext_target_oracle_oic.typings import t


class FlextTargetOracleOicServiceRuntime:
    """Service-runtime adapters used by the target-oracle-oic facade."""

    class Target(FlextMeltanoSingerTargetBase):
        """Minimal Singer target used by the service facade."""

        name = "target-oracle-oic"

    @classmethod
    def create_sink(
        cls,
        *,
        stream_name: str,
        schema: t.FlatContainerMapping,
        target_config: t.ContainerMapping,
    ) -> FlextTargetOracleOicBaseSink:
        """Create the service-level Singer sink adapter."""
        normalized_target_config = cls.normalize_singer_mapping(target_config)
        runtime_target = FlextTargetOracleOic()
        sink_class: type[FlextTargetOracleOicBaseSink] = runtime_target.get_sink_class(
            stream_name,
        )
        return sink_class(
            target=cls.Target(
                config=dict(normalized_target_config),
                validate_config=False,
            ),
            stream_name=stream_name,
            schema=dict(schema),
            key_properties=[],
        )

    @classmethod
    def normalize_singer_mapping(
        cls,
        source: t.ContainerMapping,
    ) -> dict[str, t.ContainerValue]:
        """Normalize a Singer payload mapping to the OIC runtime contract."""
        normalized: dict[str, t.ContainerValue] = {}
        for key, value in source.items():
            normalized_value = cls.normalize_singer_value(value)
            if normalized_value is not None:
                normalized[str(key)] = normalized_value
        return normalized

    @classmethod
    def normalize_singer_value(
        cls,
        value: t.NormalizedValue,
    ) -> t.ContainerValue | None:
        """Normalize a Singer payload value to the OIC runtime contract."""
        if value is None:
            return None
        if isinstance(value, Path):
            return str(value)
        if isinstance(value, (str, int, float, bool)):
            return value
        if isinstance(value, datetime):
            return value
        if isinstance(value, Mapping):
            return cls.normalize_singer_mapping(value)
        normalized_sequence: list[t.ContainerValue] = []
        for item in value:
            normalized_item = cls.normalize_singer_value(item)
            if normalized_item is not None:
                normalized_sequence.append(normalized_item)
        return normalized_sequence


__all__: list[str] = ["FlextTargetOracleOicServiceRuntime"]
