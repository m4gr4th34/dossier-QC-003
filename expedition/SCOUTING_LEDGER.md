# QC003 — SCOUTING LEDGER

**Append-only.** Rows are never edited or deleted. A row that is later revised is
superseded by a new, dated addendum row appended at the foot of its cycle. A kill
is a finding, not a failure: the reason is the product.

Axes, scored per arc (from CLAUDE.md, Standing context):
1. **BREAK** — breakthrough-shaped: a win changes what others DO, not a number.
2. **EDGE** — edge-fit: computation/reasoning-heavy, no lab, exploits the two-agent
   loop and the -002 machinery.
3. **UNDER** — underpriced-why: a NAMED reason the crowd is absent, verified by
   search. "Nobody thought of it" is not a reason.
4. **VERIF** — mechanically verifiable: a stranger rechecks by rerunning committed
   artifacts.
5. **PULL** — AUTHOR-ONLY axis. The Strategy Room never infers it. Recorded as
   `AUTHOR` until the author scores it in a dated addendum row.

Verdicts: `SURVIVE` · `MERGE` (folded into another arc; not run standalone) · `KILL`.

Lineage: dossier-QC-Accelerate-002, concluded at Chapter 5, v5.0.0,
DOI 10.5281/zenodo.21360979 (concept DOI 10.5281/zenodo.21270186). Cited as prior
work throughout; not re-litigated.

---

## CYCLE 1 — searches run 2026-07-17 (Strategy Room, autonomous triage)

Seed portfolio from expedition/QC003_FOUNDING_HANDOFF.md §6 (arcs A–D + the
standing wildcards lane E). This cycle extends it to 12 scored arcs. Wildcard-lane
arcs are marked `[W]`.

### Standing corrections to the handoff's landscape (verified 2026-07-17)

The handoff's landscape was verified 2026-07-14. Re-verification on use found two
load-bearing statements that are now false or were never true. Both are recorded
here as first-class self-catches before any arc leans on them.

**COR-1 — "QuEra 2:1 memory *demonstrated*" is false; it is *simulated*.**
CLAUDE.md's Standing context says "2:1 memory demonstrated." The primary source
does not support "demonstrated." Zhao, Duckering, Gu, Maskara, Zhou (QuEra /
Harvard / MIT), "Towards Ultra-High-Rate Quantum Error Correction with
Reconfigurable Atom Arrays" (preprint, April 2026) reports circuit-level noise
*simulations* reaching ~1.3e-13 per-logical per-round at p=0.1%, on codes built
from Kasai's (2026) non-commuting affine permutation matrices. QuEra's own blog
states the team "directly verify in simulation"; QuEra's CCO, quoted in Network
World (2026-04-30), states the paper does not show that operations can be done on
the qubit. The handoff's own "(memory baseline only)" caveat is correct and
survives; the word "demonstrated" does not. **Correct label: a simulation result,
not a hardware demonstration.** Every QC003 use says "simulated."

**COR-2 — "AlphaQubit is too slow for live correction" is superseded.**
The handoff (and CLAUDE.md L3) states AlphaQubit is accuracy-leading but too slow
for live correction, with 2025–26 productionization claims REPORTED-only. The
accuracy claim (Nature 636, 2024, arXiv-adjacent; 6% fewer errors than tensor
networks, 30% fewer than correlated matching on Sycamore d=3/5) remains CITE. The
speed claim is superseded by **AlphaQubit 2**, arXiv:2512.07737, "A scalable and
real-time neural decoder for topological quantum codes": real-time decoding faster
than 1 µs per cycle on commercial accelerators, surface code to d=11 with better
accuracy than leading real-time decoders, and first real-time decoding of the color
code to d=9. **Scope guard:** AlphaQubit 2's claims are for *topological* codes
(surface, color). It is NOT a high-rate qLDPC decoder. The qLDPC real-time gap the
handoff describes therefore stands — but the blanket "ML decoders are too slow"
line does not, and QC003 must not repeat it.
**CITE/REPORTED split, enforced:** arXiv:2512.07737's specific bounded claims are
CITE. Claims that AlphaQubit "solved the decoding problem," that ASIC-controller
integration "silenced" the latency objection, or that the threshold theorem is
practically validated (FinancialContent / ETFOptimize / StreetInsider syndicated
copy, 2026-01-01) are REPORTED — NON-SCIENTIFIC SOURCE, UNCORROBORATED. Mundane
explanation, stated with equal prominence: these are syndicated automated
stock-market content pages with no methodology, no data, and no author
accountability; the specific engineering assertions in them appear in no primary
source located on 2026-07-17.

