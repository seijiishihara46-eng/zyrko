# Zyro SVG Transition Log — 2026-07-09

Status: saved transition record
Date: 2026-07-09
Scope: Zyro SVG interpretation, Essence/Glyph/Outline distinction, image-generation canon loop

## Purpose

This note preserves the transition of understanding that happened while reviewing Zyro SVGs and image-generation outputs.

The key realization: Zyro is not only one SVG file. It has layered representations.

```text
Essence Canon  ->  Glyph Canon  ->  Centerline / Wide Stroke / Outline-Counter expressions  ->  Image-generation visual canon
```

## Starting Confusion

During image generation, Zyro started to look too much like a clean infinity symbol.

The user felt that the remembered Zyro SVG was different from the current `zyro-glyph-canonical.svg`.

This was a correct signal. The current canonical glyph is valid, but it is a reduced typographic form, not the whole visual identity.

## Recovered Core Memory

The user recovered the remembered Zyro Essence:

```text
left spiral + right droplet + one-stroke trajectory
```

Japanese shorthand:

```text
左渦・右雫・一筆書き
```

This was identified as the **Zyro Essence Canon**.

## Layer Separation

### 1. Essence Canon

The identity-level Zyro.

Required structure:

- left spiral;
- right droplet;
- one-stroke trajectory;
- convergence;
- Void weight;
- asymmetry;
- not a generic mathematical infinity sign.

This layer controls image generation, wall reliefs, relics, Hush face expression, posters, and worldbuilding visuals.

### 2. Glyph / Font Canon

The typeable Zyro.

Purpose:

- U+E000 font glyph;
- icon/UI/small-size mark;
- stable SVG and font production;
- minimal reproducible form.

Current canonical implementation:

- `CANON/SYMBOLS/zyro-glyph-canonical.svg`
- black infinity-shaped field;
- one continuous white Orbit;
- restrained left spiral;
- right Void chamber;
- 2:1 horizontal glyph structure.

This is valid, but it is a compressed typographic form.

### 3. Centerline Expression

Closest to the remembered one-stroke structure.

Representative file:

```text
ZYRO/GLYPH/zyro-centerline-master.svg
```

Meaning:

- the trajectory itself is visible;
- one-stroke logic is preserved directly;
- useful for understanding the movement from left spiral through convergence to the right side.

### 4. Outline / Counter Expression

Production-oriented conversion.

Representative file:

```text
ZYRO/GLYPH/dist/zyro-glyph-outline.svg
CANON/SYMBOLS/zyro-glyph-font-ready.svg
CANON/SYMBOLS/zyro-print-master.svg
```

Meaning:

- the stroke gains material width;
- the stroke may be expanded into outlines;
- Orbit may become a counter/hole;
- this is valid for font, print, manufacturing, and pipeline outputs.

## Key Resolution: Width Does Not Decide Correctness

A major clarification:

```text
centerline / one-stroke expression = trajectory shown directly
wide-stroke expression = trajectory has visible material width
outline / counter expression = stroke expanded, subtracted, or converted into shape
```

All can be correct.

Line width is not the core issue.

Correctness depends on whether the Essence Canon survives:

```text
left spiral
right droplet
one-stroke movement
convergence
Void weight
```

## Boundary Between SVG 3 and SVG 4

The user identified a meaningful boundary between the trusted SVG list items 3 and 4:

```text
3. zyro-centerline-master.svg
4. zyro-glyph-outline.svg
```

Interpretation:

- 3 is closer to Essence / drawing logic;
- 4 is closer to production / font / print logic;
- both are valid Zyro;
- they are not contradictory;
- they represent different stages of the same trajectory.

## Image-Generation Lessons

### Accepted

- Zyro embedded in a dark sci-fi wall;
- a desk/paper in front of the wall showing a drawn Zyro;
- ancient-future / research-room / relic-study atmosphere;
- wall relief, glow, carving, ink, or sketch expression;
- thin centerline, wide luminous line, carved channel, or outline/counter expression.

### Rejected / Failure Tags

- `right_crescent_line`
- `right_circular_recess`
- `right_eye_lens`
- `right_extra_inner_mark`
- `generic_infinity_logo`
- `left_spiral_broken_line`

Important: the left spiral must remain continuous. It may be drawn, carved, worn, or glowing, but it must not visibly break or detach from the one-stroke movement.

## Current Working Rule For Image Generation

Use this rule when generating illustrative Zyro images:

```text
Preserve the Zyro Essence: left spiral, right droplet, one-stroke trajectory, convergence, asymmetry, and Void weight.
The exact stroke width may vary. It may appear as a thin centerline, wide luminous stroke, carved wall channel, ink line, or outline/counter form.
The left spiral line must remain continuous and connected.
The right side should feel like a droplet/Void side, not a perfect oval, eye, lens, mechanical disk, or generic infinity loop.
Do not collapse Zyro into a clean generic infinity symbol.
```

## Trusted SVG Set At This Stage

High-confidence files:

```text
CANON/SYMBOLS/zyro-glyph-canonical.svg
CANON/SYMBOLS/zyro-glyph-font-ready.svg
ZYRO/GLYPH/zyro-centerline-master.svg
ZYRO/GLYPH/dist/zyro-glyph-outline.svg
CANON/SYMBOLS/zyro-print-master.svg
CANON/SYMBOLS/zyro-hush-face.svg
CANON/SYMBOLS/zyro-hush-icon.svg
ZYRO/GLYPH/icons/zyro-hush-icon.svg
```

## Final Understanding

The correct conclusion from this session:

```text
Zyro is fundamentally left spiral + right droplet + one-stroke trajectory.
The SVG differences are representation modes, not separate identities.
Centerline, wide stroke, and outline/counter can all be correct.
The Essence Canon decides whether a variation is still Zyro.
```

Short version:

```text
3 is Essence-close.
4 is production-close.
Both are correct.
The boundary is representation mode, not canon validity.
```
