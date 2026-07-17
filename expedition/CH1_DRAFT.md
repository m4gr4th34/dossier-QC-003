# CHAPTER 1 — THE RACE TO THE FIRST FAULT-TOLERANT QUANTUM COMPUTER
## Reconnaissance: the frame, the ruler, and the drill plan
### DRAFT v1 — review branch. Seals non-DOI after author review and edition integration.

Status legend used throughout: **CITE** = verified against the named primary
source on the stated date. **REPORTED** = an interested party's claim or a
secondary source, recorded but not adopted. **OPEN** = the author's own claim,
not yet verified. **[AUTHOR]** = a slot only the author may fill.

---

## 01 · WHAT THIS DOSSIER IS

One question drives it: **which physical platform reaches fault-tolerant,
useful-scale quantum computing first — and what, exactly, stands in each one's
way?**

Two predecessor publications set the stage, and this dossier is neither of them
repeated. *Quantum Computing: A General Overview* (the same author's map
dossier) surveys nine avenues at equal weight with deliberately loose odds; its
own front page states its citation audit is pending, so every claim inherited
from it enters here as REPORTED until re-verified. *dossier-QC-Accelerate-002*
(concluded at Chapter 5, DOI 10.5281/zenodo.21360979) built the measurement
discipline this dossier runs on: verify against primary sources on a stated
date, label every claim honestly, and record your own errors as findings.

The map told you the avenues exist. **This dossier drills.** Each platform gets
a full chapter that takes its single binding engineering constraint to bedrock:
the physical mechanism, the measured numbers, the scaling law, every candidate
fix and its status — written so a high-school student can follow every step,
because a constraint you can't explain plainly is a constraint you don't
actually understand. And at each bedrock we poke: is a novel solution visible?
Any such idea ships only as a scouted claim — a derivation, a simulation with
committed artifacts, or a dated falsifiable forecast. Bare ideas are worth
nothing in 2026; anyone can generate those.

**What this dossier can and cannot settle, stated up front.** Everything here
runs on simulation, published evidence, and reasoning — no lab. That covers
more than it sounds like: the instruments that grade fault-tolerance proposals
are classical simulations, so a no-lab analyst can check the field's homework
and register positions the field must later confront. What it cannot do is
derive the winner from first principles: the race partly turns on engineering
facts no simulation settles — laser power scaling, fabrication yield, cryogenic
plant economics. Where that is the situation, this dossier says so and places a
labeled bet instead of an assertion.

---

## 02 · THE STATE OF THE RACE (verified 2026-07-17 except where labeled)

