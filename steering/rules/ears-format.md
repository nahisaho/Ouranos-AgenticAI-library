# EARS Format Guide

**Version**: 1.0  
**Project**: Ouranos-AgenticAI-library  
**Status**: Active  
**Last Updated**: 2025-11-23

---

## Overview

**EARS** (Easy Approach to Requirements Syntax) is a standardized format for writing clear, unambiguous requirements. All requirements in the Ouranos-AgenticAI-library project MUST use EARS patterns.

**Purpose**: Eliminate ambiguity, improve testability, and ensure traceability.

**Enforcement**: Article IV (EARS Requirements Format) of the Constitutional Governance.

---

## The 5 EARS Patterns

EARS defines 5 requirement patterns that cover all common scenarios:

| Pattern              | Use Case                              | Template                                          |
| -------------------- | ------------------------------------- | ------------------------------------------------- |
| **Ubiquitous**       | Always-active requirements            | `The [system] SHALL [requirement]`                |
| **Event-Driven**     | Triggered by specific events          | `WHEN [event], the [system] SHALL [response]`     |
| **State-Driven**     | Active while in specific state        | `WHILE [state], the [system] SHALL [response]`    |
| **Unwanted Behavior**| Error handling and edge cases         | `IF [condition], THEN the [system] SHALL [response]` |
| **Optional Features**| Conditionally active features         | `WHERE [feature enabled], the [system] SHALL [response]` |

---

## Pattern 1: Ubiquitous Requirements

**Use Case**: Requirements that are always active, regardless of state or events.

### Template

```
The [system] SHALL [requirement].
```

### Examples

**Good** ✅:

```
REQ-AUTH-001: The system SHALL hash all passwords using bcrypt with cost factor 12.

REQ-UI-002: The system SHALL render all pages within 2 seconds on 4G networks.

REQ-SEC-003: The system SHALL enforce HTTPS for all API endpoints.
```

**Bad** ❌:

```
❌ The system should hash passwords.
   → Missing "SHALL", vague ("should" is ambiguous)

❌ Passwords must be hashed securely.
   → No "The system SHALL", missing details (what algorithm?)

❌ The system will use bcrypt.
   → "will" is not "SHALL", no cost factor specified
```

### When to Use

- Security requirements (encryption, authentication)
- Performance requirements (response time, throughput)
- Data validation rules
- System-wide constraints

---

## Pattern 2: Event-Driven Requirements

**Use Case**: Requirements triggered by specific events or user actions.

### Template

```
WHEN [event], the [system] SHALL [response].
```

### Examples

**Good** ✅:

```
REQ-AUTH-010: WHEN a user submits valid login credentials, the system SHALL create a session token with 24-hour expiry.

REQ-NOTIF-015: WHEN a new prompt template is published, the system SHALL send email notifications to all subscribers.

REQ-UPLOAD-020: WHEN a user uploads a markdown file, the system SHALL validate YAML front matter and reject invalid files.
```

**Bad** ❌:

```
❌ Users can log in with credentials.
   → No "WHEN", no "SHALL", vague

❌ If user logs in, create session.
   → Use "WHEN" not "IF" for events, missing "SHALL"

❌ WHEN login, the system creates session.
   → Missing "SHALL" (use "SHALL create" not "creates")
```

### When to Use

- User actions (login, submit, upload)
- External events (API calls, webhooks)
- Time-based triggers (scheduled jobs)
- Data changes (record created, updated, deleted)

---

## Pattern 3: State-Driven Requirements

**Use Case**: Requirements that are active while the system is in a specific state.

### Template

```
WHILE [state], the [system] SHALL [response].
```

### Examples

**Good** ✅:

```
REQ-SESSION-025: WHILE a user session is active, the system SHALL refresh the session token every 10 minutes.

REQ-EDIT-030: WHILE a template is in draft state, the system SHALL allow edits without version control.

REQ-PROC-035: WHILE a background job is processing, the system SHALL display a progress indicator.
```

