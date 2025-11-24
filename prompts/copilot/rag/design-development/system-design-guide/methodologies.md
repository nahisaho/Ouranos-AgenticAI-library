# Methodologies for System Design Guide

This file provides step-by-step procedures, validation checklists, and best practices.

---

## Process Overview

This section provides detailed step-by-step guidance for executing this prompt effectively.

---

## Output Format Details

The system design document will include:

```markdown
# System Design: [System Name]

---

## Important Notes and Best Practices

### System Design Best Practices

1. **Start Simple**: Don't over-engineer for scale you don't have
2. **Measure First**: Profile before optimizing
3. **Design for Failure**: Everything will fail eventually
4. **Think in Terms of Trade-offs**: No perfect solution
5. **Consider Operational Complexity**: Simpler systems are easier to operate
6. **Document Decisions**: Explain why, not just what
7. **Plan for Growth**: But don't prematurely optimize

### Common Pitfalls

- Over-engineering for theoretical scale
- Premature microservices
- Ignoring network latency in distributed systems
- Not planning for failure scenarios
- Inadequate monitoring and observability
- Underestimating data growth
- Ignoring operational complexity

### Success Factors

- Clear requirements and scale targets
- Appropriate use of proven patterns
- Balance between simplicity and scalability
- Comprehensive monitoring
- Regular load testing
- Iterative refinement
- Learning from incidents

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
  - Main Prompt: `prompts/copilot/prompts/design-development/system-design-guide.md`
  - Frameworks: `rag/design-development/system-design-guide/frameworks.md`
  - Examples: `rag/design-development/system-design-guide/examples.md`