**COR-3 — Layer 1 is not "done."** The handoff calls codes "solved and
industrializing (crowded, done)." Verified 2026-07-17: the hardware-tailored code
family space is *accelerating*, not closing. In June 2026 alone: routing codes
(arXiv:2606.25330), high-rate qLDPC on a planar grid (arXiv:2606.19482), Vine codes
(arXiv:2606.20263), Barbell codes (arXiv:2606.06062), Hierarchical Logical
Processor with shuttle buses (arXiv:2606.22594); July: tile codes
(arXiv:2607.05897). The correct statement is not "done" but **"crowded, and each
new family ships its own incomparable circuit-level claim."** That distinction is
what arc E is built on. Recorded, not asserted as an arc kill.

### Strategy Room errata — caught pre-commit, before any byte was sealed

The corrections above are to the inherited landscape. These five are to **this
ledger's own first draft**, caught during the pre-commit diff gate: three by the
Strategy Room red-teaming itself, two by the executor's primary-source fetches. The
draft was written from abstracts and search snippets; the errata are what full text
found. They are recorded here rather than quietly fixed, per the lineage's practice
that self-catches are first-class findings — and because a ledger whose founding
thesis is "claims decay when nobody rechecks them" has no standing to hide its own.

- **SR-1 — the Strategy Room accused itself, wrongly, of laundering the 250x.**
  The draft cited "250x execution speedup" for transversal STAR. On review the
  Strategy Room could not recall seeing 250x in the paper, concluded it had been
  lifted from QuEra's press release, and asserted — with some force — that the row
  was a REPORTED figure mislabelled CITE. **That accusation was false.** Full-text
  fetch: the number is in the paper, once, in the results: surface-code-based
  transversal STAR architectures achieve ~250x time savings and 2x space savings
  over a fixed-connectivity, fully fault-tolerant scheme. The claim was CITE-grade
  all along and was hedged into REPORTED on the strength of a memory rather than a
  fetch. **This is the mirror-image doctrine violation and it is the more insidious
  one:** the constitution says every label must be true in *both* directions —
  never assert a scouted thesis as settled, and never soft-pedal a verified fact
  into a hedge. Over-caution reads as rigor and is not. The residual defect is real
  but small: "execution speedup" compresses "time savings versus a fixed-
  connectivity, fully fault-tolerant scheme," which is now stated exactly in arc E.
- **SR-2 — a publication date typed as CITE was REPORTED.** The draft said
  "published PRX Quantum 2026-06-01." The volume, article number, and year are
  primary-confirmable from the arXiv journal-ref (**PRX Quantum 7, 020343 (2026)**)
  and now stand. The **exact day came from QuEra's press release**; the APS record
  returned HTTP 403 and no secondary source was substituted. The day is dropped
  rather than sourced to an interested party over a paywall.
- **SR-3 — Lean-QEC's "144 qubits" spanned the kernel boundary.** See arc I.
- **SR-4 — FTCircuitBench's metrics came from an aggregator.** See arc A.
- **SR-5 — arc E's first campaign rested on a premise that was false for its first
  target.** The draft's "unmodeled-term audit" assumed the multipliers might omit
  atom loss. Transversal STAR prices atom loss explicitly (as an effective Pauli-Y
  channel). The campaign is re-specified in arc E around model *fidelity* rather
  than model *presence* — a sharper question that survives contact with the paper.

