# Frameworks for Devops Engineer

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### Infrastructure as Code (IaC)

**Terraform Best Practices**:
- Modular structure with reusable components
- State management and remote backends
- Workspace isolation for environments
- Policy as Code with Sentinel or OPA

**CloudFormation/ARM Templates**:
- Nested stacks and cross-stack references
- Parameter stores and secrets integration
- Drift detection and compliance

**Pulumi**:
- Programming language-based infrastructure
- Component resource model
- Policy and compliance automation

### CI/CD Pipeline Patterns

**Pipeline as Code**:
- Declarative pipeline definitions
- Version-controlled pipeline configurations
- Reusable pipeline templates and libraries

**Security Integration**:
- Shift-left security with early scanning
- SAST, DAST, and IAST integration
- Container and infrastructure security scanning

**Testing Strategies**:
- Unit, integration, and end-to-end testing
- Contract testing for microservices
- Performance and load testing automation

### Container Orchestration

**Kubernetes Patterns**:
- Deployment, StatefulSet, and DaemonSet strategies
- Service mesh integration and traffic management
- Resource management and autoscaling

**Container Security**:
- Image scanning and vulnerability management
- Runtime security and compliance
- Network policies and segmentation

### Site Reliability Engineering (SRE)

**Reliability Principles**:
- Error budgets and SLO-based decision making
- Toil reduction and automation
- Capacity planning and performance optimization

**Chaos Engineering**:
- Fault injection and resilience testing
- Disaster recovery and business continuity
- Observability and incident response

### Cloud-Native Architecture

**Microservices Patterns**:
- Service decomposition strategies
- API gateway and service mesh
- Event-driven architecture

**Serverless Integration**:
- Function as a Service (FaaS) patterns
- Event-driven automation
- Cost optimization strategies

---

---

## Framework Integration Strategies

### Sequential Integration
Frameworks are applied one after another in different stages.

**When to use**: When frameworks build on each other logically.

### Parallel Integration
Multiple frameworks are used simultaneously within the same stage.

**When to use**: When frameworks provide complementary perspectives.

### Selective Integration
User chooses which frameworks to apply based on their specific situation.

**When to use**: When different scenarios require different analytical approaches.

---

## Best Practices

1. **Start Simple**: Don't overwhelm with too many frameworks initially
2. **Explain Why**: Always clarify the purpose and value of each framework
3. **Provide Examples**: Show how frameworks have been applied in similar scenarios
4. **Allow Flexibility**: Let users adapt frameworks to their specific needs
5. **Integrate Naturally**: Frameworks should enhance dialogue, not dominate it

---

## Version Information

- **Version**: 1.0.0
- **Last Updated**: 2025-11-24
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/design-development/devops-engineer.md`
  - Examples: `rag/design-development/devops-engineer/examples.md`
  - Methodologies: `rag/design-development/devops-engineer/methodologies.md`
