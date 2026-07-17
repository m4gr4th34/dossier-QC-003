# PREREG-1 — THE LOSS-TREATMENT SENSITIVITY CAMPAIGN
## Pre-registered 2026-07-17, BEFORE any simulation run. Author greenlight: given this date.

This document is committed before any campaign code executes. Results that
contradict expectations are published at full grade. Mid-campaign changes
require a dated addendum, never an edit to this file.

## 1. Question

When a neutral-atom architecture's atom-loss channel is modeled three
different defensible ways, how far does the logical error rate move? This is
the neutral-atom instance of the noise-model fidelity audit pre-registered in
the Cycle 1 scouting ledger (arc E), motivated by a documented discrepancy:
the transversal STAR architecture paper (arXiv:2509.18294) prices loss as an
unheralded effective Pauli-Y channel, while the platform's flagship
experiments and decoding theory (Nature 649, 39–46; PRX X 16, 011002) treat
loss as detectable and locatable.

## 2. Fixed experimental design

- **Code:** rotated surface code, distances d = 3, 5 (d = 7 if runtime
  permits; its absence is not a failure). Memory experiment, d rounds of
  syndrome extraction, both bases.
- **Noise:** circuit-level depolarizing noise at physical rate p = 1e-3 on
  all operations, PLUS an atom-loss channel applied per two-qubit gate and
  per idle round at loss rate l. Sweep the loss share of the total error
  budget: l chosen so loss constitutes {0%, 25%, 50%, 75%} of total physical
  error events, holding the total budget fixed. (0% is the control: all
  three treatments must agree there, which is the pipeline's self-test.)
- **The three treatments of each sampled loss event:**
  - **T1 — unheralded Pauli substitution (the STAR-style choice):** the loss
    is replaced by a Pauli error drawn per that paper's effective-channel
    convention; the decoder receives no heralding.
  - **T2 — delayed erasure (the Baranes-decoder regime):** the loss location
    (qubit index) is revealed to the decoder only at the END of the round in
    which it occurred; time-within-round remains unknown. Decoder edges
    touching that qubit in that round are reweighted accordingly.
  - **T3 — immediate erasure (the idealized bound):** loss location and gate
    layer are revealed at once; corresponding decoder edges become
    zero-weight (known-error) edges.
- **Decoder:** minimum-weight perfect matching (PyMatching 2.4+) with
  per-shot reweighting for T2/T3. Same decoder family across all treatments —
  the variable under test is the loss treatment, never the decoder.
- **Statistics:** ≥ 1e6 shots per (d, loss-share, treatment) cell, extended
  until the logical error rate's 95% CI half-width is < 15% of its value or
  1e8 shots, whichever first. Seeds fixed and committed.
- **Environment:** Python 3.12, stim ≥ 1.16, pymatching ≥ 2.4, numpy 2.x —
  pinned in the campaign's requirements file; versions recorded in output.

## 3. Registered outputs (the deliverable, direction-blind)

- **The sensitivity table:** logical error rate per round for every cell,
  with CIs, plus the headline ratios R21 = LER(T1)/LER(T2) and
  R31 = LER(T1)/LER(T3) at each loss share.
- All raw counts, circuits, seeds, and the exact reweighting code committed
  as artifacts. A stranger reruns the repo and reproduces the table.

## 4. Registered expectation (falsifiable, owned before running)

**E1:** At loss share ≥ 50% and d = 5, the unheralded treatment T1 overprices
the logical error rate relative to immediate erasure T3 by a factor R31 ≥ 2.
Confidence this holds: ~70% [AI-drafted estimate (author-delegated
2026-07-17); the author may override]. If E1 fails — if the treatments agree
within a factor two even when loss dominates — that is itself the finding:
it would mean the Pauli-Y shortcut is materially fine for architecture
costing at these scales, retiring this dossier's stated worry about the STAR
modeling choice, and it publishes at full grade as a negative result.

## 5. Explicit non-claims and limits

- This campaign does NOT recost the STAR architecture's 250x/2x headline; it
  measures the sensitivity of a standard memory benchmark to the loss
  treatment. Extrapolation to any published multiplier is future work and
  will not be asserted from these results.
- T2's end-of-round convention is one point in the delayed-detection design
  space, chosen for implementability; the Baranes decoder is richer.
- Rotated surface code, MWPM: chosen for tooling maturity, not because the
  platform will use them; a qLDPC follow-up is a separate prereg.
- No hardware claim of any kind follows from this campaign.

## 6. Kill condition

If the T2 reweighting cannot be validated against the 0%-loss control and
published erasure-threshold sanity points within the session's budget, the
campaign halts and reports the failure as the result. No tolerance widening;
no quiet redefinition of T2.
