"""Version information for flext-target-oracle-oic package.

This module contains version information for the flext-target-oracle-oic package.
"""

from __future__ import annotations

# Import from centralized version management system
# 🚨 ARCHITECTURAL COMPLIANCE: Using DI container
from flext_target_oracle_oic.infrastructure.di_container import (
    get_base_config,
    get_domain_entity,
    get_domain_value_object,
    get_field,
    get_service_result,
)

ServiceResult = get_service_result()
DomainEntity = get_domain_entity()
Field = get_field()
DomainValueObject = get_domain_value_object()
BaseConfig = get_base_config()

__version__ = "0.7.0"
__version_info__ = (0, 7, 0)

# FLEXT Enterprise - Unified Versioning System
# Version is managed centrally in flext_core.version
# This maintains backward compatibility while eliminating duplication.
