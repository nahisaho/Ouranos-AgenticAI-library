# GUIアプリケーション開発 プロジェクト計画書

**プロジェクト名**: Ouranos-AgenticAI-library GUI Application
**バージョン**: 1.0
**作成日**: 2025-11-23
**最終更新日**: 2025-11-23

---

## 1. プロジェクト概要

### 1.1 プロジェクト概要

本プロジェクトは、Ouranos-AgenticAI-libraryの対話型GUIアプリケーションを開発します。54以上のプロンプトテンプレートをブラウザ上で検索・閲覧・対話できるインタラクティブプラットフォームを構築し、Google NotebookLMに着想を得たユーザー体験を提供します。

### 1.2 背景

現在、プロンプトテンプレートはMarkdownファイルとしてGitリポジトリに保存されています。ユーザーがこれらのテンプレートを効果的に活用するためには、検索機能、カテゴリブラウジング、対話的なチャットインターフェースが必要です。

### 1.3 アーキテクチャ概要

**Three-Tier Interactive Prompt Platform (API-First)**

- **Frontend Layer**: Next.js 14+ with React 18（インタラクティブUI、プロンプトブラウザ、チャットインターフェース）
- **API Layer**: FastAPI with Python 3.11+（プロンプト処理、AI統合、セッション管理）
- **Database Layer**: SurrealDB（プロンプトメタデータ、チャットセッション、エンベディング）

---

## 2. 目標とスコープ

### 2.1 プロジェクト目標

#### 主要目標

1. **ユーザビリティ**: 非技術者でも直感的に使用できるGUIを提供
2. **検索性**: 54以上のテンプレートを効率的に検索・発見可能に
3. **インタラクティブ性**: AIとの対話を通じたメタプロンプト生成
4. **拡張性**: 将来の機能追加を容易にするモジュラー設計

#### 成功基準

- ページロード時間 < 2秒
- API応答時間 < 200ms（95パーセンタイル）
- テストカバレッジ > 80%
- WCAG 2.1 AAコンプライアンス

### 2.2 スコープ

#### スコープ内

- プロンプトテンプレートのブラウジング・検索UI
- カテゴリ別フィルタリング機能
- 対話型チャットインターフェース
- RESTful API（プロンプトCRUD、チャットセッション）
- 多言語サポート（英語、日本語）
- Dockerによるセルフホストデプロイ

#### スコープ外（将来フェーズ）

- ユーザー認証・認可
- カスタムプロンプト作成機能
- AIプロバイダー設定UI
- コラボレーション機能

---

## 3. ステークホルダー

### 3.1 プロジェクトチーム

| 役割 | 責任範囲 |
|------|----------|
| **プロダクトオーナー** | ビジョン、ロードマップ、優先順位決定 |
| **テックリード** | アーキテクチャ設計、技術的意思決定 |
| **フロントエンド開発者** | Next.js/React UI実装 |
| **バックエンド開発者** | FastAPI実装、データベース設計 |
| **QAエンジニア** | テスト設計・実行、品質保証 |
| **UI/UXデザイナー** | ワイヤーフレーム、プロトタイプ |

### 3.2 エンドユーザー

#### プライマリユーザー

1. **AIプロンプトエンジニア/プラクティショナー**
   - 高品質なプロンプトテンプレートの検索・活用
   - 再利用可能なプロンプトライブラリの構築

2. **プロフェッショナル/ドメインエキスパート**
   - 専門分野でのAIアシスタンス取得
   - フレームワークに基づいたガイダンス

---

## 4. 主要マイルストーン

| マイルストーン | 期間 | 成果物 | 完了基準 |
|---------------|------|--------|---------|
| **M1: 要件定義完了** | Week 1-2 | SRS、ユーザーストーリー、EARS形式要件 | ステークホルダー承認 |
| **M2: 設計完了** | Week 3-4 | アーキテクチャ設計、API仕様、DB設計、UI/UXデザイン | 設計レビュー完了 |
| **M3: MVP実装完了** | Week 5-8 | フロントエンド、バックエンド、データベース | コードレビュー完了 |
| **M4: テスト完了** | Week 9-10 | ユニットテスト、統合テスト、E2Eテスト | カバレッジ80%以上 |
| **M5: デプロイ完了** | Week 11-12 | Docker設定、CI/CD、ドキュメント | 本番環境稼働 |
| **M6: リリース** | Week 12 | v1.0リリース | 品質ゲート全項目通過 |

---

## 5. SDDワークフローに沿った作業計画

