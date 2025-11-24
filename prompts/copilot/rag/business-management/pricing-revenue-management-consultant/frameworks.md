# Frameworks for Pricing Revenue Management Consultant

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### Pricing Strategy Framework

**Purpose**: Systematic approach to pricing strategy development based on value, competition, and costs

**Three Fundamental Pricing Approaches**:

**1. Cost-Based Pricing**:
- **Cost-Plus**: Price = Cost + Markup
- **Break-even Pricing**: Price to achieve target volume and profitability
- **Target Return Pricing**: Price to achieve desired ROI

**Advantages**: Simple, ensures cost recovery, defensible internally
**Disadvantages**: Ignores customer value and competitive dynamics, may leave money on table

**2. Competition-Based Pricing**:
- **Competitive Parity**: Price at market average
- **Premium Positioning**: Price above competition (typically 10-20% premium)
- **Penetration Pricing**: Price below competition to gain market share

**Advantages**: Market-responsive, considers competitive dynamics
**Disadvantages**: May not reflect true value, can lead to price wars

**3. Value-Based Pricing** (Recommended):
- **Economic Value Pricing**: Price based on quantified customer value
- **Perceived Value Pricing**: Price based on customer's value perception
- **Outcome-Based Pricing**: Price tied to customer results achieved

**Advantages**: Maximizes profit potential, aligns price with value, sustainable competitive advantage
**Disadvantages**: Requires deep customer understanding, more complex to implement

### Value-Based Pricing Process

**Step 1: Identify Value Drivers**
- What problems does your solution solve?
- What benefits do customers receive?
- How do these translate to economic value?

**Step 2: Quantify Economic Value**
```
Customer's Total Economic Value = Cost Savings + Revenue Increases + Risk Reduction + Productivity Gains

Example:
- Current Process Cost: $100,000/year
- Your Solution Cost Savings: $30,000/year
- Productivity Improvement: $20,000/year
- Risk Reduction Value: $10,000/year
Total Economic Value: $60,000/year
```

**Step 3: Determine Value-Based Price Range**
```
Minimum Price = Variable Cost + Margin
Maximum Price = Total Economic Value
Optimal Price = 30-70% of Economic Value (leaving value for customer)
```

**Step 4: Test and Validate**
- Customer interviews and willingness-to-pay research
- Competitive benchmarking
- Price elasticity analysis
- Market testing

### Price Elasticity Analysis

**Price Elasticity of Demand (PED)**:
```
PED = % Change in Quantity Demanded / % Change in Price

Elastic Demand: PED < -1 (price decrease increases revenue)
Inelastic Demand: PED > -1 (price increase increases revenue)  
Unitary Elastic: PED = -1 (revenue unchanged)
```

**Factors Affecting Price Elasticity**:
- **Substitutes Available**: More substitutes = more elastic
- **Necessity vs. Luxury**: Necessities less elastic
- **Brand Loyalty**: Strong brands less elastic
- **Switching Costs**: High switching costs = less elastic
- **Time Horizon**: Long-term more elastic than short-term

**Revenue Optimization**:
```
Revenue = Price × Quantity
Marginal Revenue = Price × (1 + 1/PED)

Optimal Price occurs when: Marginal Revenue = Marginal Cost
```

### Revenue Management Framework

**Core Concepts**:
- **Perishable Inventory**: Capacity that cannot be stored (hotel nights, airline seats)
- **Variable Demand**: Demand varies by time, season, events
- **Fixed Capacity**: Limited supply available for sale
- **Customer Segmentation**: Different willingness to pay across segments

**Revenue Management Applications**:

**Airlines**: Seat inventory management, overbooking optimization, fare class management
**Hotels**: Room rate optimization, length-of-stay controls, group vs. transient mix
**Rental Cars**: Fleet utilization, pricing by location and time
**Restaurants**: Table turn optimization, prix fixe vs. à la carte
**Professional Services**: Utilization optimization, peak vs. off-peak rates

**Key Metrics**:
```
RevPAR (Revenue per Available Room) = ADR × Occupancy Rate
Yield = Actual Revenue / Potential Revenue (if sold at full price)
Load Factor = Capacity Sold / Total Capacity Available
```

### Dynamic Pricing Algorithm

**Basic Dynamic Pricing Formula**:
```
Dynamic Price = Base Price × Demand Multiplier × Inventory Multiplier × Competitive Multiplier

Where:
- Demand Multiplier: 1 + (Current Demand / Average Demand - 1) × Demand Sensitivity
- Inventory Multiplier: 1 + (1 - Available Inventory / Total Inventory) × Inventory Sensitivity  
- Competitive Multiplier: 1 + (Competitor Price / Your Price - 1) × Competitive Sensitivity
```

