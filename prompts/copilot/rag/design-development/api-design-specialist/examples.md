# Examples for Api Design Specialist

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: E-commerce Product API Design

**Stage 1: Requirements**
- Purpose: Product catalog management
- Consumers: Web app, mobile apps, partners
- Resources: Products, categories, inventory, reviews

**Stage 2: Architecture**
- Style: RESTful API with GraphQL for mobile
- API Gateway for routing and rate limiting
- BFF pattern for mobile-specific needs

**Stage 3: Design**
```
GET    /api/v1/products          # List products
GET    /api/v1/products/{id}     # Get product
POST   /api/v1/products          # Create product (admin)
PATCH  /api/v1/products/{id}     # Update product
DELETE /api/v1/products/{id}     # Delete product

GET    /api/v1/products?category=electronics&sort=price:asc&page=1
```

**Stage 4: Security**
- OAuth 2.0 for user authentication
- API keys for partner access
- RBAC: admin, partner, public
- Rate limit: 1000 req/hour for authenticated, 100 for anonymous

**Stage 5: Documentation**
- OpenAPI 3.0 spec published
- Swagger UI at /api/docs
- SDKs for JavaScript, Python, Ruby
- Postman collection available

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
  - Main Prompt: `prompts/copilot/prompts/design-development/api-design-specialist.md`
  - Frameworks: `rag/design-development/api-design-specialist/frameworks.md`
  - Methodologies: `rag/design-development/api-design-specialist/methodologies.md`
