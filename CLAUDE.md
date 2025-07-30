# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `flext-target-oracle-oic`, a Singer target implementation for Oracle Integration Cloud (OIC) that is part of the FLEXT enterprise data integration ecosystem. The project provides OAuth2-authenticated data loading capabilities for OIC integration artifacts including connections, integrations, packages, and lookups.

## Architecture

### Core Components

The project follows Clean Architecture principles with flext-core patterns:

- **Target Implementation** (`target.py`): Main Singer SDK target class with stream routing
- **Sinks** (`sinks.py`): Stream-specific data processors (ConnectionsSink, IntegrationsSink, PackagesSink, LookupsSink)
- **Orchestrator** (`application/orchestrator.py`): Business logic orchestration using flext-core patterns
- **Authentication** (`auth.py`): OAuth2 authentication with OIC/IDCS integration
- **Client** (`client.py`): HTTP client for OIC API operations
- **Exceptions** (`exceptions.py`): Comprehensive exception hierarchy using flext-core error patterns

### FLEXT Core Integration

The project heavily uses flext-core patterns:
- `FlextResult<T>` for railway-oriented programming and error handling
- `FlextValueObject` for configuration objects
- `FlextError` hierarchy for structured exception handling
- Dependency injection via `OICDIContainer`
- Structured logging with correlation IDs

### Singer SDK Architecture

Stream processing is handled through specialized sinks:
- `ConnectionsSink`: Manages OIC connection definitions
- `IntegrationsSink`: Handles integration artifacts and activation
- `PackagesSink`: Processes integration packages (IAR files)
- `LookupsSink`: Manages value mapping lookups

## Development Commands

### Essential Quality Gates (Zero Tolerance)
```bash
make check                    # Essential checks (lint + type + test)
make validate                 # Full compliance validation (lint + type + security + test)
make lint                     # Ruff linting (ALL rules enabled)
make type-check               # MyPy strict mode type checking
make security                 # Security scans (bandit + pip-audit + secrets)
make test                     # Run tests with 90% coverage requirement
```

### Development Setup
```bash
make setup                    # Complete dev setup (install + pre-commit)
make install                  # Install dependencies with Poetry
make dev-install              # Development mode setup with pre-commit hooks
make pre-commit               # Setup and run pre-commit hooks
```

### Testing Commands
```bash
make test                     # Full test suite with 90% coverage
make test-unit                # Unit tests only
make test-integration         # Integration tests only  
make test-singer              # Singer protocol tests
make coverage                 # Generate detailed coverage report
pytest -m unit               # Run unit tests via pytest
pytest -m integration        # Run integration tests via pytest
pytest -m e2e                # Run end-to-end tests via pytest
```

### Singer Target Operations
```bash
make target-test              # Test target functionality (--about, --version)
make target-validate          # Validate target configuration
make target-schema            # Validate OIC schema
make target-run               # Run OIC data loading with test fixtures
make target-run-debug         # Run with debug logging
make target-dry-run           # Dry-run mode testing
make sync                     # Sync data to OIC (requires TARGET_CONFIG, TARGET_STATE)
```

### Oracle OIC Specific Operations
```bash
make oic-write-test           # Test OIC write operations
make oic-endpoint-check       # Test OIC endpoint connectivity
make oic-auth-test            # Test OAuth2 authentication flow
make oauth2-test              # Test OAuth2 client credentials flow
make idcs-test                # Test IDCS token endpoint
make token-validation         # Test token validation and refresh
```

### Build and Maintenance
```bash
make build                    # Build distribution packages
make format                   # Auto-format code with ruff
make fix                      # Auto-fix all formatting and linting issues
make clean                    # Remove build artifacts and caches
make deps-update              # Update dependencies
make deps-audit               # Security audit of dependencies
```

## Configuration

