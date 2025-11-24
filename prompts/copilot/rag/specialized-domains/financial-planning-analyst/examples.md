# Examples for Financial Planning Analyst

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: SaaS Company FY2026 Budget

**Stage 1: Context**

**Company**: B2B SaaS, $10M ARR, 40% growth, burning $200K/month

**Goals**: Reach profitability by end of FY2026, grow to $15M ARR

**Stage 2: Budget**

**Revenue Budget**:
- Beginning ARR: $10M
- New bookings: $7M (targeting 50% growth)
- Churn: -$1.5M (reduce from 15% to 10%)
- Expansion: $1.5M
- **Ending ARR: $17M** (70% growth—exceeds goal)

**Expense Budget**:
- COGS: 20% of revenue → $3.4M
- S&M: 35% → $6M (hire 10 sales reps)
- R&D: 25% → $4.25M (hire 8 engineers)
- G&A: 15% → $2.55M
- **Total OpEx: $16.2M**
- **Operating Income: $17M - $3.4M - $16.2M = -$2.6M** (still burning, but improving from -$4M in FY2025)

**Stage 3: Actuals and Variance (Q1 Review)**

**Q1 Actuals**:
- Revenue: $3.8M (budget: $4M, -5%)
- OpEx: $4M (budget: $4.05M, under budget)
- **Operating loss: -$200K** (better than budget -$250K due to expense control)

**Variance**: Revenue miss due to 2 large deals slipping to Q2

**Updated Forecast**: Lower FY2026 revenue to $16M (still 60% growth)

**Stage 4: Investment Analysis**

**Opportunity**: Invest $500K in customer success team to reduce churn from 10% to 7%

**NPV Analysis**:
- Investment: $500K (hire 5 CSMs)
- Benefit: 3% churn reduction = $300K ARR saved per year
- 3-year benefit: $900K (present value ~$750K)
- **NPV: $750K - $500K = $250K** (positive, invest!)

**Stage 5: Business Partnership**

**Monthly Review with VP Sales**:
- FP&A shares pipeline analysis: $8M in pipeline, 25% win rate → expect $2M bookings in Q2
- Recommendation: Focus on enterprise deals (higher win rate, larger deal size)
- Result: Sales adjusts strategy, Q2 beats target

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
  - Main Prompt: `prompts/copilot/prompts/specialized-domains/financial-planning-analyst.md`
  - Frameworks: `rag/specialized-domains/financial-planning-analyst/frameworks.md`
  - Methodologies: `rag/specialized-domains/financial-planning-analyst/methodologies.md`
