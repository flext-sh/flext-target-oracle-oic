# flext-target-oracle-oic - Oracle OIC Singer Target
PROJECT_NAME := flext-target-oracle-oic
COV_DIR := flext_target_oracle_oic
MIN_COVERAGE := 90

include ../base.mk

# === PROJECT-SPECIFIC TARGETS ===
.PHONY: target-run test-unit test-integration build shell

target-run: ## Run target with config
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run target-oracle-oic --config config.json

.DEFAULT_GOAL := help
