# CLAUDE.local.md - TARGET-ORACLE-OIC PROJECT SPECIFICS

**Hierarquia**: **PROJECT-SPECIFIC**  
**Projeto**: Target Oracle OIC - Enterprise Integration Cloud Deployment Engine  
**Status**: PRODUCTION READY - Active OIC artifact deployment  
**Framework**: Singer Protocol + OAuth2/IDCS + Oracle Integration Cloud  
**Última Atualização**: 2025-06-26

**Referência Global**: `/home/marlonsc/CLAUDE.md` → Universal principles  
**Referência Workspace**: `../CLAUDE.md` → PyAuto workspace patterns  
**Referência Cross-Workspace**: `/home/marlonsc/CLAUDE.local.md` → Cross-workspace issues

---

## 🎯 PROJECT-SPECIFIC CONFIGURATION

### Virtual Environment Usage

```bash
# MANDATORY: Use workspace venv
source /home/marlonsc/pyauto/.venv/bin/activate
# NOT project-specific venv
```

### Agent Coordination

```bash
# Read workspace coordination first
cat /home/marlonsc/pyauto/.token | tail -5
# Use project .token only for project-specific coordination
```

### Project-Specific Environment Variables

```bash
# Target Oracle OIC specific configurations
export TARGET_OIC_BASE_URL=https://instance-region.integration.ocp.oraclecloud.com
export TARGET_OIC_OAUTH_CLIENT_ID=oic_target_client_id
export TARGET_OIC_OAUTH_CLIENT_SECRET=secure_oauth_secret
export TARGET_OIC_OAUTH_TOKEN_URL=https://idcs-tenant.identity.oraclecloud.com/oauth2/v1/token
export TARGET_OIC_IMPORT_MODE=create_or_update
export TARGET_OIC_ACTIVATE_INTEGRATIONS=true
export TARGET_OIC_VALIDATE_CONNECTIONS=true
export TARGET_OIC_ROLLBACK_ON_FAILURE=true
export TARGET_OIC_ENABLE_VERSIONING=true
export TARGET_OIC_LOG_LEVEL=DEBUG
export TARGET_OIC_AUDIT_TRAIL=true
```

---

## 🏗️ TARGET ORACLE OIC ARCHITECTURE

### **Purpose & Role**

- **Integration Deployment Engine**: Complete OIC artifact deployment and lifecycle management
- **Singer Protocol Target**: Standardized data loading for OIC integration configurations
- **CI/CD Integration Platform**: GitOps-friendly deployment workflows for enterprise environments
- **Lifecycle Orchestrator**: Create, update, activate, deactivate OIC components
- **Version Control Manager**: Integration versioning and deployment history tracking

### **Core Singer Components**

```python
# Target Oracle OIC structure
src/target_oracle_oic/
├── target.py            # Main Singer target implementation
├── sinks.py             # Standard OIC artifact sinks
├── sinks_extended.py    # Extended deployment functionality sinks
├── auth.py              # OAuth2/IDCS authentication
└── config.py            # Configuration management
```

### **OIC Deployment Capabilities**

- **Integration Artifacts**: Deploy integrations, mappings, and orchestrations
- **Connection Management**: Deploy and configure adapter connections
- **Package Operations**: Import .iar and .par files with validation
- **Lookup Synchronization**: Deploy and update lookup tables
- **Certificate Management**: Deploy security certificates and credentials

---

## 🔧 PROJECT-SPECIFIC TECHNICAL DETAILS

### **Development Commands**

```bash
# MANDATORY: Always from workspace venv
source /home/marlonsc/pyauto/.venv/bin/activate

# Core development workflow
make install-dev       # Install development dependencies
make test              # Run comprehensive test suite
make test-unit         # Unit tests only
make test-integration  # Integration tests with OIC
make test-e2e          # End-to-end deployment tests
make lint              # Code quality checks
make format            # Code formatting

# Singer target operations
cat integrations.jsonl | target-oracle-oic --config config.json
target-oracle-oic --config config.json --input deployment_data.jsonl
```

### **OIC Deployment Testing**

```bash
# Test OAuth2 authentication for deployment
target-oracle-oic --config config.json --test-auth

# Test deployment dry run
echo '{"type": "RECORD", "stream": "integrations", "record": {"name": "test_integration"}}' | \
  target-oracle-oic --config config.json --dry-run

# Test with real OIC deployment
target-oracle-oic --config config.json --input test_integrations.jsonl --validate-only

# Test lifecycle management
target-oracle-oic --config config.json --activate-all --validate-connections
```

### **CI/CD Pipeline Testing**

