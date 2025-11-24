# Frameworks for Supply Chain Management Consultant

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### SCOR Model (Supply Chain Operations Reference)

**Purpose**: Standardized framework to describe, measure, and improve supply chain performance

**Five Process Categories**:
1. **Plan**: Balance supply and demand, align supply chain plan with financial plan
2. **Source**: Procure goods and services to meet demand
3. **Make**: Transform materials into finished products
4. **Deliver**: Fulfill customer orders (warehouse, transport, install)
5. **Return**: Handle returns (defective products, excess inventory)

**Plus Enable**: Support processes (IT, HR, finance, quality, compliance)

**Performance Attributes**:
- **Reliability**: Perfect order %, fill rate, on-time delivery
- **Responsiveness**: Order fulfillment lead time
- **Agility**: Upside/downside supply chain flexibility
- **Cost**: Total supply chain cost, cost to serve
- **Asset**: Cash-to-cash cycle time, inventory turns, asset utilization

**Application**: Benchmark current performance against peers, identify gaps, implement best practices

### Bullwhip Effect

**Problem**: Small changes in customer demand cause increasingly large swings in demand upstream in supply chain

**Example**: 
- Retailer demand varies 5%
- Wholesaler demand varies 15%
- Manufacturer demand varies 30%
- Supplier demand varies 50%

**Causes**:
- **Demand signal processing**: Each tier forecasts based on orders from downstream (not actual consumer demand), adds safety margin
- **Order batching**: Orders placed in batches (e.g., monthly) create lumpiness
- **Price fluctuations**: Promotions cause forward buying (buy more when cheap)
- **Rationing**: When supply constrained, customers inflate orders

**Mitigation**:
- **Visibility**: Share point-of-sale data upstream (everyone sees real consumer demand)
- **Reduce lead times**: Faster response = less forecasting needed
- **Everyday low pricing**: Eliminate promotions that cause buying swings
- **Vendor-managed inventory**: Supplier manages customer inventory based on consumption
- **Smaller, more frequent orders**: Reduce batch sizes

### ABC Analysis (Inventory Classification)

**Purpose**: Classify inventory into categories to focus management attention

**Classification**:
- **A items**: 20% of SKUs, 80% of revenue → High attention
- **B items**: 30% of SKUs, 15% of revenue → Moderate attention
- **C items**: 50% of SKUs, 5% of revenue → Low attention

**Management Approach**:
- **A items**: 
  - Tight inventory control (high service level, safety stock, frequent review)
  - Demand forecasting with statistical methods
  - Close supplier relationships
  - Regular physical counts
- **B items**: 
  - Moderate controls (periodic review, standard service levels)
  - Basic forecasting
- **C items**: 
  - Minimal effort (bulk ordering, low safety stock, simple rules like "order when empty")
  - Accept occasional stock-outs

**Example**: Electronics retailer - A items (iPhones, laptops), B items (accessories), C items (cables)

### Economic Order Quantity (EOQ)

**Purpose**: Determine optimal order quantity that minimizes total inventory cost

**Cost Trade-off**:
- **Ordering cost**: Cost per order (setup, processing, shipping) → Decreases with larger orders
- **Holding cost**: Cost to hold inventory (storage, capital, obsolescence) → Increases with larger orders

**Formula**: EOQ = √(2DS/H)
- D = Annual demand
- S = Ordering cost per order
- H = Holding cost per unit per year

**Example**:
- Annual demand = 10,000 units
- Ordering cost = $100 per order
- Holding cost = $5 per unit per year
- EOQ = √(2 × 10,000 × 100 / 5) = √400,000 = 632 units
- Order 632 units at a time, 10,000/632 = 15.8 orders per year

**Total Annual Cost** at EOQ: (D/Q)S + (Q/2)H = (10,000/632)×100 + (632/2)×5 = $1,581 + $1,580 = $3,161

### Just-in-Time (JIT) and Lean Supply Chain

**Philosophy**: Produce and deliver exactly what is needed, when needed, in the quantity needed - minimize waste (especially inventory waste)

**Core Principles**:
- **Pull system**: Production triggered by actual demand, not forecast
- **Small lot sizes**: Frequent deliveries of small quantities
- **Zero inventory ideal**: Minimize work-in-process and finished goods
- **Quality at source**: Don't pass defects downstream (stop and fix immediately)
- **Continuous improvement**: Eliminate waste relentlessly

**Requirements** for successful JIT:
- **Reliable suppliers**: Deliver on-time, defect-free
- **Short lead times**: Quick response to demand changes
- **Stable demand**: JIT struggles with high variability
- **Geographic proximity**: Suppliers near production (reduce transportation time/cost)

**Benefits**: Lower inventory, better cash flow, faster response, less obsolescence

**Risks**: Vulnerable to disruptions (no safety stock buffer)

**Application**: High-volume, stable demand products (automotive, electronics assembly)

### Supply Chain Network Design

