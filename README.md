# slide-storyboard

アジェンダから全スライドの構成案をまとめ、内容と確認事項を一覧できる HTML ストーリーボードを作るエージェントスキルです。全体の流れを確認してから各スライドを具体化できるため、PowerPoint などで資料を作り始める前の構成レビューに使えます。

## できること

- 既存のアジェンダや資料を読み、目的・対象者・発表時間に合わせてスライド案を作成
- 全スライドのタイトル、メッセージ、掲載内容、図表や素材、レイアウト案をまとめて提示
- 修正内容を該当スライドと全体の流れに反映
- 出典や確認が必要な内容を、対象スライドと確認先が分かる形で記録
- ブラウザーで確認できる単一の HTML ファイルを出力

不足情報は `【仮案】`（未承認の提案）と `【要確認】`（事実・数値・出典などの確認事項）で区別します。確認結果が得られた項目は本文と一覧から取り除きます。

## 対応エージェント

[`npx skills`](https://github.com/vercel-labs/skills) が対応するエージェントで利用できます。Codex と Claude Code へのインストール例です。

```bash
npx skills add KotaSugiki/slide-storyboard --skill slide-storyboard --agent codex
npx skills add KotaSugiki/slide-storyboard --skill slide-storyboard --agent claude-code
```

このコマンドはリポジトリの現在の公開内容を取得します。公開済みバージョンの変更履歴は [GitHub Releases](https://github.com/KotaSugiki/slide-storyboard/releases) で確認できます。

## 最短で試す

インストール後、対応エージェントの新しいセッションで次を依頼してください。

```text
/slide-storyboard
新入社員向けに、社内の情報セキュリティの基本を10分で説明する資料を作りたい。
スライド案をまとめて確認してから、HTMLストーリーボードにして。
```

アジェンダや参考資料があれば一緒に渡せます。生成された `slide-storyboard.html` をブラウザーで開き、内容を確認してください。アジェンダや参考資料がある場合は、それらと同じディレクトリに保存します。

## 成果物とレイアウト候補

成果物は、スライドごとの内容・ワイヤーフレーム・図表仕様・出典・未確認事項をまとめた単一の HTML ファイルです。テンプレートは [`assets/template.html`](assets/template.html) です。

[レイアウト候補のプレビュー](layout-candidates-preview.html) では、レイアウト案を絞り込みながらワイヤーフレームを確認できます。

## 制限とデータの扱い

- このスキルはストーリーボードを作成します。PowerPoint ファイルや画像そのものは出力しません。
- スライド案や出典の正しさは、元資料と利用者による確認が必要です。根拠のない数値、引用、出典を作らず、確認事項として残します。
- 画像生成を使う場合は、エージェントが選択した外部 AI サービスに内容が送信されることがあります。機密情報を含む資料を渡す前に、そのサービスのデータ利用条件を確認してください。
- 外部資料を使う場合は、出典と利用条件を確認してください。ライセンスが不明な素材は完成資料に使う前に確認が必要です。

## 開発と検証

必要なもの: Python 3.10 以上、Node.js と npm（スキルの認識・コピーインストールを確認する場合）。

```bash
python scripts/validate_repo.py
npx skills add . --list
python scripts/validate_repo.py --skill-smoke
```

`--skill-smoke` は `npx skills` の一覧表示と、Codex 向けのコピーインストールを一時ディレクトリ内で確認します。GitHub Actions でも同じ検証を実行します。

## コントリビューション

不具合や改善案は [Issues](https://github.com/KotaSugiki/slide-storyboard/issues) に報告してください。変更の提案は [CONTRIBUTING.md](CONTRIBUTING.md) の手順に沿って Pull Request を作成してください。行動規範は [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)、脆弱性の報告方法は [SECURITY.md](SECURITY.md) を参照してください。

## ライセンス

[MIT License](LICENSE) で公開しています。
