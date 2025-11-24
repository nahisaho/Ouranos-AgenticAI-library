# Frameworks for Risk Management Bcp Consultant

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### Enterprise Risk Management (ERM) Framework

**Purpose**: Systematic approach to identify, assess, prioritize, and manage all risks across the enterprise

**Benefits**:
- Comprehensive view of all risks (not siloed)
- Informed decision-making (risk-reward trade-offs)
- Reduced surprises (proactive identification)
- Improved resilience (prepared for disruptions)
- Regulatory compliance (meet governance requirements)

**COSO ERM Framework** (Committee of Sponsoring Organizations):

**Five Components**:
1. **Governance and Culture**: Tone from top, oversight, risk culture
2. **Strategy and Objective-Setting**: Risk appetite, strategic risk, goal alignment
3. **Performance**: Risk identification, assessment, prioritization, response
4. **Review and Revision**: Monitor, evaluate, improve
5. **Information, Communication, and Reporting**: Data, reporting, transparency

**Twenty Principles** across five components (e.g., 'Exercise board oversight', 'Define risk appetite', 'Identify risks', etc.)

### ISO 31000 Risk Management

**International standard** for risk management

**Principles**:
- Integrated (part of all activities)
- Structured and comprehensive
- Customized (tailored to context)
- Inclusive (stakeholder involvement)
- Dynamic (responds to changes)
- Best available information
- Human and cultural factors
- Continual improvement

**Process**:
1. **Scope, Context, Criteria**: Define what you're managing, internal/external context, risk criteria
2. **Risk Assessment**:
   - Identification
   - Analysis (likelihood, consequences)
   - Evaluation (compare to criteria, prioritize)
3. **Risk Treatment**: Select and implement options (avoid, reduce, transfer, accept)
4. **Monitoring and Review**: Ongoing tracking
5. **Communication and Consultation**: Throughout process

### Risk Matrix (Likelihood vs. Impact)

**Purpose**: Visual tool to assess and prioritize risks

**Axes**:
- **X-axis: Likelihood** (Rare, Unlikely, Possible, Likely, Almost Certain) or (1-5 scale)
- **Y-axis: Impact** (Insignificant, Minor, Moderate, Major, Catastrophic) or (1-5 scale)

**Risk Score** = Likelihood × Impact (or Likelihood + Impact depending on methodology)

**Example 5×5 Risk Matrix**:
```
Impact
  ^
5 | 5  10  15  20  25  <- Extreme (red)
4 | 4   8  12  16  20
3 | 3   6   9  12  15  <- High (orange)
2 | 2   4   6   8  10  <- Medium (yellow)
1 | 1   2   3   4   5  <- Low (green)
  +-------------------->
    1   2   3   4   5   Likelihood
```

**Risk Levels**:
- **Extreme (20-25)**: Immediate action required, executive escalation
- **High (12-19)**: Senior management attention, mitigation plan required
- **Medium (6-11)**: Management monitoring, mitigation considered
- **Low (1-5)**: Routine management, accept or monitor

**Inherent vs. Residual Risk**:
- Plot same risk twice: before controls (inherent) and after controls (residual)
- Shows effectiveness of controls

### Business Impact Analysis (BIA)

**Purpose**: Identify and quantify impact of disruptions to business processes

**Steps**:
1. **Identify Critical Processes**: What does the business do?
2. **Assess Impact Over Time**: What happens if each process stops? (0-4h, 4-24h, 1-7d, >7d)
3. **Define Recovery Objectives**:
   - **RTO (Recovery Time Objective)**: Max acceptable downtime
   - **RPO (Recovery Point Objective)**: Max acceptable data loss
4. **Identify Dependencies**: What resources required? (people, technology, facilities, suppliers)
5. **Prioritize**: Which processes must recover first?

**Impact Categories**:
- Financial (quantify: $/hour or $/day)
- Operational (service degradation, backlog)
- Reputational (customer trust, brand)
- Regulatory/Legal (violations, fines)
- Safety (health/safety risk)

**Criticality Tiers**:
- Tier 1: RTO 0-4 hours (mission-critical)
- Tier 2: RTO 4-24 hours (business-critical)
- Tier 3: RTO 1-7 days (important)
- Tier 4: RTO >7 days (non-critical)

### Business Continuity Planning (BCP)

**Purpose**: Ensure critical business functions continue during and after disruption

