# ERRATUM SR-6 — TIMEKEEPING (recorded 2026-08-24)

**The error, owned by the Strategy Room.** Session 4's artifacts were drafted
with dates carried forward from the prior session's narrative instead of from
the clock. The real date, per system clock and git commit metadata, is
2026-08-24; the affected artifacts said 2026-07-19. In a dossier whose
doctrine is dated verification, a false verification date is a false label —
the same defect class this dossier documents in others (cf. Exhibit 0).

**Scope, established from git metadata (authoritative).** Sessions 1–3 are
CLEAN: every committed prose date (2026-07-14 landscape, 07-17 searches and
Chapters 1–2, 07-17..07-19 PREREG-1 chain through d55194a) matches its git
commit date. The false dates are confined to the three commits of 2026-08-24:
(1) CH3_DRAFT.md v1 — "verified on 2026-07-19" throughout, for verifications
actually performed 2026-08-24, and "five and a half months" remaining on bet
B3 where about four remain; corrected by CH3_DRAFT v2, v1 retained in
history. (2) SESSION_HANDOFF.md — "Session 4 (opened 2026-07-19)" is false;
Session 4 opened 2026-08-24. The Session 3 close date (2026-07-19) is
accurate per git; its closing commits landed late (2026-08-24), which the
git record shows honestly. (3) The results completion addendum's drafting
date (2026-07-19) is retained as the drafting session's date; its late
commit date is likewise visible in git.

**A second finding, recorded without softening.** When the render tooling
stamped provenance.json with the true date (2026-08-24), the discrepancy was
resolved the wrong way: the true stamp was reverted to preserve consistency
with the false dates. The executor surfaced the discrepancy — correctly —
but the standing rule is now explicit: **the record bends to the clock,
never the clock to the record.** The true stamp is restored and committed.

**Rule change (fix-forward).** Every session opens by establishing the real
date from the environment/git before any artifact is drafted; every prose
date derives from it. No date is ever copied forward from narrative context.