**Purpose**: Determine optimal number, location, and capacity of facilities (plants, DCs, warehouses) to minimize total cost while meeting service requirements

**Decisions**:
- How many facilities?
- Where to locate?
- What capacity for each?
- Which facilities serve which customers/markets?
- Which products produced/stored at which facilities?

**Objective**: Minimize total cost = Fixed facility costs + Variable transportation costs + Inventory holding costs

**Constraints**:
- Service level requirements (e.g., 95% of customers within 2-day ground delivery)
- Capacity limits
- Budget constraints

**Methods**:
- **Center of Gravity**: Locate facility to minimize weighted distance to demand points
- **Optimization Models**: Linear programming, mixed-integer programming
- **Simulation**: Model different scenarios, compare

**Trade-offs**:
- More facilities → Better service (closer to customers) but higher fixed costs
- Fewer facilities → Lower fixed costs, economies of scale, but longer delivery times

**Example**: National retailer - 1 central DC (low cost, 5-day delivery) vs. 4 regional DCs (higher cost, 2-day delivery) → Choose based on customer willingness to pay for faster delivery

### S&OP (Sales and Operations Planning)

**Purpose**: Integrate demand planning, supply planning, and financial planning into one consensus plan

**Process** (monthly cycle):

**Week 1: Data Gathering**
- Statistical demand forecast
- Current supply plan
- Financial targets

**Week 2: Demand Planning**
- Sales and marketing review demand forecast
- Adjust for known events (promotions, new products, market changes)
- Create consensus demand plan

**Week 3: Supply Planning**
- Operations reviews capacity to meet demand
- Identify constraints (materials, labor, equipment)
- Develop supply options (normal plan, constrained plan, expedited plan)

**Week 4: Pre-S&OP**
- Cross-functional team balances supply and demand
- Identify gaps and trade-offs
- Develop recommendations (invest in capacity? outsource? accept backorders? change pricing?)

**Week 5: Executive S&OP**
- Leadership approves plan
- Make final trade-off decisions
- Align organization on integrated plan

**Outputs**:
- Consensus demand forecast
- Supply/production plan
- Inventory targets
- Financial forecast (revenue, margin, cash)
- Agreed actions and owners

**Benefits**: Alignment, better forecast accuracy, improved service, optimized inventory

### Total Cost of Ownership (TCO)

**Purpose**: Evaluate supplier based on total cost, not just unit price

**TCO Components**:

**Acquisition Costs**:
- Unit price
- Ordering/transaction costs
- Transportation/freight
- Tariffs/duties (if international)
- Inspection costs

**Ownership Costs**:
- Inventory carrying cost (capital tied up, storage, obsolescence)
- Quality costs (defects, rework, warranty claims)
- Downtime costs (production stops due to late/defective parts)
- Supplier management (communication, problem-solving, audits)

**Post-Ownership Costs**:
- Disposal, recycling
- Environmental compliance

**Example**:
- **Supplier A**: $10/unit, 2% defect rate, 90% on-time delivery, 30-day payment terms
- **Supplier B**: $11/unit, 0.5% defect rate, 99% on-time delivery, 60-day payment terms
- TCO analysis: Supplier B has higher unit price but lower total cost due to quality and service

**Decision**: Select supplier with lowest TCO, not lowest price

### Supply Chain Risk Management (SCRM)

**Process**:

**1. Identify Risks**:
- Supplier risks (bankruptcy, quality, single-source)
- Operational risks (plant disruption, IT failure)
- Demand risks (volatility, competition)
- External risks (natural disaster, geopolitical, pandemic)

**2. Assess Risks**:
- Likelihood (High/Medium/Low)
- Impact (High/Medium/Low)
- Prioritize: High likelihood OR high impact

**3. Mitigation Strategies**:
- **Avoidance**: Don't engage in risky activity (avoid single-source, avoid high-risk regions)
- **Reduction**: Actions to reduce likelihood or impact (dual sourcing, safety stock, near-shoring, supplier audits)
- **Transfer**: Insurance, contractual terms (penalty clauses for late delivery)
- **Acceptance**: Accept risk if low likelihood and low impact (monitor but don't mitigate)

**4. Monitor and Review**:
- Early warning indicators (supplier financial health, geopolitical risk indices)
- Regular risk reviews (quarterly)
- Update mitigation plans as risks evolve

**Resilience Strategies**:
- **Redundancy**: Backup suppliers, multiple facilities, safety stock
- **Flexibility**: Ability to shift production, substitute materials, reroute shipments
- **Visibility**: Real-time tracking of inventory, shipments, supplier status
- **Collaboration**: Strong supplier relationships, joint risk planning

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
  - Main Prompt: `prompts/copilot/prompts/business-management/supply-chain-management-consultant.md`
  - Examples: `rag/business-management/supply-chain-management-consultant/examples.md`
  - Methodologies: `rag/business-management/supply-chain-management-consultant/methodologies.md`
