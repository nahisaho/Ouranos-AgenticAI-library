# Project Structure

**Project**: Ouranos-AgenticAI-library
**Last Updated**: 2025-11-21
**Version**: 1.0

---

## Architecture Pattern

**Primary Pattern**: Documentation-First Library Architecture

> This project uses a documentation-first approach for organizing prompt template libraries.
> The architecture focuses on structured markdown-based templates with YAML metadata management,
> supporting multi-language versions and optimized variants for different platforms.

---

## Directory Organization

### Root Structure

```
Ouranos-AgenticAI-library/
├── en/                   # English version (complete)
│   ├── prompts/          # 44 English prompt templates
│   ├── docs/             # English documentation
│   └── manifest.yml      # English version metadata
├── ja/                   # Japanese version (in progress)
│   ├── prompts/          # Japanese prompt templates
│   ├── docs/             # Japanese documentation
│   └── manifest.yml      # Japanese version metadata
├── copilot/              # Microsoft Copilot optimized version (planned)
│   ├── prompts/          # ≤8000 char optimized templates
│   ├── docs/             # Copilot-specific documentation
│   └── manifest.yml      # Copilot version metadata
├── docs/                 # Shared documentation
│   ├── language-guide.md # Multi-language support guide
│   └── translation-guide.md # Translation guidelines
├── steering/             # Project memory (this directory)
│   ├── structure.md      # This file
│   ├── tech.md           # Technology stack
│   ├── product.md        # Product context
│   └── rules/            # Constitutional governance
├── storage/              # SDD artifacts
│   ├── changes/          # Delta specifications
│   ├── features/         # Feature tracking
│   └── specs/            # Requirements, design, tasks
├── templates/            # Template structures
├── References/           # Reference materials
├── manifest.yml          # Root project metadata
├── REQUIREMENTS.md       # Requirements document
├── AGENTS.md             # MUSUBI SDD information
└── README.md             # Main project documentation
```

---

## Template Library Pattern

This project uses a template library pattern focused on prompt templates.

### Template Structure

Each prompt template follows this structure:

```
{category}/{template-name}.md
---
id: unique-identifier
category: category-name
frameworks:
  - Framework 1
  - Framework 2
dialogue_stages: N
version: 1.0.0
tags:
  - tag1
  - tag2
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Template Title

## 役割
[Role definition]

## 対話フロー
[Dialogue flow stages]

## 活用する専門知識・フレームワーク
[Frameworks and knowledge]

## 出力形式
[Output format]

## 使用例
[Usage examples]
```

### Template Guidelines

- **Consistency**: All templates follow identical YAML frontmatter structure
- **Multi-language**: Templates exist in multiple language versions (en, ja, copilot)
- **Metadata**: YAML frontmatter provides comprehensive metadata
- **Versioning**: Each template has version control

---

## Multi-Language Structure

### Language Version Organization

```
{lang}/
├── README.md             # Language-specific README
├── manifest.yml          # Language version metadata
├── prompts/              # Prompt templates
│   ├── general/
│   ├── business-management/
│   ├── design-development/
│   ├── hr-organization/
│   ├── education/
│   ├── research/
│   ├── document-creation/
│   ├── social-policy/
│   ├── communication/
│   ├── innovation-transformation/
│   └── specialized-domains/
└── docs/                 # Language-specific documentation
    ├── usage-guide.md
    ├── contribution.md
    └── framework-reference.md
```

### Language Version Guidelines

- **Consistency**: All language versions follow identical directory structure
- **Completeness**: Each language version aims for full template coverage
- **Optimization**: Special versions (like copilot) may have character limits
- **Documentation**: Each version includes complete documentation in target language

---

## Category Organization

### Prompt Categories

```
prompts/
├── general/              # General purpose (1 template)
├── business-management/  # Business & Management (10 templates)
├── design-development/   # Design & Development (8 templates)
├── hr-organization/      # HR & Organization (5 templates)
├── education/            # Education (4 templates)
├── research/             # Research (3 templates)
├── document-creation/    # Document Creation (3 templates)
├── social-policy/        # Social & Policy (3 templates)
├── communication/        # Communication (3 templates)
├── innovation-transformation/ # Innovation & Transformation (3 templates)
└── specialized-domains/  # Specialized Domains (3 templates)
```

### Category Guidelines

- **Focused Scope**: Each category covers specific professional domain
- **Template Count**: Balanced distribution with higher priority for business/development
- **Naming**: Consistent kebab-case directory names
- **Coverage**: Categories cover wide range of professional domains

---

## Database Organization

### Schema Organization

```
prisma/
├── schema.prisma         # Prisma schema
├── migrations/           # Database migrations
│   ├── 001_create_users_table/
│   │   └── migration.sql
│   └── 002_create_sessions_table/
│       └── migration.sql
└── seed.ts               # Database seed data
```

### Database Guidelines

- **Migrations**: All schema changes via migrations
- **Naming**: snake_case for tables and columns
- **Indexes**: Index foreign keys and frequently queried columns

---

## Test Organization

### Test Structure

