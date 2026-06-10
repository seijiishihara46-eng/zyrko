# Zyro Glyph → Font ロードマップ

最終目標: Zyro を画像素材ではなく **専用フォントの1グリフ（U+E000, 私用領域）** として固定し、
Web / PC / 資料 / Hush 顔面パーツ / Zyrko 専用フォント で同一の形が使える状態にする。

現在地: **Phase 6 ほぼ完了**。配布・CANON登録・Icon/Print派生 まで完了。
残るは Metal/3D（Blender 導入時）のみ。`Zyrko.ttf` / `Zyrko.woff2`（U+E000）実機確認済み。
2026-06-10、**v2.5 を母型として採用・凍結**。canonical = `zyro_glyph_canonical.svg`。
中心線マスター = `zyro_centerline_master.svg`（200×100, 3層）。
（v2.6 一筆書き / v2.7 数式対称 は試作したが不採用。v2.5 のシルエットを正とする。）
これ以降は「絵を直す」ではなく「文字として確定して鋳造する」作業に切り替える。

重要: canonical v2.5 は「黒フィールド＋白Orbit 1本(stroke 9)」モデル。
旧 `zyro_master.svg` の 10:25:10 リボン系（v3）は **v2.5 に不適用→ superseded**（保存のみ）。

---

## フェーズ全体図

```
Phase 0  Design Freeze        ← v2.5 を母型として確定（凍結ゲート）
Phase 1  Centerline Master    ← 1本の中心線を正とする（zyro_master.svg と統合）
Phase 2  Outline Conversion   ← stroke→path、Voidを counter 化、単一 compound path
Phase 3  Glyph Validation     ← 輪郭方向・重なり・ノード・24px 検証
Phase 4  FontForge Build      ← U+E000 に配置、UPM/スケール/サイドベアリング
Phase 5  Export & Test        ← OTF / WOFF2 出力、各サイズ・各環境で実描画確認
Phase 6  Deploy & Canonize    ← Web/PC/資料/Hush へ展開、canonical 登録
```

各 Phase はゲート（合格条件）を満たすまで次へ進まない。

---

## Phase 0 — Design Freeze（デザイン凍結）

**目的:** これ以上シルエットをいじらない、という1点を確定する。
フォント化は「形が動かない」前提で初めて意味を持つ。

**判断（2026-06-10）:** v2.5 を採用・凍結。代替案（v2.6/v2.7）は不採用。
→ `zyro_glyph_canonical.svg` を確定（唯一の母型）。`zyro_glyph_canonical_font_ready.svg` も併設。

**ゲート（達成済み）:** 24 / 40 / 80 / 160px で渦・交差・右Void が成立。

凍結後に Phase 1〜3 で扱う残課題（形は変えず、フォント化時の調整事項として持ち越し）:

- 左下 Orbit 終端を「開いたまま」か「黒地に吸収」か（最終 canonical outline で決定）
- 24px でヒンティング後に渦が閉じる場合は最内開口のみ拡大
- 交差が明るすぎる場合は展開後に局所的に細める

---

## Phase 1 — Centerline Master（中心線マスター）✅ 完了 2026-06-10

**目的:** 「外形」ではなく「中心線」を設計の正にする。
線幅・拡大縮小・太さ変更で形が崩れない土台を作る（フォントと同じ思想）。

**成果物:** `zyro_centerline_master.svg`（viewBox 0 0 200 100, canonical v2.5 準拠）
- 03 Construction Guides: 交差点(100,50) / 水平軸 / 収束軸 / Orbit包絡 / Void包絡 / 端点
- 02 Centerline: Orbit 単一軌道スパイン（`zyro-orbit-centerline`, 細線）
- 01 Outline: 黒フィールド fill ＋ Orbit を stroke 9（＝白チャンネル）= canonical の見た目
- metadata に channelSystem / convergence / void / scaling(×5) / manufacturingStep を記載

**設計判断:** v2.5 は「白チャンネル1本」モデルなので 10:25:10 リボン系は採用せず。
白チャンネル幅 = 9。黒内縁ボーダー無し（白Orbitは黒地に直接）。

**ゲート（達成）:** 中心線が1本の連続トラジェクトリ、自己交差1（収束点のみ）。
Outline 層は canonical とパス文字列が同一＝見た目一致。

---

## Phase 2 — Outline Conversion（アウトライン化 / fill-only 化）✅ 完了 2026-06-10

**目的:** stroke ベースをやめ、塗り（fill）だけにする。
白 Orbit は「黒地に空いた counter（穴）」として表現する。

**実装:** `zyro_outline.py`（pure-Python / shapely）
- canonical のベジェを48分割でフラット化 → 黒フィールド polygon / Orbit linestring
- Orbit を幅9・round cap でバッファ → 白チャンネル polygon
- `field.difference(channel)` → 黒の compound polygon（Orbit は counter）
- 出力: `zyro_glyph_outline.svg`（fill-only, evenodd, 白パス0個）

**結果:** MultiPolygon 3パーツ（外周リム＋右Void chamber＋左渦内の黒）+ counter1, valid。
**ゲート（達成）:** canonical との **ピクセル差 0.40%（縁のAAのみ）** で形状一致を確認。

---

## Phase 3 — Glyph Validation（グリフ検証）✅ 完了 2026-06-10

- 輪郭方向: 外周 CW / counter CCW（nonzero）で emit、レンダリングで穴が正しく抜けることを確認
- 重なり: shapely difference + buffer(0) で解消済み
- ノード削減: `simplify(0.25)` 適用
- self-intersection: shapely valid=True
- 24px で渦中心・交差・右Void を確認（font_test.html）

