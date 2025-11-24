# Requirements: Interactive Prompt Platform

**Feature**: Ouranos Interactive Platform v2.0  
**Status**: Stage 0 - Requirements Definition  
**Date**: 2025-11-23  
**Format**: EARS (Easy Approach to Requirements Syntax)

---

## Overview

Transform Ouranos Agentic Library from a static prompt template collection into an interactive, self-hosted AI prompt platform inspired by Google's NotebookLM. The system enables users to browse specialized prompts across 11 professional domains, engage in multi-stage dialogues with AI agents, and generate custom meta-prompts.

---

## Functional Requirements

### FR-001: Prompt Library Management

#### REQ-PROMPT-001
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** load prompt templates from the `prompts/` directory structure.

**Acceptance Criteria**:
- Read Markdown files with YAML front matter
- Parse metadata (id, category, frameworks, dialogue_stages, tags, version)
- Support multi-language prompts (en/, ja/, copilot/)
- Handle 54+ prompt templates across 11 categories

#### REQ-PROMPT-002
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** store prompt metadata in SurrealDB.

**Acceptance Criteria**:
- Store prompts collection with id, title, category, language, frameworks, dialogue_stages, content, created_at, updated_at
- Support full-text search on title and content
- Maintain referential integrity between prompts and categories

#### REQ-PROMPT-003
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** provide REST API endpoints for prompt CRUD operations.

**Acceptance Criteria**:
- `GET /api/prompts` - List all prompts with pagination
- `GET /api/prompts/{id}` - Get single prompt by ID
- `GET /api/prompts/{id}/content` - Get full markdown content
- `POST /api/prompts/search` - Search prompts (full-text)
- Response time < 200ms for list operations
- Response time < 100ms for single prompt retrieval

#### REQ-PROMPT-004
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** display prompts in a browsable UI.

**Acceptance Criteria**:
- Grid/list view of prompts with PromptCard components
- Display title, category badge, framework tags, description preview
- "Try Now" button to start dialogue
- Responsive design (mobile + desktop)
- Load time < 2 seconds for prompt list page

---

### FR-002: Category Management

#### REQ-CAT-001
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** organize prompts into 11 categories.

**Acceptance Criteria**:
- Categories: general, business-management, design-development, hr-organization, education, research, document-creation, social-policy, communication, innovation-transformation, specialized-domains
- Each category stored in `categories` collection
- Category has slug, name (multi-language), description (multi-language)

#### REQ-CAT-002
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** provide REST API endpoints for category operations.

**Acceptance Criteria**:
- `GET /api/categories` - List all categories
- `GET /api/categories/{slug}` - Get category details
- `GET /api/categories/{slug}/prompts` - Get prompts in category
- Response includes prompt count per category

#### REQ-CAT-003
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** display categories in the UI.

**Acceptance Criteria**:
- Category grid on home page (11 categories)
- Category detail page with description and prompt list
- Category filter in prompt list page
- Visual distinction between categories (colors/icons)

---

### FR-003: Dialogue Session Management

#### REQ-DIALOGUE-001
**Type**: Event-Driven  
**Priority**: P0 (Critical)

**When** a user clicks "Start Dialogue" on a prompt, the system **shall** create a new chat session.

**Acceptance Criteria**:
- `POST /api/chat/sessions` endpoint
- Session stored in `sessions` collection with id, prompt_id, current_stage, created_at, updated_at
- Session ID returned to client
- Redirect to `/chat/{sessionId}`

#### REQ-DIALOGUE-002
**Type**: State-Driven  
**Priority**: P0 (Critical)

**While** a dialogue session is active, the system **shall** track the current stage (1 through 4-5).

**Acceptance Criteria**:
- current_stage field in sessions collection
- Increment stage after each user response
- Display stage progress indicator in UI (e.g., "Stage 2/5")
- Prevent skipping stages

#### REQ-DIALOGUE-003
**Type**: Event-Driven  
**Priority**: P0 (Critical)

**When** a user sends a message in a session, the system **shall** invoke the AI agent with the prompt template.

**Acceptance Criteria**:
- `POST /api/chat/sessions/{id}/messages` endpoint
- Store message in `messages` collection with id, session_id, role (user/assistant), content, stage, created_at
- Invoke AI provider (OpenAI, Anthropic, etc.) with dialogue context
- Stream response to client in real-time
- Response time < 5 seconds for AI invocation

#### REQ-DIALOGUE-004
**Type**: Event-Driven  
**Priority**: P0 (Critical)

**When** a dialogue session reaches the final stage, the system **shall** generate a meta-prompt.

