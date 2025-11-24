# MUSUBI SDD Workflow

**Version**: 1.0  
**Project**: Ouranos-AgenticAI-library  
**Status**: Active  
**Last Updated**: 2025-11-23

---

## Overview

This document defines the 8-stage Specification-Driven Development (SDD) workflow used in the Ouranos-AgenticAI-library project, following MUSUBI methodology.

**MUSUBI** (Ultimate Specification Driven Development) ensures that all development activities are driven by clear specifications, traceability, and constitutional compliance.

---

## 8-Stage SDD Workflow

```
Stage -1: Steering (Project Memory)
    ↓
Stage 0: Requirements (EARS)
    ↓
Stage 1: Design (C4 + ADR)
    ↓
Stage 2: Tasks (Breakdown)
    ↓
Stage 3: Implementation (Code)
    ↓
Stage 4: Testing (Validation)
    ↓
Stage 5: Validation (Constitutional)
    ↓
Stage 6: Deployment
```

---

## Stage -1: Steering (Project Memory)

**Purpose**: Establish and maintain project context for all development decisions.

### Activities

- Generate/update `steering/structure.md` (architecture patterns)
- Generate/update `steering/tech.md` (technology stack)
- Generate/update `steering/product.md` (product context)
- Maintain `steering/rules/constitution.md` (9 Constitutional Articles)

### Inputs

- Project vision and objectives
- Technology choices and constraints
- Business requirements and stakeholder input

### Outputs

- `steering/structure.md` - Architecture patterns and directory organization
- `steering/tech.md` - Technology stack decisions
- `steering/product.md` - Product vision, features, metrics
- `steering/rules/constitution.md` - Immutable governance rules

### Commands

```bash
# Generate/update project memory
#sdd-steering
```

### Validation

- Steering files exist and are up-to-date
- All skills reference steering before execution
- Changes to steering require stakeholder approval

**Enforcement**: Article VI (Project Memory)

---

## Stage 0: Requirements (EARS)

**Purpose**: Define clear, unambiguous requirements using EARS format.

### Activities

- Write requirements using EARS patterns (Easy Approach to Requirements Syntax)
- Define acceptance criteria
- Identify constraints and non-functional requirements
- Create requirements traceability matrix

### EARS Patterns

1. **Event-driven**: `WHEN [event], the [system] SHALL [response]`
2. **State-driven**: `WHILE [state], the [system] SHALL [response]`
3. **Unwanted behavior**: `IF [error], THEN the [system] SHALL [response]`
4. **Optional features**: `WHERE [feature enabled], the [system] SHALL [response]`
5. **Ubiquitous**: `The [system] SHALL [requirement]`

### Inputs

- Feature requests or change requests
- User stories and use cases
- Steering context (product.md)

### Outputs

- `storage/specs/{feature}-requirements.md` - EARS-formatted requirements
- Requirements with unique IDs (REQ-XXX-NNN)
- Acceptance criteria per requirement
- Requirements traceability matrix

### Commands

```bash
# Create EARS requirements for a feature
#sdd-requirements <feature>
```

### Validation

- All requirements use EARS patterns (Article IV)
- Requirements are unambiguous
- Acceptance criteria defined
- Unique requirement IDs assigned

**Phase -1 Gate**: EARS compliance check before proceeding to design

**Enforcement**: Article IV (EARS Requirements Format)

---

## Stage 1: Design (C4 + ADR)

**Purpose**: Create architectural design using C4 diagrams and Architecture Decision Records.

### Activities

- Create C4 diagrams (Context, Container, Component, Code)
- Document Architecture Decision Records (ADRs)
- Define API contracts and data models
- Create requirements coverage matrix
- Validate against Constitutional Articles

### Design Documents

- **C4 Context Diagram**: System boundaries and external dependencies
- **C4 Container Diagram**: High-level technology choices
- **C4 Component Diagram**: Component-level architecture
- **ADRs**: Key architectural decisions with rationale
- **Requirements Coverage**: Mapping requirements to design elements

### Inputs

- Requirements document (`{feature}-requirements.md`)
- Steering context (structure.md, tech.md)
- Existing architecture and design patterns

### Outputs

- `storage/specs/{feature}-design.md` - C4 diagrams + ADRs
- Requirements coverage matrix
- API specifications (if applicable)
- Database schema (if applicable)

### Commands

```bash
# Generate C4 + ADR design for a feature
#sdd-design <feature>
```

### Validation

- Requirements coverage: all REQ-XXX-NNN mapped to design elements
- Library-First compliance (Article I)
- CLI Interface mandate (Article II)
- Simplicity Gate: ≤3 projects initially (Article VII)
- Anti-Abstraction Gate: no unnecessary wrappers (Article VIII)
- Steering alignment (Article VI)

