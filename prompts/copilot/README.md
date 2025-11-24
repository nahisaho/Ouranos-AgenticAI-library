# Ouranos Agentic Library - Microsoft Copilot Agent Edition

**Optimized Dialogue-based Agentic AI Prompt Templates (8000 Character Limit)**

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/nahisaho/ouranos-agentic-library)
[![Optimized for](https://img.shields.io/badge/Optimized_for-Microsoft_Copilot-blue.svg)](https://copilot.microsoft.com/)

> **Other Versions**: [English (Full)](../en/README.md) | [日本語 (完全版)](../ja/README.md)

## 📖 Overview

This is a **Microsoft Copilot Agent optimized version** of Ouranos Agentic Library. All prompts are condensed to **8000 characters or less** while maintaining core functionality and dialogue structure.

### Key Features

- 📏 **Character Limit Compliant**: All prompts ≤ 8000 characters
- 🎯 **Copilot Optimized**: Tailored for Microsoft Copilot Agent constraints
- 🧠 **Core Knowledge Retained**: Essential frameworks and expertise preserved
- 📝 **5-Stage Dialogue**: Complete dialogue flow maintained
- 🔍 **44 Templates**: Full category coverage in compact format

### What's Different from Full Version?

| Aspect | Full Version (en/ja) | Copilot Edition |
|--------|---------------------|-----------------|
| **Character Limit** | No limit (10k-15k chars) | ≤ 8000 characters |
| **Frameworks** | 4-8 frameworks detailed | 2-3 core frameworks |
| **Examples** | Multiple detailed examples | 1-2 concise examples |
| **Explanations** | Comprehensive | Essential only |
| **Best Practices** | Extensive | Key points only |

## 🚀 Quick Start

### Using with Microsoft Copilot

1. **Select Template**: Choose from `prompts/` directory
2. **Verify Character Count**: Check YAML frontmatter `character_count`
3. **Copy to Copilot**: Paste entire content into Microsoft Copilot
4. **Start Dialogue**: Engage in structured conversation
5. **Generate Output**: Receive optimized meta-prompt

### Example

```bash
# Clone repository
git clone https://github.com/nahisaho/ouranos-agentic-library.git
cd ouranos-agentic-library/copilot

# View optimized prompt
cat prompts/general/meta-prompt-generator.md

# Check character count
grep "character_count:" prompts/general/meta-prompt-generator.md
```

## 📂 Directory Structure

```
copilot/
├── README.md                 # This file
├── manifest.yml              # Metadata with character counts
├── prompts/                  # Optimized templates (44 prompts, all ≤8000 chars)
│   ├── general/              # General (1)
│   ├── business-management/  # Business & Management (8)
│   ├── design-development/   # Design & Development (8)
│   ├── hr-organization/      # HR & Organization (5)
│   ├── education/            # Education (4)
│   ├── research/             # Research (3)
│   ├── document-creation/    # Document Creation (3)
│   ├── social-policy/        # Social & Policy (3)
│   ├── communication/        # Communication (3)
│   ├── innovation-transformation/ # Innovation & Transformation (3)
│   └── specialized-domains/  # Specialized Domains (3)
└── docs/
    ├── copilot-usage-guide.md      # Copilot-specific usage guide
    └── character-limit-guide.md    # Character optimization guidelines
```

## 📋 Character Count Summary

All 44 prompts are optimized to stay within the 8000 character limit:

| Category | Prompts | Avg Characters | Max Characters |
|----------|---------|----------------|----------------|
| General | 1 | ~7,800 | 7,800 |
| Business & Management | 8 | ~7,500 | 7,950 |
| Design & Development | 8 | ~7,600 | 7,980 |
| HR & Organization | 5 | ~7,400 | 7,850 |
| Education | 4 | ~7,500 | 7,900 |
| Research | 3 | ~7,300 | 7,750 |
| Document Creation | 3 | ~7,200 | 7,650 |
| Social & Policy | 3 | ~7,400 | 7,800 |
| Communication | 3 | ~7,500 | 7,900 |
| Innovation & Transformation | 3 | ~7,600 | 7,950 |
| Specialized Domains | 3 | ~7,700 | 7,980 |

**All prompts verified ≤ 8000 characters**

## 🎯 Optimization Strategy

### What We Kept

✅ **Essential Elements**:
- YAML frontmatter with metadata
- Role definition (concise)
- Complete 5-stage dialogue flow
- 2-3 core frameworks per prompt
- 1 practical example
- Output format template

### What We Condensed

📉 **Reduced Elements**:
- Detailed explanations → Essential only
- Multiple examples → 1-2 examples
- Extensive best practices → Key points
- Redundant information → Eliminated
- Long quotes → Summarized

### Character Count Metadata

Each prompt includes:

```yaml
character_count: 7850
optimized_for: microsoft-copilot
full_version_en: ../en/prompts/category/filename.md
full_version_ja: ../ja/prompts/category/filename.md
```

## 🔧 Best Practices for Copilot

### Tips for Optimal Results

1. **Copy Entire Prompt**: Include YAML frontmatter and all sections
2. **Start Fresh Session**: Use new Copilot session for each template
3. **Follow Dialogue Flow**: Progress through all 5 stages
4. **Provide Context**: Be specific in your responses
5. **Reference Full Version**: For deeper understanding, check full versions

### Common Issues

| Issue | Solution |
|-------|----------|
| Truncated output | Ensure full prompt was pasted |
| Missing frameworks | Check that frontmatter was included |
| Unclear responses | Provide more specific context in Stage 1 |
| Character limit error | Verify prompt character_count ≤ 8000 |

## 📚 Documentation

- [Copilot Usage Guide](docs/copilot-usage-guide.md) - Detailed Copilot instructions
- [Character Limit Guide](docs/character-limit-guide.md) - Optimization techniques
- [Full Version (English)](../en/README.md) - Complete prompts in English
- [Full Version (Japanese)](../ja/README.md) - Complete prompts in Japanese

## 📄 License

Licensed under [Creative Commons Attribution-NonCommercial 4.0 International License](../LICENSE).

**Summary:**
- ✅ Non-commercial use, modification, and redistribution allowed
- ✅ Attribution required
- ❌ Commercial use prohibited

## 🤝 Contributing

To contribute optimized prompts:

1. Ensure character count ≤ 8000
2. Maintain 5-stage dialogue structure
3. Preserve core frameworks (2-3 minimum)
4. Include character_count in YAML frontmatter
5. Test with Microsoft Copilot

See [Full Contribution Guidelines](../en/docs/contribution.md).

## 📞 Contact

Questions or suggestions? Create an [Issue](https://github.com/nahisaho/ouranos-agentic-library/issues).

## ⚠️ Important Notes

- **Character Counting**: Uses UTF-8 character count (including spaces, newlines, YAML)
- **Copilot Versions**: Optimized for Microsoft Copilot as of November 2025
- **Updates**: Check manifest.yml for latest character counts
- **Full Content**: For comprehensive content, use [English](../en/) or [Japanese](../ja/) versions

---

**Version**: 1.0.0  
**Last Updated**: 2025-11-19  
**Status**: In Development (Optimization in Progress)  
**Character Limit**: 8000 characters maximum
