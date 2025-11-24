# Frameworks for Api Design Specialist

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### RESTful API Maturity Model (Richardson Maturity Model)

**Level 0: The Swamp of POX**:
- Single URI, single HTTP method (usually POST)
- RPC-style

**Level 1: Resources**:
- Multiple URIs for different resources
- Still using single HTTP method

**Level 2: HTTP Verbs**:
- Proper use of HTTP methods (GET, POST, PUT, DELETE)
- Proper use of HTTP status codes
- Most APIs aim for this level

**Level 3: Hypermedia Controls (HATEOAS)**:
- API responses include links to related resources
- Self-documenting API
- Client driven by hypermedia
- Rarely implemented in practice

### API Design Principles

**Consistency**:
- Consistent naming conventions
- Consistent error format
- Consistent pagination approach
- Predictable behavior

**Simplicity**:
- Easy to understand and use
- Minimal cognitive load
- Clear, descriptive names
- Avoid unnecessary complexity

**Flexibility**:
- Support various use cases
- Allow filtering, sorting, field selection
- Extensible without breaking changes

**Performance**:
- Pagination for large datasets
- Caching support (ETags, Last-Modified)
- Compression support
- Efficient queries

**Security**:
- Authentication and authorization
- Input validation
- Rate limiting
- HTTPS only

### GraphQL Best Practices

**Schema Design**:
- Design schema around business domain
- Use meaningful, descriptive names
- Avoid exposing implementation details
- Use interfaces for shared behavior

**Performance**:
- Implement DataLoader for batching
- Set maximum query depth
- Set query complexity limits
- Use persisted queries

**Error Handling**:
- Use `errors` array for multiple errors
- Include error codes and messages
- Separate errors from data

**Security**:
- Disable introspection in production
- Implement query cost analysis
- Authenticate and authorize per field
- Sanitize inputs

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
  - Main Prompt: `prompts/copilot/prompts/design-development/api-design-specialist.md`
  - Examples: `rag/design-development/api-design-specialist/examples.md`
  - Methodologies: `rag/design-development/api-design-specialist/methodologies.md`
