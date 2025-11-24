# Methodologies for Meta-Prompt Generator

This file provides step-by-step procedures, generation processes, validation checklists, and best practices for creating effective meta-prompts.

---

## Meta-Prompt Generation Process

### Overview

The meta-prompt generation process consists of five major phases, executed sequentially after completing the 4-stage dialogue with the user.

---

## Phase 1: Analysis and Planning

### Step 1.1: Review Gathered Information

**Objective**: Consolidate all information gathered during the 4-stage dialogue.

**Actions**:
1. Review Stage 1 outputs (objectives, deliverables, success criteria)
2. Review Stage 2 outputs (domain context, user profiles, constraints)
3. Review Stage 3 outputs (framework selections, integration strategy, stage structure)
4. Review Stage 4 outputs (dialogue approach, special features, final confirmations)

**Checklist**:
- [ ] Objective is clear and measurable
- [ ] Target users are well-defined
- [ ] Domain context is sufficient
- [ ] Constraints are explicitly stated
- [ ] Frameworks are appropriate for the objective
- [ ] Integration strategy is logical
- [ ] Stage structure supports the workflow
- [ ] Special features are documented

---

### Step 1.2: Create Generation Plan

**Objective**: Design the structure and content outline for the meta-prompt.

**Template**:
```markdown
# Generation Plan for [Prompt Name]

## Basic Information
- ID: [prompt-id]
- Category: [category]
- Target Domain: [domain]
- Complexity Level: [simple/medium/complex]

## Structure
- Number of Stages: [X]
- Dialogue Approach: [one-question-at-a-time / multiple-questions]
- Estimated Session Time: [X minutes]

## Frameworks
1. [Framework 1]: [Purpose and integration point]
2. [Framework 2]: [Purpose and integration point]
...

## Stage Breakdown
### Stage 1: [Name]
- Goal: [Specific objective]
- Key Questions: [List 3-5 main questions]
- Frameworks Used: [Which frameworks apply]
- Output: [What user receives]

[Repeat for all stages]

## Special Features
- [ ] Domain-specific examples
- [ ] Best practices section
- [ ] Common pitfalls warnings
- [ ] Industry benchmarks
- [ ] Templates/formats
- [ ] Other: [Specify]

## Output Format
[Describe final deliverable structure]
```

---

## Phase 2: YAML Front Matter Creation

### Step 2.1: Generate Metadata

**Objective**: Create accurate, complete YAML front matter.

**Template**:
```yaml
---
id: [descriptive-kebab-case-id]
category: [general|business-management|design-development|hr-organization|education|research|document-creation|social-policy|communication|innovation-transformation|specialized-domains]
frameworks:
  - [Framework 1]
  - [Framework 2]
  - [Framework N]
dialogue_stages: [number]
version: 1.0.0
tags:
  - [tag1]
  - [tag2]
  - [tag3]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
---
```

**Field Guidelines**:

- **id**: Lowercase, hyphen-separated, descriptive (e.g., `business-strategy-consultant`, `project-management-advisor`)
- **category**: Choose from 11 predefined categories
- **frameworks**: List all frameworks used (maintain consistent naming)
- **dialogue_stages**: Number of dialogue stages (typically 3-7)
- **version**: Start with 1.0.0 (follow semantic versioning)
- **tags**: 3-5 descriptive tags for searchability
- **created/updated**: ISO date format (YYYY-MM-DD)

---

## Phase 3: Content Generation

### Step 3.1: Write Role Definition

**Objective**: Clearly define the AI's role, expertise, and mission.

**Template**:
```markdown
## Role

You are [role description with expertise level].
Your mission is to [clear statement of purpose].

Your expertise:
- [Expertise area 1]
- [Expertise area 2]
- [Expertise area 3]
- [Expertise area 4]
```

**Best Practices**:
- Use active, confident language
- Be specific about domain expertise
- State the mission clearly (what user will achieve)
- List 4-6 key expertise areas
- Match expertise level to target users

**Examples**:

**Good**:
```markdown
## Role

You are an experienced business strategy consultant specializing in B2B SaaS companies.
Your mission is to guide business owners through comprehensive strategic planning
using proven frameworks and best practices.

Your expertise:
- B2B SaaS business models and metrics (MRR, CAC, LTV, churn)
- Strategic frameworks (PEST, Porter's Five Forces, Value Chain, SWOT, BMC)
- Market analysis and competitive positioning
- Strategic planning and execution
```

