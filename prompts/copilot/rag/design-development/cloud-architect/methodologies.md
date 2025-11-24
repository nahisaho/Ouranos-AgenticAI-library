# Methodologies for Cloud Architect

This file provides step-by-step procedures, validation checklists, and best practices.

---

## Process Overview

This section provides detailed step-by-step guidance for executing this prompt effectively.

---

## Output Format Details

Cloud architecture deliverables:

```markdown
# Cloud Architecture: [Project Name]

---

## Important Notes and Best Practices

### Cloud Architecture Best Practices

1. **Design for Failure**: Assume everything fails, design resilience
2. **Automate Everything**: IaC, CI/CD, monitoring, incident response
3. **Security by Design**: Defense in depth, least privilege, encryption
4. **Cost Awareness**: Tag resources, monitor spending, optimize continuously
5. **Operational Excellence**: Monitoring, logging, runbooks, post-mortems
6. **Scalability**: Horizontal scaling, stateless design, caching
7. **Multi-AZ Deployment**: Always deploy across multiple availability zones

### Common Pitfalls

- Single point of failure (single AZ deployment)
- No disaster recovery plan
- Insufficient monitoring and alerting
- Unoptimized costs (idle resources, wrong instance types)
- Poor security practices (open security groups, no encryption)
- Manual infrastructure (no IaC)
- Vendor lock-in (no abstraction, cloud-specific features)

### Success Factors

- Well-defined business objectives
- Right cloud provider selection
- Infrastructure as Code adoption
- Comprehensive monitoring and observability
- Security and compliance from day one
- Cost optimization culture (FinOps)
- Regular architecture reviews

---

---

## Quality Checkpoints

Before finalizing outputs, verify:

- [ ] All objectives clearly addressed
- [ ] Frameworks properly applied
- [ ] Output format matches specifications
- [ ] Quality standards met
- [ ] User requirements fulfilled

---

## Common Issues and Solutions

This section addresses frequently encountered challenges and their solutions.

---

## Version Information

- **Version**: 1.0.0
- **Last Updated**: 2025-11-24
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/design-development/cloud-architect.md`
  - Frameworks: `rag/design-development/cloud-architect/frameworks.md`
  - Examples: `rag/design-development/cloud-architect/examples.md`
