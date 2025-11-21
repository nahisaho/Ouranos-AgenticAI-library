# Language Guide

## Overview

Ouranos Agentic Library is available in three versions to meet different needs:

1. **English Version** - Full, comprehensive prompts
2. **Japanese Version** - Full, comprehensive prompts in Japanese
3. **Microsoft Copilot Agent Edition** - Optimized for 8000 character limit

---

## Version Comparison

### English Version (`/en/`)

**Purpose**: Comprehensive reference and learning

**Characteristics**:
- Full-length prompts (10,000-15,000 characters)
- 4-8 frameworks per prompt
- Multiple detailed examples
- Extensive best practices
- Complete dialogue flow (5 stages)
- In-depth explanations

**Best For**:
- Deep learning and understanding
- Reference documentation
- Comprehensive project planning
- Educational purposes
- Creating custom variations

**File Location**: `/en/prompts/{category}/{prompt-id}.md`

---

### Japanese Version (`/ja/`)

**Purpose**: 日本語ネイティブユーザー向け完全版

**Characteristics**:
- 完全版プロンプト (10,000-15,000文字)
- 各プロンプトに4-8個のフレームワーク
- 複数の詳細な例
- 包括的なベストプラクティス
- 完全な対話フロー (5段階)
- 詳細な説明
- 日本の文化的コンテキストに適応

**Best For / 最適な用途**:
- 日本語での深い学習と理解
- リファレンスドキュメント
- 包括的なプロジェクト計画
- 教育目的
- カスタムバリエーションの作成

**File Location**: `/ja/prompts/{category}/{prompt-id}.md`

**Status**: 🔄 Translation in progress (0/44 completed)

---

### Microsoft Copilot Agent Edition (`/copilot/`)

**Purpose**: Optimized for Microsoft Copilot constraints

**Characteristics**:
- Character limit: ≤8000 characters (strictly enforced)
- 2-3 core frameworks per prompt (essential only)
- 1-2 concise examples
- Key best practices only
- Complete dialogue flow maintained (5 stages, condensed)
- Optimized for quick processing

**Best For**:
- Direct use in Microsoft Copilot
- Quick deployment
- Fast iteration
- Production environments with character limits
- API integrations with size constraints

**File Location**: `/copilot/prompts/{category}/{prompt-id}.md`

**Status**: 🔄 Optimization in progress (0/44 completed)

---

## Character Count Details

| Version | Avg Characters | Max Characters | Frameworks | Examples |
|---------|----------------|----------------|------------|----------|
| **English** | 12,500 | 15,000 | 4-8 | 2-4 |
| **Japanese** | 12,500 | 15,000 | 4-8 | 2-4 |
| **Copilot** | 7,500 | 8,000 | 2-3 | 1-2 |

---

## How to Choose

### Use English Version If:
- ✅ You need comprehensive reference material
- ✅ You want to learn frameworks in depth
- ✅ You're creating custom variations
- ✅ You need multiple examples
- ✅ Character count is not a concern

### Use Japanese Version If:
- ✅ 日本語がネイティブ言語
- ✅ 日本の文化的コンテキストが重要
- ✅ 包括的なリファレンス資料が必要
- ✅ フレームワークを深く学びたい
- ✅ カスタムバリエーションを作成したい

### Use Copilot Edition If:
- ✅ You're using Microsoft Copilot Agent
- ✅ You have strict character limits (APIs, etc.)
- ✅ You need quick deployment
- ✅ You want core functionality only
- ✅ You need fast processing

---

## Migration Between Versions

### From English to Copilot

**Condensation Strategy**:
1. Keep YAML frontmatter with character_count metadata
2. Maintain 5-stage dialogue structure (condense each stage)
3. Select 2-3 most essential frameworks
4. Include 1 practical example only
5. Remove detailed explanations, keep key points
6. Eliminate redundant content

**Tools**: Character counting scripts available in `/scripts/`

### From English to Japanese

