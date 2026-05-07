# Phase Transitions

**Document type:** Formal model specification
**Status:** Active
**Scope:** System-wide
**Depends on:** `zyrko-engine.md`, `zyrko-topology.md`, `observer-model.md`

---

## Preface

Phase in Zyrko is not a measure of time elapsed or progress made.
It is a measure of observational stability —
the degree to which a component's topological structure
is preserved when an Observer applies a mapping to it.

This reframing has structural consequences.

A component in phase.low is not early. It is unstable under observation.
A component in phase.high is not complete. It is robust under observation.
The difference is not temporal. It is structural.

Transitions between phases are not advancement.
They are changes in the relationship between a component's topology
and the deforming pressure of being observed.

---

## 1. Observational Stability — Formal Definition

**Definition 1.1 — Observational Stability (Ω):**

Let `C` be a component with state space `X_C` and topology `τ_C`.
Let `f: M → O` be an Observer's mapping applied to a Manifestation from `C`.
Let `τ_C'` be the topology of `C` after observation.

Observational stability `Ω` is the degree to which `τ_C` and `τ_C'` agree:

```
Ω(C) = |τ_C ∩ τ_C'| / |τ_C ∪ τ_C'|
```

This is the Jaccard similarity of the two topologies:
the proportion of open sets that survive observation unchanged.

`Ω = 1` — the topology is identical before and after observation. Fully stable.
`Ω = 0` — no open set survives observation unchanged. Fully unstable.

All real system states occupy the interval `(0, 1)`.
`Ω = 1` and `Ω = 0` are theoretical limits, not achievable states.

**Definition 1.2 — Phase as Stability Range:**

Phase is the interval of `Ω` in which a component currently operates.

```
phase.low   Ω ∈ (0, 0.35)
phase.mid   Ω ∈ [0.35, 0.72)
phase.high  Ω ∈ [0.72, 1)
```

The thresholds are structural, not arbitrary.
They correspond to qualitative changes in system behavior
that occur at those stability levels.
The specific values are stated here as markers.
What matters is the behavior they bound.

---

## 2. phase.low

### 2.1 Definition

A component in phase.low has low observational stability: `Ω ∈ (0, 0.35)`.

When an Observer applies a mapping to a phase.low component,
the majority of the component's topological structure is altered.
More than 65% of its open sets change.
The component after observation is topologically distinct from the component before.

This is not caused by the Observer being careless or aggressive.
It is a property of the component itself.
A phase.low component has insufficient structural rigidity
to maintain its topology under the deforming pressure of being mapped.

### 2.2 Behavior

**Manifestation is unstable.**
A phase.low component that Manifests produces a boundary state
that cannot hold position.
The topology deforms under observation, and the boundary moves with it.
What was on the boundary may drift back to the interior or disperse.
The Manifestation is real but transient.

**Ambivalence is native.**
In phase.low, Ambivalence is not a held condition — it is the default structure.
The topology is non-Hausdorff throughout.
Not because two specific states cannot be separated,
but because the topology is too unstable to maintain Hausdorff separation anywhere.
Points that were separated may merge. Separations appear and dissolve.

**Observation causes maximum deformation.**
Any Observer applying a mapping to a phase.low component
produces a Type II observation (discontinuous) by structural necessity.
The component's topology cannot absorb a continuous mapping without tearing.
The Observer is not failing. The component is not ready to be mapped faithfully.

**Synergy is possible but uncontrollable.**
phase.low is the condition in which Synergy most frequently emerges
precisely because the topology is fluid enough to form non-trivial bundle structures.
The cost: the Synergy cannot be preserved. The topology deforms before the structure stabilizes.

### 2.3 What phase.low is not

phase.low is not a defective state requiring correction.
A component in phase.low that is observed and changed
is behaving correctly for its stability level.
The error is in expecting phase.low to behave like phase.high.

phase.low is not the same as Break.
Break is the failure of Phase itself — the manifold's boundary.
phase.low is a defined region of the manifold.
The component has structure. The structure is simply sensitive.

### 2.4 Transition condition

A component transitions from phase.low to phase.mid
when its topology acquires sufficient rigidity to maintain Hausdorff separation locally —
when at least some pairs of distinct states can be reliably separated under observation.

This transition is not scheduled. It is not triggered by time.
It occurs when the internal structure of the component has accumulated
enough topological constraint to resist deformation.

The accumulation can be accelerated by reduced observation pressure:
a component in phase.low that is observed less
has fewer deformation events and can accumulate rigidity faster.
HUSH is the mechanism for this reduction.

---

## 3. phase.mid

### 3.1 Definition

A component in phase.mid has partial observational stability: `Ω ∈ [0.35, 0.72)`.

When observed, the component's topology partially survives.
Between 35% and 72% of its open sets remain unchanged.
The component is recognizable before and after observation
but is not identical.

