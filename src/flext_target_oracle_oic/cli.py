"""CLI entry point for flext-target-oracle-oic using flext-cli patterns.

Provides a small, typed Click command that delegates output formatting to
flext-cli abstractions (Rich console via FlextCliHelper) and loads a standard
FlextCliContext for consistent behavior across the ecosystem.
"""

from __future__ import annotations

import uuid

import click
from rich.console import Console

try:
    # Prefer modern flext-cli abstractions when available
    from flext_cli import FlextCliConfig, FlextCliContext, FlextCliHelper
except Exception:  # pragma: no cover - fallback for environments without flext-cli
    FlextCliConfig = None
    FlextCliContext = None
    FlextCliHelper = None


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--config", type=click.Path(exists=False), help="Configuration file path")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
def main(config: str | None = None, *, verbose: bool = False) -> None:
    """Provide CLI entry point for flext-target-oracle-oic using flext-cli."""
    console = Console(quiet=not verbose)

    # Initialize flext-cli context if available; otherwise, fallback to direct console
    if (
        FlextCliConfig is not None
        and FlextCliContext is not None
        and FlextCliHelper is not None
    ):
        cfg = FlextCliConfig()
        # Apply minimal overrides for demonstration; real commands can extend this
        if hasattr(cfg, "model_copy"):
            cfg = cfg.model_copy(update={"debug": bool(verbose)})
        FlextCliContext(id=str(uuid.uuid4()), config=cfg, console=console)
        helper = FlextCliHelper(console=console)

        if verbose:
            helper.print_info("Starting flext-target-oracle-oic in verbose mode")
        if config:
            helper.print_info(f"Using config file: {config}")
        helper.print_success("flext-target-oracle-oic CLI - Ready")
        return

    # Fallback path: no flext-cli available; use raw console
    if verbose:
        console.print("Starting flext-target-oracle-oic in verbose mode")
    if config:
        console.print(f"Using config file: {config}")
    console.print("flext-target-oracle-oic CLI - Ready")


if __name__ == "__main__":  # pragma: no cover - script entry
    main()
