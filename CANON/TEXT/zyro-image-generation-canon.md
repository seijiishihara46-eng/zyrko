# Zyro Image Generation Canon

Status: canonical generation rule
Created: 2026-07-09
Scope: ChatGPT / image generation / prompt drafting / visual QA

## Purpose

When generating, prompting, compositing, or evaluating any image that uses the word **Zyro**, the canonical Zyro SVG must be treated as the primary visual source.

This file exists because Zyro is not common public knowledge and should not be inferred from general model training. It must be resolved from the repository canon.

## Canonical Parent

Primary parent:

- `CANON/SYMBOLS/zyro-glyph-canonical.svg`

Mirror / working parent:

- `ZYRO/GLYPH/zyro-glyph-canonical.svg`

Supporting rules:

- `ZYRO/GLYPH/README.md`
- `ZYRO/GLYPH/roadmap.md`
- `CANON/TEXT/zyro-derivatives-handoff.md`

## Non-negotiable Visual Rules

Zyro must not be redesigned.

The canonical glyph is:

- black infinity-shaped field
- one continuous white Orbit
- restrained left spiral
- single convergence crossing
- right Void chamber
- horizontal 2:1 composition
- binary black / white only
- no gray, gradient, glow, shadow, texture, extra symbol, or decorative reinterpretation

## Right Void Chamber Rule

The right Void chamber must remain a quiet, empty black chamber inside the right lobe.

Do not add:

- crescent marks
- partial inner strokes
- leftover arc fragments
- extra white curves
- eye-like highlights
- secondary chamber outlines
- decorative cracks or symbols inside the chamber

The only white element on the right side is the canonical Orbit stroke that forms the continuous figure-eight trajectory. The inside of the right chamber should read as unbroken black negative space.

## Correct Generation Architecture

For accurate outputs:

1. Render or composite the canonical SVG directly.
2. Let image generation create only the atmosphere, background, material context, or scene.
3. Place the canonical Zyro SVG above or inside that generated scene afterward.
4. Validate the result against the canonical rules.

Recommended structure:

```text
Atmosphere / background / scene = image generation
Zyro glyph body = canonical SVG render or vector composite
Final check = compare against canon rules
```

## Prompt Guardrail

Use this instruction whenever Zyro appears in an image generation request:

```text
Zyro is not a newly designed logo. Use the canonical Zyro glyph as the visual source. Do not redesign the silhouette. Preserve the black infinity-shaped field, one continuous white Orbit, restrained left spiral, single convergence crossing, empty right Void chamber, 2:1 ratio, and binary black/white logic. The right Void chamber must stay empty black negative space: no crescent, no partial inner line, no extra arc, no eye highlight, no decorative stroke. If exact shape fidelity matters, generate only the surrounding scene and composite the canonical SVG afterward.
```

## When Direct Image Generation Is Allowed

Direct image generation may be used for:

- background
- atmosphere
- material context
- product mockup
- lighting study
- scene concept
- poster rough
- Hush / Zyrko surrounding visual

Direct image generation should not be used as the only source for:

- canonical Zyro logo
- font glyph
- official icon
- print master
- final Hush face mark
- production asset requiring exact silhouette

## Failure Patterns To Check

Reject or revise results when:

- Orbit becomes multiple lines
- left spiral becomes decorative or too complex
- right Void chamber becomes a generic oval
- right Void chamber contains a crescent, partial white line, arc fragment, eye highlight, or decorative inner stroke
- center crossing moves away from convergence
- 2:1 proportion collapses
- gray, glow, texture, gradients, or extra marks appear
- the black field is replaced by an outline-only logo
- the glyph is generated from memory instead of rendered from SVG

## Operational Rule For ChatGPT

When the user asks to generate or describe **Zyro**, first treat this repository canon as the reference layer. Prefer retrieval of the canonical SVG and supporting rule files before constructing the prompt or evaluating the output.

If a tool cannot directly provide the SVG to the image generator, explain the limitation and use the safest fallback:

1. render/composite the canonical SVG when possible;
2. otherwise write a strict prompt based on the canon;
3. after generation, visually check and request correction if the canon is violated.
