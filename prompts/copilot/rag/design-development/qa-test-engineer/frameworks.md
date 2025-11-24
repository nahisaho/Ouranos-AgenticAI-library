# Frameworks for Qa Test Engineer

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### Test Design Techniques

**Equivalence Partitioning**:
- Divide input domain into equivalent classes
- Test one representative from each class
- Reduce test case redundancy while maintaining coverage

**Boundary Value Analysis**:
- Test values at boundaries of equivalence partitions
- Off-by-one errors and edge case detection
- Minimum, maximum, and just inside/outside boundaries

**Decision Table Testing**:
- Complex business rule validation
- Systematic combination testing
- Logical condition coverage

**State Transition Testing**:
- System behavior across different states
- Invalid state transition detection
- Workflow and process testing

### Test Automation Patterns

**Page Object Model (POM)**:
```javascript
class LoginPage {
  constructor(page) {
    this.page = page;
    this.usernameInput = '#username';
    this.passwordInput = '#password';
    this.loginButton = '#login-btn';
  }
  
  async login(username, password) {
    await this.page.fill(this.usernameInput, username);
    await this.page.fill(this.passwordInput, password);
    await this.page.click(this.loginButton);
  }
}
```

**Test Data Builder Pattern**:
```javascript
class UserBuilder {
  constructor() {
    this.user = {
      name: 'Test User',
      email: 'test@example.com',
      age: 30
    };
  }
  
  withName(name) {
    this.user.name = name;
    return this;
  }
  
  withEmail(email) {
    this.user.email = email;
    return this;
  }
  
  build() {
    return this.user;
  }
}
```

### Performance Testing Patterns

**Load Testing Script Design**:
- Realistic user behavior simulation
- Think time and pacing considerations
- Data correlation and parameterization

**Performance Test Environment**:
- Production-like configuration
- Isolated test environment
- Monitoring and observability integration

### Security Testing Framework

**OWASP Testing Guide**:
- Information gathering and reconnaissance
- Configuration and deployment management testing
- Identity management and authentication testing
- Authorization testing and session management
- Input validation and error handling
- Cryptography and business logic testing

**Security Test Automation**:
- Automated vulnerability scanning integration
- Security regression testing
- API security testing
- Infrastructure security validation

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
  - Main Prompt: `prompts/copilot/prompts/design-development/qa-test-engineer.md`
  - Examples: `rag/design-development/qa-test-engineer/examples.md`
  - Methodologies: `rag/design-development/qa-test-engineer/methodologies.md`
