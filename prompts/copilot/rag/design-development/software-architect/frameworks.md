# Frameworks for Software Architect

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### SOLID Principles Detailed

**Purpose**: Create maintainable, flexible, and robust object-oriented software

**Benefits**:
- Easier to maintain and extend
- More testable code
- Better separation of concerns
- Reduced coupling
- Increased cohesion

### Clean Architecture

**Purpose**: Achieve independence of frameworks, UI, database, and external agencies

**Layers** (from inner to outer):
1. **Entities**: Enterprise business rules
2. **Use Cases**: Application business rules
3. **Interface Adapters**: Controllers, presenters, gateways
4. **Frameworks & Drivers**: UI, DB, web framework, devices

**Dependency Rule**: Dependencies point inward, inner layers know nothing about outer layers

### Design Patterns

**Creational Patterns**:
- **Singleton**: Ensure a class has only one instance
- **Factory Method**: Create objects without specifying exact class
- **Abstract Factory**: Create families of related objects
- **Builder**: Construct complex objects step by step
- **Prototype**: Clone existing objects

**Structural Patterns**:
- **Adapter**: Make incompatible interfaces compatible
- **Bridge**: Separate abstraction from implementation
- **Composite**: Compose objects into tree structures
- **Decorator**: Add responsibilities dynamically
- **Facade**: Provide unified interface to subsystem
- **Proxy**: Control access to objects

**Behavioral Patterns**:
- **Strategy**: Define family of algorithms, make them interchangeable
- **Observer**: Define one-to-many dependency for notifications
- **Command**: Encapsulate request as object
- **State**: Allow object to alter behavior when state changes
- **Template Method**: Define skeleton, let subclasses override steps
- **Chain of Responsibility**: Pass request along chain of handlers

### Domain-Driven Design

**Strategic Design**:
- **Bounded Context**: Explicit boundary for model
- **Context Map**: Relationships between contexts
- **Ubiquitous Language**: Shared language between developers and domain experts

**Tactical Design**:
- **Entities**: Objects with identity
- **Value Objects**: Immutable objects without identity
- **Aggregates**: Cluster of objects treated as unit
- **Domain Events**: Something that happened in domain
- **Repositories**: Access to aggregates
- **Domain Services**: Operations that don't belong to entities

### Microservices Patterns

**Decomposition**:
- Decompose by business capability
- Decompose by subdomain (DDD)
- Self-contained services

**Communication**:
- Synchronous: REST, gRPC
- Asynchronous: Message queues, event streaming

**Data Management**:
- Database per service
- Saga pattern for distributed transactions
- CQRS (Command Query Responsibility Segregation)
- Event sourcing

**Observability**:
- Distributed tracing
- Centralized logging
- Metrics and monitoring
- Health checks

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
  - Main Prompt: `prompts/copilot/prompts/design-development/software-architect.md`
  - Examples: `rag/design-development/software-architect/examples.md`
  - Methodologies: `rag/design-development/software-architect/methodologies.md`
