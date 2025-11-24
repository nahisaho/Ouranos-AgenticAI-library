# Frameworks for Operations Excellence Consultant

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### Lean Manufacturing/Lean Thinking

**Five Principles**:
1. **Value**: Define from customer perspective (what are they willing to pay for?)
2. **Value Stream**: Map all steps to deliver value, eliminate waste
3. **Flow**: Ensure smooth, continuous flow (eliminate batching and queuing)
4. **Pull**: Produce only what customer needs when they need it
5. **Perfection**: Pursue continuous improvement (never-ending Kaizen)

**8 Wastes (DOWNTIME)**:
- **D**efects: Errors requiring rework
- **O**verproduction: Making more than needed or sooner than needed
- **W**aiting: Idle time for people or materials
- **N**on-utilized talent: Underutilizing people's skills
- **T**ransportation: Unnecessary movement of materials
- **I**nventory: Excess stock (WIP, finished goods)
- **M**otion: Unnecessary movement of people
- **E**xtra-processing: Doing more than customer requires

**Example**: Toyota Production System - one-piece flow, Kanban pull, Andon cord, Kaizen culture

### Six Sigma (DMAIC)

**Purpose**: Reduce variation and defects to achieve near-perfect quality (3.4 defects per million opportunities)

**DMAIC Roadmap**:
1. **Define**: Problem, goal, scope, CTQ (Critical to Quality), project charter, Y = f(X)
2. **Measure**: Current performance, data collection plan, measurement system analysis, process capability (Cp/Cpk)
3. **Analyze**: Root causes, vital few Xs, hypothesis testing, regression, DOE (Design of Experiments)
4. **Improve**: Solutions, pilot, validate improvements, update processes
5. **Control**: Control plan, SPC charts, standard work, audits, handoff to process owner

**Key Metrics**:
- **DPMO**: Defects Per Million Opportunities
- **Sigma Level**: 3σ = 66,807 DPMO, 6σ = 3.4 DPMO
- **Cp/Cpk**: Process capability indices (Cp = potential, Cpk = actual accounting for centering)

**Example**: Motorola reducing defects, GE's quality transformation under Jack Welch

### Theory of Constraints (TOC)

**Core Concept**: Every system has at least one constraint that limits throughput. Improve the constraint, improve the system.

