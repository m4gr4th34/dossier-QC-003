# CHAPTER 8 — THE RECOST
## The field's six headline multipliers on one ruler, the ruler's own price tag, and an answer to "which platform"
### DRAFT v1 — every number below is verified against the named primary source on 2026-08-25, computed by the committed harness (expedition/recost_harness.py), or labeled.

Status legend: **CITE** = verified against the named primary source on
2026-08-25. **REPORTED** = interested-party or secondary source, recorded but
not adopted. **OPEN** = the author's own analytical claim. **OPEN-CAVEATED** =
established, but only under an explicitly stated restriction (here: the stated
error-suppression model); closing the caveat is bounded verification work.
**FORECAST** = a dated, falsifiable bet with a resolution mechanism.

This chapter is self-contained: nothing below requires reading any other
chapter.

---

## 01 · WHAT THIS CHAPTER IS

Chapter 1 of this dossier made one promise about its ending. The 2026
fault-tolerance literature's unit of progress is a **multiplier against a
baseline the authors chose themselves** — six headline claims, each honest by
its own lights, no two sharing a baseline, a cost model, a noise model, or a
decoder. The promise: re-express every one of them on ONE stated baseline
with ONE stated accounting, publish each claim's sensitivity to the choices
its authors made, and register dated forecasts on which survive — with a
pre-registered kill condition: *if no ordering changes by more than its own
stated uncertainty, that is reported as a negative result, at full grade.*

This chapter keeps that promise. It does not end the way the promise
imagined, and the difference is the finding.

The six claims, re-verified against primary sources on 2026-08-25 (each
full identity in the citation cards): a transversal STAR architecture
reporting **~250× time and 2× space savings** against "a fixed-connectivity,
fully fault-tolerant scheme" [CITE: PRX Quantum 7, 020343 (2026)]; a
heterogeneous NA/SC design reporting **752× speedup** over "NA-only
baselines" and **>10× fewer qubits** than "SC-only systems" [CITE:
arXiv:2601.10144]; a heterogeneous machine reporting **138× fewer physical
qubits** than its own fully-specified monolithic baseline [CITE:
arXiv:2604.06319]; a high-rate STAR reporting **~5.5× fewer physical
qubits** than "a surface code STAR baseline" at comparable speed [CITE:
arXiv:2606.25011v1]; Tour de Gross reporting **an order of magnitude larger
logical circuits** at a given physical-qubit count than "surface code
architectures" [CITE: arXiv:2506.03094]; and routing codes reporting **~8×
less physical-qubit overhead** than "surface codes achieving a same logical
error rate" [CITE: arXiv:2606.25330].

## 02 · THE AUDIT ATE ITS OWN INPUTS FIRST

A recost is only as good as its inputs, so the first act was re-verification
— and it did not survive contact with this dossier's own table. Two errata,
recorded in full in the scouting ledger and summarized here because this
chapter must carry its own history:

**SR-7.** This dossier's Chapter 1, its claim ledger, and its citation card
for the high-rate STAR paper all asserted a "20–40× space-time cost"
reduction against "the previous best-in-class STAR architecture."
Mechanical full-text search of the paper's LaTeX source and rendered PDF
finds **neither the figure nor that baseline anywhere**. The paper's actual
headline is the ~5.5× above. Unlike every prior erratum in this dossier's
ledger, this one was **not caught before sealing** — it was live, inside the
very paragraph arguing that unrechecked multipliers decay.

**SR-8.** While checking, this dossier concluded — for the second time, five
weeks after recording the identical mistake as erratum SR-1 — that the ~250×
figure was unsupported, on the strength of a converted-HTML read. Mechanical
search found it present verbatim, both halves in a single clause. Documenting
the first error did not prevent its recurrence; a mechanical gate did. The
rule that came out of it is now standing doctrine and machinery
(verification/check_retracted.py): **an absence claim requires exhaustive
search over the authoritative corpus; a presence claim may be established by
any reliable read.**

The verified inputs — every absolute figure the six papers actually state —
are committed as `expedition/RECOST_INPUTS.md`. Everything below reads from
that file and from the committed harness, `expedition/recost_harness.py`,
which a stranger can rerun (`--check` verifies the committed results
byte-for-byte).

## 03 · THE RULER — AND WHAT REFUSES TO FIT ON IT

Building the promised common baseline immediately produces the chapter's
first result: **the six claims measure at least four different quantities, at
four different physical error rates, across three different task classes**
[OPEN: classification, from the verified inputs].

The quantities: time-and-space savings (250×), speed against one baseline
and space against another (752× / >10×), full-machine physical-qubit count
(138×), task-level physical-qubit count (5.5×), circuit size at fixed qubits
(Tour de Gross), and memory-overhead at fixed logical error (8×). The
physical error rates: 10⁻³, 7×10⁻⁴, 5×10⁻⁴, and 10⁻⁴. The tasks: Hamiltonian
simulation, a 1,000-logical-qubit machine (and RSA-2048), and abstract
memory.

