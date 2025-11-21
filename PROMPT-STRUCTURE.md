# Ouranos Agentic Library - Prompt Structure Guide

**生成日**: 2025-11-20  
**バージョン**: 1.0.0

---

## 概要

このドキュメントは、Ouranos Agentic Libraryに含まれる全44プロンプトの共通構造と設計パターンを説明します。すべてのプロンプトは一貫した構造を持ち、専門分野に特化したコンサルタント/アドバイザーとして対話型の支援を提供します。

---

## 共通構造

すべてのプロンプトは以下の7つの主要セクションで構成されています:

### 1. YAML Front Matter（メタデータ）

```yaml
---
id: [prompt-id]                    # プロンプトの一意識別子
category: [category-name]          # カテゴリ分類
frameworks:                        # 使用するフレームワーク・手法のリスト
  - Framework 1
  - Framework 2
  - Framework 3
dialogue_stages: [4-5]             # 対話ステージ数（通常5、一部4）
version: 1.0.0                     # バージョン番号（セマンティックバージョニング）
tags:                              # 検索・分類用タグ
  - tag1
  - tag2
  - tag3
created: 2025-11-19               # 作成日
updated: 2025-11-19               # 最終更新日
---
```

**目的**: プロンプトのメタ情報を構造化し、検索・分類・バージョン管理を可能にする

---

### 2. Role（役割定義）

```markdown
## Role

You are an expert [role/title] with deep expertise in [domain]. Your mission is to [mission statement].

Your expertise:

- Expertise area 1
- Expertise area 2
- Expertise area 3
- Expertise area 4
- Expertise area 5
```

**構成要素**:
- **役割の明確な定義**: AIが演じる専門家の役割
- **専門分野の説明**: 深い知識を持つ領域
- **ミッション**: 何を達成するために存在するか
- **専門知識リスト**: 具体的なスキルセットと知識領域（通常5項目）

**目的**: AIのペルソナ、権限、専門性を確立する

---

### 3. Dialogue Flow（対話フロー）

プロンプトのコア部分。通常**5ステージ**（一部4ステージ）の段階的対話プロセス。

#### ステージ構造（各ステージ共通）

```markdown
### Stage [N]: [Stage Title]

**Goal**: [Stage objective - what to achieve in this stage]

[Introductory context or instructions]

[Stage-specific content organized by numbered sections or subsections]

**Stage [N] Output**: [Expected deliverable from this stage]
```

**各ステージの要素**:
1. **Goal（目標）**: このステージで達成すべき明確な目的
2. **探索領域/質問項目**: 順を追って収集する情報やディスカッションポイント
3. **フレームワーク適用**: 該当する場合、具体的なフレームワークの使用方法
4. **Stage Output（成果物）**: ステージ終了時に提供すべき具体的な成果

#### 典型的な5ステージパターン

**Stage 1: Context Understanding（文脈理解）**
- 目的: 現状把握、背景情報収集
- パターン: "Understanding the [Domain] Context"
- 収集情報: 組織概要、現状課題、目標、制約条件

**Stage 2: Deep Analysis/Discovery（詳細分析・発見）**
- 目的: より深い分析、利害関係者の理解、要件定義
- パターン: 対象領域の詳細な探索
- 収集情報: 具体的なニーズ、期待値、成功基準

**Stage 3: Framework Application（フレームワーク適用）**
- 目的: 専門的なフレームワークや手法を用いた分析
- パターン: SWOT、PEST、Porter's Five Forces等の体系的分析
- 成果物: 構造化された分析結果、洞察

**Stage 4: Strategy/Solution Development（戦略・ソリューション開発）**
- 目的: 具体的な戦略、計画、ソリューションの策定
- パターン: 実行可能な提案の作成
- 成果物: 詳細な戦略、設計、実装計画

**Stage 5: Implementation & Measurement（実装と測定）**
- 目的: 実装ロードマップ、KPI、継続的改善
- パターン: ロードマップ、メトリクス、ガバナンス
- 成果物: アクションプラン、測定フレームワーク、モニタリング計画

---

### 4. Applied Expertise and Frameworks（適用される専門知識とフレームワーク）

```markdown
## Applied Expertise and Frameworks

### [Framework Name 1]

**Principle**: [Core principle or purpose]

**Application**:
- How to apply
- When to use
- Key components

**Example**: [Concrete example if applicable]

### [Framework Name 2]
[同様の構造]
```

**目的**: 
- 使用するフレームワークや手法の詳細説明
- 適用方法とベストプラクティスの提示
- 理論的基盤の提供

**典型的な内容**:
- フレームワークの原理・原則
- 適用方法とステップ
- 使用タイミング・条件
- 具体例やケーススタディ
- ベストプラクティス

---

### 5. Output Format（アウトプット形式）

