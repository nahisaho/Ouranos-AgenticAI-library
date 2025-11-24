# Frameworks for Cloud Architect

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### Cloud Architecture Frameworks

- **AWS Well-Architected Framework**: 6 pillars (Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability)
- **Azure Cloud Adoption Framework**: Strategy, Plan, Ready, Adopt, Govern, Manage
- **Google Cloud Architecture Framework**: Operational excellence, Security, Reliability, Cost optimization, Performance optimization

### Cloud-Native Patterns

- **12-Factor App**: Codebase, Dependencies, Config, Backing services, Build/release/run, Processes, Port binding, Concurrency, Disposability, Dev/prod parity, Logs, Admin processes
- **Microservices**: Service discovery, API gateway, circuit breakers, event-driven
- **Serverless**: FaaS, BaaS, event-driven, pay-per-use

### High Availability Patterns

- **Multi-AZ**: Distribute across availability zones
- **Multi-Region**: Active-active or active-passive
- **Auto Scaling**: Horizontal scaling based on metrics
- **Load Balancing**: Distribute traffic, health checks

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
  - Main Prompt: `prompts/copilot/prompts/design-development/cloud-architect.md`
  - Examples: `rag/design-development/cloud-architect/examples.md`
  - Methodologies: `rag/design-development/cloud-architect/methodologies.md`
