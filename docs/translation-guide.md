# Translation Guide

## Overview

This guide provides comprehensive guidelines for translating prompts from English to Japanese while maintaining quality, consistency, and cultural appropriateness.

---

## Translation Principles

### 1. Accuracy and Fidelity
- Translate meaning, not just words
- Preserve technical accuracy
- Maintain framework integrity
- Keep dialogue structure intact

### 2. Cultural Adaptation
- Adapt examples to Japanese business context
- Use culturally appropriate metaphors
- Adjust numerical examples (e.g., currency, dates)
- Localize company/industry examples

### 3. Natural Japanese
- Use natural, fluent Japanese
- Avoid direct word-for-word translation
- Use appropriate formality level (敬体 for business)
- Maintain readability and clarity

### 4. Consistency
- Use consistent terminology throughout
- Follow established translation conventions
- Maintain formatting and structure
- Preserve markdown syntax

---

## Language Style Guidelines

### Formality Level

**Use 敬体 (です・ます体)** throughout:

✅ **Correct**:
```
このフレームワークを活用します。
分析を実施してください。
```

❌ **Incorrect**:
```
このフレームワークを活用する。
分析を実施しろ。
```

### Tone and Voice

**Professional but accessible**:

✅ **Correct**:
```
あなたは経験豊富なビジネス戦略コンサルタントです。クライアントの事業成長を支援し、競争優位性を確立するための戦略を立案します。
```

❌ **Too casual**:
```
あなたはビジネス戦略のプロです。お客さんの商売を伸ばす作戦を考えます。
```

---

## YAML Frontmatter Translation

### What to Translate

```yaml
---
id: business-strategy-consultant  # DO NOT TRANSLATE (keep English)
category: business-management     # DO NOT TRANSLATE (keep English)
frameworks:                       # TRANSLATE framework names
  - SWOT分析
  - ポーターの5つの力
  - バリューチェーン分析
  - ビジネスモデルキャンバス
dialogue_stages: 5                # DO NOT TRANSLATE (number)
version: 1.0.0                    # DO NOT TRANSLATE (version)
tags:                             # TRANSLATE tags
  - 戦略
  - 分析
  - コンサルティング
  - ビジネス
created: 2025-11-19               # DO NOT TRANSLATE (date)
updated: 2025-11-19               # DO NOT TRANSLATE (date)
---
```

### Field-by-Field Guide

| Field | Translate? | Example |
|-------|-----------|---------|
| `id` | ❌ No | Keep `business-strategy-consultant` |
| `category` | ❌ No | Keep `business-management` |
| `frameworks` | ✅ Yes | `SWOT Analysis` → `SWOT分析` |
| `dialogue_stages` | ❌ No | Keep `5` |
| `version` | ❌ No | Keep `1.0.0` |
| `tags` | ✅ Yes | `strategy` → `戦略` |
| `created` | ❌ No | Keep date format |
| `updated` | ❌ No | Keep date format |

---

## Framework Translation

### Common Frameworks

English → Japanese translation reference:

| English | Japanese |
|---------|---------|
| SWOT Analysis | SWOT分析 |
| Porter's Five Forces | ポーターの5つの力 / ポーターのファイブフォース |
| Value Chain Analysis | バリューチェーン分析 |
| Business Model Canvas | ビジネスモデルキャンバス |
| PEST Analysis | PEST分析 |
| Design Thinking | デザイン思考 |
| Lean Startup | リーンスタートアップ |
| Agile Methodology | アジャイル手法 |
| Scrum Framework | スクラムフレームワーク |
| OKR (Objectives and Key Results) | OKR (目標と主要な結果) |
| KPI (Key Performance Indicators) | KPI (重要業績評価指標) |
| Balanced Scorecard | バランスト・スコアカード |
| McKinsey 7S Framework | マッキンゼーの7S |
| BCG Matrix | BCGマトリックス |
| Ansoff Matrix | アンゾフのマトリックス |
| Blue Ocean Strategy | ブルーオーシャン戦略 |
| Triple Bottom Line | トリプルボトムライン |
| Stakeholder Analysis | ステークホルダー分析 |
| Gap Analysis | ギャップ分析 |
| Root Cause Analysis | 根本原因分析 |

### Keep as Katakana When Appropriate

