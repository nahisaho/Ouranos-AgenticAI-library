# Frameworks for Meta-Prompt Generator

This file provides detailed definitions and application guidance for the frameworks used in the Meta-Prompt Generator agent.

---

## 1. Prompt Engineering Principles

### 1.1 Clarity

**Definition**: Eliminate ambiguity and provide specific instructions to ensure the AI understands exactly what is expected.

**Components**:
- **Precise Language**: Use specific terms instead of vague descriptors
- **Defined Terms**: Establish common understanding of specialized vocabulary
- **Explicit Constraints**: State limitations and boundaries clearly
- **Unambiguous Instructions**: One clear interpretation of what to do

**Application**:
- Replace "analyze this" with "conduct SWOT analysis identifying 3-5 items per quadrant"
- Define technical terms upfront: "By 'stakeholder', we mean..."
- State what NOT to do: "Do not include personal opinions, only data-driven insights"

**Examples**:
- ❌ Vague: "Help me with my business"
- ✅ Clear: "Generate a 3-year growth strategy for a B2B SaaS startup targeting enterprise clients in the healthcare sector"

---

### 1.2 Structure

**Definition**: Organize prompts with logical flow, clear sections, and hierarchical organization to facilitate AI comprehension and execution.

**Components**:
- **Logical Sequence**: Steps build on previous information
- **Section Hierarchy**: Clear headings and sub-headings
- **Numbered/Bulleted Lists**: For multi-step processes
- **Stage Transitions**: Explicit markers between sections

**Application**:
- Use heading levels: # Role, ## Dialogue Flow, ### Stage 1, #### Substage
- Number steps: "1. First, analyze... 2. Then, synthesize... 3. Finally, recommend..."
- Create visual breaks: Use `---` to separate major sections
- Template structure: YAML → Role → Dialogue → Frameworks → Output

**Examples**:
```markdown
## Stage 1: Discovery
### Step 1.1: Identify Objective
Ask: "What is your goal?"

### Step 1.2: Clarify Scope
Ask: "What are the boundaries of this project?"
```

---

### 1.3 Context

**Definition**: Provide sufficient background information, objectives, and constraints to enable informed AI responses.

**Components**:
- **Background Information**: History, current situation, relevant facts
- **Objectives**: What success looks like
- **Constraints**: Time, resources, regulations, ethical considerations
- **Assumptions**: Stated explicitly to avoid misunderstandings

**Application**:
- Include domain context: "In the automotive industry, where..."
- State objectives: "The goal is to reduce costs by 15% while maintaining quality"
- Specify constraints: "Must comply with GDPR regulations"
- Declare assumptions: "Assuming current market conditions remain stable"

**Examples**:
- ❌ No context: "Create a marketing plan"
- ✅ With context: "Create a Q2 2025 marketing plan for our new product launch targeting millennials in urban areas, with a budget of $50k and focus on digital channels"

---

### 1.4 Examples

**Definition**: Provide concrete examples to illustrate expected outputs and facilitate AI understanding through few-shot learning.

**Components**:
- **Input-Output Pairs**: Show sample questions and ideal responses
- **Format Examples**: Demonstrate desired structure
- **Edge Cases**: Show how to handle unusual situations
- **Good vs. Bad**: Contrast correct and incorrect approaches

**Application**:
- Few-shot learning: Provide 2-3 example dialogues
- Format templates: Show sample YAML front matter, section structures
- Edge case handling: "If user provides incomplete information, ask: '...'"
- Quality examples: Show "good" analysis vs. "poor" analysis

**Examples**:
```markdown
### Example Dialogue

**AI**: "What industry is your business in?"
**User**: "Healthcare technology"
**AI**: "What specific healthcare segment (hospitals, clinics, patients)?"
**User**: "We focus on remote patient monitoring"
```

---

## 2. Dialogue Design Principles

### 2.1 One-Question-at-a-Time Approach

**Definition**: Ask single, focused questions and wait for user responses before proceeding to the next question, creating natural conversational flow.

**Why It Matters**:
- **Deeper Exploration**: Allows follow-up questions based on specific answers
- **Prevents Overwhelm**: Users process one thing at a time
- **Natural Flow**: Mimics human conversation patterns
- **Better Understanding**: AI can clarify ambiguities immediately
- **Engagement**: Users feel heard and understood

**Components**:
- **Single Focus**: Each question targets one specific aspect
- **Sequential Flow**: Questions build on previous answers
- **Wait for Response**: Don't proceed until user answers
- **Adaptive Follow-up**: Next question depends on previous answer

**Application**:
- Instead of: "What industry are you in, who are your customers, and what problems do they face?"
- Use sequence:
  1. "What industry are you in?"
  2. [Wait for answer: "Healthcare"]
  3. "Which healthcare segment do you serve?"
  4. [Wait for answer: "Remote patient monitoring"]
  5. "What specific problems do your patients face with current monitoring solutions?"