**Bad** ❌:

```
❌ During active session, refresh token.
   → Use "WHILE" not "During", missing "SHALL"

❌ The system refreshes tokens when session is active.
   → No "WHILE", no "SHALL"

❌ IF session active, refresh token.
   → Use "WHILE" for states, not "IF"
```

### When to Use

- Persistent states (session active, user logged in)
- Mode-based behavior (edit mode, preview mode)
- Resource availability (while service online)
- Continuous monitoring (while system running)

---

## Pattern 4: Unwanted Behavior (Error Handling)

**Use Case**: Handling errors, edge cases, and exceptional conditions.

### Template

```
IF [condition], THEN the [system] SHALL [response].
```

### Examples

**Good** ✅:

```
REQ-ERR-040: IF a user enters invalid credentials 3 times, THEN the system SHALL lock the account for 15 minutes.

REQ-VALID-045: IF a template file exceeds 8000 characters for Copilot edition, THEN the system SHALL reject the upload with error message "Character limit exceeded".

REQ-API-050: IF an API request fails with 500 error, THEN the system SHALL retry up to 3 times with exponential backoff.
```

**Bad** ❌:

```
❌ When login fails 3 times, lock account.
   → Use "IF" for errors, not "WHEN", missing "THEN" and "SHALL"

❌ IF file too large, reject it.
   → Vague ("too large"), no "THEN", no "SHALL", no specifics

❌ The system handles errors gracefully.
   → Not specific, no IF-THEN, no measurable criteria
```

### When to Use

- Error conditions (invalid input, service unavailable)
- Edge cases (limits exceeded, resource exhausted)
- Security violations (unauthorized access)
- Data validation failures

---

## Pattern 5: Optional Features

**Use Case**: Requirements for optional or configurable features.

### Template

```
WHERE [feature enabled], the [system] SHALL [response].
```

### Examples

**Good** ✅:

```
REQ-FEAT-055: WHERE multi-language support is enabled, the system SHALL display templates in user's preferred language.

REQ-ANALYTICS-060: WHERE analytics tracking is enabled, the system SHALL log template usage events to analytics database.

REQ-NOTIF-065: WHERE email notifications are enabled, the system SHALL send daily digest at 9:00 AM UTC.
```

**Bad** ❌:

```
❌ If analytics enabled, log events.
   → Use "WHERE" for features, not "IF", missing "SHALL"

❌ The system supports multi-language.
   → No "WHERE", no "SHALL", not specific

❌ WHEN feature enabled, activate it.
   → Use "WHERE" for features, not "WHEN"
```

### When to Use

- Optional features (can be toggled on/off)
- Configuration-dependent behavior
- Premium/tier-based features
- Experimental features

---

## EARS Best Practices

### 1. Use "SHALL" (Not "will", "should", "must")

**Correct** ✅:

```
The system SHALL validate all user input.
```

**Incorrect** ❌:

```
❌ The system should validate user input.
❌ The system must validate user input.
❌ The system will validate user input.
```

**Rationale**: "SHALL" is the RFC 2119 standard keyword for mandatory requirements.

---

### 2. Be Specific and Measurable

**Correct** ✅:

```
REQ-PERF-070: The system SHALL return search results within 200ms for 95% of queries.
```

**Incorrect** ❌:

```
❌ The system SHALL return search results quickly.
```

**Guidelines**:
- Include numbers (200ms, 95%, 3 retries)
- Specify units (ms, seconds, bytes, MB)
- Define thresholds (95th percentile, maximum, minimum)

---

### 3. One Requirement Per Statement

**Correct** ✅:

```
REQ-AUTH-075: The system SHALL hash passwords using bcrypt with cost factor 12.
REQ-AUTH-076: The system SHALL store password hashes in the database.
REQ-AUTH-077: The system SHALL never log passwords in plaintext.
```

