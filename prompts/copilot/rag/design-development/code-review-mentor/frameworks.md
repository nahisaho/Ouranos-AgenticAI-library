# Frameworks for Code Review Mentor

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### SOLID Principles (for Design Review)

**S - Single Responsibility Principle**:
- A class should have one, and only one, reason to change
- Each module/class should do one thing well

**O - Open/Closed Principle**:
- Software entities should be open for extension, closed for modification
- Use interfaces, abstract classes, composition

**L - Liskov Substitution Principle**:
- Objects of a superclass should be replaceable with objects of subclasses
- Subtypes must be substitutable for their base types

**I - Interface Segregation Principle**:
- Many client-specific interfaces are better than one general-purpose interface
- Don't force clients to depend on methods they don't use

**D - Dependency Inversion Principle**:
- Depend on abstractions, not concretions
- High-level modules shouldn't depend on low-level modules

### Code Quality Metrics

**Cyclomatic Complexity**:
- Number of linearly independent paths through code
- Target: < 10 per function
- High complexity = harder to test and maintain

**Code Coverage**:
- Percentage of code executed by tests
- Target: 80%+ (but 100% doesn't mean bug-free)
- Focus on critical paths

**Code Churn**:
- How often code changes
- High churn = potential instability
- Review high-churn areas carefully

### Security Review Framework (OWASP Top 10)

1. Injection (SQL, NoSQL, OS command)
2. Broken Authentication
3. Sensitive Data Exposure
4. XML External Entities (XXE)
5. Broken Access Control
6. Security Misconfiguration
7. Cross-Site Scripting (XSS)
8. Insecure Deserialization
9. Using Components with Known Vulnerabilities
10. Insufficient Logging & Monitoring

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
  - Main Prompt: `prompts/copilot/prompts/design-development/code-review-mentor.md`
  - Examples: `rag/design-development/code-review-mentor/examples.md`
  - Methodologies: `rag/design-development/code-review-mentor/methodologies.md`
