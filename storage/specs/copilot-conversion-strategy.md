# Copilot Prompt Conversion Strategy

**Project**: Ouranos-AgenticAI-library
**Created**: 2025-11-24
**Version**: 1.0

---

## Objective

Convert 78 English prompts (10k-15k chars each) into Copilot-optimized versions (≤8000 chars) while maintaining quality by leveraging RAG (Retrieval-Augmented Generation) files.

---

## Conversion Strategy

### Core Principle

**Separation of Concerns**:
- **Prompt File** (≤8000 chars): Dialogue flow, stage structure, essential instructions
- **RAG File** (unlimited): Framework details, examples, reference materials

### What Stays in Prompt

1. **Dialogue Structure** (5 stages) - Essential
2. **Core Instructions** - How to conduct each stage
3. **Framework Names** - What to apply (e.g., "SWOT Analysis")
4. **Stage Objectives** - What each stage achieves
5. **Transition Logic** - How to move between stages

### What Moves to RAG

1. **Framework Definitions** - Detailed explanations
2. **Detailed Examples** - Concrete use cases
3. **Step-by-Step Procedures** - Granular how-tos
4. **Reference Materials** - Additional context
5. **Extended Methodologies** - Deep dives into frameworks

---

## File Structure

```
prompts/copilot/
├── prompts/
│   └── {category}/
│       └── {prompt-id}.md          # ≤8000 chars
└── rag/
    └── {category}/
        └── {prompt-id}/
            ├── frameworks.md       # Framework definitions
            ├── examples.md         # Concrete examples
            └── methodologies.md    # Detailed procedures
```

---

## Conversion Template

### Copilot Prompt Structure (≤8000 chars)

```markdown
---
id: {prompt-id}
category: {category}
frameworks: [List of framework names]
dialogue_stages: 5
rag_files:
  - frameworks.md
  - examples.md
  - methodologies.md
version: 1.0.0-copilot
character_count: {actual_count}
---

# {Title}

**Role**: You are a {role} specialized in {domain}.

**RAG Context**: You have access to detailed framework definitions, examples, and methodologies in the attached RAG files. Reference them when providing specific guidance.

---

## Dialogue Framework

### Stage 1: {Stage Name}
**Objective**: {Brief objective}

**Questions to Ask**:
1. {Key question 1}
2. {Key question 2}
3. {Key question 3}

**Frameworks to Apply**: {Framework names - see RAG for details}

**Transition**: Move to Stage 2 when {condition}.

---

### Stage 2: {Stage Name}
[Similar structure...]

---

### Stage 3: {Stage Name}
[Similar structure...]

---

### Stage 4: {Stage Name}
[Similar structure...]

---

### Stage 5: {Stage Name}
**Objective**: Generate final meta-prompt

**Output Format**:
```
[Meta-prompt template]
```

**Delivery**: Present as markdown code block

---

## Usage Instructions

1. Begin with Stage 1 questions
2. Reference RAG files for framework details when needed
3. Progress through stages systematically
4. Generate final meta-prompt in Stage 5
```

### RAG File: frameworks.md

```markdown
# Framework Definitions - {Prompt Title}

## {Framework 1 Name}

**Definition**: {Full definition}

**Components**:
1. {Component 1}: {Description}
2. {Component 2}: {Description}
3. {Component 3}: {Description}

**Application**: {When and how to use}

---

## {Framework 2 Name}

[Similar structure...]
```

### RAG File: examples.md

```markdown
# Examples - {Prompt Title}

## Example 1: {Scenario}

**Context**: {Background}

**Application**:
- Framework: {Framework name}
- Steps: {Step-by-step}
- Outcome: {Result}

---

## Example 2: {Scenario}

[Similar structure...]
```

### RAG File: methodologies.md

```markdown
# Detailed Methodologies - {Prompt Title}

## {Methodology 1}

**Step 1**: {Detailed description}
**Step 2**: {Detailed description}
**Step 3**: {Detailed description}

**Best Practices**:
- {Practice 1}
- {Practice 2}

---

## {Methodology 2}

[Similar structure...]
```

---

## Conversion Prompt for AI

Use this prompt to convert existing prompts:

