# zyro-glyph-canonical

Stabilized definition of the Zyro glyph as a typographic character.

Frozen: 2026-06-10.

## Model

- One black infinity field.
- One continuous white Orbit, restrained left spiral, single self-crossing.
- White Orbit sits directly on the black field. No inner border.
- Binary black/white. No gray, gradient, shadow, texture.
- On a dark field the black field merges; only the Orbit remains.

## Canvas

- viewBox `0 0 200 100`.
- Aspect `2:1`.
- White-channel width `9`.
- Convergence at `(100, 50)`.

## Character

- Slot `U+E000` (Private Use Area).
- Family `Zyrko`. UPM `1000`. Advance `1000`.
- Glyph = black compound path; Orbit as counters.

## Hush face placement

- markWidth = `0.84 × headWidth`.
- vertical center = `0.42 × headHeight` from head top.
- horizontally centered.

## Assets

- `SYMBOLS/zyro-glyph-canonical.svg` — display source.
- `SYMBOLS/zyro-glyph-font-ready.svg` — fill-only conversion source.
- `SYMBOLS/zyro-hush-face.svg` — face placement.
- `SYMBOLS/Zyrko.woff2`, `SYMBOLS/Zyrko.ttf` — font.

## Parent rule

- This glyph is the single parent.
- Derivatives (Metal, Print, Icon, Font, 3D) descend from it.
- Do not parent on raster images.
- Do not redesign the silhouette.

## Provenance

- Adopted from candidate `v2.5`.
- Alternatives `v2.6`, `v2.7` rejected.
- Pipeline: `zyro_outline.py` (shapely) → `zyro_font.py` (fontTools). Reproducible.