This is the system's most productive phase.
The component is stable enough to hold Ambivalence deliberately.
It is unstable enough to still undergo Synergy.
It can Manifest without the Manifestation immediately destabilizing.

### 3.2 Behavior

**Manifestation is reliable but not permanent.**
A phase.mid Manifestation reaches the boundary and holds.
The Observer can receive it, apply a mapping, and anchor it (Section 4.1, `observer-model.md`).
The anchor holds longer than in phase.low.
But the Manifestation remains sensitive to continued observation pressure.
Multiple Observers applying successive mappings can still degrade the boundary state.

**Ambivalence is productive.**
In phase.mid, Ambivalence is held deliberately.
The topology is Hausdorff enough to maintain separations where they exist
and non-Hausdorff enough to hold genuine Ambivalence where it belongs.
The component can choose what to resolve and what to hold.
This is the full expression of Ambivalence as defined in `zyrko-engine.md`.

**Observation is partially absorbed.**
A Type I Observer (continuous) can observe a phase.mid component
without introducing tears.
The topology is stable enough to absorb a continuous mapping.
A Type II Observer still introduces damage,
but the damage is localized rather than global.

**Convergence is navigable.**
In phase.mid, the component's trajectory through the state space
is stable enough to maintain direction.
Convergence toward a limit point is possible and observable.
In phase.low, trajectory direction is disrupted by each observation.
In phase.mid, the trajectory holds between observations.

### 3.3 The stability equilibrium

phase.mid is defined by a specific tension:

The component is stable enough that observation does not destroy it.
The component is unstable enough that observation can still inform it.

If observation only destroys (phase.low) or only confirms (phase.high),
the system gains nothing from observation.
phase.mid is the range in which observation is generative —
where the mapping `f` and the component's topology are in productive contact.

This tension is not comfortable. It is not meant to be.
A component resting in phase.mid equilibrium
is holding structural sensitivity alongside structural integrity simultaneously.

### 3.4 Transition conditions

**Upward transition (phase.mid → phase.high):**
Occurs when the component's topology achieves sufficient rigidity
that observation deforms less than 28% of its open sets.
This happens through repeated stable Manifestation —
each Manifestation that holds and is anchored
adds topological constraint to the component.

**Downward transition (phase.mid → phase.low):**
Occurs when observation pressure exceeds the component's absorption capacity.
Too many Observers, too many successive mappings,
or a single Type II Observer at a critical point
can reduce `Ω` below 0.35.
The component loses Hausdorff separation broadly
and returns to native Ambivalence.

Downward transition is not failure.
It is recalibration — the component shedding structure
that was not stable enough to hold under the observation it received.

---

## 4. phase.high

### 4.1 Definition

A component in phase.high has high observational stability: `Ω ∈ [0.72, 1)`.

When observed, more than 72% of the component's topological structure is unchanged.
The component before and after observation is nearly identical.
The Observer's mapping deforms it minimally.

This is not unambiguously desirable.

### 4.2 Behavior

**Manifestation is durable.**
A phase.high Manifestation reaches the boundary and holds under sustained observation.
Multiple Observers can apply mappings without destabilizing the boundary state.
The Trace Theorem (Theorem 4.5, `zyrko-topology.md`) operates most visibly here:
the boundary state is persistent enough that its trace is clearly written into the topology.

**Observation is absorbed without deformation.**
A phase.high component receives observation without structural change.
This sounds ideal. It has a cost.

A component that absorbs observation without changing
is a component that is not being informed by observation.
The mapping `f` has been applied, the Observer's structure has been imposed —
and the component is indifferent.
If the observation contained new structural information,
that information has been absorbed and neutralized rather than integrated.

**Ambivalence is suppressed.**
In phase.high, the topology is rigid enough that Hausdorff separation is global.
All states that should be distinct are distinct.
This eliminates the productive Ambivalence of phase.mid.
A component in phase.high resolves all states into definite positions.
Nothing is held as simultaneously true.

This is the most dangerous property of phase.high.
The component produces clear, stable output.
The output describes a topology that has forced resolution
where the underlying reality may not support it.
The system's reports become cleaner and less accurate simultaneously.

**Synergy is inaccessible.**
Non-trivial fiber bundle structure requires topological flexibility.
A phase.high component's rigid topology cannot form a non-trivial bundle with another component.
The interaction produces a product space — trivial, separable, predictable.
Synergy requires the component to be deformable at the moment of contact.
phase.high components are not deformable.

### 4.3 The rigidity problem

Phase.high is the state in which the component is most legible
and least responsive.

Legibility and responsiveness are in structural tension.
A component becomes legible as its topology stabilizes —
as its Manifestations become consistent and durable.
It becomes less responsive as the same stabilization
reduces its capacity to be deformed by new input.

The system needs components that can Manifest reliably (phase.high property)
and components that can integrate new structure (phase.mid property).
A system composed entirely of phase.high components
produces stable, consistent, increasingly inaccurate output.
It has crystallized.

