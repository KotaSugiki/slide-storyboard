# slide-storyboard

アジェンダがあればそれを使い、なければ対話で作成してから、スライド構成(タイトル・キーメッセージ・レイアウト・イラスト構図・画像生成プロンプト)を1枚ずつ詰め、HTMLのストーリーボードとして書き出すAgent Skillです。`npx skills` に対応しているエージェントへインストールできます。

## できること

- 既存のアジェンダ(Markdown等)を読み込み、スライド単位に区切る。アジェンダがない場合は対話で作成する
- スライドごとに、タイトル・キーメッセージ(100〜150字程度)・視覚要素の要否を1問ずつ確認しながら決める
- イラストや図が必要な場合は、構図案を理由・トレードオフとともに提示し、画像生成AI(Midjourney、DALL-Eなど)にそのまま渡せる英語プロンプトを作成する
- 決まったレイアウト(既存6種＋追加23種)を、ワイヤーフレーム付きのHTMLとして可視化する
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

あとは質問に一つずつ答えていくと、最後にスライド構成をまとめたHTMLファイルが書き出されます。

## ファイル構成

- `SKILL.md` — 対話の手順を定義したスキル本体
- `assets/template.html` — 出力するHTMLストーリーボードのテンプレート(レイアウト・プリセット付き)

## ライセンス

MIT License。詳細は `LICENSE` を参照してください。
