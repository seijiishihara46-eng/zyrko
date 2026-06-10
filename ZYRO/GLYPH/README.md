# GLYPH

The Zyro glyph. Identity mark as a typographic character.

Frozen: 2026-06-10. Adopted from candidate v2.5.

---

## What this holds

- `zyro-glyph-canonical.svg` — the frozen mother shape (single parent).
- `zyro-glyph-font-ready.svg` — fill-only conversion source (Orbit as counters).
- `zyro-centerline-master.svg` — centerline master (Guides / Centerline / Outline).
- `icons/` — released raster marks (light + dark tile).
- `roadmap.md` — phase log.
- `pipeline/` — reproducible build scripts.

The published font lives in `CANON/SYMBOLS/` (Zyrko.ttf / Zyrko.woff2).

---

## Model

- Black infinity field + one continuous white Orbit (stroke width 9).
- White sits directly on black. No inner border.
- On a dark field the black field merges; only the Orbit shows.
- Binary black/white. No gray, gradient, shadow, texture.
- Character slot `U+E000` (PUA). Family `Zyrko`. UPM 1000.

## Rules

- The canonical SVG is the single parent.
- Derivatives (Icon, Print, Font, Metal, 3D) descend from it.
- Do not parent on raster images. Do not redesign the silhouette.

---

## Rebuild

```
cd pipeline
python zyro_outline.py     # -> dist/zyro-glyph-outline.svg
python zyro_font.py        # -> dist/Zyrko.ttf, .woff2 (glyf) and .otf (CFF)
```

Requires `shapely`, `fonttools`, `brotli` (`pip install shapely fonttools brotli`).
`dist/` is a build artifact (regenerable); the canonical copy is committed in CANON.
