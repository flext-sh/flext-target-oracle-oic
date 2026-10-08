"""Singer target definition for Oracle OIC.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_oic/target
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_meltano.services.singer_target import FlextMeltanoTargetAbstractions

from flext_target_oracle_oic import c, p, r
from flext_target_oracle_oic._utilities.sink import FlextTargetOracleOicSink


class FlextTargetOracleOic(FlextMeltanoTargetAbstractions):
    """Singer target entry point for Oracle OIC."""

    name: ClassVar[str] = c.TargetOracleOic.TARGET_NAME
    default_sink_class: ClassVar[type[FlextTargetOracleOicSink]] = (
        FlextTargetOracleOicSink
    )

    @staticmethod
    def setup() -> p.Result[bool]:
        """Set up target resources.

        Returns:
            The resulting ``p.Result[bool]``.
        """
        return r[bool].ok(value=True)

    @staticmethod
    def teardown() -> p.Result[bool]:
        """Teardown target resources.

        Returns:
            The resulting ``p.Result[bool]``.
        """
        return r[bool].ok(value=True)


__all__: list[str] = ["FlextTargetOracleOic"]