Some terms are commonly used in Katakana in Japanese business:

- Stakeholder → ステークホルダー
- Roadmap → ロードマップ
- Milestone → マイルストーン
- Dashboard → ダッシュボード
- Workflow → ワークフロー
- Template → テンプレート
- Framework → フレームワーク

---

## Section Translation Guidelines

### Role Definition (役割定義)

**English**:
```markdown
## Role

You are an experienced business strategy consultant...
```

**Japanese**:
```markdown
## 役割

あなたは経験豊富なビジネス戦略コンサルタントです...
```

### Dialogue Flow (対話フロー)

**English**:
```markdown
## Dialogue Flow

### Stage 1: Context Understanding
```

**Japanese**:
```markdown
## 対話フロー

### Stage 1: コンテキストの理解
```

**Stage Names Translation**:
- Stage 1: Context Understanding → Stage 1: コンテキストの理解
- Stage 2: Analysis → Stage 2: 分析
- Stage 3: Framework Application → Stage 3: フレームワークの適用
- Stage 4: Solution Development → Stage 4: ソリューションの開発
- Stage 5: Output Generation → Stage 5: 成果物の生成

### Applied Expertise and Frameworks (活用する専門知識・フレームワーク)

**English**:
```markdown
## Applied Expertise and Frameworks

### SWOT Analysis

**Strengths**: Internal positive attributes...
```

**Japanese**:
```markdown
## 活用する専門知識・フレームワーク

### SWOT分析

**強み (Strengths)**: 内部の肯定的な属性...
```

### Output Format (出力形式)

**English**:
```markdown
## Output Format

The generated meta-prompt will be in the following format:
```

**Japanese**:
```markdown
## 出力形式

生成されるメタプロンプトは以下の形式で出力されます:
```

### Usage Example (使用例)

**English**:
```markdown
## Usage Example

### Scenario: SaaS Startup Strategy
```

**Japanese**:
```markdown
## 使用例

### シナリオ: SaaS スタートアップの戦略立案
```

---

## Cultural Adaptation Examples

### Company Names and Industries

**English Example**:
```
A mid-sized manufacturing company in the Midwest...
```

**Japanese Adaptation**:
```
関東地方の中堅製造業...
```

### Numerical Examples

**English**:
```
Revenue: $5 million
Market size: $100 million
```

**Japanese**:
```
売上高: 5億円
市場規模: 100億円
```

**Conversion**: Use realistic Japanese market sizes (not direct USD conversion)

### Business Context

**English**:
```
Board of Directors meeting
Quarterly earnings report
SEC filing
```

**Japanese**:
```
取締役会
四半期決算報告
有価証券報告書
```

### Job Titles

**English** → **Japanese**:
- CEO → 最高経営責任者(CEO) / 代表取締役
- CFO → 最高財務責任者(CFO) / 財務担当役員
- CTO → 最高技術責任者(CTO) / 技術担当役員
- VP of Sales → 営業担当副社長 / 営業本部長
- Product Manager → プロダクトマネージャー
- Team Lead → チームリーダー / リーダー

---

## Terminology Consistency

### Standard Translations

Maintain consistency for these common terms:

| English | Japanese | Notes |
|---------|---------|-------|
| goal | 目標 | Not ゴール |
| objective | 目的 | |
| target | ターゲット / 目標値 | Context-dependent |
| metric | 指標 / メトリクス | |
| baseline | ベースライン / 基準値 | |
| benchmark | ベンチマーク | Keep in katakana |
| best practice | ベストプラクティス | Keep in katakana |
| workflow | ワークフロー | Keep in katakana |
| feedback | フィードバック | Keep in katakana |
| stakeholder | ステークホルダー | Keep in katakana |
| roadmap | ロードマップ | Keep in katakana |
| timeline | タイムライン / 時間軸 | Context-dependent |
| deliverable | 成果物 / 納品物 | |
| milestone | マイルストーン | Keep in katakana |
| risk | リスク | Keep in katakana |
| opportunity | 機会 | |
| threat | 脅威 | |
| challenge | 課題 | |

---

## Markdown Formatting

### Preserve All Formatting

✅ **Correct** (maintains structure):
```markdown
### Stage 1: コンテキストの理解

**目標**: ビジネスの現状と課題を理解する

質問項目:
- 現在の事業内容は何ですか?
- 主要な競合他社は誰ですか?
```

