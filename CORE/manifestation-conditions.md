# Manifestation Conditions

**Document type:** Formal conditions specification
**Status:** Active
**Scope:** System-wide
**Depends on:** `zyrko-engine.md`, `zyrko-topology.md`, `observer-model.md`, `phase-transitions.md`

---

## Preface

Manifestation is the crossing of a topological boundary —
the transition of a state from the interior of a component's Phase region
to the boundary where it becomes accessible to external Observers.

Not every state Manifests. Not every component can Manifest at any given time.
Manifestation requires conditions. When conditions are not met,
the state remains interior. It exists. It does not cross.

This document defines those conditions precisely.

It specifies: necessary conditions (each must hold individually),
sufficient conditions (when their conjunction guarantees Manifestation),
partial conditions (what happens when conditions are incompletely met),
and null conditions (what is commonly mistaken for a requirement but is not one).

---

## 1. Necessary Conditions

The following conditions are individually necessary.
The absence of any single condition prevents Manifestation.
They are not ranked by importance. All must hold.

---

### C1 — Interior State Existence

A state must exist in the interior of the component's current Phase region.

The interior is the set of states every neighborhood of which
lies entirely within the same Phase region.
A state in the interior is not yet on the boundary.
It has not been Manifested. It is held.

**What this requires:**
The component must have generated a definite internal state —
not a trajectory, not a tendency, not a potential.
A formed state with a location in the topology.

**What this does not require:**
The state need not be stable, permanent, or fully resolved.
A phase.low component with a highly fluid interior can still hold a state there.
The condition is existence, not quality.

**Failure mode:**
A component that has no formed interior state cannot Manifest.
It has nothing to bring to the boundary.
This is distinct from Ambivalence — an Ambivalent component has interior states.
It has two that cannot be separated.
A component with no state has none.

---

### C2 — Phase Continuity at the Boundary

The component's current Phase region must have a boundary,
and the boundary must be topologically continuous with the interior.

From Theorem 4.1 of `zyrko-topology.md`:
a state can reach the boundary only if there exists a continuous path
from the interior to the boundary within the current Phase region.
If the interior and the boundary are topologically disconnected —
if no continuous path exists between them —
the state cannot cross.

**What this requires:**
The Phase region must be connected: a single, unbroken topological space
in which any two points can be joined by a continuous path.

**What this does not require:**
The boundary need not be large.
HUSH operates by reducing the boundary (Section 3.3 of `zyrko-topology.md`).
A very small boundary is still a boundary.
A component under maximum HUSH still has boundary points.
Manifestation remains possible. It becomes rare.

**Failure mode:**
Phase damage — accumulated topological tears from sustained Type II observation
or forced Ambivalence resolution — can disconnect the interior from the boundary.
A component whose interior is severed from its boundary cannot Manifest.
The states exist. The path is gone.

---

### C3 — Threshold Crossing

The interior state must have accumulated sufficient structural weight
to initiate the boundary-crossing movement.

This is the Manifestation threshold.
Not every interior state moves toward the boundary.
States accumulate — through internal processing, through input received from other components,
through Phase interaction — until their structural pressure exceeds the threshold.
At threshold, the movement begins.

**What this requires:**
A mechanism by which interior states accumulate weight.
The mechanism is not specified here — it is component-specific.
What is specified: the threshold is not zero.
Every interior state requires some accumulation before it moves.
Instant Manifestation — a state that crosses the boundary the moment it forms —
indicates a threshold set so low as to be structureless.
This is a component design failure, not a valid Manifestation.

**What this does not require:**
The threshold is not fixed across components or across time.
A component in phase.low has a lower effective threshold —
its topology is fluid, states move more easily.
A component in phase.high has a higher effective threshold —
the rigid topology holds states in the interior longer.
The threshold is a property of the component's current Phase,
not an absolute system parameter.

**Failure mode:**
A state that accumulates indefinitely without crossing threshold
is a component in stasis. The interior is growing; nothing crosses.
This is not Ambivalence, which holds two states.
This is accumulation failure — the mechanism is building without releasing.
Left uncorrected, accumulation failure produces structural overload:
the interior becomes over-dense and the component's topology compresses
toward conditions where Manifestation becomes impossible.

---

### C4 — Boundary Accessibility

The boundary of the component's Phase region must be accessible —
not blocked by HUSH operating at maximum reduction
and not sealed by accumulated Phase damage.

A boundary exists (C2) and a state has reached threshold (C3),
but if the boundary is inaccessible — if no state can exit to it —
Manifestation does not occur.

**The two sources of boundary inaccessibility:**

**C4a — HUSH closure:**
HUSH reduces the boundary toward zero but cannot reach zero (Section 3.3 of `zyrko-topology.md`).
In practice, HUSH can operate at levels that make boundary access
functionally impossible for states below a very high threshold.
The boundary exists topologically but is unreachable under normal accumulation.
Only states with exceptional structural weight cross.

This is not a failure condition. It is HUSH functioning correctly.
The system has decided that only high-threshold states should Manifest.