**Phase -1 Gates**:
- Simplicity Gate (if project count > 3)
- Anti-Abstraction Gate (if custom abstractions proposed)

**Enforcement**: Articles I, II, VI, VII, VIII

---

## Stage 2: Tasks (Breakdown)

**Purpose**: Break down design into actionable implementation tasks.

### Activities

- Decompose design into granular tasks
- Assign priorities (P0, P1, P2, P3)
- Map tasks to requirements
- Define task dependencies
- Estimate effort

### Task Structure

Each task includes:
- **ID**: TASK-XXX-NNN
- **Title**: Brief description
- **Requirements**: Linked REQ-XXX-NNN
- **Description**: Detailed task description
- **Acceptance Criteria**: Done criteria
- **Dependencies**: Other tasks that must complete first
- **Priority**: P0 (critical) to P3 (low)
- **Estimate**: Effort in hours/days

### Inputs

- Design document (`{feature}-design.md`)
- Requirements document (`{feature}-requirements.md`)

### Outputs

- `storage/specs/{feature}-tasks.md` - Task breakdown with traceability
- Task dependency graph
- Implementation roadmap

### Commands

```bash
# Break down feature into tasks
#sdd-tasks <feature>
```

### Validation

- All tasks map to requirements
- Dependencies identified
- Priorities assigned
- Acceptance criteria defined

**Enforcement**: Article V (Traceability Mandate)

---

## Stage 3: Implementation (Code)

**Purpose**: Execute implementation following Test-First (Red-Green-Blue) cycle.

### Activities

- **Red**: Write failing tests based on requirements
- **Green**: Write minimal code to pass tests
- **Blue**: Refactor with confidence
- Implement library-first architecture
- Add CLI interfaces
- Maintain traceability (code comments with REQ-XXX-NNN)

### Implementation Flow

1. **Write Test (Red)**:
   ```python
   # Test file: tests/unit/{feature}/test_service.py
   def test_requirement_REQ_AUTH_001():
       """Test REQ-AUTH-001: User login with email and password"""
       # Test implementation
       assert False  # Initially fails
   ```

2. **Write Code (Green)**:
   ```python
   # Implementation: lib/{feature}/service.py
   def login(email, password):
       """Implements REQ-AUTH-001"""
       # Minimal implementation to pass test
       pass
   ```

3. **Refactor (Blue)**:
   ```python
   # Refactor with confidence (tests passing)
   def login(email, password):
       """Implements REQ-AUTH-001: User login with email and password"""
       # Improved implementation
       user = repository.find_by_email(email)
       if user and verify_password(password, user.password_hash):
           return create_session(user)
       raise AuthenticationError()
   ```

### Inputs

- Tasks document (`{feature}-tasks.md`)
- Design document (`{feature}-design.md`)
- Steering context (structure.md, tech.md)

### Outputs

- Source code in `lib/{feature}/` (library)
- CLI interface in `lib/{feature}/cli.py`
- Tests in `tests/{feature}/`
- Updated task status

### Commands

```bash
# Execute implementation for a feature
#sdd-implement <feature>
```

### Validation

- Tests written BEFORE implementation (Article III)
- All code has corresponding tests
- Test coverage ≥ 80%
- Library-first architecture (Article I)
- CLI interface provided (Article II)
- Traceability comments (REQ-XXX-NNN in code)

**Enforcement**: Articles I, II, III, V

---

## Stage 4: Testing (Validation)

**Purpose**: Validate implementation with comprehensive testing.

### Activities

- Run unit tests
- Run integration tests (with real services)
- Run E2E tests
- Measure test coverage
- Validate traceability (requirements → tests → code)

### Test Types

1. **Unit Tests**: Test individual functions/methods in isolation
2. **Integration Tests**: Test with real databases, caches, services (Article IX)
3. **E2E Tests**: Test complete user workflows

### Integration Testing (Article IX)

**CRITICAL**: Integration tests MUST use real services, not mocks.

```yaml
# docker-compose.test.yml
services:
  test-db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: test
      POSTGRES_DB: test

  test-redis:
    image: redis:7-alpine
```

**Mocks allowed only when**:
- External service unavailable in test environment
- External service has usage limits/costs
- External service has no test environment

### Inputs

- Implementation code
- Test suites
- Requirements and design documents

### Outputs

- Test reports (coverage, pass/fail)
- Traceability report (requirements → tests → code)
- Bug reports (if tests fail)

### Commands

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=lib --cov-report=html

