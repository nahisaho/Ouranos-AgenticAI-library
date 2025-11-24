# Copilot-Optimized Prompts

This directory contains prompts optimized for **Microsoft Copilot Agent Builder**.

## 📂 Structure

```
copilot/
├── prompts/              # Copilot-optimized prompts (≤16K chars)
│   ├── general/          # 1 prompt
│   ├── business-management/  # 20 prompts
│   ├── design-development/   # 20 prompts
│   ├── hr-organization/      # 11 prompts
│   ├── education/            # 8 prompts
│   ├── research/             # 5 prompts
│   ├── document-creation/    # 3 prompts
│   ├── social-policy/        # 6 prompts
│   ├── communication/        # 6 prompts
│   ├── innovation-transformation/ # 5 prompts
│   └── specialized-domains/  # 8 prompts
└── rag/                  # RAG support files (unlimited size)
    └── {category}/{prompt-id}/
        ├── frameworks.md     # Framework definitions and guidance
        ├── examples.md       # Usage examples and scenarios
        └── methodologies.md  # Step-by-step procedures
```

## 🎯 Optimization Strategy

### Copilot Prompts (Main Files)
**Target**: ≤8,000 characters (recommended), ≤16,000 characters (hard limit)

**Contents**:
- YAML metadata (id, category, frameworks, version, RAG references)
- Role definition (concise)
- Dialogue flow (stage headings, key questions, outputs)
- Framework names and brief summaries
- Quick reference section
- RAG file references

### RAG Files (Support Files)
**Target**: Unlimited

**Contents**:
- **frameworks.md**: Full framework definitions, components, application guidance, best practices
- **examples.md**: Complete usage scenarios, dialogue walkthroughs, domain-specific examples
- **methodologies.md**: Step-by-step procedures, quality checklists, troubleshooting guides

## 📊 Conversion Stats

- **Total Prompts**: 93
- **Categories**: 11
- **RAG Files**: 279 (93 prompts × 3 files each)
- **Conversion Date**: 2025-11-24
- **Source**: `/prompts/en/prompts/`

### Character Count Distribution

| Range | Count | Percentage |
|-------|-------|------------|
| ≤8,000 chars | 20 | 21.5% |
| 8,001-16,000 | 71 | 76.3% |
| >16,000 chars | 2 | 2.2% |

**Note**: Microsoft Copilot Agent Builder supports up to 16KB (~16,000 chars). Only 2 prompts exceed this and may require manual optimization.

## 🚀 Usage with Microsoft Copilot

### 1. Import Prompt
Copy the content of a Copilot prompt file (e.g., `prompts/general/meta-prompt-generator.md`)

### 2. Configure RAG Files
Upload the corresponding RAG files from `rag/{category}/{prompt-id}/`:
- `frameworks.md`
- `examples.md`
- `methodologies.md`

### 3. Reference RAG in Instructions
The prompt will automatically reference RAG files:
```markdown
**Framework Details**: See `rag/{category}/{prompt-id}/frameworks.md`
**Usage Examples**: See `rag/{category}/{prompt-id}/examples.md`
**Step-by-Step**: See `rag/{category}/{prompt-id}/methodologies.md`
```

## 🔧 Development

### Converting Additional Prompts

```bash
python3 scripts/convert_to_copilot.py
```

### Validating Character Counts

```bash
find prompts/copilot/prompts -name "*.md" -exec wc -c {} + | sort -rn
```

## 📝 Versioning

- **Version**: 1.0.0
- **Last Updated**: 2025-11-24
- **Status**: Production Ready
- **Compatibility**: Microsoft Copilot Agent Builder

## 📖 Related Documentation

- [Main README](../../README.md)
- [Conversion Strategy](../../storage/specs/copilot-conversion-strategy.md)
- [Converter Prompt](../../storage/specs/copilot-converter-prompt.md)
- [English Prompts Source](../en/prompts/)

---

**Note**: These prompts are optimized for Microsoft Copilot Agent Builder. For other AI assistants, use the original English prompts in `/prompts/en/`.
