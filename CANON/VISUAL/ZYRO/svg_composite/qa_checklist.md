# Zyro SVG Composite QA Checklist

Status: active
Created: 2026-07-09

## Purpose

Use this checklist after placing canonical Zyro SVG assets onto a generated image.

## General Checks

- [ ] The Zyro mark comes from a listed SVG source, not image-generation redraw.
- [ ] The left spiral remains intact and continuous.
- [ ] The right droplet / Void side does not become an eye, lens, circular recess, or generic oval.
- [ ] The central convergence remains readable.
- [ ] The mark still reads as Zyro after perspective and blending.
- [ ] No extra line, crescent, symbol, or decoration was added inside the mark.

## Wall Checks

- [ ] Wall Zyro uses `wall_carve` or similar material treatment.
- [ ] Shape is still close to the source SVG.
- [ ] Glow/shadow/bevel does not alter topology.
- [ ] Stone cracks or wall texture do not cut the left spiral.
- [ ] The right side is not filled with an invented circular object.

## Clothing Checks

- [ ] Hoodie/shirt logo uses `logo_print` treatment, not wall glow.
- [ ] It follows body perspective enough to feel printed on fabric.
- [ ] It remains readable at final image size.
- [ ] Fabric wrinkles do not destroy the symbol.
- [ ] If using `zyro-print-master.svg`, the filled/counter look is preserved.

## Paper / Sketch Checks

- [ ] Paper version uses `centerline` or ink-like treatment.
- [ ] The line remains continuous.
- [ ] It does not become random decorative handwriting.

## Failure Tags

Use these tags in QA logs:

```text
svg_asset_redrawn_by_ai
print_master_shape_drift
left_spiral_broken_line
right_droplet_lost
right_circular_recess
right_eye_lens
right_extra_inner_mark
generic_infinity_logo
bad_perspective_fit
bad_fabric_fit
bad_wall_material_fit
low_legibility
```

## Pass Criteria

A composite pass is acceptable when:

```text
Zyro is exact enough to preserve Canon
and
surface integration is good enough for the intended use.
```

If there is a conflict, preserve Canon first and improve blending second.
