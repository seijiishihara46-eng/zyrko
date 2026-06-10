# zyro-derivatives-handoff

Derivation rules for Zyro outputs. Parent = `zyro-glyph-canonical`.

## Principle

- One parent: `SYMBOLS/zyro-glyph-canonical.svg`.
- Direction: SVG → raster / print / 3D / metal.
- Never parent on a raster image.
- Never redesign the silhouette.

## Icon (done)

- Light set: black mark on transparent. `zyro-icon-{16..512}.png`.
- Dark set: white Orbit on black rounded tile (Hush-face look). `zyro-icon-dark-{128,256,512}.png`.

## Print (done)

- `zyro-print-master.svg` — single-color, Orbit as counters, 60 × 30 mm, vector.
- Press: K100 (optional rich black C40 K100). No tints, gradients, shadows.

## Metal / 3D (done — Blender headless)

Reproducible: `ZYRO/GLYPH/pipeline/zyro_blender.py` (Blender 4.4).
Source: `ZYRO/GLYPH/dist/zyro-glyph-outline.svg` (fill-only, Orbit as counters).

Pipeline: import SVG curve -> fill -> mesh -> solidify + bevel -> polished
silver chrome (Metallic 1.0, Roughness 0.30) -> front softbox + key/rim/top ->
3/4 camera -> Cycles render on near-black world.

Output: `ZYRO/GLYPH/3d/zyro-metal.png` (also `CANON/VISUAL/zyro-metal.png`).
The `.blend` is regenerable (gitignored). Silver reads as the figure's face;
background stays near-black (quiet / minimal). No texture noise, no glow.

Run:
`"…\Blender 4.4\blender.exe" --background --python zyro_blender.py`

## Hush face

- Placement: markWidth `0.84 × headW`, vertical center `0.42 × headH` from top, centered.
- On the dark head the black field merges; only the Orbit shows.