**The storage half of the problem is cracking — in simulation.** For twenty
years the textbook number was brutal: roughly a hundred to a thousand fragile
physical qubits to make one reliable "logical" qubit. In April 2026 a
QuEra/Harvard/MIT team showed — **in circuit-level simulation, not on
hardware** — quantum LDPC codes with encoding rate above 1/2: about two
physical qubits per logical one, with projected memory error rates near
1.3x10^-13 per logical qubit per round at 0.1% physical error [CITE: Zhao,
Duckering, Gu, Maskara, Zhou, preprint, Apr 2026, building on Kasai's 2026
affine-permutation construction; verified 2026-07-17 against the paper and
QuEra's own scope statement]. The team's own caveat is the whole story of this
dossier: **it is a memory result.** Performing logical gates on these
ultra-high-rate codes remains open. The field can increasingly *store* a
protected qubit cheaply. It cannot yet *compute* on one cheaply. That gap —
memory-to-compute — is the racecourse.

**The decoding frontier moved, with a boundary worth stating exactly.**
Decoders are the classical programs that watch a quantum computer's error
signals and decide, live, what went wrong. Two 2025–26 results: IBM's Relay-BP
reports ~10x accuracy over the previous standard (BP+OSD) for qLDPC codes while
staying fast and compact enough for FPGAs [CITE: IBM Research publication
record, verified 2026-07-17]. Google's AlphaQubit 2 demonstrates real-time
neural decoding under 1 microsecond per cycle — surface code to distance 11,
color code to distance 9 [CITE: arXiv:2512.07737, verified 2026-07-17]. The
boundary: AlphaQubit 2's claims cover *topological* codes only. Real-time
decoding for high-rate qLDPC codes at scale remains open. Any sentence saying
"machine-learning decoders are too slow for live correction" is now false; any
sentence saying "real-time qLDPC decoding is solved" is also false.

**Logical-qubit counts, inherited as REPORTED.** Secondary trackers circulate a
leaderboard — QuEra 96 logical qubits from 448 physical; Quantinuum 48 from 98
ions; Atom Computing 24; Google 1 below-threshold logical qubit on Willow
[REPORTED: aggregator and map-dossier figures, not yet verified against primary
sources]. Each number gets verified in its platform's chapter, not repeated
here as fact. That some of these will survive verification unchanged is likely;
that all will is exactly the assumption this dossier exists to not make.

**Vendor roadmaps, labeled as what they are.** IBM targets its Starling system
(~200 logical qubits, 100M gates) around 2029; QuEra projects gigaquop-class
machines with >1,000 logical qubits; multiple vendors project 100+ logical
qubits by 2026–27 [REPORTED: vendor projections, interested parties, no
independent verification; recorded for the bet registry, adopted nowhere].

---

## 03 · THE MULTIPLIER PROBLEM — WHY THE RACE CAN'T CURRENTLY BE SCORED

Try to answer "who's winning" from the 2026 literature and you hit a wall this
dossier has now measured from both sides.

**The wall.** The field's unit of progress-claim is a multiplier against a
baseline the authors chose themselves. Within roughly thirteen months, all
CITE-verified at the grades stated in the committed scouting ledger
(expedition/SCOUTING_LEDGER.md, 2026-07-17):

| Claim | Against what baseline (the paper's words) | Source |
|---|---|---|
| ~250x time savings, 2x space | "a fixed-connectivity, fully fault-tolerant scheme" | transversal STAR, arXiv:2509.18294, PRX Quantum 7, 020343 (2026) — full text verified |
| 752x speedup; >10x fewer qubits | "NA-only baselines"; "SC-only systems" — two baselines in one abstract | arXiv:2601.10144 |
| 138x fewer physical qubits | "under detailed accounting" | arXiv:2604.06319 |
| 20–40x space-time cost | "the previous best-in-class STAR architecture" | arXiv:2606.25011 |
| ~10x qubit efficiency | "equivalent surface-code architectures" | Tour de Gross, arXiv:2506.03094 |
| ~8x overhead | surface code "at equal logical error" | routing codes, arXiv:2606.25330 |

Every multiplier is honest by its own lights. **No two share a baseline, a cost
model, a noise model, or a decoder — so no two can be compared, and no paper
claims they can.** When one team tried to put resource estimates on a common
physical-qubit scale, they excluded the most interesting new result rather than
recost it, saying so explicitly [CITE: arXiv:2508.14011 §4.7, verified
2026-07-17]. The comparison everyone needs is the comparison nobody is paid to
do: it earns no novelty credit and annoys everyone whose number shrinks.

**Exhibit 0 — a number in circulation that its paper does not contain.** Trade
coverage of the transversal STAR result reports the architecture reaching
"roughly 1,500 to 3,000 qubits." The paper states ~10,000 physical qubits at
p=10^-3, and full-text search finds no 1,500 or 1,500–3,000 figure anywhere in
it [CITE: full-text verification, 2026-07-17]. A mundane explanation exists and
is stated with equal prominence: the coverage may have conflated it with a
different, later paper (high-rate STAR, arXiv:2606.25011) — that conflation is
plausible but **unverified**. Either way the observable stands: a resource
figure is circulating attached to a paper that does not contain it.

**The self-demonstration.** This dossier's own scouting ledger committed the
same pathology in its first draft, five times, before any byte was sealed: a
multiplier paraphrased loosely, a publication date lifted from a press release,
a scaling figure quoted past its stated scope, a metric inherited from an
aggregator — and, in the other direction, a verified fact wrongly downgraded to
"unverified" on the strength of a memory instead of a fetch. All five were
caught at the pre-commit gate by one method: fetching the primary source and
reading the sentence. Nothing else worked. The full errata (SR-1..SR-5) are in
the committed ledger. A dossier whose thesis is "claims decay when nobody
rechecks them" keeps its own decay log in public; that is the price of the
thesis, and also its best evidence.

**What Chapter 8 does about it.** Re-express every multiplier above on one
stated baseline with one stated accounting; publish each claim's sensitivity to
the choices its authors made; register dated forecasts on which survive. With a
pre-registered kill condition: if no ordering changes beyond its own stated
uncertainty, that is reported as a negative result — at full grade, because
"the field's claims are mutually consistent after all" is a finding too.

---

## 04 · SIX PLATFORMS, SIX WALLS — THE DRILL PLAN

Each platform below gets one paragraph here and one full chapter later. The
paragraph names what the machine is physically made of, where it verifiably
stands, and the **single binding constraint** the chapter will take to bedrock.
Constraint choices are the author-reviewed analytical claims of this chapter
[OPEN: each platform chapter will either confirm its constraint choice or
correct it in public]. Numbers below marked REPORTED await primary verification
in their chapter.

**Ch2 — Neutral atoms.** Individual rubidium or ytterbium atoms held in a grid
of laser "tweezers"; qubits are atomic energy levels; entanglement comes from
exciting atoms into swollen Rydberg states that force neighbors to interact;
atoms are physically moved mid-computation to rewire connectivity. The current
logical-count leader [REPORTED] and home of the 2:1 simulation [CITE, §02].
**Binding constraint: loss.** Atoms escape their traps — during moves, during
gates — and a lost atom is not a flipped bit but a *missing* one. The best
architecture papers price loss as an effective Pauli error; whether that
modeling choice is conservative or optimistic against the platform's real
physics is exactly the kind of question Ch2 drills [CITE: transversal STAR's
loss model, full text verified 2026-07-17]. Plus the racecourse question: the
compute gap on high-rate codes is widest here because the storage win is
biggest here.

**Ch3 — Superconducting.** Aluminum circuits on silicon chips, cooled to ~15
millikelvin — colder than deep space — where current flows without resistance;
each qubit is a tiny oscillating circuit with a Josephson junction as its
nonlinear heart. The most industrially mature platform: Google's
below-threshold error correction [REPORTED, verify in Ch3], IBM's public
fault-tolerance roadmap [REPORTED, vendor]. **Binding constraint: wiring.**
Every qubit needs control lines into the fridge; qLDPC codes additionally
demand long-range couplings a flat chip doesn't natively have. Multilayer
wiring, couplers, and modular chip-to-chip links are the fixes on the table;
their measured cost is the drill.

**Ch4 — Trapped ions.** Charged atoms (barium, ytterbium) suspended in
electromagnetic fields inside a vacuum; qubits in atomic states so identical
and isolated they hold the field's fidelity records [REPORTED, verify in Ch4];
any ion can talk to any other via their shared repulsion. **Binding
constraint: speed and optical scale.** Gates run thousands of times slower
than superconducting ones, and each ion needs precision laser addressing —
scaling to thousands of qubits means scaling an optics bench. Chip-based traps
and photonic interconnects are the candidate fixes; whether the clock-speed
deficit is fatal at algorithm scale is a computable question, and Ch4 computes
it.

**Ch5 — Photonics.** The qubit is a particle of light in a silicon waveguide —
no vacuum chamber, no dilution refrigerator, and networking is native because
the qubit *is* already the thing that travels. **Binding constraint: loss,
again — but worse.** A lost photon is gone, most entangling operations are
probabilistic (they fail by design most attempts), so the architecture leans on
massive redundancy; the whole platform lives or dies on driving optical loss
below the fault-tolerance threshold. The map dossier's author holds a tracked,
labeled conviction that the long-term endpoint of quantum computing is optical
[REPORTED: the author's own prior forecast, QCF8 in the map dossier — recorded,
and deliberately given no vote here until Ch5 grades the loss numbers].

**Ch6 — Silicon spin.** A single electron's spin, trapped in a transistor-like
structure on a standard chip — manufactured, in 2025 demonstrations, on the
same 300mm foundry lines that make ordinary processors [REPORTED, verify in
Ch6]. The scaling story is the whole pitch: ride the trillion-dollar
semiconductor industry. **Binding constraint: no logical qubit.** Highest
manufacturing ceiling, lowest demonstrated floor — no error-corrected logical
qubit exists on this platform yet [REPORTED]. The drill: what verified
device-to-device variability and wiring density actually imply for when one
can.

**Ch7 — The engineered-qubit bets: topological and bosonic/cat.** Two
platforms that redesign the qubit itself rather than protecting a fragile one.
Topological (Microsoft): encode information in exotic quasiparticle states
that are *intrinsically* hard to disturb — if those states exist as claimed,
which the physics community actively disputes; the reviewers of the flagship
result noted it does not by itself evidence the underlying Majorana modes
[REPORTED, verify in Ch7]. Bosonic/cat (Alice & Bob, AWS lineage): store the
qubit in an oscillator's states arranged so one error type is exponentially
suppressed by construction, leaving a cheaper repetition code to catch the
rest. **Binding constraint: existence and extrapolation** — the topological
bet turns on a disputed physics claim; the cat bet on whether single-mode
suppression scales as projected. One chapter, because both are wagers that the
right qubit makes the error-correction mountain smaller instead of climbing
it.

---

## 05 · THE BET REGISTRY — OPENED

Books about this field go stale the month they print, and their authors are
never scored. This dossier's alternative: dated, falsifiable, mechanically
resolving public bets, registered before the platform chapters run, scored on
their dates whether anyone is watching or not. Three inaugural signposts are
drafted below. **Percentages are the author's alone** — the AI drafts
signposts and resolution mechanisms, never the number [AUTHOR: set percentages
before this chapter seals; any signpost may be struck or reworded].

**B1 — The compute gap closes first where storage won.** *By 2027-12-31, at
least one hardware demonstration (not simulation) of a two-qubit logical gate
on a qLDPC code with encoding rate ≥ 1/4 is public.* Resolution: an arXiv
preprint or journal paper reporting hardware data meeting the stated terms;
resolves TRUE/FALSE on the date. Author's probability: [AUTHOR: __%].

**B2 — Platform of that first demonstration.** *Conditional on B1 resolving
TRUE: the platform is neutral atoms.* Resolution: the platform named in the
resolving paper. Author's probability: [AUTHOR: __%].

**B3 — A vendor roadmap, scored rather than repeated.** *By 2026-12-31, IBM
publicly reports its Kookaburra system operating as a qLDPC memory with a
logical processing unit, per its stated 2026 roadmap.* Resolution: IBM public
technical announcement plus at least one independent secondary report.
Author's probability: [AUTHOR: __%].

The registry grows with each platform chapter: every chapter must deposit at
least one new dated bet at its close. Resolved bets are scored in public,
right or wrong, in the chapter following their date.

---

## 06 · METHOD, HONESTLY

Every factual claim in this dossier is verified against a primary source on a
stated date before it is asserted; recalled numbers are inadmissible. Measured
results and vendor projections are separated *within single sentences*.
Verification failures are fixed in the paper, never in the tolerance. The
dossier's own errors are findings: they are recorded in a public, append-only
ledger with named errata, because the alternative — quiet correction — is the
exact decay mechanism this dossier documents in others. The author reviews by
consistency and reality checks on end results, not re-derivation.

AI-use disclosure (author's own words): Created with heavy AI use, and limited human oversight, to test the capabilities of contemporary state-of-the-art AI.

*Next: Chapter 2 — Neutral atoms. The loss drill.*