本プロジェクトはSpecification Driven Development (SDD)の8ステージワークフローに従います。

### Stage 1: Research（リサーチ）

**期間**: Week 1
**担当エージェント**: System Architect, UI/UX Designer

**成果物**:
- 技術調査レポート
- 競合分析（NotebookLM等）
- UIパターン調査
- フレームワーク選定根拠

**タスク**:
1. Next.js 14 App Routerの最新機能調査
2. FastAPIとSurrealDBの統合パターン調査
3. AIチャットUIのベストプラクティス調査
4. プロンプトブラウジングUIパターン調査

---

### Stage 2: Requirements（要件定義）

**期間**: Week 1-2
**担当エージェント**: Requirements Analyst

**成果物**:
- Software Requirements Specification (SRS)
- 機能要件（EARS形式）
- 非機能要件
- ユーザーストーリー
- 受入基準

**タスク**:
1. ステークホルダーインタビュー
2. ユースケース分析
3. EARS形式での要件記述
4. 要件トレーサビリティマトリクス作成

**EARS形式要件例**:

```
REQ-PROMPT-001: WHEN a user enters a search query in the search box,
the system SHALL display matching prompt templates within 500ms,
filtered by title, category, tags, and description.

REQ-CHAT-001: WHEN a user sends a message in the chat interface,
the system SHALL maintain dialogue context and generate responses
based on the selected prompt template's dialogue stages.

REQ-I18N-001: WHERE the user has selected Japanese language preference,
the system SHALL display all UI elements and content in Japanese.
```

---

### Stage 3: Design（設計）

**期間**: Week 3-4
**担当エージェント**: System Architect, API Designer, Database Schema Designer, UI/UX Designer

**成果物**:
- C4モデル図（Context, Container, Component）
- Architecture Decision Records (ADR)
- OpenAPI仕様書
- データベーススキーマ（SurrealDB）
- ワイヤーフレーム、UIプロトタイプ

**タスク**:

1. **システムアーキテクチャ設計**
   - コンテナ図作成
   - コンポーネント図作成
   - デプロイメント図作成

2. **API設計**
   - RESTエンドポイント定義
   - リクエスト/レスポンススキーマ
   - エラーハンドリング設計

3. **データベース設計**
   - エンティティ定義（Prompt, Category, Session, Message）
   - リレーション設計
   - インデックス設計

4. **UI/UX設計**
   - ワイヤーフレーム
   - デザインシステム（shadcn/ui）
   - インタラクションフロー

---

### Stage 4: Tasks（タスク分解）

**期間**: Week 4
**担当エージェント**: Project Manager

**成果物**:
- タスクブレークダウン
- 要件カバレッジマトリクス
- スプリント計画
- 依存関係マップ

**タスクカテゴリ**:

1. **フロントエンドタスク**
   - 共通UIコンポーネント実装
   - プロンプト一覧ページ
   - プロンプト詳細ページ
   - チャットインターフェース
   - 検索機能
   - i18n対応

2. **バックエンドタスク**
   - FastAPIプロジェクトセットアップ
   - プロンプトAPI実装
   - チャットAPI実装
   - 検索サービス実装
   - SurrealDBクライアント実装

3. **インフラタスク**
   - Docker構成
   - CI/CDパイプライン
   - 環境設定

---

### Stage 5: Implementation（実装）

**期間**: Week 5-8
**担当エージェント**: Software Developer

**成果物**:
- ソースコード（TypeScript/Python）
- ユニットテスト
- 統合テスト
- コードドキュメント

**実装順序**:

**Sprint 1 (Week 5-6): コア機能**
- SurrealDBセットアップとスキーマ作成
- FastAPI基本構造とプロンプトAPI
- Next.jsプロジェクト構造とルーティング
- 基本UIコンポーネント

**Sprint 2 (Week 7-8): 応用機能**
- チャット機能
- 検索機能
- i18n対応
- エラーハンドリング

---

### Stage 6: Testing（テスト）

**期間**: Week 9-10
**担当エージェント**: Test Engineer, Quality Assurance

**成果物**:
- テスト計画書
- テストケース（EARS要件マッピング）
- ユニットテストコード
- 統合テストコード
- E2Eテストコード
- テストレポート

**テスト種別**:

1. **ユニットテスト**
   - フロントエンド: Jest + React Testing Library
   - バックエンド: pytest

2. **統合テスト**
   - API統合テスト
   - データベース統合テスト

3. **E2Eテスト**
   - Playwright/Cypress
   - ユーザーフロー検証

