# Examples for Qa Test Engineer

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: E-commerce Platform Quality Transformation

**Stage 1: Assessment**
- **Current State**: 30% automated testing, manual regression testing taking 2 weeks, 15% bug escape rate
- **Pain Points**: Slow feedback cycles, test maintenance overhead, inconsistent quality across teams
- **Team**: 2 QA engineers, 8 developers, growing to 15-person team

**Stage 2: Strategy**
- **Framework**: Test automation pyramid with 70% unit, 20% integration, 10% UI tests
- **Tools**: Jest for unit tests, Playwright for UI automation, K6 for performance testing
- **Quality Gates**: 80% code coverage, <2% test flakiness, performance budgets

**Stage 3: Implementation**
- **API Testing**: REST API automation with contract testing using Pact
- **UI Testing**: Critical user journey automation covering checkout, user registration, product search
- **Framework**: Page object model with TypeScript for type safety and maintainability

**Stage 4: Integration**
- **Performance**: Load testing in CI/CD pipeline with K6, 2-second response time SLA
- **Security**: OWASP ZAP integration for automated security scanning, dependency vulnerability checks
- **Pipeline**: 15-minute feedback cycle with parallel test execution

**Stage 5: Culture**
- **Shift-Left**: Developers writing unit tests, QA involved in story refinement
- **Metrics**: Quality dashboard showing test trends, defect metrics, customer impact
- **Results**: Bug escape rate reduced to 3%, deployment frequency increased from weekly to daily, test execution time reduced from 2 weeks to 2 hours

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
  - Main Prompt: `prompts/copilot/prompts/design-development/qa-test-engineer.md`
  - Frameworks: `rag/design-development/qa-test-engineer/frameworks.md`
  - Methodologies: `rag/design-development/qa-test-engineer/methodologies.md`
