# Examples for Software Architect

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: E-commerce Platform Architecture

**Stage 1: Requirements**
- System: Multi-tenant e-commerce platform
- Scale: 100K concurrent users, 1M products, 10K transactions/hour
- Requirements: High availability (99.9%), sub-200ms response time, PCI compliance

**Stage 2: Architecture Selection**
- Chosen: Microservices architecture
- Rationale: Independent scaling, team autonomy, fault isolation
- Patterns: API Gateway, CQRS for product catalog, Event Sourcing for orders

**Stage 3: System Design**
- Services: User Service, Product Catalog, Order Service, Payment Service, Notification Service
- Data: PostgreSQL for transactional data, Elasticsearch for product search, Redis for caching
- Communication: REST for synchronous, Kafka for events

**Stage 4: SOLID Application**
- SRP: Separate services by business capability
- OCP: Plugin system for payment providers
- DIP: Use interfaces for all service dependencies

**Stage 5: Documentation**
- Created ADRs for microservices, event-driven architecture, database choices
- Defined API contracts using OpenAPI
- 6-month roadmap: Foundation → Core Services → Optimization → Production

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
  - Main Prompt: `prompts/copilot/prompts/design-development/software-architect.md`
  - Frameworks: `rag/design-development/software-architect/frameworks.md`
  - Methodologies: `rag/design-development/software-architect/methodologies.md`
