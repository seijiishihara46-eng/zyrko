# ZYRO Visual Canon Control

Status: MVP active
Created: 2026-07-09
Scope: Zyro image generation, prompt control, visual QA, reference accumulation

## Purpose

This directory is the operational layer for turning AI-generated "Zyro-like" images into controlled Zyro visual canon.

The goal is not to let image generation define Zyro. The goal is to use image generation as an observation device, then let human judgement and canon rules decide what becomes part of the IP.

## Core Loop

```text
Canonical SVG
  -> prompt
  -> image generation
  -> visual drift appears
  -> user judges OK / NG / HOLD
  -> reason is recorded
  -> good / bad reference is saved
  -> canon rule or prompt is updated
  -> next generation becomes more constrained
```

## Source Of Truth

Canonical shape:

- `CANON/SYMBOLS/zyro-glyph-canonical.svg`

Generation rule:

- `CANON/TEXT/zyro-image-generation-canon.md`

Derivatives rule:

- `CANON/TEXT/zyro-derivatives-handoff.md`

## Folder Responsibilities

```text
CANON/VISUAL/ZYRO/
  README.md                         # this overview
  workflow.md                       # generation/review/save loop
  drive_manifest.md                 # Google Drive storage map
  prompts/                          # reusable prompt templates
  qa/                               # review schema and review log template
  reference_good/                   # text index for approved references
  reference_bad/                    # text index for rejected references
```

Image binaries are stored in Google Drive, not Git, unless they are small official canonical exports.

## Current Accepted Direction

Accepted scene type:

- `sci_fi_wall`: massive dark sci-fi stone/metal wall with Zyro embedded as relief.

Accepted behavior:

- wall may be detailed, cinematic, industrial, ancient-future, wet, cracked, reflective;
- Zyro may be carved/inset/relief;
- white Orbit may glow as one continuous channel;
- right Void chamber must stay a plain dark field;
- no circular recess, lens, eye, crescent, extra inner line, or oval pit inside the right chamber.

## Minimum Review Rule

Every generated image must be classified as one of:

- `good` — can be used as reference;
- `bad` — useful as a failure case;
- `hold` — visually interesting but not canon-safe yet.

A judgement without a reason is not a canon contribution.