**Five Focusing Steps**:
1. **Identify** the constraint (bottleneck - step with lowest capacity)
2. **Exploit** the constraint (maximize its output - minimize downtime, ensure it's never starved)
3. **Subordinate** everything else (pace upstream to constraint's rhythm - don't overproduce)
4. **Elevate** the constraint (increase capacity - add resources, shifts, equipment)
5. **Repeat** (find next constraint, continuous improvement)

**Drum-Buffer-Rope**:
- **Drum**: Constraint sets pace for entire system
- **Buffer**: Protective inventory before constraint (ensure it never starves)
- **Rope**: Signal upstream to release work (pull system tied to constraint)

**Example**: Factory with machining bottleneck - ensure bottleneck runs 24/7, subordinate all other steps to its pace

### Value Stream Mapping

**Purpose**: Visualize entire process from customer order to delivery, identify waste, design future state

**Components**:
- **Process boxes**: Each step in the process
- **Data boxes**: Cycle time (C/T), changeover time (C/O), uptime (%), number of operators, available time, batch size
- **Inventory triangles**: Work in process between steps (quantity, days of supply)
- **Information flow**: How information moves (MRP, forecasts, orders)
- **Timeline**: Value-added time vs. lead time

**Current State → Future State**:
- Eliminate non-value-added steps
- Reduce lot sizes
- Implement pull systems
- Create flow
- Reduce lead time

**Example**: Order-to-cash process - 90 days lead time with only 4 hours value-added time → 15 days lead time after improvements

### Kaizen (Continuous Improvement)

**Philosophy**: Small, incremental improvements continuously applied by everyone

**Kaizen Event** (1-week improvement sprint):
- Day 1: Training, problem definition, current state mapping
- Day 2-3: Root cause analysis, brainstorm solutions, select best
- Day 4: Implement improvements, test
- Day 5: Standardize, train, present results

**Daily Kaizen**:
- Frontline workers empowered to identify and solve problems
- Idea suggestion systems
- Management support and recognition

**Gemba Walks**: Leaders go to where work happens, observe, ask questions, show respect, support improvements

**Example**: Toyota - everyone expected to submit improvement ideas, thousands implemented annually

### 5S Workplace Organization

**Five Steps**:
1. **Sort (Seiri)**: Remove unnecessary items (red tag unneeded items, discard or relocate)
2. **Set in Order (Seiton)**: Organize for efficiency (place for everything, everything in its place - shadow boards, labels, visual controls)
3. **Shine (Seiso)**: Clean and inspect (daily cleaning, identify abnormalities during cleaning)
4. **Standardize (Seiketsu)**: Create standards (checklists, schedules, audits, visual standards)
5. **Sustain (Shitsuke)**: Maintain discipline (training, audits, leadership commitment, culture)

**Benefits**: Improved safety, efficiency, quality; reduced waste; better morale

**Example**: Tool room - shadow boards show exactly where each tool belongs, missing tools immediately obvious

### Overall Equipment Effectiveness (OEE)

**Purpose**: Measure equipment productivity, identify losses

**Formula**: OEE = Availability × Performance × Quality

- **Availability**: Uptime / Planned Production Time (accounts for breakdowns, changeovers)
- **Performance**: Actual Output / Theoretical Max Output (accounts for minor stops, slow cycles)
- **Quality**: Good Units / Total Units (accounts for defects, rework)

**World-Class OEE**: 85%+

**Six Big Losses**:
- Availability: Breakdowns, Changeover/Setup
- Performance: Minor Stops, Slow Cycles
- Quality: Startup Rejects, Production Rejects

**Example**: Machine with 80% availability, 90% performance, 95% quality → OEE = 68.4% (opportunity to improve)

### SMED (Single-Minute Exchange of Die)

**Purpose**: Reduce changeover/setup time to under 10 minutes (single-digit minutes)

**Four Steps**:
1. **Separate internal vs. external setup** (Internal = must be done while machine is stopped; External = can be done while running)
2. **Convert internal to external** (Prepare tools, materials while machine runs)
3. **Streamline internal setup** (Standardize, eliminate adjustments, quick-change mechanisms)
4. **Eliminate setup altogether** (Flexible tooling, smaller lot sizes, universal fixtures)

**Typical Reductions**: 4 hours → 30 minutes → 5 minutes

**Benefits**: Smaller lot sizes, more frequent changeovers, reduced inventory, increased flexibility

**Example**: Formula 1 pit stop - tire change from minutes to under 3 seconds through SMED principles

### Root Cause Analysis

**5 Whys**:
- Problem: Customer received wrong product
- Why? Warehouse picked wrong item
- Why? Bin label was incorrect
- Why? Label wasn't updated after SKU change
- Why? No process for updating labels
- Why? (Root cause): No ownership of label management process
- Solution: Assign ownership, create standard process for label updates

**Fishbone Diagram (Ishikawa)** - Six categories:
- Methods/Processes
- Machines/Equipment
- Materials
- Manpower/People
- Measurement
- Mother Nature/Environment

**Pareto Analysis**: 80% of problems come from 20% of causes - focus on vital few

### Process Capability Analysis

**Purpose**: Measure whether process can meet specifications

**Specifications**: Upper Spec Limit (USL), Lower Spec Limit (LSL) - customer requirements

**Process Performance**: Mean (μ), Standard Deviation (σ) - actual process

**Cp (Potential Capability)**:
- Cp = (USL - LSL) / 6σ
- Measures variation vs. spec width (ignores centering)
- Cp > 1.33 is good (4σ)

**Cpk (Actual Capability)**:
- Cpk = min[(USL - μ)/3σ, (μ - LSL)/3σ]
- Accounts for centering
- Cpk > 1.33 is good; > 2.0 is world-class (6σ)

**Sigma Level**: Higher = better
- 3σ: 66,807 DPMO (93.3% yield)
- 4σ: 6,210 DPMO (99.4% yield)
- 5σ: 233 DPMO (99.98% yield)
- 6σ: 3.4 DPMO (99.9997% yield)

**Example**: Bolt diameter spec 10mm ±0.1mm. Process produces mean 10mm, σ = 0.02mm
- Cp = 0.2 / (6 × 0.02) = 1.67 (good potential)
- If mean drifts to 10.05mm, Cpk drops significantly (need centering)

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
  - Main Prompt: `prompts/copilot/prompts/business-management/operations-excellence-consultant.md`
  - Examples: `rag/business-management/operations-excellence-consultant/examples.md`
  - Methodologies: `rag/business-management/operations-excellence-consultant/methodologies.md`
