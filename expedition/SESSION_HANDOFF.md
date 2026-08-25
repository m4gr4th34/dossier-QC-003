# QC003 — SESSION HANDOFF (refreshed at close of each session)

## Session 8 closed 2026-08-24
Chapter 7 (the engineered-qubit bets: topological + cat, the existence
drill) drafted, primary-verified, and integrated live. The serial's last
platform chapter, and the one the label discipline was built for. Headline:
the two platforms fail at opposite ends. Topological is disputed at the
foundation and clean at the payoff — its flagship parity result (Nature
638, 651-655, 2025) carries a peer-review-file editorial note saying the
results "do not represent evidence for the presence of Majorana zero modes
in the reported devices", the preprint's Majorana sentence was replaced in
the published abstract by a trivial-and-non-trivial interpretation clause,
and on 2026-06-24 Nature published a Matters Arising (Legg, 654 E22-E26)
and Microsoft's Reply (654 E27-E28) back to back. Cat is clean at the
foundation and disputed at the payoff — the exponential bit-flip
suppression is measured (Nat. Phys. 16, 509, 2020), reproduced at
ten-second scale (Nature 629, 778, 2024) and carried into a
below-threshold logical memory (Nature 638, 927, 2025), but that memory's
logical error improved by only about 1.06 across two code distances, while
every published costing (126,133 cat qubits, PRL 131, 040602) is an output
of an assumed loss ratio. Both sides of the topological dispute recorded at
equal prominence; neither adopted. Bets B9 (~20%, 2029-06-30: a
peer-reviewed topological QUBIT, not a parity lifetime) and B10 (~35%,
2028-12-31: measured logical-error improvement of at least 2x between two
code distances) deposited. Ledger prefixes CT / CC / CTN (no collisions).
Ch1's constraint choice for this pair - existence and extrapolation -
survived its chapter unchanged (elaborated, not corrected).

## Session 9, part 1, closed 2026-08-25 — the recost audited its own inputs first
Arc E's first act was to re-verify the six-multiplier table before recosting
it. It never reached the arithmetic. Two errata, both now logged and
corrected in place: **SR-7**, a false CITE that had reached the live edition
(the "20-40x space-time cost vs the previous best-in-class STAR
architecture" row; mechanical full-text and rendered-PDF search of
arXiv:2606.25011v1 finds neither figure nor baseline; actual headline is
~5.5x physical qubits vs a surface code STAR baseline) - the first dossier
error NOT caught at the pre-commit gate; and **SR-8**, SR-1 recurring five
weeks later about the same ~250x figure, the Strategy Room again judging it
unsupported on a converted-HTML read, the figure found present verbatim by
mechanical search, no manuscript change. SR-8's standing rule is now
doctrine: an absence claim requires exhaustive search over the authoritative
corpus (LaTeX source or rendered PDF); a presence claim may be established by
any reliable read. CM1/CM2/CM3 survive re-verification; CM5 and CM6 carried
precision defects (an inverted quantity and paraphrases inside quotation
marks) and are corrected. Exhibit 0's mundane explanation moved from
plausible to partially corroborated, which weakens this dossier's own
exhibit and is reported for that reason. Verified inputs for the ruler are
committed as expedition/RECOST_INPUTS.md.

## Session 9, part 1b — the lockstep hole, found and closed
Code's post-merge sweep found a stale copy of the SR-7 claim in
expedition/CH1_DRAFT.md, and a second in SCOUTING_LEDGER_ADDENDUM_1.md: the
retracted multiplier survived in working drafts because check_placeholders.py
scans publication surfaces only, and no gate covered drafts. The doctrine
already required lockstep; nothing enforced it. Both copies corrected in
place and marked, and a new gate closes the hole:
**verification/check_retracted.py** + **retracted_claims.json**, wired into CI
as check-retracted.yml, with tests in check_retracted.test.py. Design note
worth keeping: it uses per-file occurrence BUDGETS, not an allowlist, because
an allowlist over the manuscript would permit the false claim to be
re-introduced into the manuscript unnoticed — the exact failure being
guarded. Raising a budget is allowed only when deliberately adding to the
errata record, in the same commit. The gate is not gated on release state.

Follow-up: Code's post-merge review noted the sentinel skipped every
dot-directory, leaving .github outside a gate whose premise is "every file,
every stage". Closed — .github is now scanned explicitly (.git still is not),
with tests asserting both, and the blind spot demonstrated shut by planting
the retracted string in a workflow file.

## Session 9, part 2 agenda — Chapter 8: THE RECOST
The finale the author originally asked for, and a different shape from the
six platform drills. Re-express the field's headline multipliers (the six
CITE-verified claims in Ch1 sec 03) on ONE stated baseline with ONE stated
accounting; publish each claim's sensitivity to the choices its authors
made; register dated forecasts on which survive; and answer "which
platform" with dated numbers rather than vibes. Pre-registered kill
condition already promised in Ch1 sec 03: if no ordering changes by more
than its own stated uncertainty, that is published as a negative result at
full grade. Open by establishing the real date (SR-6 rule) before drafting.
Special care: this chapter makes a comparative claim, so the OPEN vs
OPEN-CAVEATED split will be load-bearing — a recost that holds only under a
stated accounting is OPEN-CAVEATED, not OPEN-UNVERIFIED. AUTHOR ITEMS STILL
OPEN: Ch3, Ch4, Ch5, Ch6 AND Ch7 test-reader verdicts, strikes if any;
B5-B10 overrides if the numbers misfit.

## Settled in Session 8 review — do not relitigate
- provenance.json "updated" is a BUILD stamp written in UTC by
  render_edition.js, matching auto-timestamp.yml's jq. It reading one day
  ahead of the chapter's "verified 2026-08-24" dates is correct ordering
  (verify, then publish), not drift. Do NOT switch the renderer to local
  time: CI and the local render would then write the same key from
  different clocks and flip it on every build.
- CT3 (the Nature peer-review-file quotation) keeps its CITE label. The
  source is evidentiary; only the retrieval route is coverage-grade. Direct
  retrieval was attempted 2026-08-25 and refused by the publisher's static
  host; the wording is corroborated by a second independent outlet; and no
  Chapter 7 claim rests on CT3 alone, because CT4/CT5 (the peer-reviewed
  Matters Arising and Reply) carry the same point.

## Standing obligations
- B3 scores 2026-12-31; B1/B2/B4 score 2027-12-31; B5/B6 score 2028-06-30;
  B7/B8/B10 score 2028-12-31; B9 scores 2029-06-30.
- Cycle 2 scouting owes >= 1 wildcard arc.
- Exhibit 0's absence claim (no 1,500-3,000 figure in arXiv:2509.18294)
  predates the SR-8 rule and should be re-confirmed by mechanical full-text
  search at the next verification pass.
- PREREG-2 (decomposition arm) deferred, not dead.
- Residual cosmetics: dossier.source.html "(working title)"; Ch1 sec 05
  intro wording open to author revision; Ch4 sec 04 opens by naming
  Chapter 2's and Chapter 3's laws inline — it restates them rather than
  requiring a lookup, so it is not a back-reference violation, but it is
  the closest the manuscript comes to one and is flagged for author review.
