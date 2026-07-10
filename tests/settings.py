"""Runtime settings for flext-target-oracle-oic tests."""

from __future__ import annotations

from typing import Annotated

from flext_tests import FlextTestsSettings

from flext_target_oracle_oic import FlextTargetOracleOicSettings, t, u


class TestsFlextTargetOracleOicSettings(
    FlextTargetOracleOicSettings,
    FlextTestsSettings,
):
    """Target Oracle OIC settings extended with the shared test namespace.

    Supplies test defaults for the production OAuth credential fields so the
    suite's argless ``fetch_global()`` construction succeeds without real creds.
    """

    oauth_client_id: Annotated[
        str,
        u.Field(default="test-oic-client-id", description="Test OAuth client id."),
    ]
    oauth_client_secret: Annotated[
        t.SecretStr,
        u.Field(
            default=t.SecretStr("test-oic-client-secret"),
            description="Test OAuth client secret.",
        ),
    ]
    oauth_token_url: Annotated[
        str,
        u.Field(
            default="https://oic.test.invalid/oauth/token",
            description="Test OAuth token endpoint.",
        ),
    ]


__all__: list[str] = ["TestsFlextTargetOracleOicSettings"]