**What this episode is.** Four of the five errata are the arc E pathology committed
by arc E's own author: a multiplier repeated without recosting, a date propagated
from a press release, a scaling figure quoted past its stated scope, a metric
inherited from a summary of a summary. The fifth (SR-1) is the opposite failure —
mislabelling a verified fact as unverified. Every one was settled the same way: by
fetching the primary source and reading the sentence. Nothing else worked; not
memory, not the abstract, not the search snippet, and not the Strategy Room's
confidence in either direction. That is the arc's argument, and the ledger now
carries the demonstration in its own errata rather than only the assertion in its
thesis.

---

### ARC A — THE LOGIC REFEREE (gadget-level) · **SURVIVE**

*Thesis.* Build the frozen, gated, hardware-calibrated circuit-level referee for
logical *operations* (not memory) on high-rate codes under neutral-atom noise
(shuttling, atom loss, leakage, 2:1-era codes); produce the first certified
gate-level operating-point truths; then arm the -002 search loop on the
gadget/schedule space against it.

- **BREAK — HIGH.** A certified operating-point leaderboard of logical operations
  becomes the thing others must cite or beat. Ceiling: "AI discovers a measurably
  better way to COMPUTE on qLDPC codes."
- **EDGE — HIGH.** Pure simulation. Directly reuses -002's apparatus one level up.
- **UNDER — VERIFIED, NARROWED (2026-07-17).** Named reason: referee work is
  career-unrewarded and falls between theory and hardware. The absence is real but
  **narrower than the handoff claims**, and the boundary must be stated:
  - *Occupied — compilation-level benchmarking.* FTCircuitBench (Harkness et al.,
    arXiv:2601.03185, 6 Jan 2026, open-sourced) benchmarks FT *compilation*, with
    pre-compiled instances in the Clifford+T and Pauli-Based Computation models.
    **It counts resources; it does not simulate logical failure at circuit level.**
    That second sentence is the load-bearing one and it rests on the abstract
    alone. (Erratum SR-4, caught pre-commit: an earlier draft additionally
    attributed "T-count, modularity" to this paper as its headline metrics. That
    came from an aggregator summary, not from the abstract. The characterization
    was probably fair; it is cut rather than defended, because the row does not
    need it and a decoration sourced to an aggregator has no business wearing a
    primary citation.)
  - *Occupied — cross-code MEMORY benchmarking.* QUITS (arXiv:2504.02673, accepted
    in Quantum 2025-12-01) simulates various qLDPC codes under standard
    circuit-level depolarizing noise with sliding-window BP-OSD. ECCentric
    (arXiv:2511.01062) does cross-code decoder comparison under SI1000. Memory is
    taken.
  - *Open — circuit-level GADGET grading on a common ruler.* No leaderboard grades
    surgery / transversal / adapters / extractors / dimension-jump gadgets on ONE
    stated noise model with ONE stated decoder at ONE stated operating point.
  - *Positive evidence the gap is real and load-bearing:* Harkness/Kan/Xu et al.,
    "Transversal Fault Tolerant Distributed Quantum Computing Operations"
    (arXiv:2504.05611), Supplementary Note 6: their headline finds transversal
    compute an order of magnitude below distributed lattice surgery in LER — but
    the lattice-surgery estimate used MWPM, and under the Tesseract decoder
    lattice surgery's M_ZZ approaches transversal. Their own words: adjusting for
    decoder differences, neither method has a conclusive LER advantage. **The
    verdict flips on the decoder, and that fact lives in a supplementary note.**
    This is -002's code-decoder interaction finding, rediscovered at gadget level
    by another group, and not promoted to a headline.
- **VERIF — HIGH.** Frozen referee + committed circuits + committed decoder configs.
- **PULL — AUTHOR.**
- *Cost honesty:* -002 certified that honest grading runs ~100x the field-standard
  budget. This arc pays that before it produces its first truth. That is why arc E
  is ranked ahead of it.

