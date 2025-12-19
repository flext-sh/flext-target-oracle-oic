"""Oracle Integration Cloud target sinks.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from typing import override

from flext_api import FlextApiClient
from flext_api.settings import FlextApiSettings
from flext_core import FlextLogger, FlextResult

# Use FLEXT Meltano wrappers instead of direct singer_sdk imports (domain separation)
from flext_meltano import FlextSink as Sink, FlextTarget as Target

from flext_target_oracle_oic.constants import c
from flext_target_oracle_oic.settings import TargetOracleOicSettings
from flext_target_oracle_oic.target_config import OICOAuth2Authenticator

# Constants - moved to c.TargetOracleOic.OAuth.HTTP_NOT_FOUND and .JSON_MIME

logger = FlextLogger(__name__)


class OICBaseSink(Sink):
    """Base sink for Oracle Integration Cloud."""

    @override
    def __init__(
        self,
        target: Target,
        stream_name: str,
        schema: dict[str, object],
        key_properties: Sequence[str] | None = None,
    ) -> None:
        """Initialize base sink with target and stream metadata."""
        super().__init__(target, stream_name, schema, key_properties)
        # Critical: Set tap_name for Singer SDK auth compatibility
        self.tap_name = "target-oracle-oic"  # Required by Singer SDK authenticators
        self._authenticator: OICOAuth2Authenticator | None = None
        self._client: FlextApiClient | None = None

    @property
    def authenticator(self: object) -> OICOAuth2Authenticator:
        """Get or create OAuth2 authenticator instance.

        Returns:
        OICOAuth2Authenticator for API authentication.

        """
        if not self._authenticator:
            # Create TargetOracleOicSettings from sink configuration
            config = TargetOracleOicSettings(
                oauth_client_id=self.config.get("oauth_client_id", ""),
                oauth_client_secret=self.config.get("oauth_client_secret", ""),
                oauth_token_url=self.config.get("oauth_token_url", ""),
                oauth_client_aud=self.config.get("oauth_client_aud"),
                oauth_scope=self.config.get("oauth_scope", ""),
                base_url=self.config.get(
                    "base_url",
                    "https://default.integration.ocp.oraclecloud.com",
                ),
            )
            self._authenticator = OICOAuth2Authenticator(config)
        return self._authenticator

    @property
    def client(self: object) -> FlextApiClient:
        """Get or create HTTP client with authentication headers.

        Returns:
        Configured FlextApiClient for OIC API requests.

        """
        if not self._client:
            # Get access token for authentication
            token_result: FlextResult[object] = self.authenticator.get_access_token()
            if not token_result.success:
                msg: str = f"Authentication failed: {token_result.error}"
                raise RuntimeError(msg)

            # Create client with Bearer token
            auth_headers = {
                "Authorization": f"Bearer {token_result.data}",
                "Content-Type": c.TargetOracleOic.OAuth.JSON_MIME,
                "Accept": c.TargetOracleOic.OAuth.JSON_MIME,
            }

            api_config = FlextApiSettings(
                base_url=self.config["base_url"],
                headers=auth_headers,
                timeout=30.0,
            )
            self._client = FlextApiClient(api_config)
        return self._client

    def preprocess_record(
        self,
        record: dict[str, object],
        _context: dict[str, object] | None,
    ) -> dict[str, object]:
        """Preprocess record before batch processing.

        Args:
        record: Raw record data to preprocess.
        _context: Optional context information (unused).

        Returns:
        Preprocessed record ready for API submission.

        """
        return record

    def process_batch(self, context: dict[str, object]) -> None:
        """Process batch of records to OIC API.

        Groups records by operation type and submits in batches
        respecting OIC API batch size limits.

        Args:
        context: Batch context containing records and metadata.

        Returns:
        object: Description of return value.

        """
        if not context.get("records"):
            return
        records_obj = context["records"]
        records: list[dict[str, object]] = (
            records_obj if isinstance(records_obj, list) else []
        )
        batch_size = min(len(records), 100)  # OIC API batch limit
        # Group records by operation type for more efficient processing
        create_records: list[dict[str, object]] = []
        update_records: list[dict[str, object]] = []
        for record in records:
            if self._record_exists(record):
                update_records.append(record)
            else:
                create_records.append(record)
        # Process creates in batches
        if create_records:
            for i in range(0, len(create_records), batch_size):
                batch = create_records[i : i + batch_size]
                self._process_create_batch(batch, context)
        # Process updates in batches
        if update_records:
            for i in range(0, len(update_records), batch_size):
                batch = update_records[i : i + batch_size]
                self._process_update_batch(batch, context)

    def _record_exists(self, _record: dict[str, object]) -> bool:
        # Default implementation - subclasses should override
        return False

    def _process_create_batch(
        self,
        records: list[dict[str, object]],
        context: dict[str, object],
    ) -> None:
        # Default implementation processes records individually
        # Subclasses should override for true batch operations
        for record in records:
            self.process_record(record, context)

    def _process_update_batch(
        self,
        records: list[dict[str, object]],
        context: dict[str, object],
    ) -> None:
        # Default implementation processes records individually
        # Subclasses should override for true batch operations
        for record in records:
            self.process_record(record, context)

    def process_record(
        self,
        _record: dict[str, object],
        _context: dict[str, object],
    ) -> None:
        """Process a single record - default implementation for base sink."""
        # Default implementation: log and skip
        # Subclasses should override this method
        self.logger.warning(
            "OICBaseSink.process_record called directly - "
            "stream '%s' should use a specific sink class",
            self.stream_name,
        )


class ConnectionsSink(OICBaseSink):
    """Oracle Integration Cloud target sink for connections."""

    name = "connections"

    def process_record(
        self,
        record: dict[str, object],
        _context: dict[str, object],
    ) -> None:
        """Process a connection record.

        Creates new connections or updates existing ones based on record ID.

        Args:
        record: Connection record data containing id and configuration.
        _context: Processing context (unused).

        """
        connection_id = str(record.get("id", ""))
        # Check if connection exists:
        response = self.client.get(
            f"/ic/api/integration/v1/connections/{connection_id}",
        )
        if response.status_code == c.TargetOracleOic.OAuth.HTTP_NOT_FOUND:
            # Create new connection
            self._create_connection(record)
        else:
            # Update existing connection
            self._update_connection(connection_id, record)

    def _create_connection(self, record: dict[str, object]) -> None:
        payload = {
            "connectionProperties": {
                "name": record["name"],
                "identifier": record["id"],
                "description": record.get("description", ""),
                "adapterType": record["adapter_type"],
                "connectionProperties": record.get("properties", {}),
            },
        }
        response = self.client.post(
            "/ic/api/integration/v1/connections",
            json=payload,
        )
        response.raise_for_status()

    def _update_connection(
        self,
        connection_id: str,
        record: dict[str, object],
    ) -> None:
        payload = {
            "connectionProperties": {
                "description": record.get("description", ""),
                "connectionProperties": record.get("properties", {}),
            },
        }
        response = self.client.put(
            f"/ic/api/integration/v1/connections/{connection_id}",
            json=payload,
        )
        response.raise_for_status()


class IntegrationsSink(OICBaseSink):
    """Oracle Integration Cloud target sink for integrations."""

    name = "integrations"

    def process_record(
        self,
        record: dict[str, object],
        _context: dict[str, object],
    ) -> None:
        """Process an integration record.

        Imports integrations to OIC with version management.

        Args:
        record: Integration record containing id, version, and integration archive.
        _context: Processing context (unused).

        """
        integration_id = str(record.get("id", ""))
        version = str(record.get("version", "01.00.0000"))
        # Check if integration exists:
        response = self.client.get(
            f"/ic/api/integration/v1/integrations/{integration_id}|{version}",
        )
        if response.status_code == c.TargetOracleOic.OAuth.HTTP_NOT_FOUND:
            # Create new integration from archive if provided:
            if "archive_content" in record:
                self._import_integration(record)
            else:
                self._create_integration(record)
        else:
            # Update existing integration
            self._update_integration(integration_id, version, record)

    def _create_integration(self, record: dict[str, object]) -> None:
        payload = {
            "name": record["name"],
            "identifier": record["id"],
            "description": record.get("description", ""),
            "pattern": record.get("pattern", "ORCHESTRATION"),
        }
        response = self.client.post(
            "/ic/api/integration/v1/integrations",
            json=payload,
        )
        response.raise_for_status()

    def _import_integration(self, record: dict[str, object]) -> None:
        archive_content = record.get("archive_content")
        if isinstance(archive_content, str):
            archive_content = archive_content.encode()
        content: bytes = (
            archive_content
            if isinstance(archive_content, bytes)
            else (
                bytes(archive_content)
                if isinstance(archive_content, bytearray)
                else b""
            )
        )
        files: dict[str, tuple[str, bytes, str]] = {
            "file": ("integration.iar", content, "application/octet-stream"),
        }
        response = self.client.post(
            "/ic/api/integration/v1/integrations/archive",
            files=files,
        )
        response.raise_for_status()

    def _update_integration(
        self,
        integration_id: str,
        version: str,
        record: dict[str, object],
    ) -> None:
        payload = {
            "description": record.get("description", ""),
        }
        response = self.client.put(
            f"/ic/api/integration/v1/integrations/{integration_id}|{version}",
            json=payload,
        )
        response.raise_for_status()


class PackagesSink(OICBaseSink):
    """Oracle Integration Cloud target sink for packages."""

    name = "packages"

    def process_record(
        self,
        record: dict[str, object],
        _context: dict[str, object],
    ) -> None:
        """Process a package record.

        Imports package archives to OIC if archive content is provided.

        Args:
        record: Package record containing id and optional archive_content.
        _context: Processing context (unused).

        """
        package_id = str(record.get("id", ""))
        # Log the package being processed
        self.logger.info("Processing package: %s", package_id)
        # Import package if archive content is provided:
        if "archive_content" in record:
            self._import_package(record)
        else:
            self.logger.warning(
                "No archive content provided for package %s",
                package_id,
            )

    def _import_package(self, record: dict[str, object]) -> None:
        archive_content = record.get("archive_content")
        if isinstance(archive_content, str):
            archive_content = archive_content.encode()
        pkg_bytes: bytes = (
            archive_content
            if isinstance(archive_content, bytes)
            else (
                bytes(archive_content)
                if isinstance(archive_content, bytearray)
                else b""
            )
        )
        files: dict[str, tuple[str, bytes, str]] = {
            "file": ("package.iar", pkg_bytes, "application/octet-stream"),
        }
        response = self.client.post(
            "/ic/api/integration/v1/packages/archive",
            files=files,
        )
        response.raise_for_status()


class LookupsSink(OICBaseSink):
    """Oracle Integration Cloud target sink for lookups."""

    name = "lookups"

    def process_record(
        self,
        record: dict[str, object],
        _context: dict[str, object],
    ) -> None:
        """Process a lookup record.

        Creates new lookups or updates existing ones based on lookup name.

        Args:
        record: Lookup record containing name and lookup definitions.
        _context: Processing context (unused).

        """
        lookup_name = str(record.get("name", ""))
        # Check if lookup exists:
        response = self.client.get(f"/ic/api/integration/v1/lookups/{lookup_name}")
        if response.status_code == c.TargetOracleOic.OAuth.HTTP_NOT_FOUND:
            # Create new lookup
            self._create_lookup(record)
        else:
            # Update existing lookup
            self._update_lookup(lookup_name, record)

    def _create_lookup(self, record: dict[str, object]) -> None:
        payload = {
            "name": record["name"],
            "description": record.get("description", ""),
            "columns": record.get("columns", []),
            "rows": record.get("rows", []),
        }
        response = self.client.post(
            "/ic/api/integration/v1/lookups",
            json=payload,
        )
        response.raise_for_status()

    def _update_lookup(self, lookup_name: str, record: dict[str, object]) -> None:
        payload = {
            "description": record.get("description", ""),
            "rows": record.get("rows", []),
        }
        response = self.client.put(
            f"/ic/api/integration/v1/lookups/{lookup_name}",
            json=payload,
        )
        response.raise_for_status()
