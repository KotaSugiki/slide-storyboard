# レイアウトプリセット候補リサーチ

調査日: 2026-09-22

## 調査の前提

現在の `SKILL.md` に定義されているプリセットは次の6種です。

- `left-text-right-visual`
- `right-text-left-visual`
- `top-visual-bottom-text`
- `center-visual-split-text`
- `full-bleed-visual`
- `text-only`

以下は、これらの単純な左右／上下分割の派生ではなく、情報の関係性や読み順そのものが変わる候補を優先しています。まだ実装はしていません。

## 候補一覧

### 1. 構造・導入を見せるレイアウト

| 候補プリセット名 | ワイヤーフレームの考え方 | 向いている内容 | 参考 |
|---|---|---|---|
| `numbered-agenda-path` | 左から右へ続く番号付きの道筋／節目を並べ、各節目に短い説明を付ける | 目次、発表の流れ、章立て | [Heydecks: agenda as a numbered path](https://heydecks.com/blog/slide-design-ideas) |
| `kpi-strip` | 上部または中央に3〜4個の数値カードを横一列で配置し、下部に短い解釈を置く | 業績サマリー、調査結果、ダッシュボード | [Heydecks: KPI strip](https://heydecks.com/blog/slide-design-ideas) |
| `single-big-number` | 画面中央〜左に1つの巨大な数値、周囲に単位・比較・一行の意味付け | 重要指標、成果、インパクトの強調 | [Heydecks: one big number](https://heydecks.com/blog/slide-design-ideas) |
| `statement-with-evidence` | 大きな結論を上部または左に置き、下部に小さな根拠3点を横並び | 経営メッセージ、研究結論、方針 | [Microsoft: one key insight per data slide](https://powerpoint.cloud.microsoft/create/en/blog/powerpoint-design-ideas/) |
| `section-divider-index` | 大きな章番号と章タイトルを一方に置き、反対側に章内の項目一覧を縦積み | セクション区切り、長い資料のナビゲーション | [Visme: aligned items / table-of-contents style](https://visme.co/blog/presentation-layout/) |

### 2. 比較・判断を見せるレイアウト

| 候補プリセット名 | ワイヤーフレームの考え方 | 向いている内容 | 参考 |
|---|---|---|---|
| `before-after-rows` | 左右2列を同じ行構造で揃え、各行を旧状態／新状態として比較 | 改善前後、リニューアル、業務改革 | [Heydecks: before-and-after split](https://heydecks.com/blog/slide-design-ideas) |
| `comparison-matrix` | 上に比較対象、左に評価軸を置く表形式。セルに○×、数値、短評 | 製品比較、競合比較、選択肢の評価 | [Gixo: comparison grid](https://gixo.ai/infographic-layout) |
| `decision-scorecard` | 左に判断基準、中央に評価、右に推奨結論を置くスコアカード | 意思決定、提案比較、投資判断 | [Heydecks: evidence / research brief](https://heydecks.com/blog/slide-design-ideas) |
| `two-by-two-matrix` | 2軸の散布図領域に対象を配置し、周囲に軸の意味を明示 | 優先順位、ポジショニング、リスク評価 | [Heydecks: 2x2 matrix](https://heydecks.com/blog/slide-design-ideas) |
| `competitive-landscape` | 横軸・縦軸のマップ上に競合や選択肢をバブル配置し、自社位置を強調 | 市場マップ、競合分析、ポジショニング | [Heydecks: landscape / where the players sit](https://heydecks.com/blog/slide-design-ideas) |

### 3. 時系列・工程を見せるレイアウト

| 候補プリセット名 | ワイヤーフレームの考え方 | 向いている内容 | 参考 |
|---|---|---|---|
| `horizontal-milestone-timeline` | 横一本の時間軸に4〜8個の節目を置き、ラベルを上下交互に配置 | 歴史、ロードマップ、リリース計画 | [Slide-deck.io: horizontal timeline](https://slide-deck.io/blog/how-to-design-a-timeline-slide) |
| `vertical-milestone-timeline` | 縦の spine と時点マーカー、右側の詳細テキストを積み上げる | 詳細な沿革、履歴、長い説明を伴う工程 | [Slide-deck.io: vertical timeline](https://slide-deck.io/blog/how-to-design-a-timeline-slide) |
| `chevron-process-flow` | 左から右に連結した矢印／シェブロンを並べ、各段階に番号と短い説明を入れる | 手順、営業ステージ、導入プロセス | [Slide-deck.io: chevron or arrow flow](https://slide-deck.io/blog/how-to-design-a-timeline-slide) |
| `roadmap-lanes` | 複数の横レーンをチーム／機能別に分け、期間を帯で示す | 複数チームの計画、製品ロードマップ、簡易ガント | [Slide-deck.io: roadmap lanes](https://slide-deck.io/blog/how-to-design-a-timeline-slide) |
| `zigzag-process` | 画面内を上下に折り返す経路で工程を進め、各曲がり角にステップカードを置く | チュートリアル、複数段階のストーリー | [Visme: zig-zag / checkerboard timeline](https://visme.co/blog/presentation-layout/) |
| `cycle-loop` | 円環上に段階を配置し、最後から最初へ戻る矢印を付ける | PDCA、運用サイクル、継続改善 | [Visme: circular infographic structures](https://visme.co/blog/infographic-layout/) |

### 4. 集合・分類・関係性を見せるレイアウト

| 候補プリセット名 | ワイヤーフレームの考え方 | 向いている内容 | 参考 |
|---|---|---|---|
| `three-pillar-columns` | 同じ幅の3本の柱を横並びにし、各柱に見出し・数値・補足を持たせる | 戦略の3本柱、サービス、価値提案 | [Heydecks: three-column breakdown](https://heydecks.com/blog/slide-design-ideas) |
| `bento-grid` | 大小のカードを2×2〜3×3の不均等グリッドに組み、1セル1メッセージにする | サービス概要、実績一覧、複数KPI | [Heydecks: bento grid](https://heydecks.com/blog/slide-design-ideas) |
| `hub-and-spoke` | 中央のトピックカードから独立した周辺カードへ放射状に接続する。矢印は使わず順序を示さない | 1テーマの構成要素、機能群、関係者 | [Gixo: hub and spoke / hub card set](https://gixo.ai/infographic-layout) |
| `radial-facets` | 中心概念を中央に置き、周囲に均等な要素を円周上へ配置する | 中心概念と観点、ブランド要素、分類 | [Gixo: radial structure](https://gixo.ai/infographic-layout) |
| `logic-tree` | 上位の問い／結論から下位の判断・分岐へ枝分かれする階層図 | 論点整理、意思決定、分類、要因分解 | [Heydecks: logic tree / framework](https://heydecks.com/blog/slide-design-ideas) |
| `hierarchy-tree` | 最上位の組織／概念から、下位ノードへ段階的に枝を伸ばす | 組織図、製品体系、情報階層 | [Visme: pyramid or tree structure](https://visme.co/blog/infographic-layout/) |
| `venn-overlap` | 2〜3個の重なる円を置き、交差領域を結論または共通価値として強調 | 共通点、統合領域、ターゲット定義 | [Visme: diagram types / Venn diagram](https://visme.co/courses/wp-content/uploads/2020/08/The-Different-Types-of-Diagrams.pdf) |
| `concentric-rings` | 中心から外側へ意味の範囲が広がる同心円で、各層にラベルを付ける | エコシステム、成熟度、優先範囲、影響範囲 | [Visme: diagram types / concentric diagram](https://visme.co/courses/wp-content/uploads/2020/08/The-Different-Types-of-Diagrams.pdf) |

### 5. 量・構成・流量を見せるレイアウト

| 候補プリセット名 | ワイヤーフレームの考え方 | 向いている内容 | 参考 |
|---|---|---|---|
| `pyramid-levels` | 幅の異なる水平層を積み上げ、上位ほど少数／重要になる構造を示す | 優先順位、成熟度、価値階層、戦略 | [Visme: pyramid or tree structure](https://visme.co/blog/infographic-layout/) |
| `funnel-stages` | 上広・下狭の段階を縦に積み、各段階の件数や転換率を表示 | 販売ファネル、採用、認知から成約まで | [Visme: infographic layouts / process and data structures](https://visme.co/blog/infographic-layout/) |
| `waterfall-bridge` | 左右の合計値を大きく置き、中間の増減を階段状の棒でつなぐ | 予算差分、利益ブリッジ、増減要因 | [Microsoft: choose chart types that match the story](https://powerpoint.cloud.microsoft/create/en/blog/powerpoint-design-ideas/) |
| `chart-with-takeaway` | 上部に結論見出し、中央に1つの大きなチャート、下部に注釈1〜2個 | トレンド、比較、単一のデータ洞察 | [Microsoft: focus each data slide on one key insight](https://powerpoint.cloud.microsoft/create/en/blog/powerpoint-design-ideas/) |
| `map-with-callouts` | 背景に地図を大きく配置し、地域ごとの吹き出しや数値カードを重ねる | 地域別実績、拠点、分布、展開計画 | [Heydecks: map when geography is the message](https://heydecks.com/blog/slide-design-ideas) |

### 6. 画像・人物・証拠を見せるレイアウト

| 候補プリセット名 | ワイヤーフレームの考え方 | 向いている内容 | 参考 |
|---|---|---|---|
| `asymmetric-rule-of-thirds` | 画面を3分割し、主役の画像／図を2区画、補助テキストを1区画に置く | 事例紹介、人物紹介、プロダクト紹介 | [Visme: rule of thirds and asymmetric balance](https://visme.co/blog/presentation-layout/) |
| `diagonal-split` | 斜めの境界線で画面を2領域に分け、片側に画像、片側に見出しと要点を置く | ブランド紹介、キャンペーン、ビジュアル重視の説明 | [Visme: diagonal separator layouts](https://visme.co/blog/presentation-layout/) |
| `layered-collage` | 写真・図形・テキストカードを部分的に重ね、奥行きのある主役を作る | クリエイティブ紹介、コンセプト、ケーススタディ | [Visme: overlapping shapes and images](https://visme.co/blog/presentation-layout/) |
| `team-grid-with-caption` | 2×2または3×2の人物グリッドと、横／縦の役割説明領域を組み合わせる | チーム紹介、登壇者、組織紹介 | [Visme: team section with image quadrants](https://visme.co/blog/presentation-layout/) |
| `case-study-proof-card` | 左に顧客／課題、中央に施策、右に成果数値を置き、1枚の証拠カードにまとめる | 導入事例、顧客実績、成果の説明 | [Heydecks: case-study card](https://heydecks.com/blog/slide-design-ideas) |
| `logo-wall-with-caption` | ロゴを均等なグリッドに並べ、下または横に「何を示すロゴか」の短い説明を置く | 顧客実績、パートナー、採用実績 | [Heydecks: logo wall](https://heydecks.com/blog/slide-design-ideas) |
| `magazine-sidebar` | 大見出し＋本文の主領域に、細いサイドバーとして引用・補足・ページ情報を添える | ブランド、記事型ストーリー、読み物 | [Handoff: magazine layouts with CSS Grid](https://handoff.design/css-layouts/magazine-layouts-grid/) |

## 優先候補

最初に実装候補として比較しやすいのは、用途が広く、現在の6種との差が明確な次の10種です。

1. `bento-grid`
2. `kpi-strip`
3. `comparison-matrix`
4. `two-by-two-matrix`
5. `horizontal-milestone-timeline`
6. `vertical-milestone-timeline`
7. `roadmap-lanes`
8. `chevron-process-flow`
9. `hub-and-spoke`
10. `case-study-proof-card`

## 選定時の注意

- `before-after-rows` や `three-pillar-columns` は見た目だけなら2カラム／3カラムに近いが、左右の内容を同じ行で対応付けること、または3要素を等価に扱うことが主目的なので、既存プリセットとは用途が異なる。
- タイムラインは単一の候補にまとめず、横・縦・シェブロン・複数レーンを別プリセットとして扱う価値がある。読み順と情報量が大きく変わるため。
- `radial-facets` と `hub-and-spoke` は似ているが、前者は中心概念から見た均等な観点、後者は独立した周辺カードの集合であり、順序を示すかどうかが違う。
- `chart-with-takeaway` はチャートの種類そのものではなく、「結論見出しを先に置く」データスライドの骨格。棒・折れ線などは将来のデータ表現側で差し替える。
- `full-bleed-visual` の単なる派生にならないよう、画像を背景全面に敷くのではなく、カード、地図、人物グリッド、斜め分割など、情報構造を持つ候補を優先する。

## 研修資料向けの追加候補

研修資料では、授業内の学習活動そのものよりも、「研修の目的を理解する」「業務の全体像をつかむ」「標準手順を再現する」「現場の判断基準を持ち帰る」ことを優先します。そのため、講師の説明用スライド、受講者の配布資料、研修後の実務リファレンスのいずれにも転用しやすい構造へ置き換えました。[Monash University](https://www.monash.edu/learning-teaching/teachhq/Teaching-practices/using-multimedia/how-to/powerpoint-slides)、[McGill University](https://teachingkb.mcgill.ca/tlk/design-slides-to-support-learning)、[MSU Effective PowerPoint](https://omerad.msu.edu/meded/effectiveppt_intro.html)

| 候補プリセット名 | ワイヤーフレームの考え方 | 向いている内容 | 参考 |
|---|---|---|---|
| `training-objectives-agenda` | 研修目的、到達基準、当日の進め方を1枚に整理 | 研修冒頭、オンボーディング、講師用導入 | [Monash University: teaching slides](https://www.monash.edu/learning-teaching/teachhq/Teaching-practices/using-multimedia/how-to/powerpoint-slides) |
| `training-roadmap` | 説明→デモ→演習→確認→現場適用の全体像を示す | 新人研修、資格研修、複数回講座 | [McGill University: slides to support learning](https://teachingkb.mcgill.ca/tlk/design-slides-to-support-learning) |
| `precheck-current-state` | 受講者の現状、困りごと、研修への期待を3列で整理 | 研修開始時のヒアリング、レベル合わせ | [Canva: KWL chart](https://www.canva.com/online-whiteboard/kwl-chart/) |
| `workshop-exercise` | 個人検討→グループ討議→代表共有の進行を示す | 社内ワークショップ、対話型研修、合意形成 | [Monash University: teaching slides](https://www.monash.edu/learning-teaching/teachhq/Teaching-practices/using-multimedia/how-to/powerpoint-slides) |
| `demonstration-walkthrough` | デモ、実施手順、完成イメージを横並び | 業務ツール研修、接客・営業、技能研修 | [MSU: Effective PowerPoint](https://omerad.msu.edu/meded/effectiveppt_intro.html) |
| `facilitator-reveal` | 問い、判断材料、講師解説を段階的に提示 | ケース討議、判断基準、参加型講義 | [MSU: Effective PowerPoint](https://omerad.msu.edu/meded/effectiveppt_intro.html) |
| `operating-model-map` | 担当業務、関係部署、入力・出力、関連ルールを接続 | 業務理解、組織オンボーディング、業務設計 | [University of Florida IFAS: concept maps](https://ask.ifas.ufl.edu/publication/wc071) |
| `root-cause-analysis` | 発生した問題を複数の観点から分解する | 品質改善、安全、問題解決、管理職研修 | [Canva: KWL and graphic organizers](https://www.canva.com/online-whiteboard/kwl-chart/) |
| `glossary-callout` | 専門用語の定義、現場例、注意点を一枚に集約 | コンプライアンス、IT、医療、業界用語 | [McGill University: slides to support learning](https://teachingkb.mcgill.ca/tlk/design-slides-to-support-learning) |
| `myth-fact` | 現場で起きやすい誤った判断と正しい基準を対比 | 安全、コンプライアンス、接客、管理職研修 | [University of Delaware: KWL](https://www1.udel.edu/dssep/teaching_strategies/kwl.htm) |
| `knowledge-check` | 判断問題、選択肢、正解理由、注意点を配置 | 研修中の確認、eラーニング、修了テスト | [McGill University: slides to support learning](https://teachingkb.mcgill.ca/tlk/design-slides-to-support-learning) |
| `action-plan` | 学んだこと、現場で変えること、実行期限を記入 | 研修の締め、受講後課題、上司とのフォローアップ | [University of Delaware: KWL](https://www1.udel.edu/dssep/teaching_strategies/kwl.htm) |
| `breakout-exercise` | チームごとの検討領域と、最後の統合欄を配置 | 集合研修、部門横断ワークショップ、企画研修 | [Monash University: teaching slides](https://www.monash.edu/learning-teaching/teachhq/Teaching-practices/using-multimedia/how-to/powerpoint-slides) |
| `case-study-scenario` | 人物、背景、問題、取るべき対応を順に追う | 営業、接客、管理職、医療・福祉のケース研修 | [University of Florida IFAS: concept maps](https://ask.ifas.ufl.edu/publication/wc071) |
| `procedure-checklist` | 準備、手順、完了条件・記録を3列で整理 | 作業手順、安全確認、店舗運営、技能訓練 | [EdrawMax: education infographics](https://edrawmax.wondershare.com/examples/education-infographic-examples.html) |
| `role-play-scenario` | 現場の状況、手がかり、取るべき行動を分けて提示 | 営業、接客、面接、クレーム対応研修 | [University of Florida IFAS: concept maps](https://ask.ifas.ufl.edu/publication/wc071) |

## 参照したサイト

- [Heydecks — Slide design ideas: 25 layouts, and when to use each](https://heydecks.com/blog/slide-design-ideas)
- [Visme — Presentation Layout: How to Create a Stunning Deck + Examples](https://visme.co/blog/presentation-layout/)
- [Visme — How to Create an Infographic Layout That’s Easy to Follow](https://visme.co/blog/infographic-layout/)
- [Gixo / Prism — Infographic Layout Ideas: Six Structures](https://gixo.ai/infographic-layout)
- [Slide-deck.io — How to Design a Timeline Slide](https://slide-deck.io/blog/how-to-design-a-timeline-slide)
- [Microsoft PowerPoint — PowerPoint design ideas and tips for 2026](https://powerpoint.cloud.microsoft/create/en/blog/powerpoint-design-ideas/)
- [Visme — The Different Types of Diagrams (PDF)](https://visme.co/courses/wp-content/uploads/2020/08/The-Different-Types-of-Diagrams.pdf)
- [Handoff — Building Magazine-Style Editorial Layouts with CSS Grid](https://handoff.design/css-layouts/magazine-layouts-grid/)
