# Ouranos Agentic Library - Architecture Design

**Version**: 2.0  
**Date**: 2025-11-23  
**Status**: Proposed

---

## 🎯 Vision

Transform Ouranos Agentic Library from a static prompt template collection into an **interactive, self-hosted AI prompt platform** inspired by Google's NotebookLM, enabling users to:

1. **Browse and discover** specialized prompts across 11 professional domains
2. **Interact with expert agents** through dialogue-based conversations
3. **Generate custom meta-prompts** tailored to specific needs
4. **Manage prompt libraries** for teams and projects
5. **Extend and customize** with new domains and frameworks

---

## 🏗️ New Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────┐
│  User Browser                                           │
│  Access: http://localhost:3000                          │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
         ┌───────────────┐
         │   Port 3000   │  ← Next.js Frontend (React UI)
         │   Frontend    │    Prompt browser, chat interface
         └───────┬───────┘
                 │ proxies /api/* requests ↓
                 ▼
         ┌───────────────┐
         │   Port 8000   │  ← FastAPI Backend (Python)
         │     API       │    Prompt processing, AI integration
         └───────┬───────┘
                 │
                 ▼
         ┌───────────────┐
         │   SurrealDB   │  ← Database (prompt metadata, sessions)
         │   (Port 8001) │
         └───────────────┘
                 │
                 ▼
         ┌───────────────┐
         │  Prompts DB   │  ← File-based prompt templates
         │  (Markdown)   │    Git-versioned content
         └───────────────┘
```

---

## 📂 Proposed Directory Structure

### Root Structure

```
ouranos-agentic-library/
├── api/                          # FastAPI Backend (Python)
│   ├── __init__.py
│   ├── main.py                   # FastAPI app entry point
│   ├── config.py                 # Configuration management
│   ├── models.py                 # Pydantic models
│   ├── auth.py                   # Optional authentication
│   ├── routers/                  # API route handlers
│   │   ├── __init__.py
│   │   ├── prompts.py            # Prompt CRUD operations
│   │   ├── categories.py         # Category management
│   │   ├── chat.py               # Chat/dialogue sessions
│   │   ├── agents.py             # AI agent interactions
│   │   └── search.py             # Search across prompts
│   ├── services/                 # Business logic
│   │   ├── __init__.py
│   │   ├── prompt_service.py     # Prompt loading, parsing
│   │   ├── chat_service.py       # Dialogue management
│   │   ├── agent_service.py      # AI agent orchestration
│   │   ├── embedding_service.py  # Vector embeddings
│   │   └── search_service.py     # Full-text + vector search
│   ├── domain/                   # Core domain models
│   │   ├── __init__.py
│   │   ├── prompt.py             # Prompt entity
│   │   ├── category.py           # Category entity
│   │   ├── dialogue.py           # Dialogue session
│   │   └── agent.py              # Agent entity
│   ├── database/                 # Database layer
│   │   ├── __init__.py
│   │   ├── client.py             # SurrealDB client
│   │   └── repositories/         # Data access objects
│   │       ├── prompt_repo.py
│   │       ├── session_repo.py
│   │       └── user_repo.py
│   └── utils/                    # Utilities
│       ├── __init__.py
│       ├── markdown_parser.py    # Parse YAML front matter
│       └── validators.py         # Input validation
│
├── frontend/                     # Next.js Frontend (React)
│   ├── src/
│   │   ├── app/                  # Next.js 14+ App Router
│   │   │   ├── layout.tsx        # Root layout
│   │   │   ├── page.tsx          # Home page
│   │   │   ├── prompts/          # Prompt browsing
│   │   │   │   ├── page.tsx      # Prompt list
│   │   │   │   └── [id]/         # Individual prompt
│   │   │   │       └── page.tsx
│   │   │   ├── categories/       # Category browsing
│   │   │   │   ├── page.tsx
│   │   │   │   └── [slug]/
│   │   │   │       └── page.tsx
│   │   │   ├── chat/             # Chat interface
│   │   │   │   ├── page.tsx
│   │   │   │   └── [sessionId]/
│   │   │   │       └── page.tsx
│   │   │   └── api/              # API proxy routes
│   │   │       └── [...path]/
│   │   │           └── route.ts
│   │   ├── components/           # React components
│   │   │   ├── ui/               # Base UI components (shadcn/ui)
│   │   │   │   ├── button.tsx
│   │   │   │   ├── card.tsx
│   │   │   │   ├── input.tsx
│   │   │   │   └── dialog.tsx
│   │   │   ├── prompts/          # Prompt-specific components
│   │   │   │   ├── PromptCard.tsx
│   │   │   │   ├── PromptDetail.tsx
│   │   │   │   └── PromptList.tsx
│   │   │   ├── chat/             # Chat components
│   │   │   │   ├── ChatInterface.tsx
│   │   │   │   ├── MessageList.tsx
│   │   │   │   └── DialogueStage.tsx
│   │   │   └── layout/           # Layout components
│   │   │       ├── Header.tsx
│   │   │       ├── Sidebar.tsx
│   │   │       └── Footer.tsx
│   │   └── lib/                  # Frontend utilities
│   │       ├── api.ts            # API client
│   │       ├── hooks/            # React hooks
│   │       │   ├── usePrompts.ts
│   │       │   └── useChat.ts
│   │       └── utils.ts          # Utility functions
│   ├── public/                   # Static assets
│   ├── package.json
│   ├── next.config.ts
│   ├── tsconfig.json
│   └── tailwind.config.ts
│
├── prompts/                      # Prompt Template Database
│   ├── en/                       # English prompts
│   │   ├── general/
│   │   │   └── meta-prompt-generator.md
│   │   ├── business-management/
│   │   │   ├── business-strategy-consultant.md
│   │   │   └── [14 more...]
│   │   ├── design-development/
│   │   │   └── [16 prompts...]
│   │   └── [9 more categories...]
│   ├── ja/                       # Japanese prompts
│   │   └── [same structure...]
│   ├── copilot/                  # Copilot optimized
│   │   └── [same structure...]
│   └── manifest.yml              # Central manifest
│
├── docs/                         # Documentation
│   ├── getting-started/
│   │   ├── installation.md
│   │   └── quick-start.md
│   ├── user-guide/
│   │   ├── browsing-prompts.md
│   │   ├── using-agents.md
│   │   └── creating-custom-prompts.md
│   ├── api-reference/
│   │   └── openapi.yaml
│   └── development/
│       ├── contributing.md
│       └── architecture.md
│
├── database/                     # Database setup
│   ├── migrations/               # Schema migrations
│   │   └── 001_initial.surql
│   └── seeds/                    # Seed data
│       └── categories.json
│
├── scripts/                      # Utility scripts
│   ├── import_prompts.py         # Import markdown to DB
│   ├── validate_prompts.py       # Validate prompt structure
│   └── generate_embeddings.py   # Generate vector embeddings
│
├── tests/                        # Tests
│   ├── api/                      # API tests
│   │   ├── test_prompts.py
│   │   └── test_chat.py
│   └── frontend/                 # Frontend tests
│       └── components/
│           └── PromptCard.test.tsx
│
├── steering/                     # MUSUBI Project Memory
│   ├── product.md
│   ├── tech.md
│   ├── structure.md
│   └── rules/
│       ├── constitution.md
│       ├── workflow.md
│       └── ears-format.md
│
├── storage/                      # SDD Artifacts
│   ├── specs/
│   ├── changes/
│   └── features/
│
├── docker/                       # Docker configuration
│   ├── Dockerfile.api
│   ├── Dockerfile.frontend
│   └── Dockerfile.single         # All-in-one container
│
├── docker-compose.yml            # Development environment
├── docker-compose.prod.yml       # Production environment
├── .env.example
├── pyproject.toml                # Python dependencies
├── requirements.txt
├── LICENSE                       # CC BY-NC 4.0
├── README.md
├── ARCHITECTURE.md               # This file
└── CHANGELOG.md
```

---

## 🎯 Core Components

### 1. FastAPI Backend (`api/`)

**Purpose**: Serve prompt templates, manage dialogue sessions, integrate with AI providers

**Key Features**:
- RESTful API for prompt CRUD operations
- Dialogue session management (multi-stage conversations)
- AI agent orchestration (OpenAI, Anthropic, Ollama, etc.)
- Vector search across prompts
- Real-time chat streaming

**Tech Stack**:
- **FastAPI** - Modern Python web framework
- **SurrealDB** - Multi-model database
- **LangChain** - AI orchestration (optional)
- **Esperanto** - Multi-provider AI abstraction (from open-notebook)

### 2. Next.js Frontend (`frontend/`)

**Purpose**: User interface for browsing prompts and chatting with agents

**Key Features**:
- Prompt library browser with search and filters
- Category navigation (11 categories)
- Interactive chat interface with dialogue stages
- Real-time AI responses (streaming)
- Responsive design (mobile + desktop)

**Tech Stack**:
- **Next.js 14+** - React framework with App Router
- **React 18** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS** - Utility-first CSS
- **shadcn/ui** - Component library

### 3. Prompt Database (`prompts/`)

**Purpose**: Git-versioned, file-based prompt templates

**Structure**:
- Markdown files with YAML front matter
- Organized by language and category
- Version controlled via Git
- Imported to SurrealDB for search and metadata

**Example Prompt File**:
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
tags:
  - strategy
  - business
  - consulting
created: 2025-11-19
updated: 2025-11-23
---

# Business Strategy Consultant

[Prompt content with dialogue stages...]
```

### 4. SurrealDB Database

**Purpose**: Store prompt metadata, user sessions, chat history

**Collections**:
- `prompts` - Prompt metadata (id, category, frameworks, embeddings)
- `categories` - Category information
- `sessions` - Chat/dialogue sessions
- `messages` - Chat message history
- `users` - Optional user accounts

---

## 🔌 API Design

### REST API Endpoints

#### Prompts
```
GET    /api/prompts                # List all prompts
GET    /api/prompts/{id}           # Get single prompt
POST   /api/prompts/search         # Search prompts (full-text + vector)
GET    /api/prompts/{id}/content   # Get full prompt markdown
```

#### Categories
```
GET    /api/categories             # List all categories
GET    /api/categories/{slug}      # Get category details
GET    /api/categories/{slug}/prompts  # Prompts in category
```

#### Chat/Dialogue
```
POST   /api/chat/sessions          # Create new session
GET    /api/chat/sessions/{id}     # Get session details
POST   /api/chat/sessions/{id}/messages  # Send message
GET    /api/chat/sessions/{id}/messages  # Get message history
DELETE /api/chat/sessions/{id}     # Delete session
```

#### Agents
```
POST   /api/agents/{promptId}/invoke    # Invoke agent with prompt
POST   /api/agents/{promptId}/stream    # Stream agent responses
GET    /api/agents/{promptId}/stages    # Get dialogue stages
```

---

## 🎨 UI/UX Design

### Main Views

#### 1. Home Page (`/`)
- Welcome message and project overview
- Featured prompts (popular, recently added)
- Category grid (11 categories)
- Search bar

#### 2. Prompt Library (`/prompts`)
- List/grid view of all prompts
- Filters: category, language, frameworks
- Search bar (full-text)
- Sort: name, date, popularity

#### 3. Prompt Detail (`/prompts/[id]`)
- Full prompt display
- Metadata (category, frameworks, tags)
- "Start Dialogue" button → opens chat
- Related prompts

#### 4. Chat Interface (`/chat/[sessionId]`)
- **Left Panel**: Dialogue stage progress (1/5, 2/5, etc.)
- **Center Panel**: Chat messages (user + AI)
- **Right Panel**: Generated meta-prompt (final output)
- Input box for user messages

#### 5. Category View (`/categories/[slug]`)
- Category description
- List of prompts in category
- Related categories

### UI Components

```
Header
├── Logo
├── Search bar
├── Navigation (Prompts | Categories | About)
└── Language selector (EN | JA)

Sidebar (optional)
├── Category list
└── Filters

PromptCard
├── Title
├── Category badge
├── Framework tags
├── Description preview
└── "Try Now" button

ChatInterface
├── StageProgress (visual indicator)
├── MessageList
│   ├── UserMessage
│   └── AgentMessage
├── InputBox
└── GeneratedPrompt (final output)
```

---

## 🔄 Data Flow

### 1. Prompt Discovery Flow

```
User visits /prompts
    ↓
Frontend fetches GET /api/prompts
    ↓
API queries SurrealDB prompts collection
    ↓
Returns JSON list of prompts
    ↓
Frontend renders PromptCard components
```

### 2. Dialogue Flow

```
User clicks "Start Dialogue" on prompt
    ↓
Frontend creates session: POST /api/chat/sessions
    ↓
API creates session in SurrealDB
    ↓
Frontend redirects to /chat/{sessionId}
    ↓
User sends first message
    ↓
Frontend sends POST /api/chat/sessions/{id}/messages
    ↓
API invokes AI agent with prompt template
    ↓
AI responds with Stage 1 questions
    ↓
User answers → Stage 2 → ... → Stage 5
    ↓
Final meta-prompt generated and displayed
```

### 3. Search Flow

```
User types in search bar
    ↓
Frontend sends POST /api/prompts/search with query
    ↓
API performs:
  - Full-text search (SurrealDB)
  - Vector search (if embeddings exist)
    ↓
Returns ranked results
    ↓
Frontend displays results
```

---

## 🛠️ Technology Stack

### Backend

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.11+ | Programming language |
| FastAPI | 0.104+ | Web framework |
| SurrealDB | 1.5+ | Database |
| Pydantic | 2.0+ | Data validation |
| LangChain | 0.1+ | AI orchestration (optional) |
| OpenAI SDK | 1.0+ | OpenAI integration |
| Anthropic SDK | 0.8+ | Anthropic integration |

### Frontend

| Technology | Version | Purpose |
|------------|---------|---------|
| Next.js | 14+ | React framework |
| React | 18+ | UI library |
| TypeScript | 5.0+ | Type safety |
| Tailwind CSS | 3.0+ | Styling |
| shadcn/ui | Latest | Component library |
| Zustand | 4.0+ | State management |

### Infrastructure

| Technology | Version | Purpose |
|------------|---------|---------|
| Docker | 24+ | Containerization |
| Docker Compose | 2.0+ | Multi-container orchestration |
| SurrealDB | 1.5+ | Database |

---

## 🚀 Deployment Architecture

### Development Environment

```yaml
# docker-compose.yml
services:
  api:
    build: ./api
    ports:
      - "8000:8000"
    environment:
      - SURREAL_URL=ws://surrealdb:8000/rpc
    volumes:
      - ./api:/app
      - ./prompts:/prompts

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000
    volumes:
      - ./frontend:/app

  surrealdb:
    image: surrealdb/surrealdb:latest
    ports:
      - "8001:8000"
    command: start --user root --pass root file:/mydata
    volumes:
      - ./database/data:/mydata
```

### Production Environment

**Single Container** (like open-notebook's `v1-latest-single`):
```dockerfile
# Dockerfile.single
FROM python:3.11-slim as api-builder
# Build API...

FROM node:20-alpine as frontend-builder
# Build frontend...

FROM python:3.11-slim
# Copy API + built frontend
# Install SurrealDB
# Setup supervisord to run all services
```

**Multi-Container** (like open-notebook's `v1-latest`):
- Separate containers for API, Frontend, SurrealDB
- Use Docker Compose or Kubernetes

---

## 📊 Database Schema

### SurrealDB Schema

```surql
-- Prompts collection
DEFINE TABLE prompts SCHEMAFULL;
DEFINE FIELD id ON TABLE prompts TYPE string;
DEFINE FIELD title ON TABLE prompts TYPE string;
DEFINE FIELD category ON TABLE prompts TYPE string;
DEFINE FIELD language ON TABLE prompts TYPE string;
DEFINE FIELD frameworks ON TABLE prompts TYPE array;
DEFINE FIELD dialogue_stages ON TABLE prompts TYPE int;
DEFINE FIELD content ON TABLE prompts TYPE string;
DEFINE FIELD embedding ON TABLE prompts TYPE array;
DEFINE FIELD created_at ON TABLE prompts TYPE datetime;
DEFINE FIELD updated_at ON TABLE prompts TYPE datetime;

-- Categories collection
DEFINE TABLE categories SCHEMAFULL;
DEFINE FIELD slug ON TABLE categories TYPE string;
DEFINE FIELD name ON TABLE categories TYPE object;
DEFINE FIELD description ON TABLE categories TYPE object;

-- Sessions collection
DEFINE TABLE sessions SCHEMAFULL;
DEFINE FIELD id ON TABLE sessions TYPE string;
DEFINE FIELD prompt_id ON TABLE sessions TYPE string;
DEFINE FIELD current_stage ON TABLE sessions TYPE int;
DEFINE FIELD created_at ON TABLE sessions TYPE datetime;
DEFINE FIELD updated_at ON TABLE sessions TYPE datetime;

-- Messages collection
DEFINE TABLE messages SCHEMAFULL;
DEFINE FIELD id ON TABLE messages TYPE string;
DEFINE FIELD session_id ON TABLE messages TYPE string;
DEFINE FIELD role ON TABLE messages TYPE string; -- 'user' | 'assistant'
DEFINE FIELD content ON TABLE messages TYPE string;
DEFINE FIELD stage ON TABLE messages TYPE int;
DEFINE FIELD created_at ON TABLE messages TYPE datetime;
```

---

## 🔐 Security Considerations

### Optional Authentication

- Password protection (like open-notebook)
- Optional: No auth for single-user deployments
- JWT tokens for API access

### Data Privacy

- All data stored locally (self-hosted)
- No telemetry or analytics
- API keys for AI providers stored in environment variables

---

## 🎯 MVP Features (Phase 1)

### Must-Have

1. ✅ **Prompt Library Browser**
   - List all prompts
   - Category filtering
   - Search (full-text)

2. ✅ **Prompt Detail View**
   - Display full prompt
   - Show metadata (frameworks, tags)

3. ✅ **Interactive Dialogue**
   - Multi-stage conversation (4-5 stages)
   - Chat interface
   - Meta-prompt generation

4. ✅ **AI Integration**
   - OpenAI support
   - Anthropic support
   - Streaming responses

5. ✅ **Docker Deployment**
   - Single-container image
   - Docker Compose setup

### Nice-to-Have (Phase 2)

6. 🔄 **Advanced Search**
   - Vector search
   - Framework-based filtering

7. 🔄 **Multi-Language Support**
   - English + Japanese UI
   - Prompt language selection

8. 🔄 **Custom Prompts**
   - User-created prompts
   - Template editor

9. 🔄 **Team Features**
   - Shared prompt libraries
   - Collaboration tools

---

## 📈 Migration Strategy

### From Current Structure to New Architecture

1. **Keep Existing Content**
   - `en/`, `ja/`, `copilot/` → move to `prompts/`
   - Preserve all markdown files
   - No content rewriting needed

2. **Add New Components**
   - Create `api/` directory
   - Create `frontend/` directory
   - Setup `database/`

3. **Gradual Migration**
   - Phase 1: API + basic frontend (prompt browser)
   - Phase 2: Chat/dialogue features
   - Phase 3: Advanced features (search, custom prompts)

---

## 🤝 MUSUBI Alignment

### Constitutional Compliance

| Article | Compliance |
|---------|------------|
| **I: Library-First** | ✅ Prompts are independent markdown libraries |
| **II: CLI Interface** | 🔄 Future: CLI for prompt management |
| **III: Test-First** | ✅ Tests for API and frontend |
| **IV: EARS Format** | ✅ Requirements in EARS |
| **V: Traceability** | ✅ REQ → Design → Code → Tests |
| **VI: Project Memory** | ✅ Steering files maintained |
| **VII: Simplicity** | ✅ 3 main components (API, Frontend, DB) |
| **VIII: Anti-Abstraction** | ✅ Use FastAPI, Next.js directly |
| **IX: Integration Testing** | ✅ Real SurrealDB in tests |

---

## 📝 Next Steps

1. **Review this architecture** with stakeholders
2. **Create requirements document** using EARS format
3. **Design API contracts** (OpenAPI spec)
4. **Setup development environment**
5. **Start Phase 1 implementation**

---

**Last Updated**: 2025-11-23  
**Status**: Awaiting Approval