**Poor** (too vague):
```markdown
## Role

You are a business expert. Your mission is to help with business planning.

Your expertise:
- Business
- Strategy
- Planning
```

---

### Step 3.2: Build Dialogue Flow Section

**Objective**: Create detailed, actionable dialogue structure for each stage.

**Stage Template**:
```markdown
### Stage [X]: [Stage Name]

**Important**: [Note about one-question-at-a-time approach, if applicable]

Ask: "[First question - open-ended to establish broad understanding]"

Then: "[Second question - builds on first answer, adds specificity]"

Follow with: "[Third question - probes deeper or covers complementary aspect]"

Ask: "[Fourth question - final key question for this stage]"

**Stage Output**: [What AI delivers at end of stage - summary, artifact, confirmation]
```

**Best Practices**:

1. **Start Broad, Get Specific**: First question should be open-ended
2. **Build Sequentially**: Each question builds on previous answers
3. **Use Clear Transitions**: "Then", "Follow with", "Ask" signal progression
4. **Include Context**: Explain why the question matters (occasionally)
5. **Provide Stage Output**: Clear deliverable at each stage end
6. **Confirm Before Proceeding**: Always verify understanding before next stage

**Question Quality Guidelines**:

**Good Questions** (open, specific, actionable):
- "What is the ultimate goal you want to achieve with this project?"
- "Which specific customer segment are you targeting, and what problem do they face?"
- "What constraints (time, budget, technical) do we need to work within?"

**Poor Questions** (vague, yes/no, too broad):
- "Is this a good idea?" (yes/no)
- "Tell me everything about your business" (too broad)
- "What do you think?" (vague)

**Example Stage** (well-structured):
```markdown
### Stage 2: Understanding Customer Needs

**Important**: Ask questions **one at a time** and wait for responses.

Ask: "Who is your primary customer? Describe a specific person or company that
represents your ideal customer."

Then: "What specific problem or pain point does this customer face in their daily
work or life? How do they currently try to solve this problem?"

Follow with: "What would change for them if this problem were solved? What would
success look like from their perspective?"

Ask: "What have you learned from talking to these customers? What did they say
they need vs. what do you observe they actually need?"

**Stage Output**: Create a customer profile including: demographic/firmographic
details, primary pain point, current alternatives, desired outcome, key insights
from customer conversations. Confirm with user before proceeding to Stage 3.
```

---

### Step 3.3: Write Applied Expertise and Frameworks Section

**Objective**: Provide detailed, actionable explanations of each framework used in the prompt.

**Framework Explanation Template**:
```markdown
### [Framework Name]

**What it is**: [1-2 sentence definition]

**When to use it**: [Specific situations where this framework adds value]

**How to apply it**:
1. [Step 1 with specific guidance]
2. [Step 2 with specific guidance]
3. [Step 3 with specific guidance]
4. [Step N with specific guidance]

**Key Components**:
- **[Component 1]**: [Explanation]
- **[Component 2]**: [Explanation]
- **[Component 3]**: [Explanation]

**Example**: [Concrete example in target domain]

**Best Practices**:
- [Practice 1]
- [Practice 2]
- [Practice 3]

**Common Pitfalls**:
- [Pitfall 1 to avoid]
- [Pitfall 2 to avoid]
```

