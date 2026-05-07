"""Internal runtime adapters for the target-oracle-oic service facade."""

from __future__ import annotations

from flext_target_oracle_oic import (
    FlextTargetOracleOic,
    FlextTargetOracleOicBaseSink,
    m,
    t,
    u,
)


class FlextTargetOracleOicServiceRuntime:
    """Service-runtime adapters used by the target-oracle-oic facade."""

    class Target(m.Meltano.SingerTargetBase):
        """Minimal Singer target used by the service facade."""

        name = "target-oracle-oic"

    @classmethod
    def create_sink(
        cls,
        *,
        stream_name: str,
        schema: t.JsonMapping,
        target_config: t.JsonMapping,
    ) -> FlextTargetOracleOicBaseSink:
        """Create the service-level Singer sink adapter."""
        normalized_target_config = u.normalize_to_json_mapping(
            target_config,
        )
        runtime_target = FlextTargetOracleOic()
        sink_class: type[FlextTargetOracleOicBaseSink] = (
            runtime_target.fetch_sink_class(
                stream_name,
            )
        )
        return sink_class(
            target=cls.Target(
                config=t.json_dict_adapter().validate_python(normalized_target_config),
                validate_config=False,
            ),
            stream_name=stream_name,
            schema=t.json_dict_adapter().validate_python(schema),
            key_properties=[],
        )


__all__: list[str] = ["FlextTargetOracleOicServiceRuntime"]