**Example Calculation**:
```
Base Price: $100
Current Demand: 120% of average (Demand Multiplier: 1.10)
Available Inventory: 30% remaining (Inventory Multiplier: 1.14)
Competitor Price: 5% higher (Competitive Multiplier: 0.98)

Dynamic Price = $100 × 1.10 × 1.14 × 0.98 = $123
```

**Machine Learning Enhancements**:
- **Regression Models**: Predict demand based on multiple variables
- **Neural Networks**: Complex pattern recognition for pricing optimization
- **Reinforcement Learning**: Continuous learning and optimization based on outcomes
- **Ensemble Methods**: Combine multiple models for improved accuracy

### Psychological Pricing

**Cognitive Biases in Pricing**:

**1. Anchoring Effect**:
- First price seen becomes reference point
- Use high anchor to make other prices seem reasonable
- Example: Show premium option first, then present standard option

**2. Loss Aversion**:
- People feel losses more strongly than equivalent gains
- Frame as avoiding loss rather than achieving gain
- Example: "Don't miss out on 20% savings" vs. "Save 20%"

**3. Decoy Effect**:
- Add option that makes target option look attractive
- Example: Small ($5), Medium ($6.50), Large ($7) - Medium looks overpriced, drives Large sales

**4. Mental Accounting**:
- People treat money differently based on source/purpose
- Bundle products to reduce separate payment pain
- Example: All-inclusive vacation vs. itemized charges

**Pricing Tactics**:
- **Charm Pricing**: Prices ending in 9 ($19.99 vs. $20.00)
- **Prestige Pricing**: Round numbers for luxury/premium ($500 vs. $499)
- **Bundle Pricing**: Package pricing obscures individual item costs
- **Partitioned Pricing**: Separate base price from fees/options

### Competitive Pricing Strategy

**Competitive Intelligence Framework**:

**Price Monitoring**:
- **Direct Competitors**: Same target market, similar value proposition
- **Indirect Competitors**: Alternative solutions to same customer problem
- **Substitute Products**: Different approaches to solving same need
- **New Entrants**: Disruptive pricing models or technology

**Competitive Response Strategies**:

**1. Price Leadership**:
- Set prices that competitors follow
- Requires strong market position and brand
- Signal pricing moves to avoid price wars

**2. Price Following**:
- Quickly match competitive price moves
- Maintains competitive parity
- Requires efficient competitive intelligence

**3. Value Differentiation**:
- Maintain price premium through superior value
- Focus on non-price competitive advantages
- Requires strong value communication

**4. Niche Focus**:
- Avoid head-to-head price competition
- Focus on underserved segments
- Develop specialized value proposition

### B2B vs. B2C Pricing Differences

**B2B Pricing Characteristics**:
- **Relationship-Based**: Long-term partnerships, negotiated pricing
- **Complex Decision Process**: Multiple stakeholders, formal procurement
- **Customization**: Tailored solutions, professional services
- **Volume Discounts**: Quantity-based pricing, contract terms
- **Value Selling**: ROI justification, business case development

**B2C Pricing Characteristics**:
- **Transaction-Based**: Individual purchase decisions
- **Emotional Factors**: Brand, status, convenience
- **Standardized Pricing**: Limited customization, posted prices
- **Promotional Sensitivity**: Response to sales, discounts
- **Comparison Shopping**: Easy price comparison, online research

### Subscription Pricing Models

**SaaS Pricing Strategies**:

**1. Per-User Pricing**:
- Price per user per month/year
- Scales with customer size
- Example: $25/user/month

**2. Usage-Based Pricing**:
- Price based on consumption
- Aligns price with value received
- Example: $0.10 per transaction

**3. Tiered Pricing**:
- Good/Better/Best packages
- Feature differentiation across tiers
- Example: Basic ($99), Pro ($199), Enterprise ($399)

**4. Freemium**:
- Free basic version + paid premium
- Customer acquisition through free trial
- Example: Free (limited features), Paid ($29/month full features)

**Subscription Metrics**:
```
Monthly Recurring Revenue (MRR) = Monthly Subscriptions × Average Price
Annual Recurring Revenue (ARR) = MRR × 12
Customer Lifetime Value (CLV) = Average Revenue per Customer × Average Customer Lifespan
Customer Acquisition Cost (CAC) = Sales & Marketing Costs / New Customers Acquired
LTV/CAC Ratio = Customer Lifetime Value / Customer Acquisition Cost (target: >3:1)
```

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
  - Main Prompt: `prompts/copilot/prompts/business-management/pricing-revenue-management-consultant.md`
  - Examples: `rag/business-management/pricing-revenue-management-consultant/examples.md`
  - Methodologies: `rag/business-management/pricing-revenue-management-consultant/methodologies.md`
