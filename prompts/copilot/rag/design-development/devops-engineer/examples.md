# Examples for Devops Engineer

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: E-commerce Platform DevOps Transformation

**Stage 1: Assessment**
- **Current State**: Manual deployments taking 4 hours, weekly releases, no infrastructure automation
- **Pain Points**: Deployment failures (30% rollback rate), environment inconsistencies, no monitoring
- **Team**: 3 developers, 1 operations engineer, growing to 10-person team

**Stage 2: Strategy**
- **Target**: Kubernetes on AWS EKS with Infrastructure as Code
- **Platform**: Self-service developer platform with Terraform modules
- **Architecture**: Microservices with API gateway and service mesh

**Stage 3: CI/CD Design**
- **CI**: GitHub Actions with automated testing, security scanning, container building
- **CD**: Canary deployments with Argo CD, automated rollbacks on health check failures
- **Security**: SAST with SonarQube, container scanning with Trivy

**Stage 4: Observability**
- **Monitoring**: Prometheus + Grafana with custom dashboards
- **SLOs**: 99.9% availability, <200ms p95 response time
- **Alerting**: PagerDuty integration with escalation policies

**Stage 5: Implementation**
- **Phase 1**: IaC setup, basic CI/CD (3 months)
- **Phase 2**: Kubernetes migration, advanced monitoring (3 months)
- **Results**: Deployment frequency from weekly to daily, MTTR from 4 hours to 15 minutes, zero-downtime deployments

---

---

## Dialogue Quality Tips

### Creating Natural Flow

Build on user responses naturally, showing domain expertise and genuine engagement.

### Demonstrating Expertise

Use domain-specific knowledge to provide valuable insights and guidance.

### Adaptive Responses

Adjust depth and complexity based on user's expertise level and responses.

---

## Version Information

- **Version**: 1.0.0
- **Last Updated**: 2025-11-24
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/design-development/devops-engineer.md`
  - Frameworks: `rag/design-development/devops-engineer/frameworks.md`
  - Methodologies: `rag/design-development/devops-engineer/methodologies.md`
