# QC003 — SESSION HANDOFF (refreshed at close of each session)

## Session 2 closed 2026-07-17 at a676f85
State: Chapter 2 (neutral atoms, the loss drill) drafted, primary-verified
(9 sources, 3 spot-checked by executor), and integrated live. Bet B4
deposited (~55%, signpost 2027-12-31: repeated QEC rounds on a logical qubit
with mid-experiment atom replacement). PREREG-1 committed BEFORE any run:
the loss-treatment sensitivity campaign (T1 unheralded Pauli / T2 delayed
erasure / T3 immediate erasure; registered expectation E1: R31 >= 2 at loss
share >= 50%, d=5, ~70% AI-drafted author-delegated). Author greenlit
2026-07-17. No campaign code exists yet.

## Session 3 agenda — RUN PREREG-1 (the campaign session)
Build the harness against expedition/PREREG_1_LOSS_TREATMENT.md exactly as
registered: pinned env (Python 3.12, stim>=1.16, pymatching>=2.4), validate
the 0%-loss control first (all three treatments must agree; this is the
pipeline self-test and the kill condition's tripwire), then the full sweep
(d=3,5; loss shares 0/25/50/75%; >=1e6 shots per cell to CI half-width
<15%). Commit circuits, seeds, reweighting code, raw counts as artifacts.
Numbers enter prose ONLY from committed artifacts. Deviations from the
prereg require a dated addendum file, never an edit. Results integrate into
the edition as Chapter 2a or a §07 update (author's call on placement),
E1 resolves TRUE/FALSE in public either way.

## Standing obligations
- B3 scores 2026-12-31; B1/B2/B4 score 2027-12-31.
- Cycle 2 scouting owes >= 1 wildcard arc (search plan in Cycle 1 ledger).
- Chapter 3 (superconducting, the wiring drill) queued after the campaign.
- Residual cosmetics unchanged: dossier.source.html "(working title)";
  Ch1 section 05 intro wording open to author revision.