A quantity cannot be ordered against a different quantity by any recosting.
So the honest ruler is narrower than the promise imagined: **one axis —
physical qubits per logical qubit at a fixed logical error target — onto
which three of the claims can be placed natively, plus explicit bridges,
each carrying a stated assumption, for the rest.** The suppression model
used for normalization, stated once: logical error = A·(p/p_th)^((d+1)/2),
with A = 0.1 and p_th = 10⁻² as defaults, both varied in §05. Every number
downstream of this model is **OPEN-CAVEATED**: true under the stated model;
closing the caveat is per-code circuit-level simulation — bounded work, and
exactly the referee work this dossier's flagship arc exists to do.

## 04 · THE RECOST — THE ONE AXIS THAT EXISTS

At a logical error target of 10⁻¹² per logical qubit per round, at p = 10⁻³,
memory scope, under the stated model [all OPEN-CAVEATED, computed by the
committed harness]:

| Architecture | Physical qubits per logical qubit |
|---|---|
| Surface code (d = 21 required) | **882** |
| Routing codes, via their own ~8× at equal logical error | **~110** |
| Rate-½ qLDPC memory (the 2026 landmark, simulation) | **~2** |

Two of the six claims are deliberately *not* in this table, and the reasons
are findings. Tour de Gross's own figures (288 physical for 12 logical) sit
at its own distance 12, which does not reach the 10⁻¹² target, and the
published record gives no scaling to that target — placing 24 next to
at-target numbers would manufacture exactly the mixed-conditions comparison
this audit exists to expose. The STAR papers' figures cost *a task*, not a
logical qubit; they enter §05's bridges instead.

The pairwise verdicts [OPEN-CAVEATED, harness]:

- **Surface vs routing codes (8×): RESOLVABLE** — but the margin over the
  normalization sensitivity is only ~2.2×.
- **Surface vs Tour de Gross (10×): RESOLVABLE on the paper's own
  circuit-size axis**; not transferable to the qubit-overhead axis without a
  cost-linearity assumption the paper does not state.
- **Tour de Gross vs routing codes: NOT RESOLVABLE.** Different axes; under
  the unstated linearity bridge their separation is ~1.25×, far inside the
  ~3.6× sensitivity. The published record cannot order these two.
- **Rate-½ qLDPC memory vs everything: RESOLVABLE, robustly** — two orders
  of magnitude of margin.
- **The cross-axis claims (250×, 752×, 138×, 5.5×): UNDEFINED against each
  other.** Not uncertain — undefined. They are different experiments.

## 05 · THE DIALS — WHAT AN AUTHOR'S CHOICE IS WORTH

The recost's second product is the price tag on each assumption, computed by
varying it across its defensible range [OPEN-CAVEATED, harness]:

| Dial | Factor | Meaning |
|---|---|---|
| Physical error rate (10⁻³ vs 10⁻⁴) | **3.6×** | the identical surface code at the identical target costs 882 vs 242 per logical qubit (d = 21 vs 11) |
| Threshold constant (0.5% vs 1%) | **1.8×** | a modeling choice inside one paper's appendix |
| Suppression prefactor (0.03 vs 0.3) | **1.2×** | nearly free |
| **Accounting scope** (full computation vs memory-only) | **~109×** | the SAME d = 15 surface code costs ~49,000 per logical in the 138× paper's own full-machine baseline, and 450 memory-only [CITE-derived arithmetic on arXiv:2604.06319's stated figures] |

Read the table bottom-up. The accounting-scope dial is **larger than every
audited multiplier except the 250×**. What a paper counts — factories,
routing, ancillas, or bare memory — moves "physical qubits per logical
qubit" by two orders of magnitude before any architecture is compared at
all. And the p-normalization dial, 3.6×, sets the **resolvability
threshold**: any two claims made at different physical error rates and
separated by less than roughly 4× cannot be ordered from the published
record, full stop [OPEN-CAVEATED].

## 06 · THE KILL CONDITION FIRES

Pre-registered in the scouting ledger before this work began: *if no
headline multiplier's ordering changes by more than its own stated
uncertainty under the common baseline, arc E is reported as a negative
result and closed.* Verdict: **it fires** [OPEN].

On the one axis where orderings exist, none changed. The qLDPC families
beat the surface code by roughly their stated factors under every dial
setting; the rate-½ memory result beats everything, robustly. The orderings
this audit might have overturned turned out mostly not to exist at all —
cross-axis, they are undefined rather than wrong. That is the negative
result, reported at full grade: **the field's headline multipliers, where
they are comparable at all, are mutually consistent.** The decay this
dossier documented is real, but it lives in *transmission* — coverage
attaching figures to the wrong papers, ledgers (including this dossier's
own) attaching baselines to the wrong claims — not in the papers'
arithmetic.

What survives the arc's closure stands on its own: two errata (SR-7, SR-8)
and a doctrine rule now enforced by machinery; the accounting-scope factor
(~109×); the resolvability threshold (~3.6×); and one pairwise ordering the
field might have assumed and cannot have (Tour de Gross vs routing codes).

