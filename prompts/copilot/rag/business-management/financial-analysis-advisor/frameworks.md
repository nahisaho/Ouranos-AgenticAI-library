# Frameworks for Financial Analysis Advisor

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### DuPont Analysis Framework

**Purpose**: Decompose ROE to understand drivers of profitability

**Formula**: ROE = Net Margin × Asset Turnover × Equity Multiplier

ROE = (Net Income/Revenue) × (Revenue/Assets) × (Assets/Equity)

**Components**:

1. **Net Margin**: Profitability (operations and cost control)
2. **Asset Turnover**: Efficiency (asset utilization)
3. **Equity Multiplier**: Leverage (financial structure)

**Application**:
- Identify which component drives ROE
- Compare to competitors and history
- Target improvements in specific areas

### Financial Modeling Best Practices

**Model Structure**:

1. **Assumptions Sheet**: All key inputs in one place
2. **Historical Financials**: Actual historical data
3. **Projections**: Income statement, balance sheet, cash flow
4. **Supporting Schedules**: Debt schedule, working capital, depreciation
5. **Valuation**: DCF, comparable analysis
6. **Outputs**: Summary and charts

**Modeling Principles**:
- Separate inputs, calculations, outputs
- Use consistent formatting and structure
- Include clear documentation
- Build in error checks
- Enable sensitivity analysis
- Keep formulas simple and transparent

### Scenario Analysis Framework

**Purpose**: Assess range of outcomes under different assumptions

**Scenarios**:

**Base Case**: Most likely outcome
- Reasonable growth assumptions
- Normal operating conditions
- Expected market conditions

**Upside Case**: Optimistic scenario
- Accelerated growth
- Margin expansion
- Favorable market conditions

**Downside Case**: Pessimistic scenario
- Slower growth or decline
- Margin compression
- Adverse market conditions

**Stress Case**: Severe adverse scenario
- Recession or crisis
- Major competitive threat
- Significant disruption

**Analysis**:
- Calculate outcomes for each scenario
- Assess probability of each
- Determine risk/reward profile
- Identify key sensitivities

### Working Capital Management

**Components**:

- **Accounts Receivable**: Money owed by customers
- **Inventory**: Products held for sale
- **Accounts Payable**: Money owed to suppliers

**Net Working Capital = Current Assets - Current Liabilities**

**Optimization**:
- Reduce DSO (collect faster)
- Reduce DIO (turn inventory faster)
- Extend DPO (pay suppliers strategically)
- Minimize cash conversion cycle

**Impact**: Frees up cash for growth and operations

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
  - Main Prompt: `prompts/copilot/prompts/business-management/financial-analysis-advisor.md`
  - Examples: `rag/business-management/financial-analysis-advisor/examples.md`
  - Methodologies: `rag/business-management/financial-analysis-advisor/methodologies.md`
