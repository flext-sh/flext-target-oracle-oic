"""Oracle OIC DI Container using flext-core patterns."""

from __future__ import annotations

from typing import Any

# Import from flext-core for foundational patterns
from flext_core import FlextContainer, FlextResult, get_logger

logger = get_logger(__name__)


class OICDIContainer:
    """Dependency Injection container for Oracle OIC target using flext-core."""

    def __init__(self) -> None:
        """Initialize OIC DI container."""
        self._container = FlextContainer()
        self._setup_dependencies()

    def _setup_dependencies(self) -> None:
        """Setup OIC-specific dependencies."""
        try:
            # Register core dependencies
            self._register_connection_components()
            self._register_pattern_components()
            self._register_singer_components()
            self._register_application_components()

            logger.info("OIC DI container dependencies setup completed")

        except Exception:
            logger.exception("OIC DI container setup failed")
            raise

    def _register_connection_components(self) -> None:
        """Register connection-related components."""
        # Import components locally to avoid circular dependencies
        from flext_target_oracle_oic.connection import (
            OICConnection,
            OICConnectionConfig,
        )

        register_result = self._container.register(
            "oic_connection_config", OICConnectionConfig,
        )
        if not register_result.is_success:
            logger.warning(
                f"Failed to register OICConnectionConfig: {register_result.error}",
            )

        register_result = self._container.register("oic_connection", OICConnection)
        if not register_result.is_success:
            logger.warning(f"Failed to register OICConnection: {register_result.error}")

    def _register_pattern_components(self) -> None:
        """Register pattern-related components."""
        from flext_target_oracle_oic.patterns import (
            OICDataTransformer,
            OICEntryManager,
            OICSchemaMapper,
            OICTypeConverter,
        )

        components = [
            ("oic_type_converter", OICTypeConverter),
            ("oic_data_transformer", OICDataTransformer),
            ("oic_schema_mapper", OICSchemaMapper),
            ("oic_entry_manager", OICEntryManager),
        ]

        for name, component_class in components:
            register_result = self._container.register(name, component_class)
            if not register_result.is_success:
                logger.warning(f"Failed to register {name}: {register_result.error}")

    def _register_singer_components(self) -> None:
        """Register Singer SDK-related components."""
        from flext_target_oracle_oic.singer import OICRecordProcessor

        register_result = self._container.register(
            "oic_record_processor", OICRecordProcessor,
        )
        if not register_result.is_success:
            logger.warning(
                f"Failed to register OICRecordProcessor: {register_result.error}",
            )

    def _register_application_components(self) -> None:
        """Register application-level components."""
        from flext_target_oracle_oic.application import OICTargetOrchestrator

        register_result = self._container.register(
            "oic_target_orchestrator", OICTargetOrchestrator,
        )
        if not register_result.is_success:
            logger.warning(
                f"Failed to register OICTargetOrchestrator: {register_result.error}",
            )

    def get_component(self, name: str) -> FlextResult[Any]:
        """Get component from container.

        Args:
            name: Component name to retrieve

        Returns:
            FlextResult containing component instance or error

        """
        try:
            return self._container.get(name)
        except Exception as e:
            logger.exception(f"Failed to get component: {name}")
            return FlextResult.fail(f"Component retrieval failed: {e}")

    def register_component(self, name: str, component: Any) -> FlextResult[None]:
        """Register component in container.

        Args:
            name: Component name
            component: Component instance or class

        Returns:
            FlextResult indicating success or error

        """
        try:
            return self._container.register(name, component)
        except Exception as e:
            logger.exception(f"Failed to register component: {name}")
            return FlextResult.fail(f"Component registration failed: {e}")

    def is_registered(self, name: str) -> bool:
        """Check if component is registered.

        Args:
            name: Component name to check

        Returns:
            True if component is registered, False otherwise

        """
        return self._container.is_registered(name)

    def get_all_registered(self) -> list[str]:
        """Get list of all registered component names.

        Returns:
            List of registered component names

        """
        return self._container.get_all_registered()

    @property
    def container(self) -> FlextContainer:
        """Get the underlying FlextContainer instance."""
        return self._container


# Global container instance
_oic_container: OICDIContainer | None = None


def get_oic_container() -> OICDIContainer:
    """Get global OIC DI container instance.

    Returns:
        Global OICDIContainer instance

    """
    global _oic_container
    if _oic_container is None:
        _oic_container = OICDIContainer()
    return _oic_container


def configure_oic_container(
    config: dict[str, Any] | None = None,
) -> FlextResult[OICDIContainer]:
    """Configure global OIC DI container.

    Args:
        config: Optional configuration for container setup

    Returns:
        FlextResult containing configured container or error

    """
    try:
        global _oic_container
        _oic_container = OICDIContainer()

        if config:
            # Apply any configuration-specific setup
            logger.info("OIC DI container configured with custom settings")

        return FlextResult.ok(_oic_container)

    except Exception as e:
        logger.exception("OIC DI container configuration failed")
        return FlextResult.fail(f"Container configuration failed: {e}")