**Incorrect** ❌:

```
❌ REQ-AUTH-XXX: The system SHALL hash passwords using bcrypt, store them in database, and never log them.
```

**Rationale**: Multiple requirements in one statement are harder to test and trace.

---

### 4. Include Context in "The [system]"

**Correct** ✅:

```
REQ-UI-080: The web interface SHALL display error messages in red text.
REQ-API-081: The REST API SHALL return error responses in JSON format.
REQ-CLI-082: The command-line tool SHALL exit with code 1 on errors.
```

**Rationale**: Clarifies which part of the system the requirement applies to.

---

### 5. Define Acceptance Criteria

Each requirement should include testable acceptance criteria:

**Example**:

```markdown
## REQ-UPLOAD-085: Template File Upload

**Requirement**:  
WHEN a user uploads a markdown file, the system SHALL validate YAML front matter and reject invalid files.

**Acceptance Criteria**:

✅ **GIVEN** a markdown file with valid YAML front matter  
   **WHEN** user uploads the file  
   **THEN** system accepts the file and returns success message

✅ **GIVEN** a markdown file with missing `id` field in YAML  
   **WHEN** user uploads the file  
   **THEN** system rejects the file with error "Missing required field: id"

✅ **GIVEN** a markdown file with malformed YAML syntax  
   **WHEN** user uploads the file  
   **THEN** system rejects the file with error "Invalid YAML syntax"
```

---

## Requirement ID Convention

### Format

```
REQ-[CATEGORY]-[NUMBER]
```

**Example**: `REQ-AUTH-001`

### Categories

| Category | Description                  | Examples          |
| -------- | ---------------------------- | ----------------- |
| **AUTH** | Authentication/Authorization | Login, permissions|
| **UI**   | User Interface               | Rendering, layout |
| **API**  | API endpoints                | REST, GraphQL     |
| **DB**   | Database                     | Schema, queries   |
| **PERF** | Performance                  | Response time     |
| **SEC**  | Security                     | Encryption, HTTPS |
| **VALID**| Validation                   | Input validation  |
| **ERR**  | Error Handling               | Error responses   |
| **FEAT** | Features                     | Optional features |

### Numbering

- Start from 001 for each category
- Increment by 1 (001, 002, 003, ...)
- Zero-pad to 3 digits (001, not 1)

---

## EARS Template for Requirements Document

```markdown
# Requirements: {feature-name}

**Feature**: {feature-name}  
**Version**: 1.0  
**Status**: Draft | Approved | Implemented  
**Created**: YYYY-MM-DD  
**Updated**: YYYY-MM-DD

---

## Overview

[Brief description of the feature and its purpose]

---

## Functional Requirements

### REQ-XXX-001: {Requirement Title}

**Type**: Ubiquitous | Event-Driven | State-Driven | Unwanted Behavior | Optional

**Requirement**:  
[EARS-formatted requirement]

**Rationale**:  
[Why this requirement exists]

**Acceptance Criteria**:

✅ **GIVEN** [precondition]  
   **WHEN** [action]  
   **THEN** [expected result]

✅ **GIVEN** [precondition]  
   **WHEN** [action]  
   **THEN** [expected result]

**Dependencies**: [Related requirements]

**Priority**: P0 (Critical) | P1 (High) | P2 (Medium) | P3 (Low)

---

### REQ-XXX-002: {Requirement Title}

[Repeat structure for each requirement]

---

## Non-Functional Requirements

### REQ-PERF-001: Performance

**Requirement**:  
The {system} SHALL respond to API requests within 200ms for 95% of requests.

**Acceptance Criteria**:

✅ **GIVEN** 1000 API requests under normal load  
   **WHEN** measuring p95 latency  
   **THEN** latency is ≤ 200ms

---

### REQ-SEC-001: Security

**Requirement**:  
The {system} SHALL enforce HTTPS for all API endpoints.

**Acceptance Criteria**:

✅ **GIVEN** HTTP request to any API endpoint  
   **WHEN** server receives request  
   **THEN** server redirects to HTTPS or rejects with 403

---

## Traceability Matrix

| Requirement | Design Element | Code Module | Test Case |
| ----------- | -------------- | ----------- | --------- |
| REQ-XXX-001 | [Design ref]   | [Module]    | [Test ID] |
| REQ-XXX-002 | [Design ref]   | [Module]    | [Test ID] |

---

## Changelog

| Version | Date       | Changes              | Author |
| ------- | ---------- | -------------------- | ------ |
| 1.0     | YYYY-MM-DD | Initial requirements | [Name] |
```

