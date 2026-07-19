# PREREG-1 — RESULTS AND E1 RESOLUTION
### Drafted 2026-07-19 from the committed canonical artifacts ONLY (campaign/results.jsonl at commit bde5a86; gates.log at 0c32aef). Prereg: expedition/PREREG_1_LOSS_TREATMENT.md · Addendum: PREREG_1_ADDENDUM_1.md.

## 1. E1: RESOLVED FALSE — and inverted

**The registered expectation.** E1 (PREREG-1 §4, committed before any code
existed): at loss share ≥ 50% and d = 5, the unheralded STAR-style treatment T1
overprices the logical error rate relative to immediate erasure T3 by a factor
R31 = LER(T1)/LER(T3) ≥ 2. Registered confidence: ~70% (AI-drafted,
author-delegated 2026-07-17).

**The measurement.** At the only share ≥ 50% cells with usable precision
(d=5, z basis, share 0.50 — statuses CI-SHORT per Addendum A1.1, uncertainties
reported in full):

| Treatment | Logical error rate | Shots | Fails |
|---|---|---|---|
| T1 unheralded Pauli-Y | 1.851e-5 ± 0.31e-5 | 7.4M | 137 |
| T2 delayed erasure | 2.333e-5 ± 0.61e-5 | 2.4M | 56 |
| T3 immediate erasure | 1.957e-5 ± 0.57e-5 | 2.3M | 45 |

**R31 = 0.95, 95% CI [0.63, 1.26]. The registered threshold of 2 is excluded
even at the CI's upper edge.** R21 = 0.79 [0.55, 1.04]. At share 0.75 the
counts are too small for a ratio claim (8/5/4 failures; R31 point estimate
0.47, CI spanning zero to 1.04) — per the addendum's rule, no conclusion leans
on those cells beyond their stated uncertainty, and they are reported, not
hidden. **E1 is FALSE at achieved precision. The AI-drafted ~70% forecast is
scored: FAILED, in public, as registered.**

**The inversion.** Not only is the unheralded treatment not ≥2x worse — where
the data are precise enough to distinguish the treatments at all, it is
*better*. At d=3 (all cells at full precision, status OK): share 0.50 gives
R31 = 0.77 [0.61, 0.92] and share 0.75 gives R31 = 0.60 [0.48, 0.73] — unity
excluded in both. The direction replicates in the x basis. The STAR-style
pricing, registered here as the suspected *pessimistic* shortcut, produced
*equal or lower* logical error rates than the erasure-physics treatments at
every measurable point of this design.

## 2. The unregistered headline: the budget-substitution effect

The largest effect in the table was not the one the prereg was pointed at.
Holding the total physical error budget fixed at p = 1e-3 and shifting its
composition from circuit-level depolarizing toward per-qubit loss events
collapses the logical error rate — under every treatment:

d=5, z, T1: **1.43e-4 (0% loss share) → 5.73e-5 (25%) → 1.85e-5 (50%) →
1.36e-6 (75%)** — a drop of roughly two orders of magnitude across the sweep,
with T2/T3 tracking the same trajectory.

Plain reading: **in this design, a unit of error budget spent as single-qubit
loss (however treated) is far less damaging than the same unit spent as
standard circuit-level depolarizing noise** — the latter includes correlated
two-qubit errors on entangling gates; the loss channel as modeled here does
not. The share sweep therefore measures the substitution at least as much as
it measures the heralding. This is itself an arc E finding: budget-equalized
comparisons of loss treatments are dominated by *what the loss budget
displaces*, a modeling choice upstream of any heralding question. [OPEN:
mechanism analysis; the sentence above describes this design, and no claim is
made about hardware or about other loss models.]

## 3. Why the inversion is plausible, and what this campaign cannot say

[OPEN — mechanism commentary, not a measured result.] T1's physical event is a
deterministic Pauli-Y at a known circuit slot: a weight-1 error that triggers
syndromes in both bases and sits exactly on an error mechanism the base
decoder graph already models. T2/T3's physical event is a maximally mixed
replacement (25% harmless, 75% X/Y/Z) *plus* location information. The
registered design compared the two published *treatments as wholes* — channel
convention and decoder knowledge together, exactly as the STAR paper on one
side and the erasure literature on the other actually use them. It therefore
**cannot decompose** how much of the inversion is channel (deterministic-Y vs
mixed) versus information (heralding value). A fourth arm — the mixed channel
*without* heralding — would isolate that, and is the natural PREREG-2
candidate; it was not registered and was not run.

Standing limits from the prereg apply in full: rotated surface code, MWPM,
memory experiment, d ≤ 5, one loss-location convention; no extrapolation to
any published multiplier, and no hardware claim.

## 4. What survives for arc E

The specific registered worry — that transversal-STAR's unheralded Pauli-Y
loss pricing materially *understates* correctable structure and thus overprices
logical error — **does not survive this test and is retired at these
parameters.** The negative result publishes at full grade, per the prereg's
own §4. What replaces it is sharper: the sensitivity that matters is not
heralded-vs-not but **loss-vs-depolarizing composition of the budget**, where
this table shows ~100x of leverage. Any cost model's split of its physical
error budget between correlated gate noise and benign-as-modeled loss is worth
two orders of magnitude of logical performance in this design — dwarfing every
treatment effect measured here.

## 5. Bookkeeping

- Gates: equivalence and 0%-control both PASS (campaign/gates.log, committed).
  Control at canonical p: T1/T2/T3 statistically indistinguishable at share 0
  for both distances (independent seeds), as designed.
- Cell statuses: all d=3 cells OK; d=5 share 0.25/0.00 OK; d=5 share
  0.50/0.75 CI-SHORT at the 3h cap (Addendum A1.1), uncertainties as tabled.
- d=5 x-basis: shares 0.75 final (T1 1.05e-6, T2 5.38e-6, T3 2.86e-6, all
  CI-SHORT; same direction), share 0.50 T1 final (1.71e-5, CI-SHORT);
  remaining x cells PENDING at drafting time and will appear in the final
  artifact commit — none is load-bearing for the E1 resolution above.
- Forecast score deposited to the registry: E1, AI-drafted ~70%, FAILED
  2026-07-19. The failure is recorded with the same prominence as a success
  would have been; a registry that only reports wins is marketing.
