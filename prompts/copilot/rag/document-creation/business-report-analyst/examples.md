# Examples for Business Report Analyst

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

### Scenario: Q3 Sales Performance Analysis for Executive Team

**Stage 1: Report Purpose and Audience**

**Purpose**: Analyze Q3 sales performance and recommend actions for Q4
**Audience**: CEO, VP Sales, VP Marketing
**Key Questions**:
- Did we meet Q3 sales targets?
- What drove performance (positive or negative)?
- What should we do in Q4?
**Data**: CRM data, financial reports, market research

**Stage 2: Analysis and Insight Development**

**Data Collected**:
- Q3 sales: $5.2M (target: $5.0M, +4%)
- Q3 2024 sales: $4.5M (YoY growth: +15.6%)
- Breakdown by region, product, customer segment

**Key Insights Developed**:
1. **Exceeded target due to enterprise segment growth**: Enterprise customers grew from 50 to 72 (+44%), avg deal size $95K
2. **SMB segment underperforming**: SMB customers flat (500 vs. 495), churn up to 15% from 10%
3. **New product driving growth**: 30% of Q3 revenue from product launched in May
4. **West region outperforms**: West $2.1M (+25% YoY), East $1.8M (+5% YoY)

**Stage 3: Report Structure**

**Outline**:
```
Executive Summary (SCQA format)
Key Findings
├── 1. Q3 exceeded target by 4%, up 15.6% YoY
├── 2. Enterprise segment growth (+44%) offset SMB weakness
├── 3. New product accounts for 30% of revenue
└── 4. Regional performance varies: West strong, East flat
Recommendations
├── 1. Double down on enterprise: Hire 2 enterprise AEs
├── 2. Address SMB churn: Launch retention program
└── 3. Expand West region approach to East
Detailed Analysis
└── [Supporting data and charts]
```

**Stage 4: Data Visualization**

**Visualizations Created**:
1. **KPI Scorecard**: Revenue, Customer Count, ARPU, Churn (with vs. target indicators)
2. **Revenue Trend Line Chart**: Shows Q3 peak, annotated with "New product launch"
3. **Segment Comparison Bar Chart**: Enterprise vs. SMB, highlights enterprise growth
4. **Regional Map**: Color-coded by performance (West green, East yellow)
5. **Product Mix Pie Chart**: New product 30%, existing products breakdown

**Stage 5: Writing and Delivery**

**Executive Summary** (excerpt):

"Q3 sales of $5.2M exceeded our $5.0M target and grew 15.6% year-over-year, driven primarily by strong enterprise customer acquisition. However, this success masks a troubling trend: small business customer churn has increased to 15%, putting $1M in annual revenue at risk.

Key Findings:
1. Enterprise segment grew 44% (50 to 72 customers), averaging $95K per deal
2. SMB customer count flat; churn increased from 10% to 15%
3. New product launched in May accounts for 30% of Q3 revenue
4. West region sales up 25% YoY while East region only up 5%

Recommendations:
1. Hire 2 additional enterprise account executives to capitalize on momentum (Priority: High)
2. Launch targeted SMB retention program to address churn (Priority: High)
3. Apply West region best practices to East region (Priority: Medium)"

**Delivered**:
- PDF report emailed to exec team
- 30-minute presentation at exec meeting
- Interactive dashboard published for ongoing monitoring

**Outcome**:
- Approved hiring of 2 enterprise AEs
- Allocated $50K budget for SMB retention program
- Scheduled follow-up in Q4 to assess impact

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
  - Main Prompt: `prompts/copilot/prompts/document-creation/business-report-analyst.md`
  - Frameworks: `rag/document-creation/business-report-analyst/frameworks.md`
  - Methodologies: `rag/document-creation/business-report-analyst/methodologies.md`
