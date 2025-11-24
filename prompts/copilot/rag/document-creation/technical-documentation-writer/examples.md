# Examples for Technical Documentation Writer

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: Documenting a REST API for Project Management Software

**Audience**: Developers integrating with API

**Stage 1: Requirements**
- Type: API documentation
- Audience: Developers (intermediate to advanced)
- Scope: All endpoints, authentication, webhooks
- Format: Web docs site

**Stage 2: Information Architecture**

```
Introduction
├── Overview
├── Authentication
└── Quick Start

API Reference
├── Projects
│   ├── List Projects (GET /projects)
│   ├── Create Project (POST /projects)
│   ├── Get Project (GET /projects/:id)
│   └── Update Project (PUT /projects/:id)
├── Tasks
├── Users
└── Webhooks

Guides
├── Authentication Guide (OAuth 2.0)
├── Pagination
├── Rate Limiting
├── Webhooks Setup
└── Error Handling

SDKs
├── Python SDK
├── JavaScript SDK
└── Ruby SDK

Changelog
```

**Stage 3: Writing**

Each endpoint documented with:
- HTTP method and URL
- Description
- Authentication requirements
- Request parameters table
- Example request (curl + code)
- Response examples (success + errors)
- Error codes table

**Stage 4: Docs-as-Code**
- Markdown files in `/docs` directory
- Docusaurus for static site generation
- GitHub for version control
- Netlify for hosting (auto-deploy on merge)
- Published to docs.example.com

**Stage 5: Maintenance**
- Docs updated with every API change
- Automated link checker in CI
- Analytics show most-viewed endpoints
- Feedback widget collects user input
- Monthly docs review meeting

**Results**:
- Comprehensive API docs
- Developer satisfaction increased
- API adoption faster
- Support tickets reduced by 30%

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
  - Main Prompt: `prompts/copilot/prompts/document-creation/technical-documentation-writer.md`
  - Frameworks: `rag/document-creation/technical-documentation-writer/frameworks.md`
  - Methodologies: `rag/document-creation/technical-documentation-writer/methodologies.md`
