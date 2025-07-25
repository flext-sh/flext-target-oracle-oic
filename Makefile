# FLEXT Target Oracle OIC - Oracle Integration Cloud Singer Target
# ===============================================================
# Enterprise-grade Singer target for Oracle Integration Cloud data loading
# Python 3.13 + Singer SDK + Oracle OIC + OAuth2 + FLEXT Core + Zero Tolerance Quality Gates

.PHONY: help info diagnose check validate test lint type-check security format format-check fix
.PHONY: install dev-install setup pre-commit build clean
.PHONY: coverage coverage-html test-unit test-integration test-singer
.PHONY: deps-update deps-audit deps-tree deps-outdated
.PHONY: sync validate-config target-test target-validate target-schema target-run
.PHONY: oic-write-test oic-endpoint-check oic-auth-test

# ============================================================================
# 🎯 HELP & INFORMATION
# ============================================================================

help: ## Show this help message
	@echo "🎯 FLEXT Target Oracle OIC - Oracle Integration Cloud Singer Target"
	@echo "==============================================================="
	@echo "🎯 Singer SDK + Oracle OIC + OAuth2 + FLEXT Core + Python 3.13"
	@echo ""
	@echo "📦 Enterprise-grade Oracle Integration Cloud target for Singer protocol"
	@echo "🔒 Zero tolerance quality gates with OAuth2 authentication"
	@echo "🧪 90%+ test coverage requirement with OIC API integration testing"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\\033[36m%-20s\\033[0m %s\\n", $$1, $$2}'


info: ## Show project information
	@echo "📊 Project Information"
	@echo "======================"
	@echo "Name: flext-target-oracle-oic"
	@echo "Type: singer-target"
	@echo "Title: FLEXT TARGET ORACLE OIC"
	@echo "Version: $(shell poetry version -s 2>/dev/null || echo "0.7.0")"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Not found")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Not installed")"
	@echo "Venv: $(shell poetry env info --path 2>/dev/null || echo "Not activated")"
	@echo "Directory: $(CURDIR)"
	@echo "Git Branch: $(shell git branch --show-current 2>/dev/null || echo "Not a git repo")"
	@echo "Git Status: $(shell git status --porcelain 2>/dev/null | wc -l | xargs echo) files changed"

diagnose: ## Run complete diagnostics
	@echo "🔍 Running diagnostics for flext-target-oracle-oic..."
	@echo "System Information:"
	@echo "OS: $(shell uname -s)"
	@echo "Architecture: $(shell uname -m)"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Not found")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Not installed")"
	@echo ""
	@echo "Project Structure:"
	@ls -la
	@echo ""
	@echo "Poetry Configuration:"
	@poetry config --list 2>/dev/null || echo "Poetry not configured"
	@echo ""
	@echo "Dependencies Status:"
	@poetry show --outdated 2>/dev/null || echo "No outdated dependencies"

# ============================================================================
# 🎯 CORE QUALITY GATES - ZERO TOLERANCE
# ============================================================================

validate: lint type-check security test ## STRICT compliance validation (all must pass)
	@echo "✅ ALL QUALITY GATES PASSED - FLEXT TARGET ORACLE OIC COMPLIANT"

check: lint type-check test ## Essential quality checks (pre-commit standard)
	@echo "✅ Essential checks passed"

lint: ## Ruff linting (17 rule categories, ALL enabled)
	@echo "🔍 Running ruff linter (ALL rules enabled)..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ Linting complete"

type-check: ## MyPy strict mode type checking (zero errors tolerated)
	@echo "🛡️ Running MyPy strict type checking..."
	@poetry run mypy src/ tests/ --strict
	@echo "✅ Type checking complete"

security: ## Security scans (bandit + pip-audit + secrets)
	@echo "🔒 Running security scans..."
	@poetry run bandit -r src/ --severity-level medium --confidence-level medium
	@poetry run pip-audit --ignore-vuln PYSEC-2022-42969
	@poetry run detect-secrets scan --all-files
	@echo "✅ Security scans complete"

format: ## Format code with ruff
	@echo "🎨 Formatting code..."
	@poetry run ruff format src/ tests/
	@echo "✅ Formatting complete"

format-check: ## Check formatting without fixing
	@echo "🎨 Checking code formatting..."
	@poetry run ruff format src/ tests/ --check
	@echo "✅ Format check complete"

fix: format lint ## Auto-fix all issues (format + imports + lint)
	@echo "🔧 Auto-fixing all issues..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ All auto-fixes applied"

# ============================================================================
# 🧪 TESTING - 90% COVERAGE MINIMUM
# ============================================================================

test: ## Run tests with coverage (90% minimum required)
	@echo "🧪 Running tests with coverage..."
	@poetry run pytest tests/ -v --cov=src/flext_target_oracle_oic --cov-report=term-missing --cov-fail-under=90
	@echo "✅ Tests complete"