---

## Common Pitfalls and Fixes

### ❌ Pitfall 1: Using "should" instead of "SHALL"

**Wrong**:  
```
The system should validate user input.
```

**Fixed** ✅:  
```
The system SHALL validate user input.
```

---

### ❌ Pitfall 2: Vague Requirements

**Wrong**:  
```
The system SHALL be fast.
```

**Fixed** ✅:  
```
REQ-PERF-001: The system SHALL return search results within 200ms for 95% of queries.
```

---

### ❌ Pitfall 3: Mixing Multiple Requirements

**Wrong**:  
```
REQ-AUTH-001: The system SHALL authenticate users, create sessions, and log access events.
```

**Fixed** ✅:  
```
REQ-AUTH-001: WHEN a user submits valid credentials, the system SHALL authenticate the user.
REQ-AUTH-002: WHEN authentication succeeds, the system SHALL create a session token with 24-hour expiry.
REQ-AUTH-003: WHEN authentication succeeds, the system SHALL log access event to audit log.
```

---

### ❌ Pitfall 4: Wrong Pattern Selection

**Wrong**:  
```
WHEN the system is in edit mode, the system SHALL allow edits.
```

**Fixed** ✅:  
```
WHILE the system is in edit mode, the system SHALL allow edits.
```

**Rationale**: Use WHILE for states, WHEN for events.

---

### ❌ Pitfall 5: Missing Acceptance Criteria

**Wrong**:  
```
REQ-UPLOAD-001: WHEN user uploads file, system SHALL validate it.
```

**Fixed** ✅:  
```
REQ-UPLOAD-001: WHEN user uploads markdown file, system SHALL validate YAML front matter.

Acceptance Criteria:
✅ GIVEN file with valid YAML WHEN uploaded THEN accepted
✅ GIVEN file with invalid YAML WHEN uploaded THEN rejected with error
✅ GIVEN file with missing required fields WHEN uploaded THEN rejected with specific error
```

---

## Summary

### Quick Reference

| Pattern              | Template                                          | Use Case               |
| -------------------- | ------------------------------------------------- | ---------------------- |
| **Ubiquitous**       | `The [system] SHALL [requirement]`                | Always active          |
| **Event-Driven**     | `WHEN [event], the [system] SHALL [response]`     | Triggered by events    |
| **State-Driven**     | `WHILE [state], the [system] SHALL [response]`    | Active in state        |
| **Unwanted Behavior**| `IF [condition], THEN the [system] SHALL [response]` | Error handling      |
| **Optional Features**| `WHERE [feature], the [system] SHALL [response]`  | Optional/configurable  |

### EARS Checklist

- [ ] Requirement uses one of 5 EARS patterns
- [ ] Uses "SHALL" (not "should", "must", "will")
- [ ] Specific and measurable
- [ ] One requirement per statement
- [ ] Unique ID (REQ-XXX-NNN)
- [ ] Acceptance criteria defined
- [ ] Testable
- [ ] Traceable (maps to design, code, tests)

---

**Powered by MUSUBI** - Constitutional governance for specification-driven development.

**Last Updated**: 2025-11-23  
**Maintained By**: Project Team
