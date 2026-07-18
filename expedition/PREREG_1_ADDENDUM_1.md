# PREREG-1 — ADDENDUM 1 (2026-07-17, BEFORE the canonical run)

Committed after harness prototyping in the Strategy Room and before any
canonical execution. PREREG_1_LOSS_TREATMENT.md is unchanged; this addendum
records deviations and bindings discovered during prototype validation.

## A1.1 — Compute cap (amends §2 statistics rule)
Prototype throughput measurement (d=5, share=0.75, fast path, modest
container): ~150 shots/s, multi-event tail dominant. At plausible d=5 logical
error rates (~1e-5), the registered CI target (half-width < 15%) implies
>1e7 shots/cell — infeasible inside the registered 1e8-shot cap on realistic
hardware in one session. Binding amendment: **each cell additionally carries a
3-hour wall-clock cap on the canonical machine.** A cell stopping at the cap
short of the CI target reports its achieved shots and CI honestly and is
marked `CI-SHORT` in the results table; CI-SHORT cells are reported, never
hidden, and no conclusion may lean on a CI-SHORT cell beyond its stated
uncertainty.

## A1.2 — Fast path sanctioned (implementation, not design)
Single-loss-event shots are exchangeable within a (location, Pauli) class;
the harness allocates their counts multinomially and batch-samples/decodes
one circuit per class ("fast path"). Statistically identical to the per-shot
loop by construction. **Gate:** the canonical machine must reproduce the
fast-vs-slow equivalence check (overlapping 95% CIs on the reference cell
d=3, p=3e-3, share=0.5, T3) before any canonical cell runs. Prototype gate
result (Strategy Room container, PROTOTYPE-grade): slow 0.00225(66) at 20k
shots vs fast 0.00230(21) at 200k shots — overlapping.

## A1.3 — Documented model constants (bindings of §2 free choices)
P_ERASE = 0.499 (graphlike-safe stand-in for a located error; weight ~ 0).
P_SPREAD = 0.25 per candidate layer for T2's within-round spread. T1 physical
substitution = deterministic Y at the loss location (the STAR convention);
T2/T3 physical event = uniformly random Pauli in {I,X,Y,Z} (maximally mixed
replacement). These follow the prereg's stated treatment definitions; they
are recorded here as the exact constants so a stranger reproduces bit-for-bit
behavior given the seeds.

## A1.4 — Prototype observation (NOT a result)
Strategy-Room smoke runs (d=3, elevated p=3e-3 for count statistics, 20k
shots — parameters intentionally non-canonical): the three treatments were
statistically indistinguishable at 50% loss share (T1 36 / T2 31 / T3 33
failures, all CIs overlapping). This is an underpowered prototype at the
wrong p and the smallest distance; it is recorded solely so that the
direction of the eventual canonical result cannot be suspected of hindsight
framing. Registered expectation E1 (~70% that R31 >= 2 at d=5, share >= 50%)
stands unmodified and unhedged: if the canonical run looks like the smoke,
E1 fails in public and the negative result publishes at full grade.

## A1.5 — Basis scope
The prereg's "both bases" holds for d=3. For d=5, the Z basis runs first;
the X basis runs as cap budget allows and is marked accordingly. Any d=5
X-basis cell not run is listed as NOT-RUN, never silently absent.
