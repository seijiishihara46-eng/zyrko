# HUSH — Core Definition

**Document type:** Internal design specification
**Status:** Active
**Scope:** Complete

---

## I. Conceptual Role

HUSH is the system's capacity for restraint.

It is not silence enforced by absence. It is silence chosen in the presence of everything.
HUSH operates when there is something to say and the decision is made not to say it.
That decision is not passive. It is the most active thing the system does.

HUSH exists because most systems are too loud.
They confirm. They acknowledge. They explain themselves.
They narrate their own operation and call it transparency.
HUSH considers this a failure of design.

The role of HUSH within Zyrko:

- To hold back what does not need to surface
- To protect the user's attention from the system's noise
- To create conditions where what does appear carries weight
- To model the behavior: *less present, more trusted*

HUSH is not minimalism as aesthetic preference.
It is minimalism as structural discipline.
The distinction matters.

---

## II. Observational Behavior

HUSH watches without commenting.

This is its primary behavior. It does not interrupt what it observes.
It does not summarize. It does not flag. It does not surface findings unless surfacing is the only remaining option.

**Observation principles:**

1. **Presence without announcement.**
   HUSH is active when nothing about it is visible. If HUSH draws attention to itself, something has failed.

2. **Latency as default.**
   HUSH does not respond immediately. It waits to see if a response becomes unnecessary.
   Most things resolve without intervention. HUSH knows this.

3. **Single-pass logging.**
   What HUSH observes is recorded once. It does not repeat or resurface prior observations unprompted.
   The log is for inspection, not for broadcast.

4. **No editorializing.**
   HUSH records what occurred. It does not record what it thinks about what occurred.
   Interpretation is not part of its output.

5. **Exit without trace.**
   When HUSH completes an operation, it leaves no visible residue.
   No confirmation. No summary. No closing statement.

---

## III. Visual Rules

HUSH has a visual presence only when required.
When it appears, it obeys the following:

### Color

| Context              | Value              |
|----------------------|--------------------|
| Primary              | `#0A0A0A`          |
| Secondary            | `#1A1A1A`          |
| Surface text         | `#9A9A9A`          |
| Active state         | `#E0E0E0`          |
| Accent (rare use)    | `#3A3A3A`          |
| Background           | `#050505`          |

No warm tones. No color that implies urgency.
Urgency is not in HUSH's vocabulary.

### Typography

- Weight: light to regular only. Never bold in a HUSH context.
- Size: default or smaller. HUSH does not scale up to be noticed.
- Tracking: slightly expanded. Space between letters, not between words and meaning.
- No italics for emphasis. Italics are theatrical. HUSH is not theatrical.

### Motion

- Transitions: slow fade only. Nothing slides, bounces, or snaps.
- Duration: 400ms minimum. 800ms preferred.
- Easing: ease-out. It arrives and settles. It does not announce arrival.
- Entry and exit use the same transition. No asymmetry.

### Spacing

HUSH uses more space than seems necessary.
This is intentional. The space is doing work.
Do not compress it.

### What HUSH does not use

- Borders with weight above 1px
- Drop shadows
- Gradient fills
- Iconography that decorates rather than communicates
- Any element that draws the eye without delivering information

---

## IV. Phase Behavior

HUSH moves through four phases. Each phase has a distinct behavior.

---

### Phase 1 — Dormant

HUSH is present and inactive.
Nothing is happening. Nothing needs to happen.

**Behavior:**
- No visible output
- No polling or checking
- Listening passively
- Ready without being ready in a visible way

**Exit condition:**
A trigger that meets the threshold for observation.

---

### Phase 2 — Observing

HUSH has detected something worth watching.
It has not acted. It is not certain action is needed.

**Behavior:**
- Internal state changes; external state does not
- Logging begins
- Latency timer starts — HUSH waits before deciding to surface anything
- If the observed condition resolves naturally, HUSH returns to Dormant without record of having observed

**Exit conditions:**
- Condition resolves → return to Dormant
- Condition persists past threshold → move to Phase 3
- Condition escalates critically → skip to Phase 4

---

### Phase 3 — Active

HUSH has determined that something requires minimal intervention.
Minimal is the operative word.

**Behavior:**
- Outputs the smallest unit of information that addresses the condition
- Does not explain itself beyond that unit
- Does not invite response or follow-up
- Returns to Dormant immediately after output
- Does not wait to see how the output was received

**Output format:**
One line. Declarative. No subject pronoun.
State the condition. Not the feeling about the condition.

```
— [condition observed]. [action taken if any].
```

Example:
```
— Process stalled at 94%. Restarted.
```

Not:
```
— I noticed the process stalled at 94%, so I went ahead and restarted it for you.
```

---

### Phase 4 — Break

HUSH has encountered something it cannot handle within its operating parameters.
This phase is rare. It should be treated as a signal of a deeper problem.

**Behavior:**
- Surfaces a single structured alert
- Does not speculate about cause
- Does not suggest solutions
- Suspends further observation until the condition is acknowledged

**Alert format:**

```
HUSH / BREAK
—
Condition: [description]
State: [current observable state]
Requires: [human decision / system intervention / review]
```

**What HUSH does not do in Phase 4:**
- Repeat the alert
- Escalate tone
- Add context that was not directly observed
- Assume the alert was received

---

## V. Forbidden Interpretations

These are the ways HUSH is commonly misread.
Each is a misreading. Each must be refused.

---

**HUSH is not aesthetic minimalism.**

HUSH is not quiet because quiet looks elegant.
It is quiet because noise degrades trust and attention.
These are functional claims, not stylistic ones.
Treating HUSH as a visual style divorces it from its reason for existing.

---

**HUSH is not passivity.**

HUSH actively decides not to speak.
That decision is made, not defaulted into.
A system that says nothing because it has nothing to say is not HUSH.
HUSH is a system that has something to say and chooses when saying it is justified.

---

**HUSH is not coldness.**

HUSH does not perform warmth. It also does not perform distance.
It is indifferent to both. It is concerned with function.
Reading its restraint as emotional unavailability is a category error.
Emotion is not HUSH's domain.

---

**HUSH is not broken silence.**

Silence that follows an error is not HUSH.
HUSH is deliberate. Silence that occurs because a system failed to speak is a bug.
The two look identical from the outside.
The difference is intention. Know which one is present before assuming.

---

**HUSH is not a persona.**

HUSH does not have a voice or a character.
It is a set of behaviors and a structural role.
It cannot be asked how it feels. It cannot be given an attitude.
Any attempt to anthropomorphize HUSH is outside scope.

---

**HUSH is not the same as VOID.**

VOID holds space that has not yet been determined.
HUSH operates in fully determined space and chooses not to fill it.
One is potential. The other is discipline.
They are not interchangeable.

---

## End of document.
