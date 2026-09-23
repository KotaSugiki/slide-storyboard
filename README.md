# slide-storyboard

アジェンダがあればそれを使い、なければ対話で作成してから、スライドごとの構成(タイトル・キーメッセージ・レイアウト・イラスト構図・画像生成プロンプト)をHTMLのストーリーボードとして書き出すAgent Skillです。`npx skills` に対応しているエージェントへインストールできます。

## できること

- 既存のアジェンダ(Markdown等)を読み込み、スライド単位に区切る。アジェンダがない場合は対話で作成する
- スライドごとに、タイトル・キーメッセージ(100〜150字程度)・視覚要素を提案し、内容の正確性に関わる事項を優先して確認する
- イラストや図が必要な場合は、構図案を理由・トレードオフとともに提示し、画像生成AI(Midjourney、DALL-Eなど)にそのまま渡せる英語プロンプトを作成する
- 決まったレイアウト(既存6種＋追加23種)を、ワイヤーフレーム付きのHTMLとして可視化する
- 情報が足りない場合も、文言の仮置きは「〖仮案〗」、数値・事実・出典など確認が必要な項目は「〖要確認〗」と示してドラフトを作る
- 各スライドとHTML末尾の一覧に、確認する情報・確認先・資料作成への影響を記す。確認済みの項目は両方から外す
- 成果物はそのままブラウザで開ける単一のHTMLファイル。これを見ながらPowerPointなどでスライドを作成する

## インストール

GitHubへ公開した後、次のコマンドでインストールできます。

```bash
npx skills add KotaSugiki/slide-storyboard --skill slide-storyboard
```

特定のエージェントだけを対象にする場合:

```bash
npx skills add KotaSugiki/slide-storyboard --skill slide-storyboard --agent claude-code
npx skills add KotaSugiki/slide-storyboard --skill slide-storyboard --agent codex
```

ローカルで確認する場合:

```bash
npx skills add . --list
npx skills add . --skill slide-storyboard --agent claude-code --copy --yes
```

`SKILL.md` はリポジトリ直下にあり、`assets/template.html` はスキルの付属ファイルとして同じディレクトリから参照されます。

## 使い方

インストール後、対応エージェントのセッション内で次のように呼び出します(ユーザー呼び出し専用のスキルのため、名前を直接入力してください)。

```
/slide-storyboard
```

必要な情報を確認しながら構成案を作り、スライド構成をまとめたHTMLファイルを書き出します。回答がない項目も、仮案と要確認を区別して表示します。

## ファイル構成

- `SKILL.md` — 対話の手順を定義したスキル本体
- `assets/template.html` — 出力するHTMLストーリーボードのテンプレート(レイアウト・プリセット付き)

## ライセンス

MIT License。詳細は `LICENSE` を参照してください。
