"""Singer Oracle OIC target protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import FlextMeltanoProtocols
from flext_oracle_oic import FlextOracleOicProtocols


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
    from flext_target_oracle_oic import p

    # Foundation protocols (inherited)
    result: p.Result[str]
    service: p.Service[str]

    # Oracle OIC protocols (inherited)
    oic: p.OracleOic.*

    # Meltano protocols (inherited)
    target: p.Meltano.Target

    # Target Oracle OIC-specific protocols
    oic_integration: p.TargetOracleOic.OracleOic.OicIntegration
    """


p = FlextTargetOracleOicProtocols
__all__: list[str] = ["FlextTargetOracleOicProtocols", "p"]