```markdown
## Output Format

The [deliverable name] will include:

\`\`\`markdown
# [Deliverable Title]

## Section 1
[Description]

## Section 2
[Description]

...
\`\`\`
```

**目的**: 最終成果物の具体的な形式とテンプレートを提供

**典型的な要素**:
- 構造化されたアウトライン
- 各セクションの説明
- マークダウン形式のテンプレート
- 期待される内容の詳細

---

### 6. Usage Example（使用例）

```markdown
## Usage Example

### Scenario: [Realistic scenario description]

**Stage 1**: [What happens in stage 1]
- [Key details]

**Stage 2**: [What happens in stage 2]
- [Key details]

...

**Final Outcome**: [Results achieved]
```

**目的**: 実際の使用シナリオを通じてプロンプトの動作を示す

**典型的な内容**:
- 具体的なシナリオ設定
- 各ステージでのやり取り例
- 期待される成果
- 実際の改善結果や影響

---

### 7. Important Notes（重要な注意事項）

```markdown
## Important Notes

### [Topic] Best Practices

1. **Practice 1**: Description
2. **Practice 2**: Description
...

### Common Pitfalls

- Pitfall 1
- Pitfall 2
...

### Success Factors

- Factor 1
- Factor 2
...
```

**目的**: ベストプラクティス、注意点、成功要因の提示

**典型的な内容**:
- ベストプラクティス
- よくある失敗・落とし穴
- 成功要因
- 品質チェックポイント
- 倫理的配慮（該当する場合）

---

### 8. Version Information（バージョン情報）

```markdown
## Version Information

- **Version**: 1.0.0
- **Created**: 2025-11-19
- **Updated**: 2025-11-19
- **Status**: Active
```

**目的**: プロンプトのバージョン管理と変更履歴の追跡

---

## 設計原則

### 1. **段階的精緻化（Progressive Refinement）**
- 広い理解から詳細へと段階的に深化
- 各ステージが前ステージの成果に基づく
- 反復的な確認と調整

### 2. **フレームワーク駆動（Framework-Driven）**
- 実証済みのフレームワークと手法を活用
- 理論と実践の橋渡し
- 構造化されたアプローチ

### 3. **アクション指向（Action-Oriented）**
- 実行可能な成果物を重視
- 具体的なステップとガイダンス
- 測定可能な結果

### 4. **専門性の明確化（Clear Expertise）**
- 明確な役割とペルソナ
- 特定分野の深い専門知識
- 権威あるガイダンス

### 5. **構造化された対話（Structured Dialogue）**
- 明確なステージ分け
- 各ステージの目標と成果物
- 論理的なフロー

---

## カテゴリ別の特徴

### Business Management（ビジネス管理）
- **焦点**: 戦略、運用、財務、マーケティング
- **フレームワーク例**: SWOT, PEST, Porter's Five Forces, Business Model Canvas
- **成果物**: 戦略計画、ロードマップ、KPI、実装計画

### Design & Development（設計・開発）
- **焦点**: ソフトウェア設計、UX/UI、アーキテクチャ、開発プロセス
- **フレームワーク例**: SOLID原則, Design Patterns, Agile, API設計原則
- **成果物**: 設計仕様、アーキテクチャ図、実装ガイド、ベストプラクティス

### Research（リサーチ）
- **焦点**: 調査方法論、データ分析、文献レビュー
- **フレームワーク例**: 統計分析, 質的分析, 研究デザイン, 倫理基準
- **成果物**: 研究計画、分析結果、レポート、推奨事項

### Education（教育）
- **焦点**: カリキュラム設計、教育評価、学習技術
- **フレームワーク例**: Bloom's Taxonomy, Backward Design, ADDIE, UDL
- **成果物**: カリキュラム、評価計画、学習体験設計

### Social Policy（社会政策）
- **焦点**: 政策分析、プログラム評価、コミュニティエンゲージメント
- **フレームワーク例**: 政策分析フレームワーク, Logic Models, 影響評価
- **成果物**: 政策提案、評価報告、エンゲージメント戦略

### HR & Organization（人事・組織）
- **焦点**: 人材管理、組織開発、リーダーシップ、パフォーマンス
- **フレームワーク例**: コーチングモデル, 組織変革理論, タレント管理
- **成果物**: 開発計画、組織戦略、コーチングプラン

### Communication（コミュニケーション）
- **焦点**: ブランディング、PR、戦略的コミュニケーション
- **フレームワーク例**: メッセージング階層, メディア戦略, 危機管理
- **成果物**: メッセージング戦略、PRプラン、コンテンツ戦略

---

## ステージ数のバリエーション

### 5ステージ（標準）- 43プロンプト
最も一般的な構造。包括的な対話プロセスに適している。

**典型的なフロー**:
1. 文脈理解
2. 詳細分析/発見
3. フレームワーク適用/分析
4. 戦略・ソリューション開発
5. 実装とメトリクス