**Acceptance Criteria**:
- Combine all user responses from stages 1-5
- Apply prompt template's meta-prompt generation rules
- Display final meta-prompt in right panel of chat UI
- Allow user to copy meta-prompt to clipboard

#### REQ-DIALOGUE-005
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** provide REST API endpoints for session management.

**Acceptance Criteria**:
- `GET /api/chat/sessions/{id}` - Get session details
- `GET /api/chat/sessions/{id}/messages` - Get message history
- `DELETE /api/chat/sessions/{id}` - Delete session
- Support pagination for message history

---

### FR-004: AI Agent Integration

#### REQ-AGENT-001
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** support multiple AI providers.

**Acceptance Criteria**:
- OpenAI (GPT-4, GPT-3.5-turbo)
- Anthropic (Claude 3.5 Sonnet, Claude 3 Opus)
- Ollama (local models)
- Provider abstraction layer (inspired by Esperanto from open-notebook)
- API keys configured via environment variables

#### REQ-AGENT-002
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** invoke AI agents with dialogue context.

**Acceptance Criteria**:
- Pass prompt template content to AI
- Include conversation history (previous messages)
- Include current stage number
- Request stage-specific questions from AI
- Handle streaming responses

#### REQ-AGENT-003
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** provide REST API endpoints for agent operations.

**Acceptance Criteria**:
- `POST /api/agents/{promptId}/invoke` - Invoke agent (non-streaming)
- `POST /api/agents/{promptId}/stream` - Stream agent responses
- `GET /api/agents/{promptId}/stages` - Get dialogue stages
- Error handling for API rate limits and failures

---

### FR-005: Search and Discovery

#### REQ-SEARCH-001
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** provide full-text search across prompts.

**Acceptance Criteria**:
- Search title, description, frameworks, tags
- Case-insensitive search
- Return ranked results
- Response time < 500ms
- Minimum 3 characters required for search

#### REQ-SEARCH-002
**Type**: Optional  
**Priority**: P2 (Medium)

**If** vector embeddings are generated, the system **shall** provide semantic search.

**Acceptance Criteria**:
- Generate embeddings for prompt content
- Store embeddings in `prompts.embedding` field
- Vector similarity search using SurrealDB
- Combine full-text and vector search results
- Response time < 1 second

#### REQ-SEARCH-003
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** provide search UI with filters.

**Acceptance Criteria**:
- Search bar in header (global search)
- Category filter dropdown
- Language filter (en/ja/copilot)
- Framework tags filter
- Real-time search results (debounced)

---

### FR-006: User Interface

#### REQ-UI-001
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** provide a home page.

**Acceptance Criteria**:
- Welcome message and project overview
- Featured prompts section (4-6 prompts)
- Category grid (11 categories with icons)
- Global search bar
- Navigation to /prompts, /categories, /about
- Load time < 2 seconds

#### REQ-UI-002
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** provide a prompt library page (`/prompts`).

**Acceptance Criteria**:
- List/grid view toggle
- Filter by category, language, frameworks
- Sort by name, date, popularity
- Pagination (20 prompts per page)
- Search bar
- Load time < 2 seconds

#### REQ-UI-003
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** provide a prompt detail page (`/prompts/[id]`).

**Acceptance Criteria**:
- Display full prompt content (rendered Markdown)
- Metadata: category, frameworks, tags, version, dates
- "Start Dialogue" button (primary CTA)
- Related prompts section (same category)
- Breadcrumb navigation

#### REQ-UI-004
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** provide a chat interface page (`/chat/[sessionId]`).

**Acceptance Criteria**:
- Three-column layout:
  - Left panel: Stage progress indicator (visual, e.g., 1/5, 2/5, ...)
  - Center panel: Chat messages (user + assistant)
  - Right panel: Generated meta-prompt (final output)
- Message input box with send button
- Auto-scroll to latest message
- Loading indicator during AI response
- Mobile-responsive (stack columns vertically)

#### REQ-UI-005
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** provide a category view page (`/categories/[slug]`).

**Acceptance Criteria**:
- Category title and description
- List of prompts in category (grid view)
- Related categories section
- Breadcrumb navigation

#### REQ-UI-006
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** support multi-language UI.

**Acceptance Criteria**:
- Language selector in header (EN | JA)
- i18n for all UI strings
- Persist language preference in localStorage
- Default to browser language

#### REQ-UI-007
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** use responsive design.

**Acceptance Criteria**:
- Mobile breakpoint: < 768px
- Tablet breakpoint: 768px - 1024px
- Desktop breakpoint: > 1024px
- Touch-friendly buttons and inputs on mobile
- Readable font sizes on all devices