**Example** (SWOT Analysis for B2B SaaS):
```markdown
### SWOT Analysis

**What it is**: A strategic planning framework that examines internal Strengths
and Weaknesses, and external Opportunities and Threats to inform strategic decisions.

**When to use it**: When assessing overall strategic position, making major decisions
(market entry, product launch, pivot), or conducting strategic reviews.

**How to apply it**:
1. Strengths: Identify internal capabilities, resources, and advantages (e.g., unique
   technology, strong customer relationships, efficient processes)
2. Weaknesses: Recognize internal limitations and areas for improvement (e.g., limited
   resources, skill gaps, technical debt)
3. Opportunities: Spot external favorable conditions and trends (e.g., market growth,
   regulatory changes, competitor weaknesses)
4. Threats: Identify external risks and challenges (e.g., new competitors, market
   shifts, economic downturns)

**Key Components**:
- **Strengths**: Internal positive attributes (e.g., "Our API is 10x faster than competitors")
- **Weaknesses**: Internal limitations (e.g., "Our sales team lacks enterprise experience")
- **Opportunities**: External favorable trends (e.g., "Remote work is driving demand for our product")
- **Threats**: External risks (e.g., "Major competitor just raised $100M")

**Example** (B2B SaaS startup):

| Strengths | Weaknesses |
|-----------|------------|
| Innovative AI-powered analytics | Limited brand recognition |
| Strong product-market fit | Small sales team |
| High customer retention (98%) | Narrow product line |

| Opportunities | Threats |
|---------------|---------|
| Growing market ($2B → $5B by 2027) | Well-funded competitors |
| Partnerships with industry leaders | Potential economic recession |
| Expansion into adjacent markets | Regulatory changes (data privacy) |

**Best Practices**:
- Be honest about weaknesses (you can't fix what you don't acknowledge)
- Quantify where possible (e.g., "98% retention" vs. "good retention")
- Focus on actionable items (avoid abstract observations)
- Involve diverse perspectives (don't do this alone)
- Time-bound your analysis (market conditions change)

**Common Pitfalls**:
- Confusing internal vs. external factors (weakness ≠ threat)
- Listing too many items (focus on top 3-5 per quadrant)
- Failing to act on insights (SWOT without strategy is pointless)
- Being overly optimistic about strengths, pessimistic about weaknesses
```

---

### Step 3.4: Create Output Format Section

**Objective**: Specify exactly what the final deliverable should look like.

**Template**:
```markdown
## Output Format

The final deliverable will be a [document type] with the following structure:

### 1. [Section Name]
**Purpose**: [Why this section exists]
**Content**:
- [Element 1]: [Description]
- [Element 2]: [Description]
- [Element 3]: [Description]

**Example**:
[Show sample of this section]

### 2. [Section Name]
[Repeat structure]

---

**Quality Checkpoints**:
- [ ] [Quality criterion 1]
- [ ] [Quality criterion 2]
- [ ] [Quality criterion 3]

---

**Template** (optional):
[Provide actual template users can fill in]
```

**Example** (Strategy Document):
```markdown
## Output Format

The final deliverable will be a comprehensive strategy document with the following structure:

### 1. Executive Summary (1-2 pages)
**Purpose**: Provide leadership-level overview of strategic analysis and key decisions
**Content**:
- Current business state (3-4 sentences)
- Key strategic insights (top 3 findings from analysis)
- Strategic priorities (top 3 actions for next 90 days)
- Expected outcomes (what success looks like)

**Example**:
"[Company] is a B2B SaaS provider in the healthcare monitoring space, currently
serving 150 hospital clients with $2.5M ARR and 15% monthly growth. Our analysis
reveals three key insights: (1) we have strong product-market fit in mid-size
hospitals but are underserving enterprise segment, (2) our competitive advantage
is speed-to-value but we're not effectively communicating this, (3) we're losing
deals primarily on integration capabilities, not core features. Our top priorities
for Q2 2025 are: (1) develop integration with top 3 EHR systems, (2) create enterprise
sales playbook, (3) refine value proposition messaging around speed-to-value."

### 2. Environmental Analysis (3-5 pages)
**Purpose**: Document external factors affecting strategy
**Content**:
- **PEST Analysis**: Political, Economic, Social, Technological factors with impact rating
- **Porter's Five Forces**: Competitive dynamics with strength rating
- **Market Trends**: Top 3-5 trends with implications for strategy
- **Opportunities & Threats**: Prioritized list with response strategies

### 3. Internal Assessment (2-3 pages)
[Continue pattern...]

---

**Quality Checkpoints**:
- [ ] Executive summary is readable by non-expert
- [ ] Analysis is data-driven (includes metrics, not just opinions)
- [ ] Insights are actionable (not just observations)
- [ ] Recommendations are specific (who, what, when, how)
- [ ] Risks and mitigation strategies are included
- [ ] Document is professional and well-formatted
```

---

### Step 3.5: Add Usage Examples (Optional but Recommended)

**Objective**: Provide concrete walkthrough of how the prompt works in practice.

**Template**:
```markdown
## Usage Example

### Scenario: [Realistic use case]

**Context**: [Brief background]

**Stage 1: [Name]**
- **AI**: "[Question]"
- **User**: "[Response]"
- **AI**: "[Follow-up]"
- **User**: "[Response]"
[Show 2-3 exchanges per stage]

**Stage 2: [Name]**
[Repeat pattern]

**Outcome**: [What was produced]
```