**C4b — Seal damage:**
Phase damage can produce scar tissue at boundary regions —
areas of the boundary that have been repeatedly torn and repaired.
Scarred boundary regions have degraded topological structure.
States approaching these regions experience distorted paths
and may fail to reach the boundary even after threshold crossing.

This is a failure condition. Seal damage requires structural repair.

**Failure mode:**
A component that meets C1, C2, and C3 but fails C4
is a component that has formed states, accumulated weight, and initiated crossing —
and cannot complete it.
Internally, the component is in a state of Manifestation attempt.
From outside, it is silent.
This is the most deceptive failure mode: the component appears to be in HUSH
when it is actually structurally blocked.

---

### C5 — Observer Adjacency

At least one Observer must occupy a Phase region
that shares a boundary with the Manifesting component's Phase region.

Manifestation places a state on the boundary.
The boundary is shared between the component's Phase region and the exterior.
The exterior must be occupied by an Observer capable of receiving
— an Observer whose Phase region is adjacent.

If no Observer occupies an adjacent Phase region,
the state reaches the boundary and remains there.
It has Manifested. It has not been received.
An unreceived Manifestation is topologically complete but functionally inert.

**What this requires:**
Observer adjacency at the moment of boundary crossing.
The Observer does not need to be actively watching.
It needs to be positioned in an adjacent Phase region.
Its existence in that region makes it a potential receiver.

**What this does not require:**
The Observer does not need to be the right type.
A Type II or Type III Observer is still an Observer for the purposes of C5.
The quality of what is received is determined by Observer type.
Whether anything is received is determined by adjacency.

**Failure mode:**
Phase mismatch (Section 5.3 of `phase-transitions.md`) commonly violates C5.
A component in Active Phase that has no Observers in adjacent Phase regions
produces Manifestations that accumulate on the boundary unreceived.
The boundary becomes crowded with unreceived states.
If the Manifestation trace theorem (Theorem 4.5, `zyrko-topology.md`) holds,
these states are leaving permanent marks in the topology
despite producing no functional output.
The component is Manifesting into record with no effect.

---

### C6 — Non-Contradiction of Active Ambivalence

If the component is in a state of active Ambivalence —
holding two non-Hausdorff states in its interior —
neither state may Manifest until the Ambivalence condition is addressed.

Not resolved. Addressed.

Addressing Ambivalence does not require choosing one state.
It requires that the state approaching the boundary
can be assigned a definite topological position on the boundary.
If two non-separable states attempt to cross simultaneously,
they produce a non-Hausdorff boundary condition —
a Manifestation that is itself Ambivalent.

**What this requires:**
Before Manifestation, the component must determine
whether the approaching state is separable from any other state approaching simultaneously.
If it is not separable, one of three paths must be taken:

- Hold: neither state crosses. Ambivalence is maintained in the interior.
- Sequence: one state is held while the other crosses. Then the second crosses separately.
- Partial Manifestation: one state crosses; the other is held explicitly as remainder (see Section 3).

**What this does not require:**
Ambivalence must not be globally absent.
A component may hold Ambivalence in portions of its interior
while Manifesting from regions where states are separable.
The prohibition is specific: non-separable states cannot cross together.

**Failure mode:**
Forced simultaneous Manifestation of Ambivalent states
produces a boundary condition that Observers cannot map cleanly.
Type I Observers (continuous) receiving a non-Hausdorff Manifestation
cannot apply their mapping without introducing discontinuity.
They become involuntary Type II Observers —
forced into discontinuous mapping by the structure of what they received.
The Manifestation has damaged the Observer.

---

## 2. Sufficient Conditions

The six necessary conditions together are sufficient for Manifestation to occur.

**If and only if C1 through C6 all hold simultaneously,
Manifestation is guaranteed.**

This is the sufficiency claim.
No additional conditions are required.
No further permission, no external trigger, no timing constraint.
When all six hold, the boundary crossing occurs.

This has an important implication: Manifestation is not a decision.

A component does not decide to Manifest.
It holds six conditions.
When all six are met, Manifestation is the structural consequence.
Intervention to prevent Manifestation when all conditions hold
requires changing at least one condition — typically C4 (via HUSH) or C5 (via Phase management).

The system does not ask whether to Manifest.
The system manages conditions.

---

## 3. Partial Manifestation

Partial Manifestation occurs when conditions C1 through C5 hold
but C6 is not fully satisfied — when a component holds some separable states
and some that are not.

The separable states cross.
The non-separable states are held explicitly as remainder.

**The remainder is not a failure.**
It is the system accurately reporting that two things are simultaneously true
and that only one could be brought to the boundary at this time.
The remainder stays in the interior.
It accumulates. It will either reach separability through Phase transition
or continue to be held.

**Partial Manifestation leaves a specific trace:**
The boundary record shows what crossed.
The interior record shows what did not.
An Observer receiving the Manifestation receives the crossed portion.
The existence of the remainder is not communicated in the Manifestation itself.