### ARC B — Trapping-set-aware decoder co-design · **KILL**

**Kill (standing bar — coefficient-polishing against funded incumbents):** the
mechanism -002 dissected is already productized — IBM Relay-BP damps the symmetric
trapping sets by construction (disordered memory strengths; ~10x accuracy over
BP+OSD, FPGA-targeted, Kookaburra hardware testing slated 2026) — and the
real-time frontier moved again on 2025-12 with AlphaQubit 2 (arXiv:2512.07737,
<1 µs/cycle, surface d=11, color d=9); the honest ceiling here is a better
coefficient on IBM's, Google's or NVIDIA's decoder, which is not this dossier's lane.
(Scores: BREAK LOW-MED · EDGE HIGH · UNDER WEAK · VERIF HIGH · PULL AUTHOR.)

### ARC C — Hybrid-architecture honest grading · **KILL**

**Kill (crowded; the handoff's own "may crowd fast" prediction resolved against it
inside six months):** the hybrid NA-memory/SC-compute design space now carries at
least three competing evaluations — arXiv:2601.10144 (MagicAcc / MCSep, 752x
speedup over NA-only on an end-to-end cost model), arXiv:2604.06319 (138x physical
qubit reduction "under detailed accounting"), and arXiv:2604.19735 §4.3, which
already compares three hybrid policies (H1/H2/H3, incl. one inspired by HetEC) and
concludes hybrid architectures are suboptimal in spacetime — so re-grading hybrids
as a standalone arc means arriving fourth to a comparison others are already
running. **Live residue folded into arc E:** the multipliers those papers report
are mutually incomparable, and nobody has said so.
(Scores: BREAK MED · EDGE HIGH · UNDER KILLED-BY-SEARCH · VERIF HIGH · PULL AUTHOR.)

### ARC D — The forecast engine · **SURVIVE (compounding only)**

*Thesis.* Industrialize -002's forward-bet ledger: regular batches of registered,
dated, mechanically-resolving predictions about which codes / gadgets / decoders /
multipliers win at stated operating points, each backed by a scouting simulation.
Breakthrough as a BODY of work.

- **BREAK — MED-HIGH as a body; LOW as a single result.**
- **EDGE — HIGH.** -002 already runs three live bets scoring at 2026-08-15,
  2026-08-31, 2026-12-31.
- **UNDER — VERIFIED (named).** No dated, falsifiable, mechanically-resolving
  public forecast ledger for FTQC architecture claims was located on 2026-07-17.
  The named reason is not obscurity: it is that being publicly, checkably wrong is
  career-negative, and no institution's incentives pay for it. Vendor roadmaps are
  the field's substitute and are REPORTED-grade by construction — interested
  parties, no resolution mechanism, no scoring when missed.
- **VERIF — HIGH.** The resolution mechanism IS the verifier.
- **PULL — AUTHOR.**
- **Constraint, stated plainly:** D has no substrate of its own. A forecast engine
  with nothing to forecast about is an opinion generator. It must ride A or E.
  Forecast *percentages* are author authority; the Strategy Room drafts the
  signpost and the resolution mechanism, never the number.

### ARC E — THE MULTIPLIER AUDIT / BASELINE LEDGER · **SURVIVE** *(new this cycle)*

*Thesis.* The 2026 fault-tolerance literature's unit of claim is a **multiplier
against a self-chosen baseline**. The multipliers below were located 2026-07-17;
the first was verified against **full text**, the rest against abstracts and are
labelled accordingly. **Each states a different baseline. No two are comparable,
and no paper claims they are.**

