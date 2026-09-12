# Zyro Drive Manifest

Status: active
Created: 2026-07-09

## Purpose

Google Drive stores visual evidence and heavier generated assets for the Zyro canon-control loop. GitHub stores text canon, prompts, QA schema, and indexes.

## Drive Root

```text
ZYRKO_IP_CANON
id: 1YTRfDHbVeD1I9KHeb6g4RmBIlq4GD21S
url: https://drive.google.com/drive/folders/1YTRfDHbVeD1I9KHeb6g4RmBIlq4GD21S
```

## Zyro Folder

```text
ZYRKO_IP_CANON/ZYRO
id: 1fG1SXshGJ1keMBaoQLkTAkqQ9xjlXH2q
url: https://drive.google.com/drive/folders/1fG1SXshGJ1keMBaoQLkTAkqQ9xjlXH2q
```

## Subfolders

### reference_good

Approved visual references.

```text
id: 1OqgZwdKYZyu1p_6lkxkl9V93RLDk-u8m
url: https://drive.google.com/drive/folders/1OqgZwdKYZyu1p_6lkxkl9V93RLDk-u8m
```

### reference_bad

Rejected images that are useful as failure examples.

```text
id: 13us-4MEZh4ErZOCy6jCAjBDIhhKvXc4K
url: https://drive.google.com/drive/folders/13us-4MEZh4ErZOCy6jCAjBDIhhKvXc4K
```

### prompt_logs

Prompt text, screenshots, and generation run notes.

```text
id: 1EbDiLlse7I1SbdfMTFX8Qg14RV8xp61F
url: https://drive.google.com/drive/folders/1EbDiLlse7I1SbdfMTFX8Qg14RV8xp61F
```

### qa_reports

Review exports, contact sheets, comparison images, and QA summaries.

```text
id: 1g4wcKThqO0LlFJVJUdoxQ44QpDQiAub0
url: https://drive.google.com/drive/folders/1g4wcKThqO0LlFJVJUdoxQ44QpDQiAub0
```

### exports

Final or near-final assets prepared for reuse.

```text
id: 1FlJR3ilaFIEUo7BzJqi_x7h0OqnyNzJ6
url: https://drive.google.com/drive/folders/1FlJR3ilaFIEUo7BzJqi_x7h0OqnyNzJ6
```

## Storage Rule

- Store binary images in Drive.
- Store review metadata in GitHub.
- Use matching IDs between Drive image filenames and GitHub review entries.

Example:

```text
Drive image:
reference_good/zyro_sci_fi_wall_0001_good.png

GitHub review:
qa/generation_reviews.jsonl entry with id = zyro_sci_fi_wall_0001
```