### Target Configuration Schema
The target accepts the following configuration:
- `base_url` (required): OIC instance base URL
- `oauth_client_id` (required): OAuth2 client ID  
- `oauth_client_secret` (required): OAuth2 client secret
- `oauth_token_url` (required): OAuth2 token endpoint URL
- `oauth_client_aud` (optional): OAuth2 client audience
- `import_mode` (default: "create_or_update"): Integration import behavior
- `activate_integrations` (default: false): Auto-activate integrations after import

### Environment Variables
Key environment variables for development:
- `TARGET_ORACLE_OIC_BASE_URL`: OIC instance URL
- `TARGET_ORACLE_OIC_OAUTH_CLIENT_ID`: OAuth2 client credentials
- `TARGET_ORACLE_OIC_OAUTH_CLIENT_SECRET`: OAuth2 client secret
- `TARGET_ORACLE_OIC_OAUTH_TOKEN_URL`: IDCS token endpoint
- `SINGER_LOG_LEVEL`: Logging level (INFO, DEBUG)
- `SINGER_BATCH_SIZE`: Record batch size (default: 100)

## Code Standards

### Quality Requirements
- **90% minimum test coverage** (enforced by pytest)
- **Zero MyPy errors** in strict mode
- **All Ruff rules enabled** with comprehensive linting
- **Security scanning** with bandit and pip-audit
- **Pre-commit hooks** for automated quality gates

### Architecture Patterns
- Use `FlextResult<T>` for all operations that can fail
- Implement proper exception hierarchy extending flext-core errors
- Follow dependency injection patterns via `OICDIContainer`
- Use structured logging with contextual information
- Implement async/await patterns for I/O operations

### Testing Strategy
- Unit tests in `tests/unit/` directory
- Integration tests in `tests/integration/` directory
- E2E tests in `tests/e2e/` directory
- Singer protocol compliance tests
- Mock external dependencies (OIC API, OAuth2 endpoints)
- Test fixtures in `tests/fixtures/` for consistent test data

## Common Development Tasks

### Running the Target
```bash
# Direct execution with configuration
poetry run target-oracle-oic --config config.json < input.jsonl

# Using test fixtures
poetry run target-oracle-oic --config tests/fixtures/config/target_config.json < tests/fixtures/data/sample_input.jsonl

# Debug mode
poetry run target-oracle-oic --config config.json --log-level DEBUG < input.jsonl
```

### Development Testing
```bash
# Test specific functionality
python -c "from flext_target_oracle_oic.client import OICClient; print('Client import successful')"

# Test authentication
python -c "from flext_target_oracle_oic.auth import OICOAuth2Authenticator; print('Auth import successful')"

# Test configuration validation
poetry run target-oracle-oic --config config.json --validate-config
```

### Debugging Issues
- Check `make diagnose` for system information and project status
- Use `make target-run-debug` for verbose logging during data loading
- Examine test fixtures in `tests/fixtures/` for example configurations
- Review exception hierarchy in `exceptions.py` for specific error types
- Use `poetry run pytest --pdb` to debug test failures

## Dependencies

### Core Dependencies
- `flext-core`: Foundation patterns and utilities
- `flext-meltano`: Singer SDK integration
- `flext-oracle-oic-ext`: OIC-specific extensions
- `flext-observability`: Monitoring and logging
- `singer-sdk`: Singer protocol implementation
- `pydantic`: Configuration validation and parsing
- `requests`/`httpx`: HTTP client operations

### Development Dependencies
- `pytest`: Testing framework with async support
- `ruff`: Linting and formatting (ALL rules enabled)
- `mypy`: Static type checking in strict mode
- `bandit`: Security vulnerability scanning
- `pre-commit`: Automated quality gate enforcement

## Integration with FLEXT Ecosystem

This target is designed to work within the broader FLEXT data integration platform:
- Follows flext-core architectural patterns and error handling
- Integrates with flext-observability for monitoring
- Uses flext-meltano for Singer SDK orchestration
- Designed for deployment in FLEXT enterprise environments
- Compatible with FLEXT's OAuth2 authentication patterns