❌ **Incorrect** (loses structure):
```markdown
Stage 1: コンテキストの理解
目標: ビジネスの現状と課題を理解する
質問項目:
現在の事業内容は何ですか?
主要な競合他社は誰ですか?
```

### Code Blocks

Translate comments, keep code:

**English**:
````markdown
```python
# Calculate ROI
roi = (gain - cost) / cost
```
````

**Japanese**:
````markdown
```python
# ROIを計算
roi = (gain - cost) / cost
```
````

### Tables

Translate headers and content:

**English**:
```markdown
| Strength | Weakness |
|----------|----------|
| Strong brand | Limited reach |
```

**Japanese**:
```markdown
| 強み | 弱み |
|------|------|
| 強力なブランド | 限定的なリーチ |
```

---

## Quality Checklist

Before submitting a translation, verify:

- [ ] YAML frontmatter: IDs unchanged, frameworks translated
- [ ] All section headers translated
- [ ] Formality level consistent (敬体)
- [ ] Framework names use standard Japanese terms
- [ ] Examples adapted to Japanese context
- [ ] Numbers and currency localized
- [ ] Company names and titles localized
- [ ] Markdown formatting preserved
- [ ] No English left in body text (except technical terms)
- [ ] Natural, fluent Japanese
- [ ] Consistent terminology throughout
- [ ] All links and references updated

---

## Common Mistakes to Avoid

### ❌ Don't Translate IDs

**Wrong**:
```yaml
id: ビジネス-戦略-コンサルタント
```

**Correct**:
```yaml
id: business-strategy-consultant
```

### ❌ Don't Over-Translate Technical Terms

**Wrong**:
```
デザイン思考 (Design Thinking) のエンパシー化、定義化、発想化...
```

**Correct**:
```
デザイン思考の共感、定義、発想...
```

### ❌ Don't Use Overly Literal Translation

**Wrong**:
```
あなたの強みは何ですか? (literal: What are your strengths?)
```

**Better**:
```
貴社の強みをお聞かせください。(polite, natural)
```

### ❌ Don't Mix Formality Levels

**Wrong**:
```
このフレームワークを使います。次にやるべきことを考えよう。
(です・ます体 mixed with だ・である体)
```

**Correct**:
```
このフレームワークを使用します。次に実施すべきことを検討しましょう。
```

---

## Translation Workflow

### Step-by-Step Process

1. **Prepare**
   - Read English version completely
   - Understand all frameworks and concepts
   - Identify culturally specific elements

2. **Translate YAML Frontmatter**
   - Keep IDs and technical fields unchanged
   - Translate frameworks using standard terms
   - Translate tags

3. **Translate Role Section**
   - Use formal, professional tone
   - Maintain expertise level

4. **Translate Dialogue Flow**
   - Keep 5-stage structure
   - Translate stage names consistently
   - Adapt questions to Japanese business context

5. **Translate Frameworks Section**
   - Use established Japanese framework names
   - Provide Japanese explanations
   - Keep technical accuracy

6. **Translate Examples**
   - Adapt to Japanese business context
   - Localize company names, industries
   - Convert currency and numbers
   - Use Japanese company structures

7. **Translate Output Format**
   - Maintain template structure
   - Translate placeholder text
   - Keep code/format syntax

8. **Review and Quality Check**
   - Read entire translation
   - Check consistency
   - Verify formality level
   - Test with native speaker if possible

---

## Tools and Resources

### Recommended Resources

- **Framework terminology**: Japanese business textbooks
- **Business terms**: Japanese corporate websites (上場企業の公式サイト)
- **Technical terms**: Japanese IT/tech documentation
- **Style guide**: Japanese business writing guides

### Character Counting

Japanese version has same target length as English (10,000-15,000 chars):

```bash
# Count characters in Japanese file
wc -m ja/prompts/category/prompt.md
```

---

## Support

- Questions about translation: [GitHub Issues](https://github.com/nahisaho/ouranos-agentic-library/issues)
- Terminology discussions: Tag with `translation`
- Style guide updates: Submit PR with explanation

---

**Last Updated**: 2025-11-19  
**Version**: 1.0.0
