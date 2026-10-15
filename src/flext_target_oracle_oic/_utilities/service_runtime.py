"""Internal runtime adapters for the target-oracle-oic service facade.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import u

from flext_target_oracle_oic import c, m, t
from flext_target_oracle_oic._utilities.sink import FlextTargetOracleOicSink
from flext_target_oracle_oic.target import FlextTargetOracleOic


class FlextTargetOracleOicServiceRuntime:
    """Service-runtime adapters used by the target-oracle-oic facade."""

    class Target(m.Meltano.SingerTargetBase):
        """Minimal Singer target used by the service facade."""

        name = c.TargetOracleOic.TARGET_NAME

    @classmethod
    def create_sink(
        cls,
        *,
        stream_name: str,
        schema: t.JsonMapping,
        target_config: t.ScalarMapping,
    ) -> FlextTargetOracleOicSink:
        """Create the service-level Singer sink adapter.

        Args:
            stream_name: Name of the Singer stream the sink receives.
            schema: Singer schema describing the stream's record structure.
            target_config: Scalar target configuration applied to the sink's
                target instance.

        Returns:
            The created Oracle OIC sink adapter.

        """
        normalized_target_config = u.normalize_to_json_mapping(target_config)
        return FlextTargetOracleOic.default_sink_class(
            target=cls.Target(
                config=t.json_dict_adapter().validate_python(normalized_target_config),
                validate_config=False,
            ),
            stream_name=stream_name,
            schema=t.json_dict_adapter().validate_python(schema),
            key_properties=[],
        )


__all__: list[str] = ["FlextTargetOracleOicServiceRuntime"]