# Integration tests
pytest tests/integration --docker
```

### Validation

- Test coverage ≥ 80% (Article III)
- All requirements have corresponding tests (Article V)
- Integration tests use real services (Article IX)
- All tests pass

**Enforcement**: Articles III, V, IX

---

## Stage 5: Validation (Constitutional)

**Purpose**: Validate compliance with all 9 Constitutional Articles.

### Activities

- Run `constitution-enforcer` validation
- Check traceability (requirements → design → code → tests)
- Validate Library-First architecture
- Validate CLI interfaces
- Check Phase -1 Gates (if triggered)

### Constitutional Validation

| Article | Validation                              | Tool                      |
| ------- | --------------------------------------- | ------------------------- |
| I       | Library-First architecture              | `constitution-enforcer`   |
| II      | CLI interface provided                  | `constitution-enforcer`   |
| III     | Test-First (Red-Green-Blue)             | Git history, coverage     |
| IV      | EARS format requirements                | `constitution-enforcer`   |
| V       | 100% traceability                       | `traceability-auditor`    |
| VI      | Steering files referenced               | Manual review             |
| VII     | ≤3 projects (Simplicity Gate)           | `constitution-enforcer`   |
| VIII    | No abstraction layers (Anti-Abstraction)| `constitution-enforcer`   |
| IX      | Real services in integration tests      | Test inspection           |

### Commands

```bash
# Validate constitutional compliance
#sdd-validate <feature>
```

### Outputs

- `storage/specs/{feature}-validation-report.md` - Compliance report
- Pass/fail status for each article
- Recommendations for fixes (if violations found)

### Validation

- All 9 Constitutional Articles validated
- Traceability matrix complete
- Phase -1 Gates passed (if applicable)

**Phase -1 Gates** (must pass before deployment):
- Simplicity Gate: Project count ≤ 3 OR approved justification
- Anti-Abstraction Gate: No custom wrappers OR approved justification

**Enforcement**: All Constitutional Articles

---

## Stage 6: Deployment

**Purpose**: Deploy validated feature to target environment.

### Activities

- Build deployable artifacts
- Run deployment scripts
- Update documentation
- Tag release in Git
- Monitor deployment

### Deployment Checklist

- [ ] All tests passing
- [ ] Constitutional validation passed
- [ ] Code review completed
- [ ] Documentation updated
- [ ] Release notes created
- [ ] Git tag created (e.g., `v1.2.0`)

### Inputs

- Validated implementation
- Validation report
- Deployment configuration

### Outputs

- Deployed feature
- Git release tag
- Updated documentation
- Release notes

### Commands

```bash
# Deploy to production
git tag v1.2.0
git push origin v1.2.0
```

### Validation

- Deployment successful
- Smoke tests passing in production
- Monitoring active

---

## Brownfield Workflow (Change Management)

For changes to existing features, use **delta specifications**:

### Change Workflow

1. **Identify Change**: Document change request in `storage/changes/`
2. **Requirements Delta**: Write EARS requirements for changes
3. **Design Delta**: Update design with changes (ADR for major decisions)
4. **Tasks Delta**: Break down change tasks
5. **Implementation**: Follow Test-First cycle
6. **Testing**: Validate changes + regression tests
7. **Validation**: Constitutional compliance
8. **Deployment**: Deploy changes

### Delta Specification Structure

```markdown
# Change: {change-id}

## Original Feature
- Feature: {feature-name}
- Version: {version}

## Change Request
- Description: [What needs to change]
- Rationale: [Why]

## Requirements Delta (EARS)
- REQ-XXX-NNN: [New/modified requirements]

## Design Delta
- [C4 diagram updates]
- [ADR for decisions]

## Tasks
- TASK-XXX-NNN: [Implementation tasks]

## Validation
- [Constitutional compliance]
- [Regression tests]
```

---

## Summary

### SDD Command Reference

| Command                      | Purpose                             | Output                          |
| ---------------------------- | ----------------------------------- | ------------------------------- |
| `#sdd-steering`              | Generate/update project memory      | `steering/*.md`                 |
| `#sdd-requirements <feature>`| Create EARS requirements            | `storage/specs/{feature}-requirements.md` |
| `#sdd-design <feature>`      | Generate C4 + ADR design            | `storage/specs/{feature}-design.md` |
| `#sdd-tasks <feature>`       | Break down into tasks               | `storage/specs/{feature}-tasks.md` |
| `#sdd-implement <feature>`   | Execute implementation              | Source code, tests              |
| `#sdd-validate <feature>`    | Validate constitutional compliance  | `storage/specs/{feature}-validation-report.md` |

### Constitutional Checkpoints

| Stage       | Articles Validated   | Phase -1 Gates           |
| ----------- | -------------------- | ------------------------ |
| Requirements| IV, V                | EARS compliance          |
| Design      | I, II, VI, VII, VIII | Simplicity, Anti-Abstraction |
| Implementation | III, V            | -                        |
| Testing     | III, V, IX           | -                        |
| Validation  | All (I-IX)           | All gates must pass      |

---

**Powered by MUSUBI** - Constitutional governance for specification-driven development.

**Last Updated**: 2025-11-23  
**Maintained By**: Project Team