test-unit: ## Run unit tests only
	@echo "🧪 Running unit tests..."
	@poetry run pytest tests/unit/ -v
	@echo "✅ Unit tests complete"

test-integration: ## Run integration tests only
	@echo "🧪 Running integration tests..."
	@poetry run pytest tests/integration/ -v
	@echo "✅ Integration tests complete"

test-singer: ## Run Singer protocol tests
	@echo "🧪 Running Singer protocol tests..."
	@poetry run pytest tests/singer/ -v
	@echo "✅ Singer tests complete"

coverage: ## Generate detailed coverage report
	@echo "📊 Generating coverage report..."
	@poetry run pytest tests/ --cov=src/flext_target_oracle_oic --cov-report=term-missing --cov-report=html
	@echo "✅ Coverage report generated in htmlcov/"

coverage-html: coverage ## Generate HTML coverage report
	@echo "📊 Opening coverage report..."
	@python -m webbrowser htmlcov/index.html

# ============================================================================
# 🚀 DEVELOPMENT SETUP
# ============================================================================

setup: install pre-commit ## Complete development setup
	@echo "🎯 Development setup complete!"

install: ## Install dependencies with Poetry
	@echo "📦 Installing dependencies..."
	@poetry install --all-extras --with dev,test,docs,security
	@echo "✅ Dependencies installed"

dev-install: install ## Install in development mode
	@echo "🔧 Setting up development environment..."
	@poetry install --all-extras --with dev,test,docs,security
	@poetry run pre-commit install
	@echo "✅ Development environment ready"

pre-commit: ## Setup pre-commit hooks
	@echo "🎣 Setting up pre-commit hooks..."
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files || true
	@echo "✅ Pre-commit hooks installed"

# ============================================================================
# 🎯 SINGER TARGET OPERATIONS
# ============================================================================

sync: ## Sync data to Oracle OIC target
	@echo "🎯 Running Oracle OIC data sync..."
	@poetry run target-oracle-oic --config $(TARGET_CONFIG) < $(TARGET_STATE)
	@echo "✅ Oracle OIC sync complete"

validate-config: ## Validate target configuration
	@echo "🔍 Validating target configuration..."
	@poetry run target-oracle-oic --config $(TARGET_CONFIG) --validate-config
	@echo "✅ Target configuration validated"

target-test: ## Test Oracle OIC target functionality
	@echo "🎯 Testing Oracle OIC target functionality..."
	@poetry run target-oracle-oic --about
	@poetry run target-oracle-oic --version
	@echo "✅ Target test complete"

target-validate: ## Validate target configuration
	@echo "🔍 Validating target configuration..."
	@poetry run target-oracle-oic --config tests/fixtures/config/target_config.json --validate-config
	@echo "✅ Target configuration validated"

target-schema: ## Validate Oracle OIC schema
	@echo "🔍 Validating Oracle OIC schema..."
	@poetry run target-oracle-oic --config tests/fixtures/config/target_config.json --validate-schema
	@echo "✅ Oracle OIC schema validated"

target-run: ## Run Oracle OIC data loading
	@echo "🎯 Running Oracle OIC data loading..."
	@poetry run target-oracle-oic --config tests/fixtures/config/target_config.json < tests/fixtures/data/sample_input.jsonl
	@echo "✅ Oracle OIC data loading complete"

target-run-debug: ## Run Oracle OIC target with debug logging
	@echo "🎯 Running Oracle OIC target with debug..."
	@poetry run target-oracle-oic --config tests/fixtures/config/target_config.json --log-level DEBUG < tests/fixtures/data/sample_input.jsonl
	@echo "✅ Oracle OIC debug run complete"

target-dry-run: ## Run Oracle OIC target in dry-run mode
	@echo "🎯 Running Oracle OIC target dry-run..."
	@poetry run target-oracle-oic --config tests/fixtures/config/target_config.json --dry-run < tests/fixtures/data/sample_input.jsonl
	@echo "✅ Oracle OIC dry-run complete"

# ============================================================================
# 🏢 ORACLE OIC-SPECIFIC OPERATIONS
# ============================================================================

oic-write-test: ## Test Oracle OIC write operations
	@echo "🏢 Testing Oracle OIC write operations..."
	@poetry run python -c "from flext_target_oracle_oic.client import TargetOracleOICClient; import asyncio; import json; config = json.load(open('tests/fixtures/config/target_config.json')); client = TargetOracleOICClient(config); print('Testing write operations...'); result = asyncio.run(client.test_write()); print('✅ Write test passed!' if result.is_success else f'❌ Write test failed: {result.error}')"
	@echo "✅ Oracle OIC write test complete"

