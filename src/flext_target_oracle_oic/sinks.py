"""Oracle Integration Cloud target sinks."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import httpx

# Removed circular dependency - use DI pattern
from flext_core import get_logger

# Import directly from Singer SDK to avoid circular imports
from singer_sdk.sinks import Sink

from flext_target_oracle_oic.auth import OICAuthConfig, OICOAuth2Authenticator

if TYPE_CHECKING:
    from collections.abc import Sequence

    from singer_sdk import Target

logger = get_logger(__name__)


class OICBaseSink(Sink):
    """Base sink for Oracle Integration Cloud."""

    def __init__(
        self,
        target: Target,
        stream_name: str,
        schema: dict[str, object],
        key_properties: Sequence[str] | None = None,
    ) -> None:
        super().__init__(target, stream_name, schema, key_properties)
        # CRITICAL: Set tap_name for Singer SDK auth compatibility
        self.tap_name = "target-oracle-oic"  # Required by Singer SDK authenticators
        self._authenticator: OICOAuth2Authenticator | None = None
        self._client: httpx.Client | None = None

    @property
    def authenticator(self) -> OICOAuth2Authenticator:
        """Get or create OAuth2 authenticator instance.

        Returns:
            OICOAuth2Authenticator for API authentication.

        """
        if not self._authenticator:
            # Create OICAuthConfig from sink configuration
            auth_config = OICAuthConfig(
                oauth_client_id=self.config.get("oauth_client_id", ""),
                oauth_client_secret=self.config.get("oauth_client_secret", ""),
                oauth_token_url=self.config.get("oauth_token_url", ""),
                oauth_client_aud=self.config.get("oauth_client_aud"),
                oauth_scope=self.config.get("oauth_scope", ""),
            )
            self._authenticator = OICOAuth2Authenticator(auth_config)
        return self._authenticator

    @property
    def client(self) -> httpx.Client:
        """Get or create HTTP client with authentication headers.

        Returns:
            Configured httpx.Client for OIC API requests.

        """
        if not self._client:
            # Get access token for authentication
            token_result = self.authenticator.get_access_token()
            if not token_result.is_success:
                msg = f"Authentication failed: {token_result.error}"
                raise RuntimeError(msg)

            # Create client with Bearer token
            auth_headers = {
                "Authorization": f"Bearer {token_result.data}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }

            self._client = httpx.Client(
                base_url=self.config["base_url"],
                headers=auth_headers,
                timeout=30.0,
            )
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

        """
        if not context.get("records"):
            return
        batch_size = min(len(context["records"]), 100)  # OIC API batch limit
        records = context["records"]
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
        self, record: dict[str, object], context: dict[str, object]
    ) -> None:
        """Process a single record - default implementation for base sink.

        Args:
            record: Record data to process.
            context: Processing context.

        """
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
        self, record: dict[str, object], _context: dict[str, object]
    ) -> None:
        """Process a connection record.

        Creates new connections or updates existing ones based on record ID.

        Args:
            record: Connection record data containing id and configuration.
            _context: Processing context (unused).

        """
        connection_id = record.get("id") or ""
        # Check if connection exists:
        response = self.client.get(
            f"/ic/api/integration/v1/connections/{connection_id}",
        )
        if response.status_code == 404:
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

    def _update_connection(self, connection_id: str, record: dict[str, object]) -> None:
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
        self, record: dict[str, object], _context: dict[str, object]
    ) -> None:
        """Process an integration record.

        Imports integrations to OIC with version management.

        Args:
            record: Integration record containing id, version, and integration archive.
            _context: Processing context (unused).

        """
        integration_id = record.get("id") or ""
        version = record.get("version", "01.00.0000")
        # Check if integration exists:
        response = self.client.get(
            f"/ic/api/integration/v1/integrations/{integration_id}|{version}",
        )
        if response.status_code == 404:
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

        # Proper type for httpx files parameter
        files: dict[str, bytes | str] = {
            "file": archive_content or b"",
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
        self, record: dict[str, object], _context: dict[str, object]
    ) -> None:
        """Process a package record.

        Imports package archives to OIC if archive content is provided.

        Args:
            record: Package record containing id and optional archive_content.
            _context: Processing context (unused).

        """
        package_id = record.get("id") or ""
        # Log the package being processed
        self.logger.info(f"Processing package: {package_id}")
        # Import package if archive content is provided:
        if "archive_content" in record:
            self._import_package(record)
        else:
            self.logger.warning(f"No archive content provided for package {package_id}")

    def _import_package(self, record: dict[str, object]) -> None:
        archive_content = record.get("archive_content")
        if isinstance(archive_content, str):
            archive_content = archive_content.encode()
        files = {
            "file": ("package.iar", archive_content or b"", "application/octet-stream"),
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
        self, record: dict[str, object], _context: dict[str, object]
    ) -> None:
        """Process a lookup record.

        Creates new lookups or updates existing ones based on lookup name.

        Args:
            record: Lookup record containing name and lookup definitions.
            _context: Processing context (unused).

        """
        lookup_name = record.get("name") or ""
        # Check if lookup exists:
        response = self.client.get(f"/ic/api/integration/v1/lookups/{lookup_name}")
        if response.status_code == 404:
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