**ゲート（達成）:** 4 contours, valid, 全サイズ視認 OK。

---

## Phase 4 — Font Build（フォント組み込み）✅ 完了 2026-06-10

**実装:** `zyro_font.py`（fontTools FontBuilder, TTF）
- U+E000 → `zyro` グリフ、UPM 1000、5x スケール
- bbox (25,35)–(975,465)、advance 1000、ascent 800 / descent -200
- グリフ順: .notdef / space / zyro。name/OS2/post 設定済み

**ゲート（達成）:** U+E000 に1グリフ、メトリクス健全。
**残:** 縦位置の最終確定は Hush 顔面パーツと並べて調整（Phase 6 で実施）。

---

## Phase 5 — Export & Test（書き出しと実機検証）✅ 完了 2026-06-10

- 出力: `Zyrko.ttf`（1.6KB）/ `Zyrko.woff2`（0.96KB）
- テスト: ブラウザ @font-face で U+E000 を 200/96/48/24/16px・白地黒地・インラインで描画確認（`zyro_font_test.html`）
- canonical との形状一致は Phase 2 で 0.40% 差を確認済み

**ゲート（達成）:** 全サイズで Zyro と判別でき、インライン文字として成立。
**残（必要時）:** PC へのインストール実機テスト / OTF(CFF) 版が必要なら別途生成。

---

## Phase 6 — Deploy & Canonize（展開と正典化）🔶 進行中

**目的:** 公式アセットとして固定し、派生の親にする。

- `zyro_glyph_canonical.svg`（Phase 0 凍結形）= 唯一の親
- 派生はすべてここから: `Zyro Metal` / `Zyro Print` / `Zyro Icon` / `Zyro Font` / `Zyro 3D`
- フォントを Web / PC / 資料 / Hush 顔面に組み込み
- Zyrko CANON に登録（公式アイコン Logo/Zyro logo.png 系列と整合）

**✅ Hush 顔面 配置仕様 確定（2026-06-10, `zyro_hush_face.svg`）:**
- 黒頭の上で黒fieldは同化し白Orbitのみ可視（＝3Dのシルバー顔面と一致）
- **markWidth = 0.84 × headW**
- **vertical center = 0.42 × headH（頭頂から／アイレベル）**
- **horizontally centered**
- 実測検証: 幅0.843 / 縦0.415 / 中央ずれ-0.5px → 参照3Dと一致

**✅ Item 1 配布完了:** `zyro-font.css`（@font-face）/ `zyro-font-usage.html`（使い方・PC設置）。
ブラウザ実機で読込・描画確認済み（エンティティ法 / CSS ::before 法）。

**✅ Item 2 CANON 登録完了:**
- `Zyrko/CANON/SYMBOLS/` に zyro-glyph-canonical.svg / zyro-glyph-font-ready.svg / zyro-hush-face.svg / Zyrko.woff2 / Zyrko.ttf
- `Zyrko/CANON/TEXT/zyro-glyph-canonical.md`（安定化仕様）

**🔶 Item 3 派生展開:**
- ✅ Icon: light 6サイズ `zyro-icons/zyro-icon-{16..512}.png` ＋ dark 3サイズ `zyro-icon-dark-{128,256,512}.png`（canonical からcanvas書き出し）
- ✅ Print: `zyro-print-master.svg`（単色K100, Orbit=counter, 60×30mm ベクタ）
- ✅ 派生ルール文書: `Zyrko/CANON/TEXT/zyro-derivatives-handoff.md`
- ⏳ Metal / 3D: Blender 段（外部ツール）。font-ready SVG ＋ 手順を handoff 済み。

**ゲート（達成）:** 「canonical SVG → Icon/Print/Font」一方向フロー確立。画像を親にしない。
Metal/3D は Blender 導入時に handoff 手順で実行。

---

## 次セッション計画（おすすめ順・2026-06-10 確定）

- **A. リポジトリ整備（軽い／冒頭で片付け）**
  - `zyro-glyph-canon` ブランチ（commit 7258e1f）を master へマージ／push
  - ビルド素材（`zyro_outline.py` / `zyro_font.py` / `zyro_font_roadmap.md` / `zyro-icons/`）を `Zyrko/ZYRO/` へ移して git 追跡化
- **D/E. 可視成果**
  - D: `zyro-font.css` を WEBSITE（リポジトリルート）へ組込
  - E: Hush 顔面アイコン完成（頭＋帽子シルエット込み1枚 SVG、配置 0.84/0.42 適用）
- **B. 本命 Metal/3D（Blender 段）**
  - `zyro-glyph-font-ready.svg` → カーブ取込 → 押し出し → ダークメタル（handoff 手順どおり）
- **C. 任意**: 顔面用 em 中央寄せ字形バリアント／OTF(CFF) 版／favicon.ico

## 解決済みの判断（記録）

1. 凍結対象 → **v2.5**（v2.6/v2.7 不採用）
2. 設計モデル → 黒フィールド＋白Orbit1本（10:25:10 リボンは不採用）
3. フォント形式 → `Zyrko` 単独フォント、U+E000、TTF/WOFF2
4. ツール経路 → **pure-Python 再現パイプライン**（shapely + fontTools）
5. 左下 Orbit 終端 → 現状（開いたまま）で凍結。最終調整は Metal/3D 段で再検討可

---

## ツール現状メモ

- ローカル ffmpeg は SVG デコーダ無し → PNG プレビューはブラウザ / Inkscape / rsvg 系が必要
- FontForge は Python スクリプトでバッチ化可能（再現性のため推奨）
```

```
更新ルール: 各 Phase 完了時に該当ゲートのチェックを埋め、現在地を1行更新する。
```