## 07 · THE RACE ON THE CORRECTED BOARD

The recost's last number is the dossier's thesis made quantitative. On the
memory axis, the span from the surface code to the rate-½ qLDPC landmark is
**~432×** — a verified-simulation win of two orders of magnitude, sitting on
the shelf. On the compute-inclusive axis, every claim on the shared ruler
compresses to **~8–12×**. The memory-to-compute gap is not a slogan;
at the current published record it is the difference between 432× and 10×
[OPEN-CAVEATED: both ends under the stated model and scopes].

Where that leaves each platform, in one verdict line each, composed from
this dossier's seven drills [OPEN: author-reviewed synthesis; each chapter's
full evidence stands behind its line]:

- **Neutral atoms** hold the widest verified storage win and the widest
  compute gap — the 432× lives here, and so does the burden of B1.
- **Superconducting** compounds fastest below threshold (Λ = 2.14 per
  distance step, real-time decoding demonstrated) and pays the most per
  qubit in wiring and refrigeration.
- **Trapped ions** hold the fidelity records and a wall-clock budget that is
  ~98% refrigeration and transport.
- **Photonics** is winning its component war industrially and has not yet
  put a logical qubit below threshold.
- **Silicon spin** has the field's best factory and its smallest arrays.
- **Engineered qubits** are one decisive experiment (topological) and one
  demonstrated-but-thin exponent (cat) away from mattering to this table.

## 08 · THE ANSWER — AND THE BETS THAT MAKE IT FALSIFIABLE

"Which platform reaches fault-tolerant, useful-scale quantum computing
first?" This dossier answers the way it has insisted the field should: as a
dated probability distribution with a mechanical resolution, not a
narrative. Milestone, defined for resolution: **the first public hardware
demonstration of a megaquop-class computation — at least 10⁶ error-corrected
logical operations on at least 50 logical qubits, with measured logical
error rates reported.**

The distribution [FORECAST-type content; AI-drafted percentages,
author-delegated 2026-07-17, the author may override any number; conditional
on the milestone being reached by 2031-12-31]: **neutral atoms ~35%,
superconducting ~32%, trapped ions ~11%, photonics ~8%, silicon spin ~7%,
engineered qubits ~7%.**

**B11 — The referee gap persists.** *By 2027-12-31, no peer-reviewed
publication or artifact-committed preprint (by any group, this dossier's
lineage included) places at least four of the six claims audited here on a
single stated baseline with a single stated accounting.* Resolves TRUE if
none exists on the date; a documented search is the mechanism. Probability:
**~70%**. Rationale: the one team that tried stopped at the wall and said so
[CITE: arXiv:2508.14011 §4.7]; the work remains career-unrewarded; and this
chapter is itself evidence of how much of the task is un-liftable — but the
dossier's own flagship arc is aimed at exactly this, which is why the bet
explicitly includes ourselves.

**B12 — The megaquop clock.** *By 2031-12-31, at least one platform publicly
demonstrates a megaquop-class computation as defined above.* Probability:
**~55%**. Rationale: the transversal STAR costing puts the hardware bill
near 10,000 physical qubits at 10⁻³ [CITE: PRX Quantum 7, 020343 (2026)] —
inside announced 2027–29 roadmaps — while every platform chapter of this
dossier verified that the composing experiment is always the hard part.

**B13 — The platform.** *Conditional on B12 resolving TRUE: the platform is
neutral atoms.* Probability: **~35%**. Rationale: the storage win and the
reconfigurability that the megaquop-scale costings themselves lean on are
both native here; the strongest argument against is superconducting's
demonstrated below-threshold compounding and industrial decoding stack.

## 09 · METHOD NOTE

Every input figure was re-verified against its primary source on 2026-08-25
under the SR-8 rule (absence claims by mechanical search of the
authoritative corpus only). All derived numbers come from the committed,
deterministic, stdlib-only harness `expedition/recost_harness.py`, whose
committed output `recost_results.json` must match a rerun byte-for-byte —
enforced by `recost_harness.test.py` in the repository's test suite. One
harness defect is on the record in the spirit of this dossier's errata: a
floating-point boundary in the distance calculation inflated d = 21 to 23 at
p = 10⁻³ and was caught pre-commit by the test's independently hand-derived
spot checks; the fix went into the harness, never the test. The suppression
model and its constants are stated in §03 and priced in §05; every number
that depends on them is labeled OPEN-CAVEATED, and the caveat closes by
per-code circuit-level simulation — the referee work this dossier's flagship
arc exists to do. The kill condition was pre-registered before the audit
began and its firing is reported at full grade. Created with heavy AI use,
and limited human oversight, to test the capabilities of contemporary
state-of-the-art AI.

*This closes the dossier's planned arc: seven drills, one recost, thirteen
live bets, every label true. The bets score on their dates whether anyone is
watching or not.*
