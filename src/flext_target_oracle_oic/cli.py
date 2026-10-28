"""CLI facade for target Oracle OIC package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence

from flext_target_oracle_oic.api import FlextTargetOracleOicService


class FlextTargetOracleOicCli:
    """Minimal CLI wrapper bound to the target service facade."""

    @classmethod
    def run(cls, args: Sequence[str] | None = None) -> int:
        """Execute the canonical target CLI entry point.

        Args:
            args: Optional command-line arguments; defaults to ``sys.argv[1:]``
                when omitted.

        Returns:
            The process exit code.

        """
        _ = cls
        exit_code: int = FlextTargetOracleOicService().cli_main(args)
        return exit_code


def main() -> int:
    """Run the target Oracle OIC CLI entry point.

    Returns:
        The process exit code.

    """
    return FlextTargetOracleOicCli.run()


__all__: list[str] = ["FlextTargetOracleOicCli", "main"]
