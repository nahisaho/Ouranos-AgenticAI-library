# Ouranos Agentic Library - 日本語版

**対話型Agentic AIプロンプトのテンプレートライブラリ**

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/nahisaho/ouranos-agentic-library)

> **他の言語**: [English](../en/README.md) | [Microsoft Copilot (最適化版)](../copilot/README.md)

## 📖 概要

Ouranos Agentic Libraryは、AIが対話を通じてユーザーの目的を明確化し、専門知識やフレームワークを活用してメタプロンプトを生成するための**対話型プロンプトテンプレート集**です。

### 特徴

- 🎯 **目的駆動型**: ユーザーの目的を対話的に明確化
- 🧠 **専門知識統合**: 各分野の理論・フレームワークを活用
- 📝 **構造化テンプレート**: 一貫したフォーマットで再利用可能
- 🔍 **多様なカテゴリ**: ビジネスから教育まで幅広い領域をカバー
- 📚 **YAMLマニフェスト**: メタデータによる体系的な管理

## 🚀 使い方

### 基本的な使用方法

1. **カテゴリの選択**: `prompts/` ディレクトリから目的に合ったカテゴリを選択
2. **テンプレートの参照**: マークダウンファイルを開いて内容を確認
3. **AIへの適用**: テンプレート内容をAIチャットにコピー&ペースト
4. **対話の実行**: AIとの対話を通じてメタプロンプトを生成

### クイックスタート

```bash
# リポジトリのクローン
git clone https://github.com/nahisaho/ouranos-agentic-library.git
cd ouranos-agentic-library/ja

# プロンプトの参照
cat prompts/general/meta-prompt-generator.md
```

詳細な使い方は [使い方ガイド](docs/usage-guide.md) を参照してください。

## 📂 ディレクトリ構成

```
ja/
├── README.md                 # このファイル
├── manifest.yml              # プロンプトのメタデータ
├── prompts/                  # プロンプトテンプレート (44プロンプト)
│   ├── general/              # 汎用 (1)
│   ├── business-management/  # ビジネス・経営 (8)
│   ├── design-development/   # デザイン・開発 (8)
│   ├── hr-organization/      # 人材・組織 (5)
│   ├── education/            # 教育 (4)
│   ├── research/             # 研究 (3)
│   ├── document-creation/    # 文書作成 (3)
│   ├── social-policy/        # 社会・政策 (3)
│   ├── communication/        # コミュニケーション (3)
│   ├── innovation-transformation/ # イノベーション・変革 (3)
│   └── specialized-domains/  # 専門領域 (3)
└── docs/                     # 追加ドキュメント
    ├── usage-guide.md        # 使い方ガイド
    ├── contribution.md       # 貢献ガイドライン
    └── framework-reference.md # フレームワーク参照集
```

## 📋 カテゴリ一覧

### 高優先度カテゴリ

| カテゴリ | 説明 | サンプル数 |
|---------|------|-----------|
| **汎用** | 汎用的な対話型プロンプト作成 | 1 |
| **ビジネス・経営** | 戦略立案、経営分析、マーケティングなど | 8 |
| **デザイン・開発** | ソフトウェア設計、UX/UI、システム開発など | 8 |
| **人材・組織** | 組織開発、人材育成、チームビルディングなど | 5 |
| **教育** | カリキュラム設計、教材作成、学習支援など | 4 |

### その他のカテゴリ

研究、文書作成、社会・政策、コミュニケーション、イノベーション・変革、専門領域など、各カテゴリに2-3個のサンプルを用意しています。

**合計: 44プロンプト**

## 🎓 対象ユーザー

- AIプロンプトエンジニア
- ビジネスコンサルタント
- ソフトウェア開発者・設計者
- 教育関係者
- 研究者
- その他、AIを活用した業務改善を目指す専門家

## 📄 ライセンス

このプロジェクトは [Creative Commons Attribution-NonCommercial 4.0 International License](../LICENSE) の下でライセンスされています。

**要約:**
- ✅ 非営利目的での利用・改変・再配布が可能
- ✅ 著作権表示が必要
- ❌ 商用利用は不可

詳細は [LICENSE](../LICENSE) ファイルをご確認ください。

## 🤝 貢献

プロジェクトへの貢献を歓迎します！詳細は [貢献ガイドライン](docs/contribution.md) をご覧ください。

### 貢献の方法

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/amazing-prompt`)
3. 変更をコミット (`git commit -m 'Add amazing prompt'`)
4. ブランチにプッシュ (`git push origin feature/amazing-prompt`)
5. プルリクエストを作成

## 📚 ドキュメント

- [使い方ガイド](docs/usage-guide.md) - 詳細な使用方法
- [貢献ガイドライン](docs/contribution.md) - プロジェクトへの貢献方法
- [フレームワーク参照集](docs/framework-reference.md) - 活用されているフレームワーク一覧
- [要件定義書](../REQUIREMENTS.md) - プロジェクトの詳細な要件

## 📞 お問い合わせ

質問や提案がある場合は、[Issues](https://github.com/nahisaho/ouranos-agentic-library/issues) を作成してください。

## 🌟 謝辞

このプロジェクトは、AI技術の発展と多様な専門知識の集積により実現しました。すべての貢献者に感謝します。

---

**Version**: 1.0.0  
**Last Updated**: 2025-11-19  
**Status**: 進行中 (1/44プロンプト完成、2.3%)
