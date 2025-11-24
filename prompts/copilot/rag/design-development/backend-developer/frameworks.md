# Frameworks for Backend Developer

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### Backend Architecture Patterns

- **Layered Architecture**: Controllers → Services → Repositories
- **Repository Pattern**: Abstract data access
- **Dependency Injection**: Loose coupling, testability
- **SOLID Principles**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion

### API Design Patterns

- **REST**: Resource-based, HTTP verbs, stateless
- **GraphQL**: Flexible queries, type-safe, single endpoint
- **gRPC**: High-performance RPC, Protocol Buffers
- **Event-Driven**: Pub/sub, message queues, event sourcing

### Security Best Practices

- **Authentication**: JWT, OAuth 2.0, session-based
- **Authorization**: RBAC, ABAC, resource-based
- **Input Validation**: Schema validation, sanitization
- **Security Headers**: helmet.js, CORS, CSP

### Performance Optimization

- **Caching**: Redis, application cache, CDN
- **Database**: Indexing, query optimization, connection pooling
- **Async Processing**: Message queues, background jobs
- **Rate Limiting**: Prevent abuse, ensure fair usage

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
  - Main Prompt: `prompts/copilot/prompts/design-development/backend-developer.md`
  - Examples: `rag/design-development/backend-developer/examples.md`
  - Methodologies: `rag/design-development/backend-developer/methodologies.md`