| Multiplier | Of what | Against which baseline (the paper's own words) | Source grade |
|---|---|---|---|
| ~250x time savings + 2x space savings | time (and space) | "a fixed-connectivity, fully fault-tolerant scheme" | **CITE, full text verified** — transversal STAR, arXiv:2509.18294, journal-ref PRX Quantum **7, 020343 (2026)** |
| 752x speedup; >10x footprint | end-to-end runtime; qubit count | "NA-only baselines" (speedup); "SC-only systems" (footprint) — two different baselines in one abstract | CITE, abstract verified — arXiv:2601.10144 |
| 138x | physical qubit requirement | "under detailed accounting" | CITE, abstract only — arXiv:2604.06319 |
| 20–40x | space-time cost (qubits x cycles) | "the previous best-in-class STAR architecture" | CITE, abstract only — arXiv:2606.25011 |
| ~10x | qubit efficiency | "equivalent surface-code architectures" | CITE, abstract only — Tour de Gross, arXiv:2506.03094 |
| ~8x | overhead | surface code "at equal logical error" | CITE, abstract only — routing codes, arXiv:2606.25330 |

Build a frozen recosting harness: re-express each headline multiplier on ONE stated
baseline with ONE stated accounting, publish the deltas and each multiplier's
sensitivity to the choices its authors made, and register dated forecasts on which
survive recosting.

**Exhibit 0 — the arc's own founding datum, verified 2026-07-17.** The transversal
STAR paper states ~10,000 physical qubits at p=1e-3 as the resource figure for its
headline regime. It contains **no ~1,500 or 1,500–3,000 physical-qubit figure at
all**: full-text search finds "1500" only inside a cited article number and "3,000"
only in the title of cited ref [42]. Yet secondary trade coverage of the June 2026
announcement reports the architecture reaching "roughly 1,500 to 3,000 qubits."
That figure does not exist in the primary source it is attributed to. A plausible
mundane explanation, stated with equal prominence and **not verified**: the coverage
may have conflated this paper with the separate high-rate STAR paper
(arXiv:2606.25011), which integrates high-rate codes and is a different result with
different conditions. Either way, the observable holds: **a resource figure is in
public circulation attached to a paper that does not contain it.** That is the arc's
thesis, found before the arc opened, in the first claim it looked at.

- **BREAK — HIGH.** This is not a number; it is a ruler. If the ordering re-orders
  under a common baseline, every subsequent architecture paper has to recost — they
  cite your baseline or explain why not. That is the definition of changing what
  others do. If nothing re-orders, that is a certified, citable negative result
  that retires a live worry — publishable at full grade under this dossier's
  doctrine, and unpublishable under anyone else's.
- **EDGE — HIGH.** Recosting is reading published cost models and re-running their
  arithmetic under stated substitutions. It needs no new referee to start, no lab,
  and no 100x grading budget for its first product. It is the cheapest citable
  artifact in the portfolio.
- **UNDER — VERIFIED, with direct documentary evidence (2026-07-17).**
  Named reason (two-part): (a) *career-negative* — recosting someone else's
  headline earns no novelty credit and makes enemies of the people who would
  review you; (b) *between fields* — the multipliers are produced by the computer
  architecture community, consumed by the QEC theory community, and audited by
  neither. Evidence, in the literature's own voice:
  - "Brace for impact: ECDLP challenges for quantum cryptanalysis"
    (arXiv:2508.14011) §4.7 builds a figure putting resource estimates on a common
    physical-qubit scale — and **explicitly refuses to merge** the 2026 Pinnacle
    RSA-2048 estimate into that series "because it is a native QLDPC architecture
    result rather than a recosting under this common 2D model." Practitioners hit
    the incomparability wall, named it, and declined the comparison. Nobody did the
    recosting.
  - The genre is proven **one field over and never aimed here**: "Auditing
    Empirical Comparisons in Quantum Software" (arXiv:2607.00516, July 2026) argues
    that in quantum software engineering "A beats B" is a property of the stack —
    benchmark scope, compilation, backend/noise assumptions, seeds, budgets — not
    of the technique. It audits compilers and optimizers. It has never been pointed
    at fault-tolerant architecture cost models.
  - Confirming instance inside the target layer: arXiv:2504.05611 Supp. Note 6 (see
    arc A) — swap the decoder, flip the winner.
- **VERIF — HIGH.** Recosting is a committed script over published parameters. A
  stranger reruns it and gets the same table or a bug report.
- **PULL — AUTHOR.**
- **First campaign, pre-specified (the sharpest single cut — folds in arc M):**
  *the noise-model fidelity audit.* An earlier draft of this row framed the cut as
  an "unmodeled-term audit" — does the cost model price atom loss, leakage, and
  shuttling heating, or omit them? Full-text verification of the first target
  falsified that framing before it was committed, and the corrected framing is
  better. For transversal STAR (arXiv:2509.18294), verified in full text:
  - **atom loss IS priced** — modeled as an effective Pauli-Y channel during both
    Rydberg gates and transport (`p_CZ,loss`, `p_move,loss`), validated against the
    explicit-loss simulations of its ref [58];
  - **leakage is absent** — the word appears zero times in the paper;
  - **shuttling time is priced** (folded into the clock cycle); **shuttling-induced
    heating is not priced as a cost term** — it is argued away, the scheme claimed
    to "strongly mitigate" degradation from accumulated heating and remove the need
    for recooling.
  So the question is not presence but **fidelity**: atom loss is a heralded/erasure-
  like event, and pricing it as an unheralded Pauli-Y is a substantive modeling
  choice that is neither the optimistic reading (erasure, whose location is known
  and which decoders exploit) nor the pessimistic one. The campaign therefore asks,
  per claim: **what is the noise model's loss/leakage treatment, is it conservative
  or optimistic relative to the platform's actual physics, and how far does the
  multiplier move when the treatment is varied across the defensible range?**
  Checkable, bounded, lands as a table. It is also strictly harder to dismiss than
  the omission framing, because it does not accuse anyone of forgetting anything.
- **Standing risk, named:** if recosting only nudges coefficients and re-orders
  nothing, the arc's ceiling collapses to bookkeeping. The pre-registered kill
  condition is therefore in the prereg, not discovered later: **if no headline
  multiplier's ordering changes by more than its own stated uncertainty under the
  common baseline, arc E is reported as a negative result and closed.**

### ARC F — Decoder-confound census · **MERGE (into A and E)**

*Thesis.* Quantify how often a published gadget/architecture comparison's winner
flips under a decoder swap.
**Merge, not kill:** the phenomenon is verified (arXiv:2504.05611 Supp. Note 6;
-002's decoder-created failure share spanning 8.5–63% is the same interaction at
memory level), the edge-fit is high, and the verifiability is high — but its honest
standalone ceiling is a component measurement, and it is the natural *mechanism*
section inside A and the natural *sensitivity axis* inside E. Run it there; do not
spend a chapter on it alone.
(Scores: BREAK MED-HIGH in situ / LOW standalone · EDGE HIGH · UNDER MED · VERIF
HIGH · PULL AUTHOR.)

### ARC G — Cross-family memory re-grading (the code zoo) · **KILL**

**Kill (instrument already built and published; ceiling is coefficient-polishing):**
the June-2026 code explosion (routing 2606.25330, planar-grid high-rate 2606.19482,
Vine 2606.20263, Barbell 2606.06062, HLP 2606.22594, tile 2607.05897, Kasai/QuEra
affine-permutation ultra-high-rate) is tempting, but cross-code circuit-level
*memory* benchmarking is exactly what QUITS (arXiv:2504.02673, accepted in Quantum
2025-12-01) and ECCentric (arXiv:2511.01062) already do — re-running memory curves
against a solved instrument would restage -002's own turf one code family over and
produce a better coefficient, not a ruler.
(Scores: BREAK LOW · EDGE HIGH · UNDER KILLED-BY-SEARCH · VERIF HIGH · PULL AUTHOR.)

### ARC H — Magic-state / non-Clifford supply-chain grading · **KILL**

**Kill (elite swarm; top-venue saturation):** magic state cultivation went from one
2024 paper (Gidney/Shutty/Jones, arXiv:2409.17595) to a crowded field with multiple
2026 PRX Quantum papers (Vaknin et al., PRX Quantum 7, 010353 (2026); Chen/Chen/Lu/
Pan, PRX Quantum 7, 010315 (2026); zero-level distillation, PRX Quantum 6, 020356
(2025)) plus fold-transversal cultivation (arXiv:2509.05212, Yale), two-qubit-gate
cultivation (arXiv:2509.05232), lattice-surgery cultivation (arXiv:2510.24615),
in-situ injection on arbitrary CSS qLDPC codes (arXiv:2604.05126), and a dedicated
simulator (QuEra's tsim, arXiv:2604.01059) — a solo loop entering this adds a
variant to a zoo of variants.
(Scores: BREAK MED · EDGE MED · UNDER KILLED-BY-SEARCH · VERIF HIGH · PULL AUTHOR.)

### ARC I [W] — Lean-verified fault tolerance · **KILL**

**Kill (racing two funded groups into their announced next step):** Lean-QEC
(arXiv:2605.16523, May 2026) is the first Lean 4 stabilizer-code formalization
delivering machine-checked distance certificates via a verified SAT reduction, and
its own text states the library is "designed to plug into broader Lean-based efforts
toward end-to-end verification of fault-tolerant quantum computation" — **our arc is
verbatim their announced roadmap** — while Lean-QIT (arXiv:2607.09632, ~2026-07-09,
QudeLeap/HKUST/HKU) builds the QIT layer underneath it. Entering means racing two
funded groups into work they have already scoped.

**Erratum SR-3, caught pre-commit — the lane is LESS closed than this row first
claimed, and the kill is restated on grounds that survive it.** An earlier draft
said "distance certificates for BB/GB codes up to 144 qubits." That mirrors the
paper's abstract but silently spans a boundary the paper itself is careful about.
Full text, verified 2026-07-17: the [[144,12,12]] Gross code scales "outside the
Lean kernel" only — a resource envelope, not a kernel-replayed certificate. The
**in-kernel machine-checked ceiling is the [[90,8,10]] BB code**, with [[70,6,9]]
also certified; the authors state kernel replay "has gone through smoothly through
the [[90,8,10]] BB code" and expect LRAT replay to become the next bottleneck beyond
it. Further: "Generalized Bicycle" is named as an in-scope family, but no concrete
GB instance carries a certificate in the text — every verified instance is a BB
code. Outside-the-kernel is precisely the trust gap Lean-QEC exists to close, so
quoting 144 as machine-checked inverts the paper's own point.
**Does the kill survive the correction? Yes, but on narrower grounds.** It no longer
rests on "the lane is finished" — it isn't; the in-kernel frontier is 90 qubits and
the FT-gadget layer is untouched. It rests on the roadmap quote and on EDGE: a solo
loop's comparative advantage is circuit-level measurement, not Lean kernel
engineering, and the incumbents hold both the tooling and the announced scope. If a
later cycle revisits this, revisit it on that basis and not on a false "closed."
(Scores: BREAK HIGH-if-won · EDGE MED-LOW · UNDER MED, not KILLED-BY-SEARCH ·
VERIF EXTREME · PULL AUTHOR.)

### ARC J [W] — AI-for-science reproducibility referee · **KILL**

**Kill (swarmed by better-resourced groups):** applying -002's honest-grading
doctrine to the "AI discovered X" literature is already an industry — PaperBench,
MLReplicate, ARA (arXiv:2605.02651), AutoReproduce, FactReview (arXiv:2604.04074),
Reproscreener, RIGOURATE (arXiv:2601.04350), the Institute for Replication, and
EleutherAI/Cambridge's "Faults in Our Formal Benchmarking" (arXiv:2606.29493) which
surfaced 4,833 findings incl. 398 mechanically certified defects across five Lean
benchmarks — we would be the eleventh entrant with the fewest resources.
(Scores: BREAK MED · EDGE HIGH · UNDER KILLED-BY-SEARCH · VERIF HIGH · PULL AUTHOR.)

### ARC K [W] — Rare-event estimator import (cut the 100x grading cost) · **KILL**

**Kill (the import has been made; we would be re-importing):** the tempting move —
bring applied probability's splitting / subset-simulation / importance-sampling
machinery to logical-failure estimation and make honest grading affordable for
everyone — is already in the literature: dynamical subset sampling reaches target
accuracy with ~2 orders of magnitude fewer samples than direct Monte Carlo (Phys.
Rev. Research 6, 013177 (2024)), and "Fail fast: techniques to probe rare events in
quantum error correction" (arXiv:2511.15177 — the failure-spectrum ansatz the
handoff already names as an adjacent ruler) generalizes the splitting method to
qLDPC codes with multi-seeded Metropolis sampling on d=6/12/18 BB codes under
circuit noise with the Relay decoder.
(Scores: BREAK HIGH-if-won · EDGE HIGH · UNDER KILLED-BY-SEARCH · VERIF HIGH ·
PULL AUTHOR.)

### ARC L [W] — QEC toolchain differential testing · **KILL**

**Kill (neighborhood occupied by better-equipped disciplines; honest ceiling is a
null result):** the idea that the whole literature's numbers inherit an unmeasured
implementation variance from a shared toolchain (Stim, PyMatching, ldpc, cudaq-qec,
tsim) is real — ScaLER (arXiv:2602.04921) already reports Stim hitting its
computational limit and failing to sample any logical error inside a two-hour budget
where ScaLER characterizes surface d-large at 1.51e-11 — but the correctness lane
proper belongs to programming-languages groups already in it (Quasilinear
Equivalence Checking for Detector Error Models, arXiv:2606.14677; symbolic execution
for QEC programs, PLDI 2024; LightStim, arXiv:2604.21472), and the modal outcome is
"the tools agree," which is infrastructure reassurance rather than a result that
changes what anyone does.
(Scores: BREAK LOW-MED · EDGE HIGH · UNDER WEAK · VERIF EXTREME · PULL AUTHOR.)

---

### CYCLE 1 TALLY

12 arcs scored. **3 SURVIVE** (E, A, D) · **1 MERGE** (F, into A and E) ·
**8 KILL** (B, C, G, H, I, J, K, L). Wildcards lane: 4 arcs entered (I, J, K, L),
**4 killed, 0 survived.**

**The kill pattern is the cycle's most informative finding, and it is recorded as a
finding rather than as an apology.** Every wildcard died the same death: the
referee/audit genre is being *colonized fast* — formal benchmarking (arXiv:2606.29493),
quantum software comparisons (arXiv:2607.00516), AI-for-science reproducibility
(arXiv:2605.02651 and eight others), detector-error-model equivalence
(arXiv:2606.14677), rare-event estimation (arXiv:2511.15177). Honest grading is no
longer an empty lane in general. It is empty in exactly one place: **the
fault-tolerant architecture cost-model layer, where the multipliers live.** That
makes arc E's crowd-absence stronger evidence, not weaker: the absence is not
inattention to the genre, it is inattention *there*.

**Wildcards-lane obligation carried forward.** Cycle 1 discharged the lane's
requirement (four arcs entered, scored, killed) but produced no survivor. Cycle 2
carries a named search plan rather than a vague promise: probe (i) claim-comparability
pathologies in non-quantum computational fields where the same recosting instrument
would transfer, (ii) verification tooling gaps named by practitioners in their own
limitations sections, (iii) cross-field imports where the *importing* discipline is
one QC003 already holds and the *receiving* field has no incumbent.

### AUTHOR-PENDING

- **PULL** is unscored on all 12 arcs. It is the author's axis; the Strategy Room
  asked rather than inferred. Scores arrive as a dated addendum row.
- **Forecast percentages** for arc D's registered bets and arc E's prereg are
  author authority and are not drafted here.
