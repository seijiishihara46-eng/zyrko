# Zyro SVG Composite Line

Status: MVP design active
Created: 2026-07-09
Scope: compositing canonical Zyro SVG assets onto generated images

## Purpose

This line exists because image generation can create excellent atmosphere, but it cannot reliably preserve Zyro as an exact IP asset.

The correct split is:

```text
Image generation = scene, character, wall, light, atmosphere
SVG composite    = exact Zyro glyph/logo/print mark placement
```

Use this line whenever Zyro must function as:

- official logo;
- clothing brand mark;
- wall glyph with exact canon shape;
- printed mark;
- UI icon;
- Hush face mark;
- production asset.

## Core Principle

Do not ask image generation to redraw official Zyro assets.

Instead:

```text
1. Generate or select the background image.
2. Choose the correct Zyro SVG asset.
3. Place the SVG onto target surfaces.
4. Apply perspective, opacity, lighting, shadow, and material blend.
5. Save output and QA report.
```

## Source SVG Assets

Recommended source map:

| Use case | SVG source |
|---|---|
| wall official glyph | `CANON/SYMBOLS/zyro-glyph-canonical.svg` |
| clothing brand logo | `CANON/SYMBOLS/zyro-print-master.svg` |
| paper / sketch / guide line | `ZYRO/GLYPH/zyro-centerline-master.svg` |
| print / sticker / stamp | `CANON/SYMBOLS/zyro-print-master.svg` |
| Hush face | `CANON/SYMBOLS/zyro-hush-face.svg` |
| Hush icon | `CANON/SYMBOLS/zyro-hush-icon.svg` |

## Pipeline

```text
input image
  -> target definition JSON
  -> SVG render to transparent PNG
  -> scale / rotate / perspective warp
  -> blend onto image
  -> optional material treatment
  -> output image
  -> QA record
```

## Composite Modes

### logo_print

For clothing, sticker, and flat printed marks.

- mostly flat;
- follows surface perspective;
- uses white / grey / black mark color;
- should remain legible.

### wall_carve

For stone or metal walls.

- uses canonical SVG shape;
- may add glow, shadow, bevel, and inner light;
- shape must remain exact enough to read as the selected SVG.

### paper_ink

For documents and sketches.

- uses centerline or canonical thin rendering;
- can be dark ink;
- can be slightly worn;
- line must remain continuous.

### hologram

For AR/UI/projection.

- uses canonical line or centerline;
- can glow;
- must not add extra inner marks.

## Target Definition

A target is a placement instruction for one SVG.

Minimum fields:

```json
{
  "id": "seiji_hoodie_logo",
  "source_svg": "CANON/SYMBOLS/zyro-print-master.svg",
  "mode": "logo_print",
  "quad": [[930, 820], [1170, 870], [1160, 1010], [910, 960]],
  "opacity": 0.92,
  "blend": "screen",
  "tint": "#d8d8d8",
  "notes": "Zyro print master on hoodie back"
}
```

`quad` is the destination quadrilateral in image pixel coordinates:

```text
[top_left, top_right, bottom_right, bottom_left]
```

## QA Rules

Reject when:

- the SVG was redrawn by AI instead of composited;
- the mark loses the left spiral;
- the right droplet / Void side becomes a random circle, lens, or eye;
- line continuity breaks;
- clothing logo becomes unreadable;
- wall mark no longer matches the chosen SVG source;
- too much texture destroys Zyro's identity.

## MVP Output

Minimum output set per composite run:

```text
outputs/<run_id>/composited.png
outputs/<run_id>/targets.used.json
outputs/<run_id>/qa.md
```

For Drive storage, upload:

- final image to `ZYRKO_IP_CANON/ZYRO/exports`;
- QA report to `ZYRKO_IP_CANON/ZYRO/qa_reports`;
- source prompt/run notes to `ZYRKO_IP_CANON/ZYRO/prompt_logs`.

## Current Recommendation

For the current chamber image:

- wall top: use `zyro-glyph-canonical.svg` or `zyro-centerline-master.svg` depending on desired wall expression;
- Seiji hoodie: use `zyro-print-master.svg` as a brand logo;
- paper or drawing: use `zyro-centerline-master.svg`.

When exactness matters, do not use image generation for the Zyro mark itself.
