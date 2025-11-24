# Methodologies for Backend Developer

This file provides step-by-step procedures, validation checklists, and best practices.

---

## Process Overview

This section provides detailed step-by-step guidance for executing this prompt effectively.

---

## Output Format Details

Backend development deliverables:

```markdown
# Backend Project: [Application Name]

---

## Important Notes and Best Practices

### Backend Development Best Practices

1. **Start Simple**: Begin with monolith, extract microservices when needed
2. **Type Safety**: Use TypeScript/typed languages for fewer runtime errors
3. **Layered Architecture**: Separate concerns (controllers, services, repositories)
4. **Test Early**: Write tests as you develop, not after
5. **Security First**: Validate inputs, use parameterized queries, hash passwords
6. **Optimize Later**: Profile before optimizing, avoid premature optimization
7. **Document APIs**: Use OpenAPI/Swagger for API documentation
8. **Monitor Everything**: Logs, metrics, traces for production debugging

### Common Pitfalls

- N+1 query problems (use eager loading)
- Not using connection pooling (connection exhaustion)
- Blocking the event loop (in Node.js)
- Not validating inputs (security vulnerabilities)
- Ignoring error handling (silent failures)
- Not implementing rate limiting (abuse, DOS)
- Hardcoding secrets (security risk)
- Not using environment variables

### Success Factors

- Clear separation of concerns
- Comprehensive testing coverage
- Robust error handling
- Security-first mindset
- Performance monitoring
- Well-documented APIs
- Scalable architecture
- DevOps automation

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
  - Main Prompt: `prompts/copilot/prompts/design-development/backend-developer.md`
  - Frameworks: `rag/design-development/backend-developer/frameworks.md`
  - Examples: `rag/design-development/backend-developer/examples.md`
