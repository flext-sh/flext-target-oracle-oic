"""Singer Oracle OIC target protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol, runtime_checkable

from flext_core.protocols import FlextProtocols
from flext_meltano.protocols import FlextMeltanoProtocols
from flext_oracle_oic.protocols import FlextOracleOicProtocols
from flext_target_oracle_oic.typings import t


class FlextTargetOracleOicProtocols(FlextMeltanoProtocols, FlextOracleOicProtocols):
    """Singer Target Oracle OIC protocols extending OracleOic and Meltano protocols.

    Extends both FlextOracleOicProtocols and FlextMeltanoProtocols via multiple inheritance
    to inherit all Oracle OIC protocols, Meltano protocols, and foundation protocols.

    Architecture:
    - EXTENDS: FlextOracleOicProtocols (inherits .OracleOic.* protocols)
    - EXTENDS: FlextMeltanoProtocols (inherits .Meltano.* protocols)
    - ADDS: Target Oracle OIC-specific protocols in TargetOracleOic namespace
    - PROVIDES: Root-level alias `p` for convenient access

    Usage:
    from flext_target_oracle_oic.protocols import p

    # Foundation protocols (inherited)
    result: p.Result[str]
    service: p.Service[str]

    # Oracle OIC protocols (inherited)
    oic: p.OracleOic.*

    # Meltano protocols (inherited)
    target: p.Meltano.TargetProtocol

    # Target Oracle OIC-specific protocols
    oic_integration: p.TargetOracleOic.OracleOic.OicIntegrationProtocol
    """

    class TargetOracleOic:
        """Singer Target domain protocols."""

        class OracleOic:
            """Singer Target Oracle OIC domain protocols for Oracle OIC loading.

            Provides protocol definitions for Oracle OIC integration operations, including
            data integration, transformation, batch processing, payload validation,
            throughput optimization, and integration status tracking.
            """

            @runtime_checkable
            class OicIntegrationProtocol(FlextProtocols.Service[t.GeneralValueType], Protocol):
                """Protocol for Oracle OIC integration.

                Defines the interface for integrating data with Oracle OIC.
                """

                def integrate(
                    self, data: Mapping[str, t.JsonValue]
                ) -> FlextProtocols.Result[bool]:
                    """Integrate data with Oracle OIC.

                    Args:
                        data: Data to integrate.

                    Returns:
                        Result indicating success or failure of the integration.

                    """
                    ...

                def transform_to_oic(
                    self,
                    record: Mapping[str, t.JsonValue],
                ) -> FlextProtocols.Result[Mapping[str, t.JsonValue]]:
                    """Transform Singer record to OIC format.

                    Args:
                        record: Singer record to transform.

                    Returns:
                        Result containing the transformed record in OIC format.

                    """
                    ...

                def invoke_integration(
                    self,
                    payload: Mapping[str, t.JsonValue],
                ) -> FlextProtocols.Result[Mapping[str, t.JsonValue]]:
                    """Invoke OIC integration with payload.

                    Args:
                        payload: Integration payload.

                    Returns:
                        Result containing the integration response.

                    """
                    ...

                def process_batch(
                    self,
                    records: list[Mapping[str, t.JsonValue]],
                ) -> FlextProtocols.Result[bool]:
                    """Process batch of records for OIC.

                    Args:
                        records: List of records to process.

                    Returns:
                        Result indicating success or failure of the batch processing.

                    """
                    ...

                def validate_payload(
                    self,
                    payload: Mapping[str, t.JsonValue],
                ) -> FlextProtocols.Result[bool]:
                    """Validate payload for OIC compatibility.

                    Args:
                        payload: Payload to validate.

                    Returns:
                        Result indicating whether the payload is valid.

                    """
                    ...

                def optimize_throughput(
                    self,
                    config: Mapping[str, t.JsonValue],
                ) -> FlextProtocols.Result[Mapping[str, t.JsonValue]]:
                    """Optimize OIC throughput settings.

                    Args:
                        config: Configuration to optimize.

                    Returns:
                        Result containing optimized configuration.

                    """
                    ...

                def track_integration_status(
                    self,
                    integration_id: str,
                ) -> FlextProtocols.Result[Mapping[str, t.JsonValue]]:
                    """Track integration execution status.

                    Args:
                        integration_id: ID of the integration to track.

                    Returns:
                        Result containing the integration status information.

                    """
                    ...


# Runtime alias for simplified usage
p = FlextTargetOracleOicProtocols

__all__ = [
    "FlextTargetOracleOicProtocols",
    "p",
]