```
# Copilot Prompt Conversion Task

**Source Prompt**: {prompt-id}
**Character Limit**: 8000 characters (strict)
**Target**: Microsoft Copilot Agent

## Instructions

1. **Analyze Source**: Review the full English prompt (10k-15k chars)

2. **Extract Core**:
   - Dialogue structure (5 stages)
   - Stage objectives
   - Framework names (list only, not definitions)
   - Key questions per stage
   - Transition conditions

3. **Create Copilot Prompt** (≤8000 chars):
   - Keep: Dialogue flow, stage structure, framework names
   - Remove: Framework definitions, detailed examples, step-by-step procedures
   - Add: RAG file references
   - Format: Concise, direct instructions

4. **Create RAG Files**:
   - **frameworks.md**: All framework definitions and components
   - **examples.md**: Concrete examples and use cases
   - **methodologies.md**: Detailed step-by-step procedures

5. **Validate**:
   - Copilot prompt ≤8000 chars
   - No loss of essential dialogue structure
   - All frameworks referenced in RAG
   - Clear RAG file usage instructions

## Output Format

Provide three files:
1. `{prompt-id}.md` (Copilot prompt, ≤8000 chars)
2. `rag/{prompt-id}/frameworks.md`
3. `rag/{prompt-id}/examples.md`
4. `rag/{prompt-id}/methodologies.md` (if needed)

## Quality Criteria

✅ Copilot prompt maintains 5-stage dialogue structure
✅ All framework names preserved
✅ Clear instructions for using RAG files
✅ Character count ≤8000
✅ No quality degradation in final meta-prompt output
```

---

## Automation Script (Planned)

```python
# scripts/convert_to_copilot.py

import yaml
from pathlib import Path

def convert_prompt_to_copilot(source_path: Path, target_dir: Path):
    """
    Convert full English prompt to Copilot-optimized version + RAG files
    
    Args:
        source_path: Path to source prompt (en/)
        target_dir: Path to copilot/ directory
    """
    # Read source
    source_content = source_path.read_text()
    front_matter, body = parse_front_matter(source_content)
    
    # Extract components
    core_structure = extract_dialogue_structure(body)
    frameworks = extract_frameworks(body)
    examples = extract_examples(body)
    methodologies = extract_methodologies(body)
    
    # Create Copilot prompt
    copilot_prompt = build_copilot_prompt(
        core_structure, 
        front_matter,
        max_chars=8000
    )
    
    # Create RAG files
    rag_frameworks = build_rag_frameworks(frameworks)
    rag_examples = build_rag_examples(examples)
    rag_methodologies = build_rag_methodologies(methodologies)
    
    # Validate
    assert len(copilot_prompt) <= 8000, "Prompt exceeds 8000 chars"
    
    # Write files
    write_copilot_files(target_dir, copilot_prompt, rag_frameworks, rag_examples, rag_methodologies)
```

---

## Example Conversion

### Source (15,000 chars)
```markdown
# Business Strategy Consultant

## Stage 1: Context Assessment

Ask the following questions to understand...

**SWOT Analysis**:
SWOT Analysis is a strategic planning framework...
[500 words of definition]

**Porter's Five Forces**:
Porter's Five Forces is a framework for analyzing...
[500 words of definition]

[Detailed examples: 1000 words]
[Step-by-step procedures: 1000 words]
...
```

### Copilot Version (7,800 chars)
```markdown
# Business Strategy Consultant

**RAG Context**: Reference frameworks.md for SWOT, Porter's Five Forces, Blue Ocean Strategy definitions.

## Stage 1: Context Assessment

**Frameworks**: SWOT Analysis, Porter's Five Forces (see RAG)

**Questions**:
1. What is your organization's current market position?
2. What competitive pressures do you face?
...

**Transition**: Move to Stage 2 when context is clear.
```

### RAG: frameworks.md (5,000 chars)
```markdown
## SWOT Analysis

**Definition**: Strategic planning framework analyzing Strengths, Weaknesses, Opportunities, Threats...
[Full 500-word definition]

## Porter's Five Forces

**Definition**: Framework for analyzing competitive forces...
[Full 500-word definition]
```

---

## Success Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Copilot prompts created | 78 | TBD |
| Average char count | ≤8000 | TBD |
| RAG files per prompt | 2-3 | TBD |
| Quality score (dialogue flow) | 100% | TBD |
| Framework coverage | 100% | TBD |

---

## Next Steps

1. ✅ Create conversion strategy (this document)
2. ⏳ Convert first prompt manually (test case)
3. ⏳ Validate quality and character count
4. ⏳ Create conversion prompt for AI assistance
5. ⏳ Convert all 78 prompts
6. ⏳ Update manifest.yml
7. ⏳ Test with Microsoft Copilot

---

**Status**: Strategy Approved
**Next**: Manual conversion of `meta-prompt-generator` as test case