4. **パフォーマンステスト**
   - ロードテスト
   - ストレステスト

5. **アクセシビリティテスト**
   - WCAG 2.1 AA検証

---

### Stage 7: Deployment（デプロイ）

**期間**: Week 11-12
**担当エージェント**: DevOps Engineer

**成果物**:
- Dockerfile（frontend, api, single）
- docker-compose.yml
- CI/CDパイプライン（GitHub Actions）
- デプロイメントガイド
- 環境変数設定

**デプロイ構成**:

```yaml
# docker-compose.yml
services:
  frontend:
    build: ./docker/Dockerfile.frontend
    ports:
      - "3000:3000"
  api:
    build: ./docker/Dockerfile.api
    ports:
      - "8000:8000"
  surrealdb:
    image: surrealdb/surrealdb
    ports:
      - "8001:8000"
```

---

### Stage 8: Monitoring（監視）

**期間**: Week 12以降（継続）
**担当エージェント**: DevOps Engineer

**成果物**:
- 監視ダッシュボード
- アラート設定
- ログ集約設定
- パフォーマンスメトリクス

**監視項目**:

1. **アプリケーション監視**
   - API応答時間
   - エラー率
   - リクエスト数

2. **インフラ監視**
   - CPU/メモリ使用率
   - ディスク使用率
   - コンテナヘルスチェック

3. **ユーザー体験監視**
   - Core Web Vitals
   - ページロード時間
   - ユーザーセッション

---

## 6. リソース要件

### 6.1 人的リソース

| 役割 | 人数 | 期間 | スキルセット |
|------|------|------|-------------|
| テックリード | 1 | 12週 | Next.js, FastAPI, システム設計 |
| フロントエンド開発者 | 1-2 | 8週 | React 18, TypeScript, Tailwind CSS |
| バックエンド開発者 | 1 | 8週 | Python, FastAPI, SurrealDB |
| UI/UXデザイナー | 1 | 4週 | Figma, デザインシステム |
| QAエンジニア | 1 | 4週 | テスト自動化, Playwright |
| DevOpsエンジニア | 1 | 2週 | Docker, GitHub Actions |

### 6.2 技術リソース

**開発環境**:
- Visual Studio Code
- Node.js 18+
- Python 3.11+
- Docker Desktop
- Git

**クラウドリソース**:
- GitHub（リポジトリホスティング）
- Vercel/Netlify（フロントエンドホスティング：将来）
- SurrealDB Cloud（オプション）

### 6.3 ツール・ライセンス

| ツール | 用途 | ライセンス |
|--------|------|------------|
| Figma | UI/UXデザイン | Free/Pro |
| GitHub | バージョン管理、CI/CD | Free |
| Postman | APIテスト | Free |

---

## 7. リスク管理

### 7.1 リスク一覧

| リスクID | リスク内容 | 確率 | 影響度 | 対策 |
|---------|-----------|------|--------|------|
| R001 | SurrealDB習熟不足による遅延 | 中 | 高 | 早期プロトタイピング、ドキュメント整備 |
| R002 | AIプロバイダーAPI変更 | 低 | 中 | 抽象化レイヤー、フォールバック実装 |
| R003 | パフォーマンス要件未達成 | 中 | 高 | 早期負荷テスト、最適化スプリント確保 |
| R004 | チーム離脱 | 低 | 高 | ナレッジ共有、ドキュメント整備 |
| R005 | スコープクリープ | 中 | 中 | MVPスコープ厳守、変更管理プロセス |

### 7.2 リスク対応戦略

**回避**: R005 - 明確なスコープ定義と変更管理
**軽減**: R001, R003 - 早期検証とバッファ期間確保
**転嫁**: R002 - AIプロバイダー抽象化
**受容**: R004 - ドキュメント整備による影響最小化

---

## 8. 品質ゲート

### 8.1 フェーズ別品質ゲート

#### Gate 1: 要件定義完了（Week 2）

- [ ] 全要件がEARS形式で記述
- [ ] ステークホルダー承認取得
- [ ] トレーサビリティマトリクス作成
- [ ] ユーザーストーリーと受入基準定義

#### Gate 2: 設計完了（Week 4）

- [ ] 全要件がアーキテクチャにマッピング
- [ ] ADR作成完了
- [ ] OpenAPI仕様書完成
- [ ] データベーススキーマ承認
- [ ] UI/UXデザイン承認

#### Gate 3: 実装完了（Week 8）