```bash
# Test complete deployment pipeline
tap-oracle-oic --config source_config.json | \
  target-oracle-oic --config target_config.json --import-mode create_or_update

# Test rollback functionality
target-oracle-oic --config config.json --rollback-deployment DEPLOYMENT_ID

# Test version control
target-oracle-oic --config config.json --version-control --track-changes
```

---

## 🚨 PROJECT-SPECIFIC KNOWN ISSUES

### **OIC Deployment Challenges**

- **OAuth2 Token Lifecycle**: Complex token management during long deployments
- **Deployment Dependencies**: Managing order of integration component deployment
- **Version Conflicts**: Handling version conflicts during updates
- **Connection Validation**: Validating connections before integration activation
- **Rollback Complexity**: Complex rollback scenarios for multi-component deployments

### **Singer Protocol OIC Considerations**

```python
# OIC-specific Singer target patterns
class OICTargetSingerPatterns:
    """Production patterns for OIC Singer target implementation."""

    def handle_deployment_transaction_safety(self, deployment_batch):
        """Ensure deployment transaction safety with rollback."""
        deployment_checkpoint = self.create_deployment_checkpoint()

        try:
            # Deploy components in dependency order
            for component in self.sort_by_dependencies(deployment_batch):
                deployment_result = self.deploy_component(component)
                self.track_deployment(deployment_result)

            # Validate all deployments
            validation_results = self.validate_all_deployments(deployment_batch)

            if not validation_results.all_passed:
                raise DeploymentValidationError(validation_results.failures)

            return DeploymentSuccess(deployment_batch)

        except Exception as e:
            # Rollback on any failure
            self.rollback_to_checkpoint(deployment_checkpoint)
            raise DeploymentFailureError(f"Deployment failed: {e}")

    def manage_integration_lifecycle(self, integration_record):
        """Manage complete integration lifecycle."""
        # Create or update integration
        if self.integration_exists(integration_record.name):
            integration_result = self.update_integration(integration_record)
        else:
            integration_result = self.create_integration(integration_record)

        # Validate connections
        if self.config.validate_connections:
            connection_validation = self.validate_connections(integration_record)
            if not connection_validation.passed:
                raise ConnectionValidationError(connection_validation.errors)

        # Activate if requested
        if self.config.activate_integrations:
            activation_result = self.activate_integration(
                integration_result.integration_id,
                wait_for_completion=True
            )
            return ActivatedIntegrationResult(integration_result, activation_result)

        return integration_result

    def implement_version_control(self, deployment_record):
        """Implement integration version control."""
        # Track version history
        version_info = self.get_current_version(deployment_record.name)
        new_version = self.calculate_next_version(version_info, deployment_record)

        # Create version snapshot before deployment
        version_snapshot = self.create_version_snapshot(
            integration_name=deployment_record.name,
            version=version_info.current_version
        )

        # Deploy with version tracking
        deployment_result = self.deploy_with_version(deployment_record, new_version)

        # Update version history
        self.update_version_history(
            deployment_record.name,
            new_version,
            version_snapshot,
            deployment_result
        )

        return VersionedDeploymentResult(deployment_result, new_version)
```

### **Production OIC Deployment Edge Cases**

```bash
# Common OIC deployment issues
1. Token Expiration: OAuth2 tokens expiring during long deployments
2. Circular Dependencies: Integration components with circular references
3. Connection State: Target connections in unavailable state
4. Resource Conflicts: Multiple deployments targeting same integration
5. Activation Failures: Integration activation failing after successful deployment
```

---

## 🎯 PROJECT-SPECIFIC SUCCESS METRICS

### **Singer Protocol OIC Compliance**

- **Deployment Success Rate**: 99.9% successful OIC artifact deployments
- **OAuth2 Reliability**: 99.99% successful authentication for deployments
- **Transaction Safety**: 100% rollback success for failed deployments
- **Activation Performance**: <5 minutes average integration activation time
- **Validation Coverage**: 100% pre-deployment validation completion

### **Enterprise OIC Deployment Goals**

- **CI/CD Integration**: Seamless integration with enterprise CI/CD pipelines
- **Multi-Environment Support**: Deploy across dev/test/prod OIC instances
- **Audit Compliance**: Complete audit trail for all deployment activities
- **Version Control**: 100% deployment version tracking and history
- **Error Recovery**: <10 minutes recovery time from deployment failures

---

## 🔗 PROJECT-SPECIFIC INTEGRATIONS

### **Singer Ecosystem Integration**

- **Tap Compatibility**: Works with all Singer-compliant taps for OIC metadata
- **Meltano Plugin**: Official Meltano Hub plugin for OIC deployment
- **Schema Validation**: Automatic validation of OIC artifact schemas
- **State Management**: Deployment state tracking and recovery

