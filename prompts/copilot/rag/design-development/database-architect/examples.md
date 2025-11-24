# Examples for Database Architect

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: High-Traffic E-commerce Platform Database

**Stage 1: Requirements Assessment**
- **Workload**: High-volume OLTP with real-time analytics requirements
- **Scale**: 1M+ users, 10K+ concurrent connections, 100GB+ daily data growth
- **Performance**: <50ms query response, 99.9% availability, global distribution

**Stage 2: Technology Selection**
- **Primary Database**: PostgreSQL with read replicas for OLTP workloads
- **Analytics**: ClickHouse for real-time analytics and reporting
- **Cache**: Redis for session storage and frequently accessed data
- **Search**: Elasticsearch for product search and recommendations

**Stage 3: Scaling Strategy**
- **Sharding**: User-based sharding across 4 database shards
- **Read Replicas**: 3 read replicas per region with automatic failover
- **Caching**: Multi-level caching with Redis and application-level cache

**Stage 4: Operations Setup**
- **Monitoring**: Comprehensive monitoring with Prometheus and Grafana
- **Security**: Role-based access control, encryption at rest and in transit
- **Backup**: Automated daily backups with point-in-time recovery capability

**Stage 5: Evolution Planning**
- **Migration Framework**: Zero-downtime migration capability
- **Technology Roadmap**: Evaluation of cloud-native databases for future scaling
- **Innovation Pipeline**: Quarterly technology assessment and adoption planning

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
  - Main Prompt: `prompts/copilot/prompts/design-development/database-architect.md`
  - Frameworks: `rag/design-development/database-architect/frameworks.md`
  - Methodologies: `rag/design-development/database-architect/methodologies.md`
