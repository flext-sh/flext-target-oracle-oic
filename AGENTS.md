# AGENTS.md — flext-target-oracle-oic

> **Parent workspace law** lives in [`../AGENTS.md`](../AGENTS.md) — read it first.
> Universal engineering core: `~/.agents/UNIVERSAL_CORE.md`. Composition: global skills + parent/root `AGENTS.md` + this scope delta. Do not re-embed universal law.
>
> **Standalone / independent mode:** when `../AGENTS.md` does not resolve, pin the parent raw `AGENTS.md` URL to the same branch/release as this package (never `main`).

<!-- AIHUB-AGENTS-SCOPE-LOCAL-BEGIN -->
**Package:** `flext_target_oracle_oic` · deps: `flext-api`, `flext-cli`, `flext-core`, `flext-db-oracle`, `flext-meltano`, `flext-observability`, `flext-oracle-oic`

## Overview

Singer **target** (loader) for Oracle Integration Cloud. Thin driver over `flext-meltano` (ADR-006), delegating OIC operations to `flext-oracle-oic`. Widest dependency fan-in of the connectors.

## Structure

```text
src/flext_target_oracle_oic/
├── api.py            # FlextTargetOracleOicService(FlextMeltanoTargetServiceBase)
├── target.py         # FlextTargetOracleOic(FlextMeltanoTargetAbstractions) — per-stream OIC sinks
├── cli.py
├── singer/ application/ connection/ patterns/   # supporting implementation
├── constants.py typings.py protocols.py models.py utilities.py   # AUTO-GENERATED facets
└── _utilities/
```

## Code Map

| Symbol | Kind | Location | Role |
|--------|------|----------|------|
| `FlextTargetOracleOicService` | class | `api.py` | `FlextMeltanoTargetServiceBase` |
| `FlextTargetOracleOic` | class | `target.py` | `FlextMeltanoTargetAbstractions`; maps named OIC streams → dedicated sinks |

## Conventions (specific to this package)

- Named OIC streams map to **dedicated sink classes**; supporting logic lives in `singer/`/`application/`/`connection/`/`patterns/`.
- Config/settings canonical pattern: ADR-012.
- Codemod governance (ast-grep + make mod): ADR-014.

## Commands

```bash
make check PROJECT=flext-target-oracle-oic
make test  PROJECT=flext-target-oracle-oic       # tests/unit
```
<!-- AIHUB-AGENTS-SCOPE-LOCAL-END -->
