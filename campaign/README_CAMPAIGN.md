# PREREG-1 campaign code — provenance and run order

Prototyped and validated in the Strategy Room container 2026-07-17
(stim 1.16.0, pymatching 2.4.0, numpy 2.4.4, Python 3.12). Prototype numbers
are PROTOTYPE-grade only; canonical numbers come exclusively from runner.py
output committed as artifacts by the executor.

Run order on the canonical machine (all mandatory, in order):
1. pip install per requirements (stim>=1.16 pymatching>=2.4 numpy>=2 — NO scipy).
2. GATE 1 — equivalence: run_cell (slow) vs run_cell_fast on the reference
   cell d=3, p=3e-3, share=0.5, T3 (20k slow / 200k fast, any seeds).
   95% CIs must overlap. Record both lines in gates.log.
3. GATE 2 — control: run_cell_fast at share=0.0 for T1/T2/T3, d=3, p=1e-3,
   200k shots, same seed: the three LERs must be IDENTICAL (same code path).
   Record in gates.log. Any gate failure => STOP (prereg S6 kill condition).
4. python3 runner.py --out results.jsonl   (resumable; ~hours; cells cap at
   3h wall-clock each per ADDENDUM A1.1; d=5 x-basis cells run last).
5. Commit: harness.py runner.py README_CAMPAIGN.md gates.log results.jsonl
   and the addendum. Do NOT summarize or interpret results — the Strategy
   Room drafts the write-up from the committed artifacts only.