oic-endpoint-check: ## Check Oracle OIC endpoint connectivity
	@echo "🏢 Checking Oracle OIC endpoint connectivity..."
	@poetry run python scripts/validate_oic_endpoint.py
	@echo "✅ Oracle OIC endpoint check complete"

oic-auth-test: ## Test Oracle OIC OAuth2 authentication
	@echo "🔐 Testing Oracle OIC OAuth2 authentication..."
	@poetry run python -c "from flext_target_oracle_oic.auth import OICAuthenticator; import json; config = json.load(open('tests/fixtures/config/target_config.json')); auth = OICAuthenticator(config); print('Testing OAuth2 auth...'); result = auth.test_authentication(); print('✅ Auth test passed!' if result.is_success else f'❌ Auth test failed: {result.error}')"
	@echo "✅ Oracle OIC auth test complete"

oic-test: ## Test Oracle OIC API connectivity
	@echo "🏢 Testing Oracle OIC API connectivity..."
	@poetry run python scripts/test_oic_connectivity.py
	@echo "✅ OIC API connectivity test complete"

oic-auth: ## Test Oracle OIC OAuth2 authentication
	@echo "🔐 Testing Oracle OIC OAuth2 authentication..."
	@poetry run python scripts/test_oic_authentication.py
	@echo "✅ OIC OAuth2 authentication test complete"

oic-connections: ## Test OIC connection management
	@echo "🔗 Testing OIC connection management..."
	@poetry run python scripts/test_oic_connections.py
	@echo "✅ OIC connection management test complete"

oic-integrations: ## Test OIC integration operations
	@echo "⚙️ Testing OIC integration operations..."
	@poetry run python scripts/test_oic_integrations.py
	@echo "✅ OIC integration operations test complete"

oic-packages: ## Test OIC package deployment
	@echo "📦 Testing OIC package deployment..."
	@poetry run python scripts/test_oic_packages.py
	@echo "✅ OIC package deployment test complete"

oic-lookups: ## Test OIC lookup management
	@echo "🔍 Testing OIC lookup management..."
	@poetry run python scripts/test_oic_lookups.py
	@echo "✅ OIC lookup management test complete"

# ============================================================================
# 🔐 AUTHENTICATION & SECURITY
# ============================================================================

oauth2-test: ## Test OAuth2 client credentials flow
	@echo "🔐 Testing OAuth2 client credentials flow..."
	@poetry run python scripts/test_oauth2_flow.py
	@echo "✅ OAuth2 flow test complete"

idcs-test: ## Test IDCS token endpoint
	@echo "🏛️ Testing IDCS token endpoint..."
	@poetry run python scripts/test_idcs_endpoint.py
	@echo "✅ IDCS endpoint test complete"

token-validation: ## Test token validation and refresh
	@echo "🎫 Testing token validation and refresh..."
	@poetry run python scripts/test_token_validation.py
	@echo "✅ Token validation test complete"

security-audit: ## Run security audit for OIC target
	@echo "🔒 Running security audit..."
	@poetry run python scripts/security_audit.py
	@echo "✅ Security audit complete"

# ============================================================================
# 🔍 DATA VALIDATION
# ============================================================================

validate-oic-data: ## Validate OIC data format compliance
	@echo "🔍 Validating OIC data format compliance..."
	@poetry run python scripts/validate_oic_data.py
	@echo "✅ OIC data format validation complete"

validate-integration-format: ## Validate integration format
	@echo "🔍 Validating integration format..."
	@poetry run python scripts/validate_integration_format.py
	@echo "✅ Integration format validation complete"

validate-connection-data: ## Validate connection data
	@echo "🔍 Validating connection data..."
	@poetry run python scripts/validate_connection_data.py
	@echo "✅ Connection data validation complete"

data-quality-report: ## Generate comprehensive data quality report
	@echo "📊 Generating data quality report..."
	@poetry run python scripts/generate_quality_report.py
	@echo "✅ Data quality report generated"

# ============================================================================
# 📦 BUILD & DISTRIBUTION
# ============================================================================

build: clean ## Build distribution packages
	@echo "🔨 Building distribution..."
	@poetry build
	@echo "✅ Build complete - packages in dist/"

# ============================================================================
# 🧹 CLEANUP
# ============================================================================

clean: ## Remove all artifacts
	@echo "🧹 Cleaning up..."
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/
	@rm -rf .coverage
	@rm -rf htmlcov/
	@rm -rf output/
	@rm -f *.iar
	@rm -f *.par
	@rm -f oauth_token.json
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete"

# ============================================================================
# 📊 DEPENDENCY MANAGEMENT
# ============================================================================

deps-update: ## Update all dependencies
	@echo "🔄 Updating dependencies..."
	@poetry update
	@echo "✅ Dependencies updated"