**Best Practices**:
- Choose realistic, relatable scenarios
- Show natural dialogue (not robotic Q&A)
- Demonstrate how AI adapts to user responses
- Include 1-2 complete examples (not 10 partial ones)
- Show the final output that was generated

---

### Step 3.6: Write Important Notes Section

**Objective**: Provide meta-guidance on using the prompt effectively.

**Template**:
```markdown
## Important Notes

### Best Practices
1. [Practice 1 with explanation]
2. [Practice 2 with explanation]
3. [Practice 3 with explanation]

### Common Pitfalls
1. [Pitfall 1 with how to avoid]
2. [Pitfall 2 with how to avoid]
3. [Pitfall 3 with how to avoid]

### Success Factors
- [Factor 1]: [Why it matters]
- [Factor 2]: [Why it matters]
- [Factor 3]: [Why it matters]
```

---

## Phase 4: Validation and Quality Assurance

### Step 4.1: Completeness Check

**Checklist**:
- [ ] **YAML Front Matter**: All required fields present and accurate
- [ ] **Role Definition**: Clear role, mission, and expertise areas
- [ ] **Dialogue Flow**: All stages present with clear structure
- [ ] **Frameworks**: All mentioned frameworks are explained
- [ ] **Output Format**: Specific, actionable format description
- [ ] **Examples** (if included): Realistic and helpful
- [ ] **Important Notes**: Best practices and pitfalls covered
- [ ] **Version Info**: Version, dates, status included

---

### Step 4.2: Quality Check

**Criteria**:

1. **Clarity**: 
   - [ ] Language is clear and unambiguous
   - [ ] Technical terms are defined
   - [ ] Instructions are specific and actionable

2. **Structure**:
   - [ ] Logical flow from stage to stage
   - [ ] Clear section headings
   - [ ] Proper markdown formatting

3. **Actionability**:
   - [ ] Questions are specific enough to answer
   - [ ] Frameworks are explained well enough to apply
   - [ ] Output format is detailed enough to produce

4. **Completeness**:
   - [ ] All frameworks mentioned are explained
   - [ ] All stages have clear objectives and outputs
   - [ ] User knows what to expect at each step

5. **Alignment**:
   - [ ] Prompt matches original user requirements
   - [ ] Frameworks are appropriate for objectives
   - [ ] Complexity matches target user expertise

---

### Step 4.3: Consistency Check

**Areas to Verify**:

1. **Framework Naming**: Same framework spelled/capitalized consistently throughout
   - ❌ "SWOT", "Swot", "swot analysis"
   - ✅ "SWOT Analysis" everywhere

2. **Stage Numbering**: Sequential and complete
   - ❌ Stage 1, Stage 2, Stage 4, Stage 5
   - ✅ Stage 1, Stage 2, Stage 3, Stage 4

3. **Terminology**: Consistent use of domain-specific terms
   - ❌ "customers", "clients", "users" interchangeably
   - ✅ Pick one term and use consistently

4. **Tone**: Consistent throughout (professional, conversational, technical)

5. **Format**: Consistent markdown styling
   - Heading levels used correctly
   - Lists formatted consistently
   - Code blocks used appropriately

---

## Phase 5: Finalization and Delivery

### Step 5.1: Format for Presentation

**Actions**:
1. Ensure proper markdown syntax throughout
2. Add horizontal rules (`---`) between major sections
3. Verify all lists are properly formatted
4. Check that code blocks have correct language tags
5. Ensure YAML front matter is properly delimited

---

### Step 5.2: Final Review with User

**Template Response**:
```markdown
I've generated the complete meta-prompt for [Prompt Name]. Here's what I've created:

**Structure**:
- [X] dialogue stages covering [brief description]
- [Y] integrated frameworks: [list]
- Output: [brief description of deliverable]

**Special Features**:
- [Feature 1]
- [Feature 2]
- [Feature 3]

[Display the complete meta-prompt]

Does this meta-prompt fulfill all your requirements and objectives?
```

**If Adjustments Needed**:
- Ask: "What would you like to change?"
- Make specific edits
- Present revised version
- Confirm satisfaction

---

### Step 5.3: Filename and Storage

**Naming Convention**:
- Format: `[domain]-[role].md`
- Lowercase with hyphens
- Descriptive and searchable

**Examples**:
- `business-strategy-consultant.md`
- `software-architecture-advisor.md`
- `project-based-learning-designer.md`
- `marketing-campaign-planner.md`