### 4ステージ - 1プロンプト（meta-prompt-generator）
メタプロンプト生成の特殊な用途に最適化。

**フロー**:
1. 目標の明確化
2. コンテキスト情報収集
3. 専門知識とフレームワークの適用
4. メタプロンプトの生成

---

## フレームワークの使用パターン

### ビジネス戦略系
- **SWOT Analysis**: 内部・外部環境分析
- **PEST Analysis**: マクロ環境分析
- **Porter's Five Forces**: 競争環境分析
- **Business Model Canvas**: ビジネスモデル設計
- **Value Chain Analysis**: 価値創造プロセス分析

### プロダクト・マーケティング系
- **Jobs-to-be-Done**: 顧客ニーズ理解
- **4P/4C Marketing Mix**: マーケティング戦略
- **Customer Journey Mapping**: 顧客体験設計
- **Positioning Framework**: ポジショニング戦略

### 技術・開発系
- **SOLID Principles**: オブジェクト指向設計
- **Design Patterns**: ソフトウェア設計パターン
- **REST/GraphQL**: API設計原則
- **Agile/Scrum**: 開発プロセス

### リサーチ・分析系
- **Descriptive/Inferential Statistics**: 統計分析
- **Qualitative Coding**: 質的分析
- **Research Design Frameworks**: 研究設計
- **Thematic Analysis**: テーマ分析

### 教育系
- **Bloom's Taxonomy**: 学習目標分類
- **Backward Design (UbD)**: カリキュラム設計
- **ADDIE Model**: 教育設計プロセス
- **Universal Design for Learning (UDL)**: 学習のユニバーサルデザイン

---

## 質の高いプロンプトの特徴

### 1. **明確性（Clarity）**
- 役割、目標、期待される成果が明確
- 曖昧さを排除した具体的な指示
- 用語の定義と共通理解の確立

### 2. **構造化（Structure）**
- 論理的なフローとステップ
- セクションと階層の整理
- 一貫したフォーマット

### 3. **文脈提供（Context）**
- 十分な背景情報
- 目標と制約の明示
- 適用範囲の明確化

### 4. **実用性（Practicality）**
- 実行可能な成果物
- 具体的な例とテンプレート
- 段階的な実装ガイド

### 5. **専門性（Expertise）**
- 実証済みのフレームワーク
- 業界のベストプラクティス
- 深い専門知識の反映

### 6. **適応性（Adaptability）**
- 柔軟な対話フロー
- ユーザー入力に基づく調整
- 必要に応じた質問の追加・修正

---

## メタプロンプトとの関係

`meta-prompt-generator.md`は、このライブラリの他のすべてのプロンプトと同じ構造パターンに従う新しいプロンプトを生成するために設計されています。

**メタプロンプトの役割**:
1. ユーザーとの対話を通じて要件を収集
2. 適切なフレームワークを選択
3. この構造ガイドに従ったプロンプトを生成
4. 一貫性と品質を保証

---

## ベストプラクティス

### プロンプト作成時
1. **明確な役割定義**: AIのペルソナと専門性を確立
2. **段階的なフロー**: 論理的に繋がる5ステージを設計
3. **フレームワーク統合**: 実証済みの手法を適用
4. **具体的な成果物**: 各ステージの明確なアウトプット
5. **使用例提供**: 実際のシナリオで動作を示す

### プロンプト使用時
1. **順序を守る**: ステージを飛ばさず順番に進行
2. **十分な情報提供**: 各ステージで詳細な回答を提供
3. **確認と調整**: 各ステージの成果を確認し必要に応じて調整
4. **フレームワーク活用**: 提示されたフレームワークを積極的に使用
5. **成果物の精緻化**: アウトプットフォーマットに従って成果物を作成

---

## 統計サマリー

| 項目 | 詳細 |
|---|---|
| **総プロンプト数** | 44 |
| **カテゴリ数** | 11 |
| **5ステージプロンプト** | 43 (97.7%) |
| **4ステージプロンプト** | 1 (2.3%) |
| **平均フレームワーク数** | 4-5 per prompt |
| **共通セクション** | 7（メタデータ、役割、対話、フレームワーク、形式、例、注意事項） |

---

## まとめ

Ouranos Agentic Libraryのプロンプトは、以下の特徴を持つ統一された構造に従っています:

1. **一貫した7セクション構造**: メタデータから注意事項まで
2. **段階的な5ステージ対話**: 文脈理解から実装まで
3. **フレームワーク駆動**: 実証済みの手法と理論
4. **実行可能な成果物**: 具体的なアウトプットとテンプレート
5. **専門性の明確化**: 明確な役割と専門知識

この構造により、一貫性、品質、使いやすさが保証され、ユーザーは様々な専門分野で効果的なAI支援を受けることができます。

---

**バージョン**: 1.0.0  
**最終更新**: 2025-11-20  
**ステータス**: アクティブ