---

### FR-007: Data Import and Validation

#### REQ-IMPORT-001
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** provide a script to import prompts from markdown to SurrealDB.

**Acceptance Criteria**:
- `scripts/import_prompts.py` script
- Read all markdown files in `prompts/en/`, `prompts/ja/`, `prompts/copilot/`
- Parse YAML front matter and content
- Insert into `prompts` collection
- Idempotent (can run multiple times)
- Log import results (success/failures)

#### REQ-IMPORT-002
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** provide a script to validate prompt structure.

**Acceptance Criteria**:
- `scripts/validate_prompts.py` script
- Validate YAML front matter (required fields: id, category, frameworks, dialogue_stages)
- Validate markdown structure (headings, sections)
- Check for broken links
- Report validation errors with file paths

#### REQ-IMPORT-003
**Type**: Optional  
**Priority**: P2 (Medium)

**If** embedding service is enabled, the system **shall** provide a script to generate embeddings.

**Acceptance Criteria**:
- `scripts/generate_embeddings.py` script
- Generate embeddings for prompt content using OpenAI embeddings API
- Store in `prompts.embedding` field
- Progress bar for batch processing
- Handle API rate limits

---

## Non-Functional Requirements

### NFR-001: Performance

#### REQ-PERF-001
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** respond to API requests within acceptable time limits.

**Acceptance Criteria**:
- GET /api/prompts: < 200ms (p95)
- GET /api/prompts/{id}: < 100ms (p95)
- POST /api/chat/sessions/{id}/messages: < 5s (p95, including AI response)
- POST /api/prompts/search: < 500ms (p95)

#### REQ-PERF-002
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** load frontend pages within acceptable time limits.

**Acceptance Criteria**:
- Home page: < 2s (First Contentful Paint)
- Prompt list page: < 2s (First Contentful Paint)
- Prompt detail page: < 1.5s (First Contentful Paint)
- Chat page: < 1.5s (First Contentful Paint)
- Measured on standard broadband connection (10 Mbps)

#### REQ-PERF-003
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** support concurrent users.

**Acceptance Criteria**:
- Minimum 10 concurrent chat sessions
- No performance degradation with < 100 prompts in database
- Database query optimization (indexes on id, category, language)

---

### NFR-002: Security

#### REQ-SEC-001
**Type**: Optional  
**Priority**: P2 (Medium)

**If** authentication is enabled, the system **shall** protect API endpoints.

**Acceptance Criteria**:
- Password protection for entire application (like open-notebook)
- JWT tokens for API access
- Session expiry (24 hours)
- Secure password storage (bcrypt)

#### REQ-SEC-002
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** validate all user inputs.

**Acceptance Criteria**:
- Sanitize markdown content before rendering
- Validate API request payloads (Pydantic models)
- Prevent SQL injection (SurrealDB parameterized queries)
- Prevent XSS attacks (React automatic escaping)

#### REQ-SEC-003
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** store API keys securely.

**Acceptance Criteria**:
- AI provider API keys in environment variables
- No API keys in source code or logs
- .env.example file with placeholder values
- Docker secrets support (production)

---

### NFR-003: Deployment

#### REQ-DEPLOY-001
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** support Docker deployment.

**Acceptance Criteria**:
- `docker-compose.yml` for development environment
- `docker-compose.prod.yml` for production environment
- Single-container option (`Dockerfile.single`)
- Multi-container option (separate frontend, api, database)
- Services: frontend (port 3000), api (port 8000), surrealdb (port 8001)

#### REQ-DEPLOY-002
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** provide environment configuration.

**Acceptance Criteria**:
- `.env.example` file with all required variables
- Environment variables: SURREAL_URL, OPENAI_API_KEY, ANTHROPIC_API_KEY, OLLAMA_URL, APP_PASSWORD (optional)
- Validation at startup (missing required vars → error)

#### REQ-DEPLOY-003
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** support zero-downtime deployments.

**Acceptance Criteria**:
- Health check endpoints: GET /api/health, GET /health
- Database migrations run before deployment
- Graceful shutdown (finish in-flight requests)

---

### NFR-004: Data Privacy

#### REQ-PRIVACY-001
**Type**: Ubiquitous  
**Priority**: P0 (Critical)

The system **shall** store all data locally.

**Acceptance Criteria**:
- SurrealDB data directory in Docker volume
- No telemetry or analytics to external services
- No third-party tracking scripts
- Privacy-first architecture (inspired by open-notebook)

#### REQ-PRIVACY-002
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** not log sensitive information.

