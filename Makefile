# FLEXT-TARGET-ORACLE-OIC Makefile
# Migrated to use base.mk - 2026-01-03

PROJECT_NAME := flext-target-oracle-oic
MIN_COVERAGE := 100

# Include shared base.mk for standard targets
include ../base.mk

# =============================================================================
# SINGER TARGET CONFIGURATION
# =============================================================================

TARGET_CONFIG ?= config.json
TARGET_STATE ?= state.json

# =============================================================================
# SINGER TARGET OPERATIONS
# =============================================================================

.PHONY: load validate-target-config test-target dry-run test-singer

load: ## Run target data loading
	$(POETRY) run target-oracle-oic --config $(TARGET_CONFIG) --state $(TARGET_STATE)

validate-target-config: ## Validate target configuration
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "import json; json.load(open('$(TARGET_CONFIG)'))"

test-target: ## Test target functionality
	$(POETRY) run target-oracle-oic --about
	$(POETRY) run target-oracle-oic --version

dry-run: ## Run target in dry-run mode
	$(POETRY) run target-oracle-oic --config $(TARGET_CONFIG) --dry-run

# =============================================================================
# OIC-SPECIFIC TARGETS
# =============================================================================

.PHONY: oic-auth-test oic-connect oic-write-test oic-endpoint-check

oic-auth-test: ## Test Oracle OIC authentication
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_target_oracle_oic.auth import test_auth; test_auth()"

oic-connect: ## Test Oracle OIC connection
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_target_oracle_oic.client import test_connection; test_connection()"

oic-write-test: ## Test Oracle OIC write operations
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_target_oracle_oic.operations import test_write; test_write()"

oic-endpoint-check: ## Test Oracle OIC endpoints
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_target_oracle_oic.endpoints import test_endpoints; test_endpoints()"

# =============================================================================
# PROJECT-SPECIFIC TEST TARGETS
# =============================================================================

test-singer: ## Run Singer protocol tests
	$(POETRY) run pytest $(TESTS_DIR) -m singer -v
