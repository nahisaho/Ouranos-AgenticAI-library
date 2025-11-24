# Examples for Code Review Mentor

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: Reviewing a User Authentication Feature

**Context**:
- Language: Node.js/TypeScript
- Change: Add JWT authentication
- Size: 350 lines
- Risk: High (security-critical)

**Review Findings**:

**Blocking**:
- 🔴 JWT secret is hardcoded (should be in env variable)
- 🔴 No token expiration validation
- 🔴 Password stored in plain text (use bcrypt)

**Suggestions**:
- 💡 Add rate limiting to login endpoint
- 💡 Consider refresh token pattern for better UX
- 💡 Extract token generation into utility function

**Questions**:
- ❓ Why JWT over session-based auth for this use case?
- ❓ What's the token expiration time?

**Positive**:
- ✅ Great test coverage (92%)
- ✅ Clear error messages for users

**Outcome**: Request changes → Fixed → Approved

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
  - Main Prompt: `prompts/copilot/prompts/design-development/code-review-mentor.md`
  - Frameworks: `rag/design-development/code-review-mentor/frameworks.md`
  - Methodologies: `rag/design-development/code-review-mentor/methodologies.md`
