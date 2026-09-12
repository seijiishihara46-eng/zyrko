# Zyro Visual Canon Workflow

Status: MVP active
Created: 2026-07-09

## Goal

Build a repeatable loop that turns AI image generation variance into Zyro visual canon.

## Roles

### GitHub

Stores the stable structure:

- canonical rules
- prompt templates
- QA schemas
- generation review logs
- indexes for good / bad references

GitHub is the reproducible text layer.

### Google Drive

Stores heavier visual material:

- generated PNG/WebP/JPEG images
- contact sheets
- prompt screenshots
- QA report exports
- temporary comparison images

Drive is the visual evidence layer.

### ChatGPT

Acts as the operator:

- reads the canon files
- drafts prompts
- evaluates generated images against QA rules
- writes review summaries
- updates GitHub rules when a new drift pattern is discovered

### User

Acts as canon authority:

- approves `good`
- rejects `bad`
- marks ambiguous results as `hold`
- gives high-level visual judgement when AI cannot infer taste reliably

## One-Cycle Procedure

```text
1. Read current canon files
2. Select scene/use-case prompt
3. Generate 3 to 5 images
4. Classify each image: good / bad / hold
5. Record reason for each judgement
6. Store image binary in Drive
7. Store review JSON or JSONL entry in GitHub
8. If a new drift pattern appears, update `zyro-image-generation-canon.md`
9. If a new accepted expression appears, add it to the relevant prompt/template
```

## Judgement Categories

### good

Use when the image can guide future production.

Required:

- Zyro still reads as Zyro;
- right Void chamber remains plain dark field;
- Orbit remains single continuous trajectory;
- scene atmosphere supports Zyro instead of replacing it.

### bad

Use when the image is a useful failure case.

Common causes:

- right chamber becomes circular recess / eye / lens / oval pit;
- Orbit becomes multiple lines;
- left spiral becomes decorative or chaotic;
- Zyro turns into a generic infinity logo;
- extra marks appear inside the symbol.

### hold

Use when the image is interesting but not safe as reference.

Examples:

- atmosphere is good but symbol is distorted;
- symbol is good but scene language is off-brand;
- one detail may become a future variation, but not canon yet.

## File Naming

Use short, searchable IDs:

```text
zyro_sci_fi_wall_0001_good.png
zyro_sci_fi_wall_0002_bad_right_recess.png
zyro_sci_fi_wall_0003_hold_atmosphere_good_symbol_weak.png
```

## Review Entry Rule

Every saved image should have a review entry containing:

- id
- date
- use_case
- judgement
- reason
- drive_file_url or drive_file_id
- prompt_version
- canon_version
- failure_tags
- next_rule_update

## Stop Condition

A use-case is considered stable when:

- 5+ `good` references exist;
- 5+ common `bad` patterns are recorded;
- prompt template can repeatedly generate acceptable outputs;
- user no longer needs to explain the same NG reason repeatedly.
