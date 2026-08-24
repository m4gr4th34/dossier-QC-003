# PREREG-1 RESULTS — ADDENDUM 1 (COMPLETION, 2026-07-19)
### Closes the PENDING label in PREREG_1_RESULTS.md §5. Drafted exclusively from the full committed table (campaign/results.jsonl at d55194a, 48/48 cells final).

## The d=5 x-basis tail, now complete

All eight previously-PENDING cells are final. Statuses: share 0.50 T2/T3
CI-SHORT (3h cap per PREREG-1 ADDENDUM A1.1); shares 0.25 and 0.00 all OK.
No registered cell is missing from the table; nothing was truncated.

**Controls (share 0.00, x):** 1.279e-4 / 1.500e-4 / 1.392e-4 (T1/T2/T3),
all CIs overlapping — clean, as in every prior control.

**Share 0.25, x:** R31 = 1.19 [0.94, 1.44], R21 = 0.94 [0.74, 1.14] —
treatments statistically indistinguishable, mirroring the z basis.

**Share 0.50, x — the one new finding:** T1 1.712e-5 ± 0.30e-5 (125 fails,
7.3M shots), T2 3.043e-5 ± 0.71e-5, T3 2.905e-5 ± 0.73e-5.
**R31 = 0.59 [0.41, 0.77] and R21 = 0.56 [0.40, 0.73] — unity excluded.**
The inversion reported in the main document — the unheralded STAR-style
treatment outperforming both erasure treatments — was significant at d=3
(both bases) but only directional at d=5 in the z basis. It is now
**significant at d=5** in the x basis. E1's falsification is thereby
strengthened: the registered threshold (R31 ≥ 2) is excluded at share 0.50
in both bases, and the *opposite* of E1 (R31 < 1) is established in one
basis at each distance.

**Basis asymmetry: no claim.** The x-basis T3 rate at share 0.50 sits 1.48x
above its z counterpart, but the ratio's CI [0.91, 2.06] includes unity;
with 12 CI-SHORT cells in the table, apparent x/z differences at this
precision are not distinguishable from noise and none is asserted.

**Budget substitution replicates in x:** T1 trajectory 1.28e-4 → 7.12e-5 →
1.71e-5 → 1.05e-6 across shares 0/0.25/0.50/0.75 — the same ~two-order
collapse as z. The main document's §2 finding stands unchanged in both bases.

## Status of the document set

PREREG_1_RESULTS.md §5's PENDING is closed by this addendum; per doctrine the
main document is not edited. The campaign's full chain of custody:
prereg (a676f85) → code + pre-run addendum (f60e953) → gates + checkpoint 1
(0c32aef) → E1-critical cells (bde5a86) → resolution + scored forecast
(fb2b65d) → full table (d55194a) → this completion. Every number above is
recomputable from committed shots/fails; no other analyses were run.
