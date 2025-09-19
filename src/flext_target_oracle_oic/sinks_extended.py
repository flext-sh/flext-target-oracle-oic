"""Oracle Integration Cloud Extended Sinks.

Professional-grade sinks for additional OIC entities including libraries,
certificates, schedules, and projects.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes
from flext_target_oracle_oic.sinks import OICBaseSink

# Constants
HTTP_NOT_FOUND = 404


class LibrariesSink(OICBaseSink):
    """Oracle Integration Cloud target sink for libraries."""

    name = "libraries"

    def process_record(
        self,
        record: FlextTypes.Core.Dict,
        _context: FlextTypes.Core.Dict,
    ) -> None:
        """Process a library record.

        Args:
            record: Library record to process.
            _context: Record context (unused).

        """
        library_id = str(record.get("id", ""))
        # Check if library exists:
        response = self.client.get(f"/ic/api/integration/v1/libraries/{library_id}")
        if response.status_code == HTTP_NOT_FOUND:
            # Create new library
            self._create_library(record)
        else:
            # Update existing library
            self._update_library(library_id, record)

    def _create_library(self, record: FlextTypes.Core.Dict) -> None:
        # If archive content is provided, import it
        if "archive_content" in record:
            self._import_library(record)
            return
        payload = {
            "name": record["name"],
            "identifier": record["id"],
            "description": record.get("description", ""),
            "type": record.get("type", "JAVASCRIPT"),
            "version": record.get("version", "1.0"),
        }
        response = self.client.post(
            "/ic/api/integration/v1/libraries",
            json=payload,
        )
        response.raise_for_status()

    def _import_library(self, record: FlextTypes.Core.Dict) -> None:
        archive_content = record.get("archive_content")
        if isinstance(archive_content, str):
            archive_content = archive_content.encode()
        lib_bytes: bytes
        if isinstance(archive_content, bytes):
            lib_bytes = archive_content
        elif isinstance(archive_content, bytearray):
            lib_bytes = bytes(archive_content)
        else:
            lib_bytes = b""
        files: dict[str, tuple[str, bytes, str]] = {
            "file": (
                "library.jar",
                lib_bytes,
                "application/octet-stream",
            ),
        }
        response = self.client.post(
            "/ic/api/integration/v1/libraries/archive",
            files=files,
        )
        response.raise_for_status()

    def _update_library(self, library_id: str, record: FlextTypes.Core.Dict) -> None:
        payload = {
            "description": record.get("description", ""),
            "version": record.get("version", "1.0"),
        }
        response = self.client.put(
            f"/ic/api/integration/v1/libraries/{library_id}",
            json=payload,
        )
        response.raise_for_status()


class CertificatesSink(OICBaseSink):
    """Oracle Integration Cloud target sink for certificates."""

    name = "certificates"

    def process_record(
        self,
        record: FlextTypes.Core.Dict,
        _context: FlextTypes.Core.Dict,
    ) -> None:
        """Process a certificate record.

        Args:
            record: Certificate record to process.
            _context: Record context (unused).

        """
        cert_alias = str(record.get("alias", ""))
        # Check if certificate exists:
        response = self.client.get(f"/ic/api/integration/v1/certificates/{cert_alias}")
        if response.status_code == HTTP_NOT_FOUND:
            # Create new certificate
            self._create_certificate(record)
        else:
            # Update existing certificate
            self._update_certificate(cert_alias, record)

    def _create_certificate(self, record: FlextTypes.Core.Dict) -> None:
        # Certificate content must be provided
        cert_content = record.get("certificate_content")
        if not cert_content:
            self.logger.warning(
                "No certificate content provided for %s",
                record.get("alias"),
            )
            return
        if isinstance(cert_content, str):
            cert_content = cert_content.encode()
        # Ensure bytes type for files parameter
        content_bytes: bytes = (
            bytes(cert_content) if isinstance(cert_content, (bytes, bytearray)) else b""
        )
        files: dict[str, tuple[str, bytes, str]] = {
            "certificate": (
                f"{record['alias']}.cer",
                content_bytes,
                "application/x-x509-ca-cert",
            ),
        }
        data = {
            "alias": record["alias"],
            "description": record.get("description", ""),
            "password": record.get("password", ""),  # For private key certificates
        }
        response = self.client.post(
            "/ic/api/integration/v1/certificates",
            data=data,
            files=files,
        )
        response.raise_for_status()

    def _update_certificate(
        self, cert_alias: str, record: FlextTypes.Core.Dict,
    ) -> None:
        # Certificates can only be replaced, not updated
        # Delete and recreate if needed:
        if "certificate_content" in record:
            # Delete existing
            response = self.client.delete(
                f"/ic/api/integration/v1/certificates/{cert_alias}",
            )
            response.raise_for_status()
            # Create new
            self._create_certificate(record)


class ProjectsSink(OICBaseSink):
    """Oracle Integration Cloud target sink for projects."""

    name = "projects"

    def process_record(
        self,
        record: FlextTypes.Core.Dict,
        _context: FlextTypes.Core.Dict,
    ) -> None:
        """Process a project record.

        Args:
            record: Project record to process.
            _context: Record context (unused).

        """
        project_id = str(record.get("id", ""))
        # Check if project exists:
        response = self.client.get(f"/ic/api/integration/v1/projects/{project_id}")
        if response.status_code == HTTP_NOT_FOUND:
            # Create new project
            self._create_project(record)
            # Update existing project
            self._update_project(project_id, record)

    def _create_project(self, record: FlextTypes.Core.Dict) -> None:
        payload = {
            "name": record["name"],
            "identifier": record["id"],
            "description": record.get("description", ""),
            "parentId": record.get("parentId"),
            "visibility": record.get("visibility", "PRIVATE"),
            "properties": record.get("properties", {}),
        }
        response = self.client.post(
            "/ic/api/integration/v1/projects",
            json=payload,
        )
        response.raise_for_status()
        # Create folders if provided:
        if "folders" in record:
            project_id_var = str(record.get("id", ""))
            folders = record.get("folders", [])
            if isinstance(folders, list):
                for folder in folders:
                    if isinstance(folder, dict):
                        self._create_folder(project_id_var, folder)

    def _create_folder(self, project_id: str, folder: FlextTypes.Core.Dict) -> None:
        payload = {
            "name": folder["name"],
            "type": folder.get("type", "INTEGRATION"),
            "description": folder.get("description", ""),
        }
        response = self.client.post(
            f"/ic/api/integration/v1/projects/{project_id}/folders",
            json=payload,
        )
        response.raise_for_status()

    def _update_project(self, project_id: str, record: FlextTypes.Core.Dict) -> None:
        payload = {
            "description": record.get("description", ""),
            "visibility": record.get("visibility", "PRIVATE"),
            "properties": record.get("properties", {}),
        }
        response = self.client.put(
            f"/ic/api/integration/v1/projects/{project_id}",
            json=payload,
        )
        response.raise_for_status()


class SchedulesSink(OICBaseSink):
    """Oracle Integration Cloud target sink for schedules."""

    name = "schedules"

    def process_record(
        self,
        record: FlextTypes.Core.Dict,
        _context: FlextTypes.Core.Dict,
    ) -> None:
        """Process a schedule record.

        Args:
            record: Schedule record to process.
            _context: Record context (unused).

        """
        schedule_id = str(record.get("id", ""))
        integration_id = str(record.get("integrationId", ""))
        if not integration_id:
            self.logger.warning(
                "No integration ID provided for schedule %s",
                schedule_id,
            )
            return
        # Check if schedule exists:
        response = self.client.get(
            f"/ic/api/integration/v1/integrations/{integration_id}/schedule",
        )
        if response.status_code == HTTP_NOT_FOUND:
            # Create new schedule
            self._create_schedule(integration_id, record)
            # Update existing schedule
            self._update_schedule(integration_id, record)

    def _create_schedule(
        self, integration_id: str, record: FlextTypes.Core.Dict,
    ) -> None:
        payload = self._build_schedule_payload(record)
        response = self.client.post(
            f"/ic/api/integration/v1/integrations/{integration_id}/schedule",
            json=payload,
        )
        response.raise_for_status()

    def _update_schedule(
        self, integration_id: str, record: FlextTypes.Core.Dict,
    ) -> None:
        payload = self._build_schedule_payload(record)
        response = self.client.put(
            f"/ic/api/integration/v1/integrations/{integration_id}/schedule",
            json=payload,
        )
        response.raise_for_status()

    def _build_schedule_payload(
        self, record: FlextTypes.Core.Dict,
    ) -> FlextTypes.Core.Dict:
        payload = {
            "scheduleType": record.get("scheduleType", "SIMPLE"),
            "enabled": record.get("enabled", True),
            "timezone": record.get("timezone", "UTC"),
        }

        if payload["scheduleType"] == "SIMPLE":
            payload.update(
                {
                    "frequency": record.get("frequency", "DAILY"),
                    "interval": record.get("interval", 1),
                    "startTime": record.get("startTime"),
                    "endTime": record.get("endTime"),
                },
            )
        # Cron schedule
        elif payload["scheduleType"] == "CRON":
            payload["cronExpression"] = record.get("cronExpression", "0 0 * * *")
        # Calendar schedule
        elif payload["scheduleType"] == "CALENDAR":
            payload.update(
                {
                    "calendarId": record.get("calendarId"),
                    "includeHolidays": record.get("includeHolidays", False),
                    "includeWeekends": record.get("includeWeekends", True),
                },
            )
        # Execution windows
        if "executionWindows" in record:
            payload["executionWindows"] = record["executionWindows"]
        # Advanced options
        payload.update(
            {
                "priority": record.get("priority", 5),
                "maxConcurrentExecutions": record.get("maxConcurrentExecutions", 1),
                "retryOnFailure": record.get("retryOnFailure", False),
                "retryCount": record.get("retryCount", 3),
                "retryInterval": record.get("retryInterval", 5),
            },
        )
        return payload


class BusinessEventsSink(OICBaseSink):
    """Oracle Integration Cloud target sink for business events."""

    name = "business_events"

    def process_record(
        self,
        record: FlextTypes.Core.Dict,
        _context: FlextTypes.Core.Dict,
    ) -> None:
        """Process a business event record.

        Args:
            record: Business event record to process.
            _context: Record context (unused).

        """
        # Business events are typically published, not created
        self._publish_event(record)

    def _publish_event(self, record: FlextTypes.Core.Dict) -> None:
        event_type = str(record.get("eventType", ""))
        payload = {
            "eventType": event_type,
            "eventName": record.get("eventName", ""),
            "eventVersion": record.get("eventVersion", "1.0"),
            "sourceSystem": record.get("sourceSystem", ""),
            "sourceApplication": record.get("sourceApplication", ""),
            "correlationId": record.get("correlationId", ""),
            "businessKey": record.get("businessKey", ""),
            "payload": record.get("payload", {}),
            "headers": record.get("headers", {}),
            "priority": record.get("priority", 5),
            "ttl": record.get("ttl", 3600),
        }
        response = self.client.post(
            "/ic/api/integration/v1/events/publish",
            json=payload,
        )
        response.raise_for_status()


class MonitoringConfigSink(OICBaseSink):
    """Oracle Integration Cloud target sink for monitoring configuration."""

    name = "monitoring_config"

    def process_record(
        self,
        record: FlextTypes.Core.Dict,
        _context: FlextTypes.Core.Dict,
    ) -> None:
        """Process a monitoring configuration record.

        Args:
            record: Monitoring config record to process.
            _context: Record context (unused).

        """
        config_type = record.get("configType", "alerts")
        if config_type == "alerts":
            self._configure_alerts(record)
        elif config_type == "metrics":
            self._configure_metrics(record)
        elif config_type == "tracing":
            self._configure_tracing(record)

    def _configure_alerts(self, record: FlextTypes.Core.Dict) -> None:
        payload = {
            "alertRules": record.get("alertRules", []),
            "recipients": record.get("recipients", []),
            "enabled": record.get("enabled", True),
            "severityThreshold": record.get("severityThreshold", "ERROR"),
        }
        response = self.client.put(
            "/ic/api/integration/v1/monitoring/alerts/config",
            json=payload,
        )
        response.raise_for_status()

    def _configure_metrics(self, record: FlextTypes.Core.Dict) -> None:
        payload = {
            "metricsEnabled": record.get("metricsEnabled", True),
            "retentionPeriod": record.get("retentionPeriod", 30),
            "aggregationInterval": record.get("aggregationInterval", 300),
            "customMetrics": record.get("customMetrics", []),
        }
        response = self.client.put(
            "/ic/api/integration/v1/monitoring/metrics/config",
            json=payload,
        )
        response.raise_for_status()

    def _configure_tracing(self, record: FlextTypes.Core.Dict) -> None:
        payload = {
            "tracingEnabled": record.get("tracingEnabled", True),
            "payloadTracingEnabled": record.get("payloadTracingEnabled", False),
            "traceLevel": record.get("traceLevel", "INFO"),
            "samplingRate": record.get("samplingRate", 1.0),
        }
        response = self.client.put(
            "/ic/api/integration/v1/monitoring/tracing/config",
            json=payload,
        )
        response.raise_for_status()


class IntegrationActionsSink(OICBaseSink):
    """Oracle Integration Cloud target sink for integration actions."""

    name = "integration_actions"

    def process_record(
        self,
        record: FlextTypes.Core.Dict,
        _context: FlextTypes.Core.Dict,
    ) -> None:
        """Process an integration action record.

        Args:
            record: Integration action record to process.
            _context: Record context (unused).

        """
        action = record.get("action", "")
        integration_id = str(record.get("integrationId", ""))
        version = str(record.get("version", "01.00.0000"))
        if not integration_id:
            self.logger.warning("No integration ID provided for action")
            return
        if action == "activate":
            self._activate_integration(integration_id, version, record)
        elif action == "deactivate":
            self._deactivate_integration(integration_id, version)
        elif action == "test":
            self._test_integration(integration_id, version, record)
        elif action == "clone":
            self._clone_integration(integration_id, version, record)

    def _activate_integration(
        self,
        integration_id: str,
        version: str,
        record: FlextTypes.Core.Dict,
    ) -> None:
        payload = {
            "enableTracing": record.get("enableTracing", False),
            "payloadTracingEnabled": record.get("payloadTracingEnabled", False),
        }
        response = self.client.post(
            f"/ic/api/integration/v1/integrations/{integration_id}|{version}/activate",
            json=payload,
        )
        response.raise_for_status()

    def _deactivate_integration(self, integration_id: str, version: str) -> None:
        response = self.client.post(
            f"/ic/api/integration/v1/integrations/{integration_id}|{version}/deactivate",
        )
        response.raise_for_status()

    def _test_integration(
        self,
        integration_id: str,
        version: str,
        record: FlextTypes.Core.Dict,
    ) -> None:
        test_payload = record.get("testPayload", {})
        response = self.client.post(
            f"/ic/api/integration/v1/integrations/{integration_id}|{version}/test",
            json=test_payload,
        )
        response.raise_for_status()

    def _clone_integration(
        self,
        integration_id: str,
        version: str,
        record: FlextTypes.Core.Dict,
    ) -> None:
        payload = {
            "name": record.get("newName", f"{integration_id}_clone"),
            "identifier": record.get("newIdentifier", f"{integration_id}_clone"),
            "version": record.get("newVersion", "01.00.0001"),
            "description": record.get("description", "Cloned integration"),
        }
        response = self.client.post(
            f"/ic/api/integration/v1/integrations/{integration_id}|{version}/clone",
            json=payload,
        )
        response.raise_for_status()


class ConnectionActionsSink(OICBaseSink):
    """Oracle Integration Cloud target sink for connection actions."""

    name = "connection_actions"

    def process_record(
        self,
        record: FlextTypes.Core.Dict,
        _context: FlextTypes.Core.Dict,
    ) -> None:
        """Process a connection action record.

        Args:
            record: Connection action record to process.
            _context: Record context (unused).

        """
        action = record.get("action", "")
        connection_id = str(record.get("connectionId", ""))
        if not connection_id:
            self.logger.warning("No connection ID provided for action")
            return
        if action == "test":
            self._test_connection(connection_id)
        elif action == "refresh_metadata":
            self._refresh_metadata(connection_id)

    def _test_connection(self, connection_id: str) -> None:
        response = self.client.post(
            f"/ic/api/integration/v1/connections/{connection_id}/test",
        )
        response.raise_for_status()
        # Get test results
        result = response.json()
        if result.get("status") != "SUCCESS":
            self.logger.warning(
                "Connection test failed for %s: %s",
                connection_id,
                result.get("message"),
            )

    def _refresh_metadata(self, connection_id: str) -> None:
        response = self.client.post(
            f"/ic/api/integration/v1/connections/{connection_id}/refreshMetadata",
        )
        response.raise_for_status()
