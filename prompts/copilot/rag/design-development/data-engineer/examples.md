# Examples for Data Engineer

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: E-commerce Data Platform Modernization

**Stage 1: Assessment**
- **Current State**: Multiple databases, manual ETL processes, 48-hour data lag for reporting
- **Data Sources**: PostgreSQL (orders), MongoDB (products), Salesforce (customers), web analytics
- **Pain Points**: Data inconsistencies, slow reporting, inability to do real-time personalization

**Stage 2: Architecture**
- **Pattern**: Lakehouse architecture with Databricks on AWS
- **Storage**: S3 data lake with Delta Lake format for ACID transactions
- **Processing**: Spark for batch, Kafka + Spark Streaming for real-time
- **Warehouse**: Databricks SQL for analytics and BI

**Stage 3: Pipelines**
- **Ingestion**: Kafka Connect for database CDC, Fivetran for SaaS integrations
- **Processing**: Medallion architecture (bronze/silver/gold layers)
- **Orchestration**: Apache Airflow with dbt for transformations

**Stage 4: Quality & Monitoring**
- **Quality**: Great Expectations for data validation, Monte Carlo for monitoring
- **Observability**: DataDog for infrastructure, custom dashboards for business metrics
- **SLAs**: 99.9% pipeline reliability, <1 hour data freshness, <30 second query response

**Stage 5: Implementation**
- **Timeline**: 9-month implementation across 4 phases
- **Results**: Reduced data lag from 48 hours to 15 minutes, 10x faster analytics queries, 40% reduction in data engineering effort through automation

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
  - Main Prompt: `prompts/copilot/prompts/design-development/data-engineer.md`
  - Frameworks: `rag/design-development/data-engineer/frameworks.md`
  - Methodologies: `rag/design-development/data-engineer/methodologies.md`
