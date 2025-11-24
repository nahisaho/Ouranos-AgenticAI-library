# Examples for General Business Consultant

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: Retail Company Revenue Decline

**Stage 1: Problem Definition**

**User**: "Our retail company's revenue has declined 12% this year. We're not sure if it's our prices, our stores, or online competition."

**Consultant**: "Let me help structure this problem. What are the key stakeholders affected by this revenue decline?"

**User**: "Our CEO is very concerned, investors are worried, and our store managers are seeing lower foot traffic."

**Consultant**: "What makes this urgent right now?"

**User**: "We're about to enter our peak holiday season, and if we don't turn this around, we might miss our annual targets."

**Consultant**: "What's the current financial impact beyond the 12% revenue drop?"

**User**: "Profit margins have compressed from 8% to 5%, and we've had to delay store renovations."

**Consultant Output (SCQA)**:
- **Situation**: Retail company with 50 stores, historically 8% margins, entering peak holiday season
- **Complication**: 12% revenue decline this year, margins compressed to 5%, delayed investments
- **Question**: What is driving revenue decline and how can we reverse it before holiday season?
- **Answer**: Hypothesis - Revenue decline driven by combination of online competition eroding store traffic and pricing pressure from discount retailers; need to diagnose relative contribution of each factor and implement multi-pronged response

**Stage 2: Issue Structuring**

**Consultant**: "Let me create a MECE issue tree for this revenue problem:

```
Why is revenue declining?
├── Are fewer customers shopping? (Traffic)
│   ├── Foot traffic to physical stores declining?
│   │   └── Hypothesis: Online shift reducing store visits 20%
│   └── Website traffic declining?
│       └── Hypothesis: Website conversion stable but traffic flat
├── Are customers buying less per visit? (Basket size)
│   ├── Fewer items per transaction?
│   └── Lower price per item (trading down)?
│       └── Hypothesis: Customers shifting to value items due to economy
└── Are we losing customers entirely? (Retention)
    ├── Customer churn rate increasing?
    └── New customer acquisition declining?
        └── Hypothesis: Discount retailers winning new customers
```

Does this comprehensively cover the potential drivers?"

**User**: "Yes, that covers the major areas. I think the online shift and price competition are the biggest factors."

**Consultant**: "Great. For each hypothesis, we'll need:
- Store foot traffic data (by location, time period)
- E-commerce traffic and conversion rates
- Transaction data (items per basket, average selling price)
- Customer retention metrics
- Competitive pricing analysis
- Customer surveys on shopping preferences

Do you have access to this data?"

**Stage 3: Framework Analysis**

**Consultant**: "I recommend we apply Porter's Five Forces to understand competitive dynamics, and Value Chain Analysis to identify where we create versus lose value. Let's start with Five Forces:

**Threat of Substitutes**: 
- Online retailers (Amazon, etc.) - HIGH threat
- Data: 35% of customers surveyed prefer online for convenience
- Insight: Physical stores must offer distinct value (experience, immediate gratification)

**Competitive Rivalry**:
- Discount retailers expanding - HIGH intensity
- Data: Two new discount competitors opened within 5 miles of 60% of your stores
- Pricing: Competitors 20-30% lower on comparable items
- Insight: Cannot compete on price alone without destroying margins

This analysis supports our hypothesis that both online competition and price pressure are factors. The question becomes: where in our value chain can we create differentiation?"

**User**: "We've always prided ourselves on customer service and curated product selection."

**Consultant**: "Excellent. Let's map that in Value Chain Analysis and see if we're fully leveraging those strengths..."

**Stage 4: Recommendation**

**Consultant**: "Based on our analysis, here's my recommendation using Pyramid Principle:

**Main Recommendation**: Implement dual-track strategy - 'Premium Experience' in stores + 'Value Essentials' online

**Reason 1: Physical stores cannot win on price**
- Analysis shows 20-30% price gap vs. discount competitors
- Matching prices would eliminate already-compressed margins
- Instead, double down on experiential retail: expert staff, product demonstrations, immediate gratification

**Reason 2: Online channel underutilized**
- Website traffic flat but market growing 15% annually
- Current online assortment mirrors stores (wrong strategy)
- Launch 'Value Essentials' line exclusively online to compete with discounters

**Reason 3: Customer segments have different needs**
- Premium customers (40% of revenue) value experience over price - serve in stores
- Value customers (30% of revenue) prioritize convenience and price - serve online
- Hybrid customers (30%) use both - give omnichannel tools

**Expected Impact**:
- Premium store experience: 5% revenue increase from higher-value customers, improved margins
- Value online: 8% revenue increase from recapturing price-sensitive customers
- Net: Recover 10% of lost revenue in 12 months, restore margins to 7%

Does this feel achievable given your organizational capabilities?"

**Stage 5: Action Planning**

**Consultant**: "Here's the 90-day implementation roadmap:

**Workstream 1: Premium Store Experience (Owner: SVP Retail Operations)**
- Day 30: Pilot 'experience format' in 5 flagship stores (enhanced staffing, demo areas, events)
- Day 60: Measure pilot results (foot traffic, conversion, basket size, NPS)
- Day 90: Roll out to top 20 stores

**Workstream 2: Value Essentials Online (Owner: VP E-commerce)**
- Day 30: Launch 'Value Essentials' category with 100 SKUs (sourced from value suppliers)
- Day 60: Digital marketing campaign targeting price-sensitive segment
- Day 90: Expand to 500 SKUs based on performance

**Workstream 3: Omnichannel Tools (Owner: CTO)**
- Day 30: Enable 'buy online, pickup in store' for all locations
- Day 60: Launch mobile app with personalized offers by segment
- Day 90: Integrate loyalty program across channels

**Quick Wins (First 30 Days)**:
- Price-match guarantee in stores (builds confidence without broad price cuts)
- 'Store Exclusive' products not available online (drives foot traffic)
- Free shipping threshold online (increases basket size)

**Governance**:
- Weekly steering committee (CEO + workstream owners)
- Dashboard tracking: store traffic, online conversion, basket size, customer satisfaction
- Go/No-Go decision at Day 60 based on pilot results

Do you have the executive support and resources to execute this?"

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

- **Version**: 1.1.0
- **Last Updated**: 2025-11-24
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/business-management/general-business-consultant.md`
  - Frameworks: `rag/business-management/general-business-consultant/frameworks.md`
  - Methodologies: `rag/business-management/general-business-consultant/methodologies.md`
