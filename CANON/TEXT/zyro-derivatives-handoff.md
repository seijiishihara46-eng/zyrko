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

## Metal / 3D (Blender stage — external tool)

Source: `SYMBOLS/zyro-glyph-font-ready.svg` (centerline + field).

1. Import SVG as curve.
2. Use the black field as the body; the Orbit centerline as the inset channel.
3. Extrude / bevel for depth. Keep edges clean (Void = perfect black, no glow).
4. Metal: dark chrome / black metal. The Orbit reads as the bright inset (the silver face).
5. No texture noise, no emissive glow. Preserve quiet / minimal.

## Hush face

- Placement: markWidth `0.84 × headW`, vertical center `0.42 × headH` from top, centered.
- On the dark head the black field merges; only the Orbit shows.
