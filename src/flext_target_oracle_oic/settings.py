"""Configuration for target-oracle-oic using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Annotated

from flext_core import FlextSettings
from pydantic import Field, SecretStr

from flext_target_oracle_oic.constants import c


class TargetOracleOicConfig(FlextSettings):
    """Runtime settings for Oracle OIC target authentication and IO."""

    oauth_client_id: Annotated[str, Field(..., description="OAuth client identifier")]
    oauth_client_secret: Annotated[
        SecretStr, Field(..., description="OAuth client secret")
    ]
    oauth_token_url: Annotated[str, Field(..., description="OAuth token endpoint URL")]
    oauth_scope: Annotated[
        str | None,
        Field(
            default=c.TargetOracleOic.DEFAULT_OAUTH_SCOPE,
            description="OAuth scope used in token requests",
        ),
    ]
    oauth_client_aud: Annotated[
        str | None,
        Field(
            default=None,
            description="Optional audience used by OAuth provider",
        ),
    ]
    timeout: Annotated[
        int, Field(default=30, ge=1, description="HTTP timeout in seconds")
    ]

    def get_oauth_client_secret_value(self) -> str:
        """Return the plaintext secret value for outgoing requests."""
        return self.oauth_client_secret.get_secret_value()

    def get_oauth_headers(self) -> Mapping[str, str]:
        """Return static HTTP headers required for token requests."""
        return {
            c.TargetOracleOic.HEADER_CONTENT_TYPE: c.TargetOracleOic.HEADER_CONTENT_TYPE_FORM,
            c.TargetOracleOic.HEADER_ACCEPT: c.TargetOracleOic.HEADER_CONTENT_TYPE_JSON,
        }


__all__ = ["TargetOracleOicConfig"]