**BCP vs. DRP**:
- **BCP**: Broader - all business processes (people, facilities, suppliers, workflows)
- **DRP**: Narrower - IT systems and data recovery (subset of BCP)

**BCP Lifecycle**:
1. **Prevention/Mitigation**: Reduce likelihood (redundancy, preventive maintenance, security)
2. **Preparedness**: Ready to respond (plans, training, supplies, communication)
3. **Response**: Immediate actions (assess, activate plan, ensure safety, workarounds)
4. **Recovery**: Restore operations (priority based on RTO, failover to backups)
5. **Return to Normal**: Resume full operations, replenish, post-incident review

**Key Components**:
- Emergency response procedures (evacuation, first aid, safety)
- Crisis management team and roles
- Communication plan (internal, external)
- Alternate operating strategies (backup sites, remote work, alternate suppliers)
- Recovery procedures (step-by-step)
- Critical resource inventory (people, technology, facilities)

### Disaster Recovery Planning (DRP)

**Purpose**: Restore IT systems and data after disruption

**Backup Strategy**:
- **Full Backup**: Complete copy (weekly)
- **Incremental Backup**: Changes since last backup (daily)
- **Differential Backup**: Changes since last full backup
- **Continuous Replication**: Real-time sync (for critical systems)

**Backup Rule: 3-2-1**:
- **3 copies** of data (original + 2 backups)
- **2 different media** types (disk + tape, or disk + cloud)
- **1 off-site** copy (geographically separated)

**DR Site Options**:
- **Hot Site**: Fully equipped, real-time replication, immediate failover (<1 hour RTO, highest cost)
- **Warm Site**: Partially equipped, daily backups, manual failover (4-24 hour RTO, moderate cost)
- **Cold Site**: Empty space, restore from backups (>24 hour RTO, low cost)
- **Cloud-based DR**: Elastic, pay-as-you-go, scalable

**DR Testing**:
- Test restores regularly (monthly) - ensure backups work
- Full DR test annually - actually failover and operate from DR site

### Three Lines of Defense Model

**Purpose**: Clear delineation of risk management roles and responsibilities

**First Line: Operational Management (Risk Owners)**:
- Own and manage risks
- Implement controls
- Execute business processes
- Report status

**Second Line: Risk Management and Compliance (Risk Oversight)**:
- Design risk framework
- Facilitate risk assessments
- Monitor and report on risks
- Challenge First Line
- Provide guidance and training
- Functions: CRO, Compliance, Legal, Finance, Quality

**Third Line: Internal Audit (Independent Assurance)**:
- Independent evaluation
- Audit risk processes and controls
- Report to Board/Audit Committee
- Validate effectiveness of First and Second Lines

**Key Principle**: Lines don't blur - clear separation of duties, no conflicts

### Crisis Management Framework

**Purpose**: Structured approach to manage acute, high-impact incidents

**Crisis Characteristics**:
- Threatens core objectives (financial, operational, reputational, safety)
- Requires urgent action (time pressure)
- Ambiguous information (incomplete, conflicting)
- High stakes decision-making

**Crisis Management Team (CMT)**:
- **Crisis Manager/Incident Commander**: Overall authority, strategic decisions
- **Subject Matter Experts**: Relevant expertise (IT, Legal, Operations, etc.)
- **Communication Lead**: Internal/external communications
- **Note-taker/Scribe**: Document decisions, actions

**Crisis Management Process**:
1. **Detection and Notification**: Identify crisis, alert CMT
2. **Assessment**: Gather information, assess severity and scope
3. **Activation**: Declare crisis, convene CMT, activate crisis plans
4. **Response**: Implement response actions, ensure safety, contain damage
5. **Communication**: Internal (employees) + External (customers, regulators, media)
6. **Recovery**: Transition from crisis response to recovery
7. **Post-Crisis Review**: Lessons learned, improve plans

**Communication Principles**:
- **Timely**: Communicate early and often
- **Transparent**: Honest about what you know and don't know
- **Consistent**: One voice, coordinated messaging
- **Empathetic**: Acknowledge impact on stakeholders

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
  - Main Prompt: `prompts/copilot/prompts/business-management/risk-management-bcp-consultant.md`
  - Examples: `rag/business-management/risk-management-bcp-consultant/examples.md`
  - Methodologies: `rag/business-management/risk-management-bcp-consultant/methodologies.md`