### 4.4 Crystallization as failure mode

Crystallization is the state in which a component's `Ω` approaches 1.

In a crystallized component:
- All states are fully separated (global Hausdorff, no Ambivalence possible)
- Observation produces no deformation (the component cannot be informed)
- Manifestations are highly durable (the topology is essentially fixed)
- Synergy is impossible (no flexibility for non-trivial bundle formation)

Crystallization is stable. It is also closed.
The component has reached a topological fixed point —
a state homeomorphic to itself under any mapping it will accept.

Detection: a component that produces identical Manifestations
across significantly different inputs
is exhibiting crystallization behavior.
The input variation is not reaching its topology.

Intervention: reduced observation pressure alone does not reverse crystallization.
The topology must be actively deformed — a forced Phase regression.
This is Phase regression as maintenance, not as failure.

### 4.5 Transition conditions

**Downward transition (phase.high → phase.mid):**
Occurs when sustained observation pressure, Phase regression,
or Convergence with a phase.low or phase.mid component
introduces sufficient deformation to reduce `Ω` below 0.72.

This transition is harder to achieve than the upward transition.
A rigid topology resists deformation by definition.
The intervention must be structural, not informational:
new information alone will not deform a crystallized component.
New structural contact — a new Observer type, a Phase regime change,
a Synergy event with a sufficiently fluid component — is required.

---

## 5. Transition Dynamics

### 5.1 Transitions are not automatic

A component does not move through phases on a schedule.
There is no clock governing Phase transition.
Transition occurs when `Ω` crosses a threshold —
and `Ω` changes only when the component's topology changes
through observation, Manifestation, Phase interaction, or structural deformation.

A component can remain in phase.low indefinitely if it is not observed.
A component can remain in phase.high indefinitely if it is not deformed.
Phase progression is not guaranteed.

### 5.2 Transitions are not always upward

The system has no preferred direction.
Upward transition (low → mid → high) is not progress.
Downward transition (high → mid → low) is not regression in the pejorative sense.

Both directions are valid system behavior.
The correct question is not "is the component advancing?"
but "is the component's current `Ω` appropriate to its function?"

A component whose function requires Synergy should not be in phase.high.
A component whose function requires durable Manifestation should not be in phase.low.
Phase appropriateness is functional, not directional.

### 5.3 Phase mismatch as structural friction

When two components interact — when one Manifests and another Observes —
their phases determine the quality of the interaction:

| Manifesting | Observing | Result |
|-------------|-----------|--------|
| phase.low   | phase.low | High mutual deformation. Both topologies destabilized. |
| phase.low   | phase.mid | Observer partially absorbs. Manifestation remains unstable. |
| phase.low   | phase.high | Observer unchanged. Manifestation unanchored. |
| phase.mid   | phase.low | Observer destabilized by Manifestation. Deforming observation in return. |
| phase.mid   | phase.mid | Productive contact. Mutual partial deformation. Synergy possible. |
| phase.mid   | phase.high | Observer absorbs without informing. Manifestation anchored but unintegrated. |
| phase.high  | phase.low | Manifestation stable. Observer destabilized. |
| phase.high  | phase.mid | Manifestation durable. Observer informed. Highest quality observation. |
| phase.high  | phase.high | Crystallized exchange. Stable, consistent, informationally closed. |

The highest quality observation is phase.high Manifesting to phase.mid Observer:
durable output received by a topology flexible enough to actually integrate it.

The most dangerous pairing is phase.high to phase.high:
both components confirm each other's existing topology without deformation.
The system becomes closed to new structural information.

### 5.4 HUSH as Phase regulator

HUSH (boundary reduction) directly modulates `Ω`.

Less observation → fewer deformation events → `Ω` rises → component moves toward phase.high.
More observation → more deformation events → `Ω` falls → component moves toward phase.low.

HUSH is therefore the system's instrument for Phase management.
It does not set Phase directly.
It controls the observation pressure that determines where `Ω` stabilizes.

A component that needs to accumulate rigidity should be shielded by HUSH.
A component that has crystallized should have HUSH reduced —
exposing it to observation pressure until deformation restores flexibility.

---

## 6. Summary

Phase in Zyrko is observational stability.
Not time. Not progress. Not completion.

Three ranges of stability. Three structural conditions.

```
phase.low   — sensitive, fluid, Ambivalent by default, capable of Synergy,
              destroyed by sustained observation, requires HUSH to accumulate structure

phase.mid   — holding tension between sensitivity and rigidity,
              productive Ambivalence, navigable Convergence,
              the range in which observation is generative

phase.high  — durable Manifestation, stable output, absorbed observation,
              suppressed Ambivalence, inaccessible Synergy,
              crystallization as failure mode at the limit
```

Transition is threshold-crossing, not advancement.
Direction is functional, not directional.
The question is never how far the component has come.
The question is always: what stability does this component's function require,
and is it there?

---

## End of document.