```
tests/
├── unit/                 # Unit tests (per library)
│   └── auth/
│       └── service.test.ts
├── integration/          # Integration tests (real services)
│   └── auth/
│       └── login.test.ts
├── e2e/                  # End-to-end tests
│   └── auth/
│       └── user-flow.test.ts
└── fixtures/             # Test data and fixtures
    └── users.ts
```

### Test Guidelines

- **Test-First**: Tests written BEFORE implementation (Article III)
- **Real Services**: Integration tests use real DB/cache (Article IX)
- **Coverage**: Minimum 80% coverage
- **Naming**: `*.test.ts` for unit, `*.integration.test.ts` for integration

---

## Documentation Organization

### Documentation Structure

```
docs/
├── architecture/         # Architecture documentation
│   ├── c4-diagrams/
│   └── adr/              # Architecture Decision Records
├── api/                  # API documentation
│   ├── openapi.yaml
│   └── graphql.schema
├── guides/               # Developer guides
│   ├── getting-started.md
│   └── contributing.md
└── runbooks/             # Operational runbooks
    ├── deployment.md
    └── troubleshooting.md
```

---

## SDD Artifacts Organization

### Storage Directory

```
storage/
├── specs/                # Specifications
│   ├── auth-requirements.md
│   ├── auth-design.md
│   ├── auth-tasks.md
│   └── payment-requirements.md
├── changes/              # Delta specifications (brownfield)
│   ├── add-2fa.md
│   └── upgrade-jwt.md
├── features/             # Feature tracking
│   ├── auth.json
│   └── payment.json
└── validation/           # Validation reports
    ├── auth-validation-report.md
    └── payment-validation-report.md
```

---

## Naming Conventions

### File Naming

- **TypeScript**: `PascalCase.tsx` for components, `camelCase.ts` for utilities
- **React Components**: `PascalCase.tsx` (e.g., `LoginForm.tsx`)
- **Utilities**: `camelCase.ts` (e.g., `formatDate.ts`)
- **Tests**: `*.test.ts` or `*.spec.ts`
- **Constants**: `SCREAMING_SNAKE_CASE.ts` (e.g., `API_ENDPOINTS.ts`)

### Directory Naming

- **Features**: `kebab-case` (e.g., `user-management/`)
- **Components**: `kebab-case` or `PascalCase` (consistent within project)

### Variable Naming

- **Variables**: `camelCase`
- **Constants**: `SCREAMING_SNAKE_CASE`
- **Types/Interfaces**: `PascalCase`
- **Enums**: `PascalCase`

---

## Integration Patterns

### Library → Application Integration

```typescript
// ✅ CORRECT: Application imports from library
import { AuthService } from '@/lib/auth';

const authService = new AuthService(repository);
const result = await authService.login(credentials);
```

```typescript
// ❌ WRONG: Library imports from application
// Libraries must NOT depend on application code
import { AuthContext } from '@/app/contexts/auth'; // Violation!
```

### Service → Repository Pattern

```typescript
// Service layer (business logic)
export class AuthService {
  constructor(private repository: UserRepository) {}

  async login(credentials: LoginRequest): Promise<LoginResponse> {
    // Business logic here
    const user = await this.repository.findByEmail(credentials.email);
    // ...
  }
}

// Repository layer (data access)
export class UserRepository {
  constructor(private prisma: PrismaClient) {}

  async findByEmail(email: string): Promise<User | null> {
    return this.prisma.user.findUnique({ where: { email } });
  }
}
```

---

## Deployment Structure

### Deployment Units

**Projects** (independently deployable):

1. Ouranos-AgenticAI-library - Main application

> ⚠️ **Simplicity Gate (Article VII)**: Maximum 3 projects initially.
> If adding more projects, document justification in Phase -1 Gate approval.

### Environment Structure

```
environments/
├── development/
│   └── .env.development
├── staging/
│   └── .env.staging
└── production/
    └── .env.production
```

---

## Multi-Language Support

### Language Policy

- **Primary Language**: English
- **Documentation**: English first (`.md`), then Japanese (`.ja.md`)
- **Code Comments**: English
- **UI Strings**: i18n framework

### i18n Organization

```
locales/
├── en/
│   ├── common.json
│   └── auth.json
└── ja/
    ├── common.json
    └── auth.json
```

---

## Version Control

### Branch Organization

- `main` - Production branch
- `develop` - Development branch
- `feature/*` - Feature branches
- `hotfix/*` - Hotfix branches
- `release/*` - Release branches

### Commit Message Convention

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Example**:

```
feat(auth): implement user login (REQ-AUTH-001)

Add login functionality with email and password authentication.
Session created with 24-hour expiry.

Closes REQ-AUTH-001
```

---

## Constitutional Compliance

This structure enforces:

- **Article I**: Library-first pattern in `lib/`
- **Article II**: CLI interfaces per library
- **Article III**: Test structure supports Test-First
- **Article VI**: Steering files maintain project memory

---

## Changelog

### Version 1.1 (Planned)

- [Future changes]

---

**Last Updated**: 2025-11-21
**Maintained By**: {{MAINTAINER}}
