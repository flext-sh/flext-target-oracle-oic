# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export map part."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map

FLEXT_TARGET_ORACLE_OIC_LAZY_IMPORTS_PART_01 = build_lazy_import_map(
    {
        "._utilities.service_runtime": ("FlextTargetOracleOicServiceRuntime",),
        ".api": (
            "FlextTargetOracleOicService",
            "target_oracle_oic",
        ),
        ".cli": (
            "FlextTargetOracleOicCli",
            "main",
        ),
        ".constants": (
            "FlextTargetOracleOicConstants",
            "c",
        ),
        ".models": (
            "FlextTargetOracleOicModels",
            "m",
        ),
        ".protocols": (
            "FlextTargetOracleOicProtocols",
            "p",
        ),
        ".settings": ("FlextTargetOracleOicSettings",),
        ".typings": (
            "FlextTargetOracleOicTypes",
            "t",
        ),
        ".utilities": (
            "FlextTargetOracleOicUtilities",
            "u",
        ),
    },
)

__all__: list[str] = ["FLEXT_TARGET_ORACLE_OIC_LAZY_IMPORTS_PART_01"]