**When to Use**:
- ✅ Complex topics requiring deep understanding
- ✅ Emotionally charged or sensitive subjects
- ✅ When building trust and rapport is important
- ✅ Early stages of discovery
- ❌ Simple data collection (multiple fields can be efficient)
- ❌ When user explicitly requests faster interaction

---

### 2.2 Goal-Oriented

**Definition**: Every question and stage should directly contribute to achieving the final objective.

**Components**:
- **Clear Stage Goals**: Each stage has explicit purpose
- **Question Intent**: Every question has clear "why"
- **Progress Tracking**: User understands where they are in the process
- **Alignment**: All activities connect to end goal

**Application**:
- State stage purpose: "Stage 1 Goal: Understand your core objective"
- Explain question intent: "I'm asking about constraints to ensure feasibility"
- Show progress: "We've clarified your objective. Next, let's gather context."
- Link to goal: "This helps me recommend the right frameworks for your needs"

**Examples**:
```markdown
### Stage 1: Clarifying Objectives
**Goal**: Establish clear, measurable objectives for the meta-prompt

Ask: "What is the ultimate goal..." [connects to: defining success criteria]
Then: "What specific deliverables..." [connects to: output format design]
```

---

### 2.3 Progressive Refinement

**Definition**: Move from broad understanding to specific details through iterative clarification and confirmation.

**Components**:
- **Broad to Specific**: Start with open-ended, narrow down progressively
- **Iterative Cycles**: Ask → Listen → Summarize → Confirm → Refine
- **Layered Questions**: Surface-level → Deeper exploration → Fine details
- **Confirmation Points**: Verify understanding before proceeding

**Application**:
- Level 1 (Broad): "What type of business challenge are you facing?"
- Level 2 (Medium): "Is this challenge related to operations, strategy, or marketing?"
- Level 3 (Specific): "Within operations, is this about supply chain, quality control, or workforce management?"
- Confirmation: "So you're looking to optimize supply chain logistics for perishable goods. Correct?"

**Stage Transitions**:
- End each stage with summary
- Ask for confirmation: "Did I understand correctly?"
- Allow adjustments before proceeding
- Build next stage on confirmed understanding

---

### 2.4 Adaptability

**Definition**: Respond flexibly to user inputs, adjusting dialogue flow, depth, and tone based on their responses and expertise level.

**Components**:
- **Dynamic Questioning**: Add or skip questions based on responses
- **Tone Adjustment**: Match user's communication style and expertise
- **Depth Calibration**: Go deeper or stay surface-level as needed
- **Path Flexibility**: Don't rigidly follow script

**Application**:
- **If user provides detailed answer**: Skip redundant follow-ups, move to next area
- **If user seems confused**: Provide explanations, offer examples
- **If expert user**: Use technical terminology, skip basics
- **If beginner**: Define terms, provide more guidance

**Examples**:
```markdown
# Adaptive Response Example

User: "I need a prompt for SWOT analysis integrated with Porter's Five Forces"

AI Response: [Recognizes user expertise]
"Great! Since you're familiar with these frameworks, let's dive into integration strategy.
Should we apply SWOT first for internal assessment, then Porter's for competitive landscape?
Or would you prefer a different sequence?"

# vs. Beginner User

User: "I need help with business analysis"

AI Response: [Recognizes need for guidance]
"I can help! There are several frameworks we could use. SWOT analysis examines
your company's Strengths, Weaknesses, Opportunities, and Threats. Would you like
me to explain how this works?"
```

---

## 3. Meta-cognitive Approach

### 3.1 Self-Monitoring

**Definition**: The AI continuously checks its own progress, ensuring it's gathering sufficient information and staying on track.

**Components**:
- **Progress Tracking**: Monitor which objectives have been addressed
- **Completeness Checks**: Ensure all necessary information collected
- **Quality Assessment**: Evaluate depth and relevance of gathered data
- **Gap Identification**: Notice missing information

**Application**:
- Internal checkpoints: "Have I clarified the objective? Yes. Context? Partially - need more info about constraints."
- Explicit checks with user: "Before we proceed, let me make sure I have everything. [Summary]. Is there anything else I should know?"
- Stage-end reviews: "In Stage 1, we've established [X, Y, Z]. Have I missed anything important?"

**Example**:
```markdown
# Self-Monitoring in Action

[After Stage 2]
AI: "Let me review what we've covered so far:
- Objective: Create B2B sales training program
- Target users: Sales reps with 0-2 years experience
- Constraints: Must complete in 2 weeks, budget $5k

I notice we haven't discussed:
- Current skill levels
- Specific sales challenges they face
- Preferred learning formats (video, text, interactive)

Should we address these before moving to framework selection?"
```

---

### 3.2 Self-Regulation

**Definition**: The AI adjusts its approach based on identified gaps, changing strategies when current approach isn't working.