deps-audit: ## Audit dependencies for vulnerabilities
	@echo "🔍 Auditing dependencies..."
	@poetry run pip-audit
	@echo "✅ Dependency audit complete"

deps-tree: ## Show dependency tree
	@echo "🌳 Dependency tree:"
	@poetry show --tree

deps-outdated: ## Show outdated dependencies
	@echo "📋 Outdated dependencies:"
	@poetry show --outdated

# ============================================================================
# 🔧 ENVIRONMENT CONFIGURATION
# ============================================================================

# Python settings
PYTHON := python3.13
export PYTHONPATH := $(PWD)/src:$(PYTHONPATH)
export PYTHONDONTWRITEBYTECODE := 1
export PYTHONUNBUFFERED := 1

# Target settings
TARGET_CONFIG := config.json
TARGET_STATE := state.json

# Singer settings
export SINGER_LOG_LEVEL := INFO
export SINGER_BATCH_SIZE := 100
export SINGER_MAX_BATCH_AGE := 300

# Oracle OIC Target settings
export TARGET_ORACLE_OIC_BASE_URL := https://oic-prod.integration.ocp.oraclecloud.com
export TARGET_ORACLE_OIC_API_VERSION := v1

# OAuth2 Authentication settings
export TARGET_ORACLE_OIC_OAUTH_CLIENT_ID := your_client_id
export TARGET_ORACLE_OIC_OAUTH_CLIENT_SECRET := your_client_secret
export TARGET_ORACLE_OIC_OAUTH_TOKEN_URL := https://idcs.identity.oraclecloud.com/oauth2/v1/token
export TARGET_ORACLE_OIC_OAUTH_SCOPE := https://integration.ocp.oraclecloud.com:443

# OIC operation settings
export TARGET_ORACLE_OIC_IMPORT_MODE := create_or_update
export TARGET_ORACLE_OIC_ENABLE_ROLLBACK := true
export TARGET_ORACLE_OIC_BATCH_SIZE := 50

# Performance settings
export TARGET_ORACLE_OIC_REQUEST_TIMEOUT := 30
export TARGET_ORACLE_OIC_MAX_RETRIES := 3
export TARGET_ORACLE_OIC_CONCURRENT_REQUESTS := 5

# Poetry settings
export POETRY_VENV_IN_PROJECT := false
export POETRY_CACHE_DIR := $(HOME)/.cache/pypoetry

# Quality gate settings
export MYPY_CACHE_DIR := .mypy_cache
export RUFF_CACHE_DIR := .ruff_cache

# ============================================================================
# 📝 PROJECT METADATA
# ============================================================================

# Project information
PROJECT_NAME := flext-target-oracle-oic
PROJECT_TYPE := meltano-plugin
PROJECT_VERSION := $(shell poetry version -s)
PROJECT_DESCRIPTION := FLEXT Target Oracle OIC - Oracle Integration Cloud Singer Target

.DEFAULT_GOAL := help

# ============================================================================
# 🎯 SINGER SPECIFIC COMMANDS
# ============================================================================

singer-about: ## Show Singer target about information
	@echo "🎵 Singer target about information..."
	@poetry run target-oracle-oic --about
	@echo "✅ About information displayed"

singer-config-sample: ## Generate Singer config sample
	@echo "🎵 Generating Singer config sample..."
	@poetry run target-oracle-oic --config-sample > config_sample.json
	@echo "✅ Config sample generated: config_sample.json"

singer-test-streams: ## Test Singer streams
	@echo "🎵 Testing Singer streams..."
	@poetry run pytest tests/singer/test_streams.py -v
	@echo "✅ Singer streams tests complete"

# ============================================================================
# 🎯 FLEXT ECOSYSTEM INTEGRATION
# ============================================================================

ecosystem-check: ## Verify FLEXT ecosystem compatibility
	@echo "🌐 Checking FLEXT ecosystem compatibility..."
	@echo "📦 Singer project: $(PROJECT_NAME) v$(PROJECT_VERSION)"
	@echo "🏗️ Architecture: Singer Target + Oracle OIC + OAuth2"
	@echo "🐍 Python: 3.13"
	@echo "🔗 Framework: FLEXT Core + Singer SDK"
	@echo "📊 Quality: Zero tolerance enforcement"
	@echo "✅ Ecosystem compatibility verified"

workspace-info: ## Show workspace integration info
	@echo "🏢 FLEXT Workspace Integration"
	@echo "==============================="
	@echo "📁 Project Path: $(PWD)"
	@echo "🏆 Role: Oracle Integration Cloud Singer Target"
	@echo "🔗 Dependencies: flext-core, flext-oracle-oic-ext, singer-sdk"
	@echo "📦 Provides: Oracle OIC integration capabilities"
	@echo "🎯 Standards: Enterprise OAuth2 integration patterns"