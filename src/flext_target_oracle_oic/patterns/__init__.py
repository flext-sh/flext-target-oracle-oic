"""Oracle OIC patterns using flext-core patterns."""

from __future__ import annotations

from flext_target_oracle_oic.patterns.oic_patterns import (
    OICDataTransformer,
    OICEntryManager,
    OICSchemaMapper,
    OICTypeConverter,
)

__all__: list[str] = [
    "OICDataTransformer",
    "OICEntryManager",
    "OICSchemaMapper",
    "OICTypeConverter",
]
