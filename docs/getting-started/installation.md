# Ouranos Interactive Platform - Getting Started

## 🎯 Overview

Ouranos Interactive Platform v2.0 is an interactive, self-hosted AI prompt platform inspired by Google's NotebookLM. Browse 54+ specialized prompts across 11 professional domains and engage in multi-stage dialogues with AI agents.

## 🏗️ Architecture

- **Frontend**: Next.js 14+ with React 18 (port 3000)
- **API**: FastAPI with Python 3.11+ (port 8000)
- **Database**: SurrealDB (port 8001)

## 📋 Prerequisites

- Docker & Docker Compose
- (Optional) OpenAI API key or Anthropic API key for AI features

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/nahisaho/Ouranos-AgenticAI-library.git
cd Ouranos-AgenticAI-library
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env and add your API keys
```

Required variables:
```env
OPENAI_API_KEY=sk-your-openai-api-key-here
# or
ANTHROPIC_API_KEY=sk-ant-your-anthropic-api-key-here
```

### 3. Start Services

```bash
docker-compose up -d
```

This will start:
- **Frontend**: http://localhost:3000
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **SurrealDB**: http://localhost:8001

### 4. Access Application

Open your browser and navigate to:
- **Home Page**: http://localhost:3000
- **Prompt Library**: http://localhost:3000/prompts
- **API Documentation**: http://localhost:8000/docs

## 📦 Development Setup

### Backend (FastAPI)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn api.main:app --reload --port 8000
```

### Frontend (Next.js)

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

### Database (SurrealDB)

```bash
# Start SurrealDB locally
docker run -p 8001:8000 surrealdb/surrealdb:latest start --user root --pass root file:/mydata
```

## 📚 Documentation

- **Architecture**: See [ARCHITECTURE.md](ARCHITECTURE.md)
- **Requirements**: See [storage/specs/interactive-platform-requirements.md](storage/specs/interactive-platform-requirements.md)
- **API Reference**: http://localhost:8000/docs (when running)
- **MUSUBI Workflow**: See [steering/rules/workflow.md](steering/rules/workflow.md)

## 🧪 Testing

```bash
# Backend tests
pytest tests/

# Frontend tests
cd frontend
npm run test
```

## 🛠️ Development Workflow (MUSUBI SDD)

This project follows MUSUBI Specification-Driven Development:

1. **Stage 0: Requirements** - EARS format requirements
2. **Stage 1: Design** - C4 diagrams + ADRs
3. **Stage 2: Tasks** - Implementation task breakdown
4. **Stage 3: Implementation** - Code development
5. **Stage 4: Testing** - Test-First development
6. **Stage 5: Validation** - Constitutional compliance

### Available Commands

- `#sdd-requirements <feature>` - Create EARS requirements
- `#sdd-design <feature>` - Generate C4 + ADR design
- `#sdd-tasks <feature>` - Break down into tasks
- `#sdd-implement <feature>` - Execute implementation
- `#sdd-validate <feature>` - Validate constitutional compliance

## 📄 License

This project is licensed under CC BY-NC 4.0. See [LICENSE](LICENSE) for details.

## 🤝 Contributing

See [CONTRIBUTING.md](docs/development/contributing.md) for contribution guidelines.

## 🔗 Links

- **Repository**: https://github.com/nahisaho/Ouranos-AgenticAI-library
- **Issues**: https://github.com/nahisaho/Ouranos-AgenticAI-library/issues
- **MUSUBI Documentation**: [steering/rules/](steering/rules/)

---

**Status**: Stage 0 Complete - Ready for Stage 1 (Design Phase)  
**Last Updated**: 2025-11-23