**Acceptance Criteria**:
- No API keys in logs
- No user messages in error logs (log session ID only)
- Configurable log levels (DEBUG, INFO, WARNING, ERROR)

---

### NFR-005: Maintainability

#### REQ-MAINT-001
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** follow MUSUBI Constitutional Articles.

**Acceptance Criteria**:
- Article I: Prompts are independent libraries (Git-versioned markdown)
- Article II: CLI interface for prompt management (future)
- Article III: Test coverage > 70% for API and frontend
- Article VII: Maximum 3 deployment units (frontend, api, database)
- Article VIII: Use FastAPI, Next.js directly (no abstraction layers)

#### REQ-MAINT-002
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** provide comprehensive documentation.

**Acceptance Criteria**:
- README.md with installation and quick start
- ARCHITECTURE.md with system design
- API documentation (OpenAPI spec)
- User guide (browsing prompts, using agents)
- Developer guide (contributing, architecture)

#### REQ-MAINT-003
**Type**: Ubiquitous  
**Priority**: P1 (High)

The system **shall** use consistent coding standards.

**Acceptance Criteria**:
- Python: Black formatter, isort, mypy type checking
- TypeScript: ESLint, Prettier, strict mode
- Git commit messages: Conventional Commits format
- Pre-commit hooks for linting and formatting

---

## Acceptance Criteria Summary

### MVP (Phase 1) - Must Have

| Requirement | Priority | Status |
|------------|----------|--------|
| REQ-PROMPT-001 to REQ-PROMPT-004 | P0 | Planned |
| REQ-CAT-001 to REQ-CAT-003 | P0-P1 | Planned |
| REQ-DIALOGUE-001 to REQ-DIALOGUE-005 | P0-P1 | Planned |
| REQ-AGENT-001 to REQ-AGENT-003 | P0-P1 | Planned |
| REQ-SEARCH-001, REQ-SEARCH-003 | P1 | Planned |
| REQ-UI-001 to REQ-UI-007 | P0-P1 | Planned |
| REQ-IMPORT-001, REQ-IMPORT-002 | P0-P1 | Planned |
| REQ-PERF-001 to REQ-PERF-003 | P0-P1 | Planned |
| REQ-SEC-002, REQ-SEC-003 | P1 | Planned |
| REQ-DEPLOY-001 to REQ-DEPLOY-003 | P0-P1 | Planned |
| REQ-PRIVACY-001, REQ-PRIVACY-002 | P0-P1 | Planned |
| REQ-MAINT-001 to REQ-MAINT-003 | P1 | Planned |

### Phase 2 - Nice to Have

| Requirement | Priority | Status |
|------------|----------|--------|
| REQ-SEARCH-002 (Vector search) | P2 | Future |
| REQ-IMPORT-003 (Embeddings) | P2 | Future |
| REQ-SEC-001 (Authentication) | P2 | Future |

---

## Traceability

This requirements document will be traced to:

1. **Design**: C4 diagrams + ADRs (Stage 1)
2. **Tasks**: Implementation tasks (Stage 2)
3. **Code**: Source code references (Stage 3)
4. **Tests**: Test cases (Stage 4)
5. **Validation**: Validation report (Stage 5)

---

## Constitutional Compliance

| Article | Compliance | Evidence |
|---------|------------|----------|
| **I: Library-First** | ✅ | Prompts are independent markdown libraries (REQ-PROMPT-001) |
| **II: CLI Interface** | 🔄 | Future: CLI for prompt management |
| **III: Test-First** | ✅ | Test coverage requirements (REQ-MAINT-001) |
| **IV: EARS Format** | ✅ | All requirements in EARS format |
| **V: Traceability** | ✅ | Traceability section links REQ → Design → Code → Tests |
| **VI: Project Memory** | ✅ | Steering files maintained (steering/) |
| **VII: Simplicity** | ✅ | 3 deployment units (REQ-DEPLOY-001) |
| **VIII: Anti-Abstraction** | ✅ | Use FastAPI, Next.js directly (REQ-MAINT-001) |
| **IX: Integration Testing** | ✅ | Real SurrealDB in tests (REQ-MAINT-001) |

---

## Next Steps

1. **Stage 1: Design** - Create C4 diagrams and ADRs
2. **Stage 2: Tasks** - Break down into implementation tasks
3. **Stage 3: Implementation** - Start coding
4. **Stage 4: Testing** - Write tests (TDD)
5. **Stage 5: Validation** - Validate against constitutional articles

---

**Last Updated**: 2025-11-23  
**Status**: Stage 0 Complete - Ready for Design Phase
