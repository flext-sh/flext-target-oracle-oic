"""Simple helper API for Oracle OIC target configuration workflows."""

from __future__ import annotations

from flext_core import FlextResult, FlextTypes as t

from .target_config import TargetOracleOicConfig


def setup_oic_target(
    config: TargetOracleOicConfig | None = None,
) -> FlextResult[TargetOracleOicConfig]:
    """Resolve and validate target configuration."""
    resolved = config or TargetOracleOicConfig.get_global_instance()
    validation = resolved.validate_business_rules()
    if validation.is_failure:
        return FlextResult[TargetOracleOicConfig].fail(
            validation.error or "Configuration validation failed",
        )
    return FlextResult[TargetOracleOicConfig].ok(resolved)


def validate_oic_target_config(config: TargetOracleOicConfig) -> FlextResult[bool]:
    """Validate provided target configuration object."""
    return config.validate_business_rules()


def get_oic_target_config_schema() -> dict[str, t.GeneralValueType]:
    """Return JSON schema for target configuration model."""
    return TargetOracleOicConfig.model_json_schema()


__all__ = [
    "get_oic_target_config_schema",
    "setup_oic_target",
    "validate_oic_target_config",
]