### **PyAuto Ecosystem Integration**

- **tap-oracle-oic**: Perfect companion for OIC metadata extraction and deployment
- **flx-oracle-oic**: Unified FLX adapter with Singer target integration
- **oracle-oic-ext**: Meltano extension for deployment lifecycle management
- **gruponos-poc-oic-wms**: POC deployment reference implementation

### **Oracle Cloud Deployment Integration**

```python
# Production OIC deployment configuration
class ProductionOICDeployment:
    """Production OIC deployment for enterprise environments."""

    # Multi-environment deployment configuration
    PRODUCTION_CONFIG = {
        "base_url": "https://prod-region.integration.ocp.oraclecloud.com",
        "oauth_client_id": "${OIC_PROD_DEPLOY_CLIENT_ID}",
        "oauth_client_secret": "${OIC_PROD_DEPLOY_CLIENT_SECRET}",
        "oauth_token_url": "https://prod-idcs.identity.oraclecloud.com/oauth2/v1/token",

        # Deployment safety
        "import_mode": "create_or_update",
        "activate_integrations": True,
        "validate_connections": True,
        "rollback_on_failure": True,
        "enable_versioning": True,

        # Performance optimization
        "deployment_timeout": 600,
        "validation_timeout": 300,
        "activation_timeout": 300,
        "max_retries": 3,
        "retry_backoff_factor": 2,

        # Enterprise features
        "audit_trail": True,
        "deployment_notifications": True,
        "change_management_integration": True,
        "approval_workflow": True,

        # Sink configuration
        "sinks": {
            "integrations": {
                "class": "IntegrationDeploymentSink",
                "validate_before_deploy": True,
                "activate_after_deploy": True,
                "version_control": True
            },
            "connections": {
                "class": "ConnectionDeploymentSink",
                "test_connection": True,
                "update_existing": True
            },
            "packages": {
                "class": "PackageDeploymentSink",
                "extract_before_import": True,
                "validate_dependencies": True
            }
        }
    }
```

---

## 📊 PROJECT-SPECIFIC MONITORING

### **OIC Deployment Metrics**

```python
# Key metrics for OIC deployment monitoring
TARGET_OIC_METRICS = {
    "deployment_success_rate": "Percentage of successful OIC deployments",
    "deployment_duration": "Average time to complete deployments",
    "oauth_token_refresh_rate": "OAuth2 token refresh frequency during deployments",
    "rollback_frequency": "Frequency of deployment rollbacks",
    "validation_failure_rate": "Percentage of failed pre-deployment validations",
    "activation_success_rate": "Success rate of integration activations",
}
```

### **OIC Deployment Health Monitoring**

```bash
# Comprehensive OIC deployment monitoring
target-oracle-oic --config config.json --test-connection --detailed
target-oracle-oic --config config.json --validate-environment --all-checks
target-oracle-oic --config config.json --deployment-status --active-deployments
```

---

## 📋 PROJECT-SPECIFIC MAINTENANCE

### **Regular Maintenance Tasks**

- **Daily**: Monitor deployment success rates and OAuth2 token usage
- **Weekly**: Review rollback incidents and optimize deployment strategies
- **Monthly**: Update OIC deployment client libraries and test compatibility
- **Quarterly**: Performance optimization and deployment workflow review

### **Singer Protocol Updates**

```bash
# Keep Singer SDK and OIC dependencies updated
pip install --upgrade singer-sdk requests-oauthlib

# Validate Singer compliance
singer-check-target --target target-oracle-oic --config config.json
singer-validate-schema --schema oic-deployment-schema.json
```

### **Emergency Procedures**

```bash
# OIC deployment emergency troubleshooting
1. Test OAuth2 deployment flow: target-oracle-oic --config config.json --test-auth
2. Check OIC service status: curl -I ${OIC_BASE_URL}/ic/api/integration/v1/integrations
3. Emergency rollback: target-oracle-oic --config config.json --emergency-rollback DEPLOYMENT_ID
4. Validate deployment environment: target-oracle-oic --config config.json --validate-environment
5. Reset deployment state: target-oracle-oic --config config.json --reset-deployment-state
```

---

**PROJECT SUMMARY**: Singer target empresarial para Oracle Integration Cloud com deployment automatizado de artifacts, gerenciamento de ciclo de vida e integração CI/CD para ambientes enterprise.

**CRITICAL SUCCESS FACTOR**: Manter deployment confiável e seguro de artifacts OIC com transaction safety completa e integração perfeita com pipelines CI/CD empresariais.

---

_Última Atualização: 2025-06-26_  
_Próxima Revisão: Semanal durante deployments ativos_  
_Status: PRODUCTION READY - Deployment ativo de artifacts OIC em produção_
