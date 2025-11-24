# Project Structure

**Project**: Ouranos-AgenticAI-library
**Last Updated**: 2025-11-24
**Version**: 2.0

---

## Architecture Pattern

**Primary Pattern**: Monorepo with Library-First + Interactive Platform

> Ouranos Agentic Library is evolving from a static markdown prompt library (v1.0) into an interactive AI platform (v2.0). The architecture maintains the core prompt templates as git-versioned markdown files while adding FastAPI backend and Next.js frontend for interactive dialogue sessions.

---

## Directory Organization

### Root Structure (v2.0)

```
Ouranos-AgenticAI-library/
├── prompts/              # Prompt Template Library (v1.0 - CORE ASSET)
│   ├── en/               # English prompts (78 completed)
│   ├── ja/               # Japanese prompts (1 completed, 77 planned)
│   ├── copilot/          # Copilot optimized (0 completed, 78 planned)
│   └── manifest.yml      # Centralized metadata
│
├── api/                  # FastAPI Backend (v2.0 - IN DEVELOPMENT)
│   ├── main.py
│   ├── config.py
│   ├── routers/
│   ├── services/
│   ├── domain/
│   └── database/
│
├── frontend/             # Next.js Frontend (v2.0 - IN DEVELOPMENT)
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   └── lib/
│   ├── package.json
│   └── next.config.ts
│
├── database/             # Database setup
│   ├── migrations/
│   └── seeds/
│
├── docs/                 # Documentation
│   ├── getting-started/
│   └── language-guide.md
│
├── steering/             # MUSUBI Project Memory
│   ├── product.md
│   ├── tech.md
│   ├── structure.md      # This file
│   └── rules/
│       ├── constitution.md
│       ├── workflow.md
│       └── ears-format.md
│
├── storage/              # SDD Artifacts
│   ├── specs/
│   ├── changes/
│   └── features/
│
├── docker/               # Docker configuration
│   ├── Dockerfile.api
│   └── Dockerfile.frontend
│
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
├── LICENSE               # CC BY-NC 4.0
├── README.md
├── ARCHITECTURE.md
├── REQUIREMENTS.md
└── MANIFEST.md
```

---

## Library-First Pattern (Article I)

**Core Asset**: Prompt templates in `prompts/` directory

### Prompt Template Structure

Each prompt follows this markdown structure:

```
prompts/en/prompts/{category}/{prompt-id}.md
```

**Example**:
```markdown
---
id: business-strategy-consultant
category: business-management
frameworks:
  - SWOT Analysis
  - Porter's Five Forces
  - Blue Ocean Strategy
dialogue_stages: 5
version: 1.0.0
---

# Business Strategy Consultant

## Stage 1: Context Assessment
[Dialogue content...]

## Stage 2: Strategic Framework
[Dialogue content...]

...
```

### Library Guidelines

- **Independence**: Prompts are version-controlled markdown files
- **Metadata**: YAML front matter for structured data
- **Categories**: 11 categories (general, business-management, design-development, etc.)
- **Languages**: Multi-language support (en, ja, copilot)

---

## Application Structure (v2.0 - Planned)

### API Structure (`api/`)

```
api/
├── main.py               # FastAPI app entry point
├── config.py             # Configuration management
├── routers/              # API route handlers
│   ├── prompts.py        # Prompt CRUD operations
│   ├── categories.py     # Category management
│   ├── chat.py           # Chat/dialogue sessions
│   └── search.py         # Search across prompts
├── services/             # Business logic
│   ├── prompt_service.py
│   ├── chat_service.py
│   └── agent_service.py
├── domain/               # Core domain models
│   ├── prompt.py
│   └── dialogue.py
└── database/             # Database layer
    └── repositories/
```

### Frontend Structure (`frontend/`)

```
frontend/src/
├── app/                  # Next.js 14+ App Router
│   ├── page.tsx          # Home page
│   ├── prompts/          # Prompt browsing
│   ├── categories/       # Category browsing
│   └── chat/             # Chat interface
├── components/           # React components
│   ├── ui/               # Base UI (shadcn/ui)
│   ├── prompts/          # Prompt-specific
│   └── chat/             # Chat components
└── lib/                  # Frontend utilities
    └── api.ts            # API client
```

---

## Naming Conventions

### File Naming

- **Python**: `snake_case.py`
- **TypeScript**: `PascalCase.tsx` for components, `camelCase.ts` for utilities
- **Markdown**: `kebab-case.md`
- **Tests**: `test_*.py` (Python), `*.test.tsx` (TypeScript)

### Directory Naming

- **Features**: `kebab-case/`
- **Components**: `PascalCase/` or `kebab-case/` (consistent within project)

---

## Constitutional Compliance

This structure enforces:

- **Article I (Library-First)**: Prompts are independent markdown libraries
- **Article II (CLI Interface)**: Future: CLI for prompt management
- **Article III (Test-First)**: Test structure supports Test-First
- **Article VI (Project Memory)**: Steering files maintain project context
- **Article VII (Simplicity)**: 3 main components (Prompts, API, Frontend)

---

## Version Control

### Branch Organization

- `main` - Production branch (current: v1.0 static library)
- `develop` - Development branch (future: v2.0 interactive platform)
- `feature/*` - Feature branches
- `hotfix/*` - Hotfix branches

### Commit Message Convention

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Example**:

```
feat(prompts): add AI/ML Strategy Consultant prompt

Add new Tier 1 CRITICAL prompt for AI/ML strategy consulting.
Includes 8 frameworks: AI/ML Lifecycle, Responsible AI, etc.

Closes REQ-MECE-001
```

---

**Last Updated**: 2025-11-24
**Maintained By**: Project Team

See ARCHITECTURE.md for detailed architecture design.