**Translation Guidelines**:
1. Maintain exact structure and format
2. Translate all content including YAML frontmatter
3. Adapt examples to Japanese cultural context
4. Preserve all frameworks (translate framework names)
5. Keep same dialogue flow and stages
6. Adjust idioms and expressions for natural Japanese

**See**: `/docs/translation-guide.md` for detailed guidelines

### From Copilot to Full Version

**Expansion Strategy**:
1. Use Copilot version as outline
2. Expand each framework with detailed explanations
3. Add 2-3 additional frameworks
4. Include multiple examples
5. Add best practices sections
6. Expand dialogue stages with more detail

**Reference**: Full English version for expansion patterns

---

## Language-Specific Features

### English Version
- Uses US English spelling
- Industry-standard terminology
- Global business context
- International frameworks

### Japanese Version
- Uses formal business Japanese (敬体)
- Japanese business terminology
- Japanese cultural context
- Localized framework names (e.g., SWOT分析)
- Examples relevant to Japanese business practices

### Copilot Edition
- Concise, clear English
- Minimal jargon
- Direct instructions
- Optimized for AI parsing
- Essential terminology only

---

## File Naming Conventions

All versions use the same file naming pattern:

```
{category}/{prompt-id}.md
```

Examples:
- `en/prompts/business-management/business-strategy-consultant.md`
- `ja/prompts/business-management/business-strategy-consultant.md`
- `copilot/prompts/business-management/business-strategy-consultant.md`

This allows easy cross-referencing between versions.

---

## Metadata Tracking

Each prompt includes YAML frontmatter with version-specific metadata:

### English/Japanese Versions

```yaml
---
id: business-strategy-consultant
category: business-management
frameworks:
  - SWOT Analysis
  - Porter's Five Forces
  - Value Chain Analysis
  - Business Model Canvas
dialogue_stages: 5
version: 1.0.0
tags:
  - strategy
  - analysis
  - consulting
created: 2025-11-19
updated: 2025-11-19
---
```

### Copilot Edition (Additional Metadata)

```yaml
---
id: business-strategy-consultant
category: business-management
frameworks:
  - SWOT Analysis
  - Porter's Five Forces
dialogue_stages: 5
version: 1.0.0
character_count: 7850
optimized_for: microsoft-copilot
full_version_en: ../en/prompts/business-management/business-strategy-consultant.md
full_version_ja: ../ja/prompts/business-management/business-strategy-consultant.md
tags:
  - strategy
  - analysis
  - consulting
  - copilot-optimized
created: 2025-11-19
updated: 2025-11-19
---
```

---

## Cross-Reference System

The `manifest.yml` in the root directory maps all three versions:

```yaml
prompts:
  - id: business-strategy-consultant
    category: business-management
    files:
      en: en/prompts/business-management/business-strategy-consultant.md
      ja: ja/prompts/business-management/business-strategy-consultant.md
      copilot: copilot/prompts/business-management/business-strategy-consultant.md
    status:
      en: complete
      ja: in_progress
      copilot: planned
```

---

## Contribution Guidelines

### Contributing to English Version
- Follow existing structure and style
- Include 4-8 frameworks minimum
- Provide 2-4 detailed examples
- Maintain 5-stage dialogue flow
- No character limit

### Contributing to Japanese Version
- Follow translation guide strictly
- Maintain cultural appropriateness
- Use formal business Japanese
- Adapt examples to Japanese context
- No character limit

### Contributing to Copilot Edition
- **Strict 8000 character limit**
- Include character_count in YAML frontmatter
- Maintain 5-stage dialogue (condensed)
- 2-3 core frameworks minimum
- 1-2 concise examples
- Test with Microsoft Copilot before submitting

---

## Support and Questions

- **English Version**: See [English README](../en/README.md)
- **Japanese Version**: See [日本語README](../ja/README.md)
- **Copilot Edition**: See [Copilot README](../copilot/README.md)
- **General Issues**: [GitHub Issues](https://github.com/nahisaho/ouranos-agentic-library/issues)

---

**Last Updated**: 2025-11-19  
**Version**: 1.0.0