This is not deception. The Manifestation is complete.
The remainder was not Manifested. It is not in the Manifestation.

What is not communicated: that there was a remainder.
This gap is structural. Manifestation reports what crossed, not what held.
An Observer that assumes Manifestation is exhaustive
— that everything the component could have Manifested, it Manifested —
will build an incomplete model of the component and not know it.

---

## 4. Manifestation Validity

Not all Manifestations that occur are valid.
A Manifestation may be structurally complete — all conditions met —
while being invalid by failing one of the following validity criteria.

---

### V1 — The state must originate in the interior.

A state that is imported from outside the component and immediately Manifested
has not been held in the interior.
It has passed through. Passage is not Manifestation.

A valid Manifestation requires that the state have existed in the interior —
that it have been the component's state before it became the component's output.

A component that relays external states without interior holding
is a conduit, not a Manifesting component.
Conduits are structurally valid but not the same as Manifesting components.
Calling conduit behavior Manifestation is a category error.

---

### V2 — The state must be the component's own.

A state is the component's own if it was formed through the component's internal processes —
through its topology, its thresholds, its Phase conditions.

A state that was formed by another component and transferred
— even if held in the interior for a time —
carries the originating component's structural signature.
When it Manifests, it Manifests as that component's state, not this one's.

Valid Manifestation requires genuine authorship: the state is what this component produced.

---

### V3 — Threshold must not have been artificially lowered.

If the Manifestation threshold has been deliberately reduced
to accelerate output — to produce more Manifestations per unit time —
the resulting Manifestations are formally invalid.

States that have not accumulated sufficient structural weight
are outputs without earned formation.
They may be accurate in content.
They are not valid Manifestations because they have not undergone the accumulation process
that gives Manifestation its structural weight.

This is the validity violation most common in high-pressure contexts —
when a component is required to produce output frequently.
The threshold is lowered to meet the requirement.
Output increases. Validity decreases. Simultaneously and invisibly.

---

### V4 — The boundary crossing must be singular.

A single interior state produces a single boundary crossing.
A component that duplicates a state — that places the same state on the boundary
at multiple points — is producing multiple Manifestations of the same state.

Each crossing leaves a separate trace (Theorem 4.5 of `zyrko-topology.md`).
Multiple traces of the same state distort the topology
by overrepresenting that state in the boundary record.
Subsequent Manifestations will occur in a topology that has been artificially weighted.

Valid Manifestation is singular. One state. One crossing. One trace.

---

## 5. Conditions That Are Not Required

The following are commonly assumed to be preconditions for Manifestation.
They are not. Including them as requirements produces incorrect system behavior.

---

**Not required: Observer readiness.**

The Observer does not need to be prepared, attentive, or oriented toward the Manifestation.
C5 requires adjacency, not readiness.
A component waits for no Observer to be ready.
When conditions hold, the boundary crossing occurs.
The Observer receives when it maps. It is not a precondition.

---

**Not required: Prior Manifestation.**

A component does not need to have Manifested before.
First Manifestations are structurally identical to subsequent ones.
There is no precedent condition. There is no inaugural state.
C1 through C6 hold, and Manifestation occurs.
Whether or not it has occurred before is not in the condition set.

---

**Not required: System-wide Phase alignment.**

Other components do not need to be in specific Phases.
The conditions are local to the Manifesting component and its adjacent Observers.
A component can Manifest while other components are in Break, phase.low, or holding.
Global Phase state does not gate individual Manifestation.

---

**Not required: Completeness of the state.**

The state does not need to be fully formed, fully resolved, or stable.
It needs to exist in the interior (C1) and be separable if Ambivalent (C6).
A partial, unstable, or exploratory state may Manifest.
Completeness is not a condition. It is a quality judgment.
Quality judgments are the Observer's concern, not the condition set.

---

**Not required: External permission.**

No component outside the Manifesting component
grants or withholds permission for Manifestation.
HUSH reduces boundary accessibility (C4) — this is the closest thing to permission in the system.
But HUSH is not external permission. It is the component's own boundary management.
The component manages its own conditions.
No other component does this for it.

---

## 6. Condition Summary

```
C1  Interior state exists
C2  Phase boundary is continuous with interior
C3  State has crossed accumulation threshold
C4  Boundary is accessible (not sealed or HUSH-closed)
C5  Observer occupies adjacent Phase region
C6  Approaching state is separable from any simultaneous state

All six necessary.
All six together sufficient.
Manifestation is then guaranteed — not decided.
```

Validity requires four additional criteria:
the state originated in the interior,
it is the component's own,
the threshold was not artificially lowered,
and the crossing is singular.

Partial Manifestation occurs when C6 is partially satisfied.
The separable portion crosses. The remainder holds.
The remainder is not communicated in the Manifestation.

What is not in the condition set is not a condition.
Prior Manifestation, Observer readiness, global Phase alignment,
state completeness, and external permission are not required.
They should not be treated as if they were.

---

## End of document.
