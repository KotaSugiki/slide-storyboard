# コントリビューション

不具合報告、改善案、文書やスキルの変更を歓迎します。まず既存の [Issues](https://github.com/KotaSugiki/slide-storyboard/issues) を検索し、関連する報告がなければ Issue を作成してください。セキュリティ上の問題は公開 Issue に書かず、[SECURITY.md](SECURITY.md) の手順を使ってください。

## 変更の流れ

1. Issue の目的と完了条件を確認します。小さな誤字修正など Issue が不要な変更は、そのまま Pull Request を作成できます。
2. `main` から作業ブランチを作ります。名前は `docs/issue-12-readme`、`fix/issue-15-template` のように変更内容と Issue 番号が分かるものにします。
3. 変更は関連する範囲に絞ります。スキルの手順を変えた場合は `README.md` と `assets/template.html` の説明も確認し、用語と表示を揃えます。
4. `python scripts/validate_repo.py` を実行します。スキルのインストール経路を変更した場合は Node.js と npm を用意し、`python scripts/validate_repo.py --skill-smoke` も実行します。
5. Pull Request には、目的、主な変更、検証結果、関連 Issue を記載します。画面や HTML の見た目を変えた場合は、変更前後のスクリーンショットを添えてください。

## Pull Request の確認項目

- [ ] Issue または変更理由が記載されている
- [ ] README、SKILL、テンプレート間で説明や `【仮案】`／`【要確認】` の表記が一致している
- [ ] 検証コマンドと結果が記載されている
- [ ] 機密情報や、利用条件が不明な第三者素材を追加していない

## サポート範囲とメンテナンス

このリポジトリが保守する対象は、スキル本体、HTML テンプレート、README、検証スクリプトです。エージェント製品や `npx skills` の仕様変更による問題は、再現できる環境とコマンドを添えて報告してください。メンテナーは内容を確認して優先度と対応時期を決めます。すべての提案の採用や即時対応を保証するものではありません。

## 行動規範

参加者は [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) に従ってください。