- [ ] コードレビュー完了
- [ ] ユニットテストカバレッジ80%以上
- [ ] 静的解析エラーなし
- [ ] セキュリティスキャン完了
- [ ] 重大バグなし

#### Gate 4: テスト完了（Week 10）

- [ ] 全テストケース実行完了
- [ ] 全EARs要件のテスト通過
- [ ] パフォーマンス基準達成
- [ ] アクセシビリティ基準達成
- [ ] 未解決の重大/高優先度バグなし

#### Gate 5: デプロイ完了（Week 12）

- [ ] ステージング環境テスト完了
- [ ] 監視・アラート設定完了
- [ ] ドキュメント更新完了
- [ ] ロールバック手順確認
- [ ] 本番デプロイ成功

---

## 9. 成果物一覧

### 9.1 ドキュメント成果物

| 成果物 | フォーマット | 保存場所 |
|--------|-------------|---------|
| Software Requirements Specification | Markdown | `storage/specs/srs.md` |
| 機能要件（EARS形式） | Markdown | `docs/requirements/functional/` |
| 非機能要件 | Markdown | `docs/requirements/non-functional/` |
| アーキテクチャ設計書 | Markdown + 図 | `docs/architecture/` |
| API仕様書 | OpenAPI YAML | `docs/api-reference/openapi.yaml` |
| データベース設計書 | Markdown | `storage/specs/database-design.md` |
| テスト計画書 | Markdown | `storage/specs/test-plan.md` |
| デプロイメントガイド | Markdown | `docs/guides/deployment.md` |
| ユーザーガイド | Markdown | `docs/user-guide/` |

### 9.2 ソースコード成果物

| 成果物 | 言語 | 保存場所 |
|--------|------|---------|
| フロントエンドコード | TypeScript/React | `frontend/` |
| バックエンドコード | Python/FastAPI | `api/` |
| データベースマイグレーション | SurrealQL | `database/migrations/` |
| テストコード | TypeScript/Python | `tests/` |
| CI/CD設定 | YAML | `.github/workflows/` |
| Docker設定 | Dockerfile/YAML | `docker/` |

### 9.3 デザイン成果物

| 成果物 | フォーマット | 保存場所 |
|--------|-------------|---------|
| ワイヤーフレーム | Figma/PNG | `docs/design/wireframes/` |
| UIモックアップ | Figma/PNG | `docs/design/mockups/` |
| デザインシステム | Figma/Markdown | `docs/design/system/` |

---

## 10. コミュニケーション計画

### 10.1 定例ミーティング

| 会議 | 頻度 | 参加者 | 目的 |
|------|------|--------|------|
| デイリースタンドアップ | 毎日 | 開発チーム | 進捗共有、障害対応 |
| スプリント計画 | 2週ごと | 全員 | スプリントゴール設定 |
| スプリントレビュー | 2週ごと | 全員 | 成果物デモ |
| レトロスペクティブ | 2週ごと | 開発チーム | プロセス改善 |

### 10.2 報告・ドキュメント

- **日次**: Git commit、プルリクエスト
- **週次**: 進捗レポート
- **マイルストーン**: 成果物レビュー

---

## 11. 承認

| 役割 | 氏名 | 署名 | 日付 |
|------|------|------|------|
| プロダクトオーナー | | | |
| テックリード | | | |
| エンジニアリングマネージャー | | | |

---

## 付録

### A. 用語集

| 用語 | 定義 |
|------|------|
| EARS | Easy Approach to Requirements Syntax - 要件記述形式 |
| SDD | Specification Driven Development - 仕様駆動開発 |
| ADR | Architecture Decision Record - アーキテクチャ決定記録 |
| SRS | Software Requirements Specification - ソフトウェア要件仕様書 |

### B. 参考資料

- [steering/structure.md](/home/nahisaho/GitHub/Ouranos-AgenticAI-library/steering/structure.md) - プロジェクト構造
- [steering/tech.md](/home/nahisaho/GitHub/Ouranos-AgenticAI-library/steering/tech.md) - 技術スタック
- [steering/product.md](/home/nahisaho/GitHub/Ouranos-AgenticAI-library/steering/product.md) - プロダクトコンテキスト
- [steering/rules/workflow.md](/home/nahisaho/GitHub/Ouranos-AgenticAI-library/steering/rules/workflow.md) - SDDワークフロー
- [steering/rules/ears-format.md](/home/nahisaho/GitHub/Ouranos-AgenticAI-library/steering/rules/ears-format.md) - EARS形式ガイド

---

**文書終了**
