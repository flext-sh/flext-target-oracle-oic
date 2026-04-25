"""CLI facade for target Oracle OIC package."""

from __future__ import annotations

from flext_target_oracle_oic import (
    FlextTargetOracleOicService,
    t,
)


class FlextTargetOracleOicCli:
    """Minimal CLI wrapper bound to the target service facade."""

    @classmethod
    def run(cls, args: t.StrSequence | None = None) -> int:
        """Execute the canonical target CLI entry point."""
        _ = cls
        return FlextTargetOracleOicService().cli_main(args)


def main() -> int:
    """Run the target Oracle OIC CLI entry point."""
    return FlextTargetOracleOicCli.run()


__all__: list[str] = ["FlextTargetOracleOicCli", "main"]