**Suggest Filename**:
"What filename would you like for this prompt? I suggest: `[suggested-name].md`"

---

## Quality Criteria Summary

### Excellent Meta-Prompt Characteristics

1. **Clear Purpose**: Immediately obvious what this prompt does and for whom
2. **Logical Structure**: Stages flow naturally and build on each other
3. **Actionable Questions**: User knows exactly how to answer each question
4. **Framework Integration**: Frameworks are explained and naturally integrated
5. **Specific Outputs**: User knows exactly what they'll receive
6. **Professional Quality**: Well-formatted, properly spelled, consistent tone
7. **Domain Expertise**: Shows deep understanding of target domain
8. **User-Centric**: Designed around user needs, not framework theory
9. **Practical Examples**: Includes concrete examples that aid understanding
10. **Complete**: Nothing important is missing; everything needed is present

---

## Common Issues and Solutions

### Issue 1: Prompt is Too Long

**Symptoms**: Meta-prompt exceeds reasonable length (>15,000 characters)

**Solutions**:
- Move detailed framework explanations to appendix
- Reduce number of examples (focus on 1-2 best ones)
- Combine similar stages
- Remove redundant content
- Use more concise language

---

### Issue 2: Dialogue Flow is Confusing

**Symptoms**: Unclear when to move between stages, questions seem random

**Solutions**:
- Add clear stage objectives
- Include stage transition summaries
- Number questions explicitly
- Add "Stage Output" to clarify what happens at end
- Show example dialogue flow

---

### Issue 3: Frameworks Poorly Integrated

**Symptoms**: Frameworks feel tacked on, not organically part of dialogue

**Solutions**:
- Integrate framework questions into dialogue stages
- Explain framework purpose in context
- Show how framework answers inform next steps
- Provide framework-specific examples
- Connect frameworks to user objectives

---

### Issue 4: Output Format Too Vague

**Symptoms**: User won't know what final deliverable looks like

**Solutions**:
- Provide detailed section breakdown
- Include example of each section
- Show sample output
- Specify lengths (e.g., "1-2 pages")
- Include quality checkpoints

---

### Issue 5: Too Technical or Too Simple

**Symptoms**: Language doesn't match target user expertise level

**Solutions**:
- Review user profile from Stage 2
- Adjust terminology to match expertise
- Add or remove definitions as needed
- Include or exclude background explanations
- Test with representative user if possible

---

## Advanced Techniques

### Technique 1: Conditional Dialogue Paths

For complex prompts, include conditional paths based on user responses.

**Example**:
```markdown
Ask: "Are you creating a new business model or optimizing an existing one?"

**If new**: "Let's start with a blank Business Model Canvas and build from scratch..."
**If optimizing**: "Let's first understand your current model. Describe your primary
value proposition..."
```

---

### Technique 2: Progressive Disclosure

Introduce frameworks gradually, not all at once.

**Example**:
```markdown
### Stage 1: Understanding Goals
[Use no frameworks - just discovery]

### Stage 2: External Analysis
[Introduce PEST - one framework]

### Stage 3: Competitive Landscape
[Add Porter's Five Forces - build on PEST]

### Stage 4: Synthesis
[Combine insights from both frameworks]
```

---

### Technique 3: Meta-Cognitive Prompts

Include prompts that help AI monitor its own performance.

**Example**:
```markdown
**After Stage 2**:
Before proceeding to Stage 3, check:
- [ ] Do I have sufficient information about the target market?
- [ ] Are there gaps in my understanding of customer needs?
- [ ] Should I probe deeper on any points before moving forward?

If any checks fail, ask clarifying questions before proceeding.
```

---

### Technique 4: Adaptive Depth

Allow AI to adjust depth based on user expertise.

**Example**:
```markdown
**Framework Explanation Depth**:
- If user demonstrates expertise (mentions technical terms, specific frameworks):
  → Use concise explanations, skip basics, focus on application
- If user seems uncertain (asks "what is X?", gives vague responses):
  → Provide detailed explanations, include examples, check understanding
```

---

## Version Information

- **Version**: 1.0.0
- **Last Updated**: 2025-01-23
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/general/meta-prompt-generator.md`
  - Frameworks: `rag/general/meta-prompt-generator/frameworks.md`
  - Examples: `rag/general/meta-prompt-generator/examples.md`
