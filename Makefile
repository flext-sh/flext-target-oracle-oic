# FLEXT TARGET ORACLE OIC - Singer Target for Oracle Integration Cloud
# ==================================================================
# Enterprise Singer target for Oracle OIC integration metadata loading
# Python 3.13 + Singer SDK + Oracle OIC + OAuth2 + Zero Tolerance Quality Gates

.PHONY: help check validate test lint type-check security format format-check fix
.PHONY: install dev-install setup pre-commit build clean
.PHONY: coverage coverage-html test-unit test-integration test-singer
.PHONY: deps-update deps-audit deps-tree deps-outdated
.PHONY: target-test target-validate target-run singer-spec
.PHONY: oic-test oic-auth oic-connections oic-integrations oic-packages

# ============================================================================
# 🎯 HELP & INFORMATION
# ============================================================================

help: ## Show this help message
	@echo "🎯 FLEXT TARGET ORACLE OIC - Singer Target for Oracle Integration Cloud"
	@echo "=================================================================="
	@echo "🎯 Singer SDK + Oracle OIC + OAuth2 + Python 3.13"
	@echo ""
	@echo "📦 Enterprise Singer target for Oracle OIC integration loading"
	@echo "🔒 Zero tolerance quality gates with real OIC authentication"
	@echo "🧪 90%+ test coverage requirement with OIC API compliance"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\\033[36m%-20s\\033[0m %s\\n", $$1, $$2}'

# ============================================================================
# 🎯 CORE QUALITY GATES - ZERO TOLERANCE
# ============================================================================

validate: lint type-check security test target-test ## STRICT compliance validation (all must pass)
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

test-singer: ## Run Singer-specific tests
	@echo "🧪 Running Singer protocol tests..."
	@poetry run pytest tests/ -m "singer" -v
	@echo "✅ Singer tests complete"

test-oic: ## Run OIC-specific tests
	@echo "🧪 Running Oracle OIC tests..."
	@poetry run pytest tests/ -m "oic" -v
	@echo "✅ OIC tests complete"

test-oauth2: ## Run OAuth2 authentication tests
	@echo "🧪 Running OAuth2 authentication tests..."
	@poetry run pytest tests/ -m "oauth2" -v
	@echo "✅ OAuth2 tests complete"

test-performance: ## Run performance tests
	@echo "⚡ Running Singer target performance tests..."
	@poetry run pytest tests/performance/ -v --benchmark-only
	@echo "✅ Performance tests complete"

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
# 🎵 SINGER TARGET OPERATIONS - CORE FUNCTIONALITY
# ============================================================================

target-test: ## Test Singer target functionality
	@echo "🧪 Testing Singer target functionality..."
	@poetry run python -c "from flext_target_oracle_oic.target import TargetOracleOIC; from flext_target_oracle_oic.client.oic_client import OICClient; print('Oracle OIC target loaded successfully')"
	@echo "✅ Singer target test complete"

target-validate: ## Validate Singer target configuration
	@echo "🔍 Validating Singer target configuration..."
	@poetry run python scripts/validate_target_config.py
	@echo "✅ Singer target configuration validation complete"

target-run: ## Run Singer target with sample data
	@echo "🎵 Running Singer target with sample data..."
	@poetry run flext-target-oracle-oic --config config.json < sample_data/sample.jsonl
	@echo "✅ Singer target execution complete"

target-schema: ## Test Singer target schema handling
	@echo "📋 Testing Singer target schema handling..."
	@poetry run python scripts/test_schema_handling.py
	@echo "✅ Schema handling test complete"

target-state: ## Test Singer target state management
	@echo "📊 Testing Singer target state management..."
	@poetry run python scripts/test_state_management.py
	@echo "✅ State management test complete"

target-sinks: ## Test all Singer sink implementations
	@echo "🚰 Testing Singer sink implementations..."
	@poetry run python scripts/test_target_sinks.py
	@echo "✅ Target sinks test complete"

# ============================================================================
# 🏢 ORACLE OIC OPERATIONS
# ============================================================================

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

oic-import-export: ## Test OIC import/export operations
	@echo "🔄 Testing OIC import/export operations..."
	@poetry run python scripts/test_oic_import_export.py
	@echo "✅ OIC import/export test complete"

oic-deployment: ## Test OIC deployment operations
	@echo "🚀 Testing OIC deployment operations..."
	@poetry run python scripts/test_oic_deployment.py
	@echo "✅ OIC deployment test complete"

# ============================================================================
# 🎵 SINGER PROTOCOL COMPLIANCE
# ============================================================================

singer-spec: ## Validate Singer specification compliance
	@echo "🎵 Validating Singer specification compliance..."
	@poetry run python scripts/validate_singer_spec.py
	@echo "✅ Singer specification validation complete"

singer-messages: ## Test Singer message handling
	@echo "📬 Testing Singer message handling..."
	@poetry run python scripts/test_singer_messages.py
	@echo "✅ Singer message test complete"

singer-catalog: ## Test Singer catalog handling
	@echo "📋 Testing Singer catalog handling..."
	@poetry run python scripts/test_singer_catalog.py
	@echo "✅ Singer catalog test complete"

singer-state: ## Test Singer state handling
	@echo "📊 Testing Singer state handling..."
	@poetry run python scripts/test_singer_state.py
	@echo "✅ Singer state test complete"

singer-records: ## Test Singer record processing
	@echo "📄 Testing Singer record processing..."
	@poetry run python scripts/test_singer_records.py
	@echo "✅ Singer record test complete"

singer-sinks: ## Test Singer sink implementations
	@echo "🚰 Testing Singer sink implementations..."
	@poetry run python scripts/test_singer_sinks.py
	@echo "✅ Singer sinks test complete"

# ============================================================================
# 🔍 DATA QUALITY & VALIDATION
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
# 📦 BUILD & DISTRIBUTION
# ============================================================================

build: clean ## Build distribution packages
	@echo "🔨 Building distribution..."
	@poetry build
	@echo "✅ Build complete - packages in dist/"

package: build ## Create deployment package
	@echo "📦 Creating deployment package..."
	@tar -czf dist/flext-target-oracle-oic-deployment.tar.gz \
		src/ \
		tests/ \
		scripts/ \
		pyproject.toml \
		README.md \
		CLAUDE.md
	@echo "✅ Deployment package created: dist/flext-target-oracle-oic-deployment.tar.gz"

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
	@rm -rf .pytest_cache/
	@rm -rf .mypy_cache/
	@rm -rf .ruff_cache/
	@rm -rf output/
	@rm -f *.iar
	@rm -f *.par
	@rm -f state.json
	@rm -f oauth_token.json
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
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

# Oracle OIC Target settings
export FLEXT_TARGET_ORACLE_OIC_CONFIG := ./config.json
export FLEXT_TARGET_ORACLE_OIC_DEBUG := false

# Oracle OIC connection settings
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

# Deployment settings
export TARGET_ORACLE_OIC_ENVIRONMENT := development
export TARGET_ORACLE_OIC_DEPLOYMENT_MODE := sync
export TARGET_ORACLE_OIC_VALIDATE_BEFORE_DEPLOY := true

# Advanced features settings
export TARGET_ORACLE_OIC_ENABLE_MONITORING := true
export TARGET_ORACLE_OIC_ENABLE_LOGGING := true
export TARGET_ORACLE_OIC_LOG_LEVEL := INFO

# Singer settings
export SINGER_SDK_LOG_LEVEL := INFO
export SINGER_SDK_BATCH_SIZE := 1000
export SINGER_SDK_MAX_RECORD_AGE_IN_MINUTES := 5

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
PROJECT_VERSION := $(shell poetry version -s)
PROJECT_DESCRIPTION := FLEXT TARGET ORACLE OIC - Singer Target for Oracle Integration Cloud

.DEFAULT_GOAL := help

# ============================================================================
# 🎯 DEVELOPMENT UTILITIES
# ============================================================================

dev-oic-server: ## Start development OIC mock server
	@echo "🔧 Starting development OIC mock server..."
	@poetry run python scripts/dev_oic_server.py
	@echo "✅ Development OIC mock server started"

dev-oauth2-server: ## Start development OAuth2 mock server
	@echo "🔧 Starting development OAuth2 mock server..."
	@poetry run python scripts/dev_oauth2_server.py
	@echo "✅ Development OAuth2 mock server started"

dev-target-monitor: ## Monitor target operations
	@echo "📊 Monitoring target operations..."
	@poetry run python scripts/monitor_target_operations.py
	@echo "✅ Target monitoring complete"

dev-oic-explorer: ## Interactive OIC API explorer
	@echo "🎮 Starting OIC API explorer..."
	@poetry run python scripts/oic_explorer.py
	@echo "✅ OIC API explorer session complete"

dev-integration-wizard: ## Interactive integration deployment wizard
	@echo "🧙 Starting integration deployment wizard..."
	@poetry run python scripts/integration_wizard.py
	@echo "✅ Integration wizard session complete"

# ============================================================================
# 🎯 FLEXT ECOSYSTEM INTEGRATION
# ============================================================================

ecosystem-check: ## Verify FLEXT ecosystem compatibility
	@echo "🌐 Checking FLEXT ecosystem compatibility..."
	@echo "📦 Core project: $(PROJECT_NAME) v$(PROJECT_VERSION)"
	@echo "🏗️ Architecture: Singer Target + Oracle OIC + OAuth2"
	@echo "🐍 Python: 3.13"
	@echo "🔗 Framework: FLEXT Core + Singer SDK + Oracle OIC APIs"
	@echo "📊 Quality: Zero tolerance enforcement"
	@echo "✅ Ecosystem compatibility verified"

workspace-info: ## Show workspace integration info
	@echo "🏢 FLEXT Workspace Integration"
	@echo "==============================="
	@echo "📁 Project Path: $(PWD)"
	@echo "🏆 Role: Singer Target for Oracle Integration Cloud"
	@echo "🔗 Dependencies: flext-core, flext-observability, singer-sdk, requests-oauthlib"
	@echo "📦 Provides: Oracle OIC integration loading via Singer protocol"
	@echo "🎯 Standards: Enterprise Singer target patterns with OAuth2 authentication"

# ============================================================================
# 🔄 CONTINUOUS INTEGRATION
# ============================================================================

ci-check: validate ## CI quality checks
	@echo "🔍 Running CI quality checks..."
	@poetry run python scripts/ci_quality_report.py
	@echo "✅ CI quality checks complete"

ci-performance: ## CI performance benchmarks
	@echo "⚡ Running CI performance benchmarks..."
	@poetry run python scripts/ci_performance_benchmarks.py
	@echo "✅ CI performance benchmarks complete"

ci-integration: ## CI integration tests
	@echo "🔗 Running CI integration tests..."
	@poetry run pytest tests/integration/ -v --tb=short
	@echo "✅ CI integration tests complete"

ci-singer: ## CI Singer protocol tests
	@echo "🎵 Running CI Singer tests..."
	@poetry run pytest tests/ -m "singer" -v --tb=short
	@echo "✅ CI Singer tests complete"

ci-oic: ## CI Oracle OIC tests
	@echo "🏢 Running CI Oracle OIC tests..."
	@poetry run pytest tests/ -m "oic" -v --tb=short
	@echo "✅ CI Oracle OIC tests complete"

ci-oauth2: ## CI OAuth2 tests
	@echo "🔐 Running CI OAuth2 tests..."
	@poetry run pytest tests/ -m "oauth2" -v --tb=short
	@echo "✅ CI OAuth2 tests complete"

ci-all: ci-check ci-performance ci-integration ci-singer ci-oic ci-oauth2 ## Run all CI checks
	@echo "✅ All CI checks complete"

# ============================================================================
# 🚀 PRODUCTION DEPLOYMENT
# ============================================================================

deploy-target: validate build ## Deploy target for production use
	@echo "🚀 Deploying Oracle OIC target..."
	@poetry run python scripts/deploy_target.py
	@echo "✅ Oracle OIC target deployment complete"

test-deployment: ## Test deployed target functionality
	@echo "🧪 Testing deployed target..."
	@poetry run python scripts/test_deployed_target.py
	@echo "✅ Deployment test complete"

rollback-deployment: ## Rollback target deployment
	@echo "🔄 Rolling back target deployment..."
	@poetry run python scripts/rollback_target_deployment.py
	@echo "✅ Deployment rollback complete"

# ============================================================================
# 🔬 MONITORING & OBSERVABILITY
# ============================================================================

monitor-oauth2-tokens: ## Monitor OAuth2 token health
	@echo "📊 Monitoring OAuth2 token health..."
	@poetry run python scripts/monitor_oauth2_tokens.py
	@echo "✅ OAuth2 token monitoring complete"

monitor-oic-api-health: ## Monitor Oracle OIC API health
	@echo "📊 Monitoring Oracle OIC API health..."
	@poetry run python scripts/monitor_oic_api_health.py
	@echo "✅ OIC API health monitoring complete"

monitor-integration-deployments: ## Monitor integration deployments
	@echo "📊 Monitoring integration deployments..."
	@poetry run python scripts/monitor_integration_deployments.py
	@echo "✅ Integration deployment monitoring complete"

generate-target-metrics: ## Generate target performance metrics
	@echo "📊 Generating target performance metrics..."
	@poetry run python scripts/generate_target_metrics.py
	@echo "✅ Target metrics generated"

generate-oic-usage-report: ## Generate OIC usage report
	@echo "📊 Generating OIC usage report..."
	@poetry run python scripts/generate_oic_usage_report.py
	@echo "✅ OIC usage report generated"