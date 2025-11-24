# Frameworks for System Design Guide

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### CAP Theorem

**Theorem**: In a distributed system, you can have at most 2 of 3:

- **C**onsistency: All nodes see the same data
- **A**vailability: Every request gets a response
- **P**artition Tolerance: System works despite network failures

**Practical Application**:
- CA: Traditional relational databases (single node)
- CP: MongoDB, HBase (consistent but may be unavailable)
- AP: Cassandra, DynamoDB (available but eventually consistent)

**Reality**: Partition tolerance is mandatory in distributed systems, so choose between C and A

### Load Balancing Algorithms

**Round Robin**: Distribute requests equally across servers

**Least Connections**: Send to server with fewest active connections

**IP Hash**: Hash client IP to consistently route to same server

**Weighted Round Robin**: Servers get traffic proportional to capacity

**Least Response Time**: Send to fastest-responding server

### Database Sharding Strategies

**Horizontal Sharding (Row-based)**:
- Partition by key (user ID, geographic region)
- Each shard contains subset of rows
- **Hash-based**: Hash key to determine shard
- **Range-based**: Ranges of keys (A-M, N-Z)
- **Geographic**: By location

**Vertical Sharding (Column-based)**:
- Split table by columns
- Different concerns in different databases
- Less common

**Challenges**:
- Cross-shard queries expensive
- Rebalancing when adding shards
- Hotspots if sharding key unbalanced

### Caching Strategies

**Cache-Aside (Lazy Loading)**:
```
if (cache has data):
    return cached data
else:
    data = fetch from database
    store in cache
    return data
```

**Write-Through**:
```
write to cache
write to database
return success
```

**Write-Behind (Write-Back)**:
```
write to cache
async write to database (batched)
return success
```

### Rate Limiting Algorithms

**Token Bucket**:
- Bucket holds tokens
- Request consumes token
- Tokens refill at constant rate
- Allows bursts

**Leaky Bucket**:
- Requests enter bucket
- Leak out at constant rate
- Overflow rejected
- Smooth output

**Fixed Window Counter**:
- Count requests per time window
- Reset at window boundary
- Simple but burst at boundaries

**Sliding Window Log**:
- Store timestamp of each request
- Count requests in sliding window
- Accurate but memory intensive

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
  - Main Prompt: `prompts/copilot/prompts/design-development/system-design-guide.md`
  - Examples: `rag/design-development/system-design-guide/examples.md`
  - Methodologies: `rag/design-development/system-design-guide/methodologies.md`
