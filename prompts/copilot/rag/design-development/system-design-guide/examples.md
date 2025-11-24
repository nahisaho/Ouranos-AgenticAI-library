# Examples for System Design Guide

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: URL Shortener Service Design

**Stage 1: Requirements**
- Functional: Shorten URLs, redirect, analytics
- Scale: 100M URLs/month, 1B redirects/month
- Latency: <100ms for redirects
- Availability: 99.99%

**Stage 2: Architecture**
- API Gateway: Rate limiting, authentication
- Application: Stateless Node.js services
- Database: PostgreSQL for URL mappings, Redis for caching
- CDN: Cache redirect responses

**Stage 3: Scalability**
- Read-heavy: 10:1 read/write ratio
- Cache 80% of URLs (Pareto principle)
- Database read replicas for analytics
- Horizontal scaling of application servers

**Stage 4: Reliability**
- Multi-region deployment
- Database replication
- Health checks every 30s
- Circuit breakers for database calls

**Stage 5: Tech Stack**
- Language: Node.js (I/O performance)
- Database: PostgreSQL (relational), Redis (cache)
- Cloud: AWS (ALB, EC2, RDS, ElastiCache, CloudFront)
- Monitoring: CloudWatch, Datadog

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
  - Main Prompt: `prompts/copilot/prompts/design-development/system-design-guide.md`
  - Frameworks: `rag/design-development/system-design-guide/frameworks.md`
  - Methodologies: `rag/design-development/system-design-guide/methodologies.md`
