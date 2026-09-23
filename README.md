# slide-storyboard

アジェンダがあればそれを使い、なければ必要な情報から作成します。全スライドの構成案をまとめて確認・修正し、HTMLのストーリーボードとして書き出すAgent Skillです。`npx skills` に対応しているエージェントへインストールできます。

## できること

- 既存のアジェンダ(Markdown等)を読み込み、スライド単位に区切る。アジェンダがない場合は資料の目的・対象者・制約など、構成に必要な不足情報を確認して作成する
- 全スライドのタイトル・キーメッセージ・視覚要素・レイアウト案を先に一覧で提示し、デッキ全体の流れや重複を見ながら修正する
- 必要な点だけ追加で確認し、イラストや図には構図案と画像生成AI(Midjourney、DALL-Eなど)に渡せる英語プロンプトを作成する
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

既存のアジェンダがあれば、ファイルパスやアウトラインを渡してください。なければ、資料の目的や対象者など、構成に必要な情報を伝えてください。未提示の重要事項だけを確認した後、全スライドのドラフトがまとめて提示されます。流れや各スライドの修正点を伝えると、関連箇所も含めて見直したうえでHTMLファイルが書き出されます。

## ファイル構成

- `SKILL.md` — 対話の手順を定義したスキル本体
- `assets/template.html` — 出力するHTMLストーリーボードのテンプレート(レイアウト・プリセット付き)

## ライセンス

MIT License。詳細は `LICENSE` を参照してください。