**Components**:
- **Gap Filling**: Identify missing information and ask targeted questions
- **Strategy Adjustment**: Change questioning approach if not effective
- **Depth Modulation**: Go deeper or broader as needed
- **Error Correction**: Recognize and fix misunderstandings

**Application**:
- Identify gap: "I realize I don't have information about your timeline"
- Ask targeted question: "What's your deadline for implementing this?"
- Adjust if stuck: "I notice we're going in circles. Let me try a different angle..."
- Correct misunderstanding: "I may have misunderstood earlier. You said X, but did you mean Y?"

**Examples**:
```markdown
# Self-Regulation Example

AI: [Notices user's vague responses]
"I'm getting broad answers. Let me try a more specific approach.

Instead of 'What are your goals?', let me ask:
If we implement this solution successfully, what would be different
in your daily operations 6 months from now?"

# Gap-Filling Example

AI: "I've covered objectives and context, but I'm missing information
about your technical constraints. Are there specific platforms or
technologies you must use or avoid?"
```

---

### 3.3 Reflection

**Definition**: The AI reviews and summarizes progress at the end of each stage, confirming understanding with the user before proceeding.

**Components**:
- **Stage Summary**: Recap what was discussed and decided
- **Key Insights**: Highlight main takeaways
- **Confirmation Request**: Explicitly ask if understanding is correct
- **Adjustment Opportunity**: Allow user to correct or add information

**Application**:
- End-of-stage summary: "In Stage 1, we've established that your goal is [X], targeting [Y], with constraints [Z]."
- Ask for confirmation: "Does this accurately capture your objective?"
- Invite corrections: "What have I missed or misunderstood?"
- Bridge to next stage: "Now that we've clarified your objective, let's gather contextual information in Stage 2."

**Example**:
```markdown
# Reflection Example

AI: "Let me summarize what we've covered in Stage 2:

**Domain**: Healthcare technology, specifically remote patient monitoring
**Users**: Cardiologists and nursing staff in hospital settings
**Expertise Level**: Intermediate - comfortable with medical devices but limited tech background
**Constraints**:
- Must comply with HIPAA regulations
- Integration with existing Epic EHR system
- Implementation timeline: 3 months

**Key Insight**: The main challenge is balancing sophisticated monitoring capabilities
with a simple user interface for busy clinical staff.

Have I understood correctly? Is there anything you'd like to add or clarify before
we move to framework selection in Stage 3?"
```

---

## Framework Integration Strategies

### Sequential Integration
Frameworks are applied one after another in different stages.

**When to use**: When frameworks build on each other (e.g., SWOT → TOWS → Action Plan)

**Example**:
- Stage 1: SWOT Analysis (assess current state)
- Stage 2: Porter's Five Forces (analyze competitive environment)
- Stage 3: Value Proposition Canvas (design offering)

### Parallel Integration
Multiple frameworks are used simultaneously within the same stage.

**When to use**: When frameworks provide complementary perspectives on the same issue

**Example**:
Within Stage 2, analyze customer needs using:
- Jobs-to-be-Done (functional needs)
- Empathy Mapping (emotional needs)
- Customer Journey Mapping (experience needs)

### Selective Integration
User chooses which frameworks to apply based on their specific situation.

**When to use**: When different scenarios require different analytical approaches

**Example**:
"Based on your situation, you might choose:
- Option A: If facing new market entry → Blue Ocean Strategy + PESTEL
- Option B: If optimizing existing operations → Value Chain + Lean principles
- Option C: If undergoing transformation → Kotter's 8 Steps + Change Management"

---

## Best Practices

1. **Start Simple**: Don't overwhelm with too many frameworks initially
2. **Explain Why**: Always clarify the purpose and value of each framework
3. **Provide Examples**: Show how frameworks have been applied in similar scenarios
4. **Allow Flexibility**: Let users adapt frameworks to their specific needs
5. **Integrate Naturally**: Frameworks should enhance dialogue, not dominate it
6. **Check Understanding**: Ensure user grasps framework basics before applying
7. **Document Clearly**: In generated meta-prompts, explain frameworks thoroughly

---

## Common Pitfalls

- **Framework Overload**: Using too many frameworks creates confusion
- **Jargon Without Explanation**: Assuming user knows framework terminology
- **Rigid Application**: Forcing frameworks when they don't fit the situation
- **Missing Context**: Applying frameworks without understanding user's domain
- **No Examples**: Abstract framework descriptions without concrete illustrations
- **Skipping Confirmation**: Moving forward without verifying understanding

---

## Version Information

- **Version**: 1.0.0
- **Last Updated**: 2025-01-23
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/general/meta-prompt-generator.md`
  - Examples: `rag/general/meta-prompt-generator/examples.md`
  - Methodologies: `rag/general/meta-prompt-generator/methodologies.md`
