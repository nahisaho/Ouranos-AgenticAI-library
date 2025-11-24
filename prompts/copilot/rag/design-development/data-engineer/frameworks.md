# Frameworks for Data Engineer

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### Data Pipeline Patterns

**Batch Processing Patterns**:
- **Lambda Architecture**: Separate batch and speed layers
- **Kappa Architecture**: Stream processing only
- **Change Data Capture**: Real-time data synchronization

**Stream Processing Patterns**:
- **Event Sourcing**: Immutable event log as source of truth
- **CQRS**: Separate read and write models
- **Event-Driven Architecture**: Loosely coupled system communication

### Data Modeling Approaches

**Dimensional Modeling**:
```sql
-- Star Schema Example
CREATE TABLE fact_sales (
    sale_id BIGINT PRIMARY KEY,
    customer_key INT REFERENCES dim_customer(customer_key),
    product_key INT REFERENCES dim_product(product_key),
    date_key INT REFERENCES dim_date(date_key),
    quantity INT,
    unit_price DECIMAL(10,2),
    total_amount DECIMAL(12,2)
);

CREATE TABLE dim_customer (
    customer_key INT PRIMARY KEY,
    customer_id VARCHAR(50),
    customer_name VARCHAR(200),
    segment VARCHAR(50),
    country VARCHAR(100)
);
```

**Data Vault Modeling**:
```sql
-- Hub Table
CREATE TABLE hub_customer (
    customer_hk VARCHAR(32) PRIMARY KEY,
    customer_id VARCHAR(50),
    load_date TIMESTAMP,
    record_source VARCHAR(100)
);

-- Link Table
CREATE TABLE link_customer_order (
    customer_order_hk VARCHAR(32) PRIMARY KEY,
    customer_hk VARCHAR(32),
    order_hk VARCHAR(32),
    load_date TIMESTAMP,
    record_source VARCHAR(100)
);

-- Satellite Table
CREATE TABLE sat_customer_details (
    customer_hk VARCHAR(32),
    load_date TIMESTAMP,
    customer_name VARCHAR(200),
    email VARCHAR(200),
    phone VARCHAR(50),
    end_date TIMESTAMP,
    PRIMARY KEY (customer_hk, load_date)
);
```

### Data Quality Framework

**Great Expectations Example**:
```python
import great_expectations as ge

# Create expectation suite
expectation_suite = ge.core.ExpectationSuite("customer_data_quality")

# Add expectations
expectation_suite.add_expectation(
    ge.core.ExpectationConfiguration(
        expectation_type="expect_column_to_exist",
        kwargs={"column": "customer_id"}
    )
)

expectation_suite.add_expectation(
    ge.core.ExpectationConfiguration(
        expectation_type="expect_column_values_to_not_be_null",
        kwargs={"column": "customer_id"}
    )
)

expectation_suite.add_expectation(
    ge.core.ExpectationConfiguration(
        expectation_type="expect_column_values_to_be_unique",
        kwargs={"column": "customer_id"}
    )
)
```

### Performance Optimization

**Query Optimization Techniques**:
- Proper indexing strategies
- Partition pruning
- Predicate pushdown
- Columnar storage benefits

**Resource Management**:
- Dynamic resource allocation
- Query queue management
- Workload isolation
- Cost-based optimization

---

---

## Framework Integration Strategies

### Sequential Integration
Frameworks are applied one after another in different stages.

**When to use**: When frameworks build on each other logically.

### Parallel Integration
Multiple frameworks are used simultaneously within the same stage.

**When to use**: When frameworks provide complementary perspectives.

### Selective Integration
User chooses which frameworks to apply based on their specific situation.

**When to use**: When different scenarios require different analytical approaches.

---

## Best Practices

1. **Start Simple**: Don't overwhelm with too many frameworks initially
2. **Explain Why**: Always clarify the purpose and value of each framework
3. **Provide Examples**: Show how frameworks have been applied in similar scenarios
4. **Allow Flexibility**: Let users adapt frameworks to their specific needs
5. **Integrate Naturally**: Frameworks should enhance dialogue, not dominate it

---

## Version Information

- **Version**: 1.0.0
- **Last Updated**: 2025-11-24
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/design-development/data-engineer.md`
  - Examples: `rag/design-development/data-engineer/examples.md`
  - Methodologies: `rag/design-development/data-engineer/methodologies.md`
