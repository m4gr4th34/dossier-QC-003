# QC003 — SESSION HANDOFF (refreshed at close of each session)

## Session 9 closed 2026-08-25
Chapter 8 (THE RECOST) drafted and integrated live — the dossier's planned
arc is complete: seven drills, one recost, thirteen live bets. The recost
kept Ch1's promise with a modified shape, and the modification is the
finding. (1) The audit ate its own inputs first: errata SR-7 (a false CITE
live on the page — the "20-40x vs best-in-class" claim, absent from its
paper) and SR-8 (SR-1 recurring; the ~250x is present verbatim), the
absence-claim doctrine now enforced by verification/check_retracted.py.
(2) The ruler: the six claims measure four different quantities at four
physical error rates across three task classes — only three lift onto the
one real axis (phys qubits per logical at fixed logical error). Committed,
rerunnable harness: expedition/recost_harness.py (+ .test.py, byte-identity
--check; one FP boundary bug caught pre-commit by the test's hand-derived
spot checks, fixed in the harness never the test). (3) The numbers, all
OPEN-CAVEATED under the stated model: surface 882 per logical at p=1e-3
(d=21) vs 242 at 1e-4 (d=11) -> p-dial 3.64x; threshold-constant dial
1.82x; prefactor 1.2x; ACCOUNTING dial ~109x (same d=15 code, 49,000
full-machine vs 450 memory-only, from arXiv:2604.06319's own figures).
Resolvability threshold ~3.6x: TdG-vs-routing is NOT orderable from the
published record (sep ~1.25x). (4) The pre-registered kill condition FIRES:
no ordering changes; arc E closes as a negative result at full grade — the
decay is in transmission, not the papers' arithmetic. (5) Memory-vs-compute
quantified: ~432x vs ~8-12x. (6) The answer: megaquop-class milestone
defined; distribution NA 35 / SC 32 / ions 11 / photonics 8 / Si 7 /
engineered 7 (AI-drafted, author-override); bets B11 (~70%, 2027-12-31,
referee gap persists — includes ourselves), B12 (~55%, 2031-12-31,
megaquop clock), B13 (~35%, conditional platform = NA). Ledger prefix CA +
CB11-13 + CAN1; sentinel budgets raised for Ch8's sec 02 erratum
restatement (the deliberate-friction path, documented in place).

## Session 10 agenda — seal review and the next cycle
The planned arc is complete; what remains is author work and the next
scouting cycle. AUTHOR ITEMS OPEN: test-reader verdicts for Ch3-Ch8;
overrides for B5-B13 percentages and the Ch8 distribution; seal/DOI
decisions (Ch1 seals NON-DOI per standing doctrine; the author decides
which chapters are citable). NEXT CYCLE OWES: Cycle 2 scouting with >= 1
wildcard arc (standing requirement); arc A (the logic referee) is the
flagship successor now that arc E has closed — the OPEN-CAVEATED caveats
in CA2-CA6 close by exactly its referee work; PREREG-2 (decomposition arm)
deferred, not dead.

## Standing obligations
- Bets score: B3 2026-12-31; B1/B2/B4 2027-12-31; B11 2027-12-31; B5/B6
  2028-06-30; B7/B8/B10 2028-12-31; B9 2029-06-30; B12/B13 2031-12-31.
- Exhibit 0's absence claim (no 1,500-3,000 figure in arXiv:2509.18294)
  predates the SR-8 rule and should be re-confirmed by mechanical full-text
  search at the next verification pass.
- Residual cosmetics: dossier.source.html "(working title)"; Ch1 sec 05
  intro wording open to author revision; Ch4 sec 04 names Ch2/Ch3 laws
  inline (restated, not back-referenced; flagged for author review).

## Settled decisions — do not relitigate
- provenance.json "updated" is a UTC build stamp (matches
  auto-timestamp.yml); reading a day ahead of verification dates is correct
  ordering, not drift. Do not switch the renderer to local time.
- CT3 keeps CITE: evidentiary source, coverage-grade retrieval, corroborated
  twice, load carried by CT4/CT5.
- SR-8 rule (standing doctrine, enforced): absence claims need exhaustive
  search over the authoritative corpus (LaTeX/PDF); presence claims may use
  any reliable read.
- check_retracted.py uses per-file occurrence budgets, not an allowlist;
  budgets rise only with deliberate errata additions, in the same commit.
  .github is scanned; .git is not; SELF is two named files, never a glob.
