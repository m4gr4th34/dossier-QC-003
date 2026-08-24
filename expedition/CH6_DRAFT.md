# CHAPTER 6 — SILICON SPIN: THE YIELD DRILL
## The platform betting that the hardest part of quantum computing is already a solved industry
### DRAFT v1 — every number below verified against the named primary source on 2026-08-24 unless labeled REPORTED.

Status legend: **CITE** = verified against the named primary source on
2026-08-24. **REPORTED** = interested-party or secondary source, recorded but
not adopted. **OPEN** = the author's own analytical claim. **FORECAST** = a
dated, falsifiable bet with a resolution mechanism.

This chapter is self-contained: nothing below requires reading any other
chapter.

---

## 01 · THE MACHINE, PHYSICALLY

A silicon spin qubit is a single electron (or a single atom's nucleus)
sitting inside what is essentially a transistor. Metal gates on a silicon
chip — the same material, the same lithography family, in several cases
literally the same production lines as the processor in your laptop — shape
an electric corral a few tens of nanometers across that holds exactly one
electron. The qubit is that electron's spin: a tiny quantum magnet pointing
up or down. In the donor variant, the qubit is the nuclear spin of a single
phosphorus atom placed into the crystal, one of the most isolated quantum
objects accessible to any technology.

Why silicon specifically: purified silicon-28 has no nuclear spin of its
own, so an isotopically enriched chip is *magnetically silent* — the
electron's quantum state floats in near-perfect quiet. The measured
lifetimes on a foundry-made device: dephasing time T2* of 30.4 µs, echo
time of 803 µs, and a relaxation time T1 of **6.3 seconds** [CITE:
arXiv:2410.15590, the Diraq/imec unit-cell paper]. Seconds, on a chip made
in a 300 mm industrial line, with gate pitch under 100 nm and the active
layer enriched to a residual 400 ppm of spin-carrying silicon-29 [CITE:
same].

The pitch, in one sentence: **every other platform must invent its
factory; this one claims the factory already exists** — the
trillion-dollar CMOS industry — and the qubit is small enough
(transistor-sized) to use it. This chapter drills whether the claim's
load-bearing word — *yield* — means what the pitch needs it to mean.

## 02 · WHAT THE YIELD PROBLEM IS

"Yield" in a classical fab means: what fraction of manufactured devices
work. Silicon spin's headline results are exactly yield results, and the
2025 landmark is genuinely strong: Diraq and imec reported silicon spin-
qubit **unit cells fabricated in an industry-compatible 300 mm CMOS flow
with every fundamental operation — single-qubit, two-qubit, state
preparation and measurement — exceeding 99% fidelity, demonstrated on four
separate two-qubit devices from the same wafer**, with readout above 99.9%
on three of them [CITE: the September 2025 Nature "Industry-compatible
silicon spin-qubit unit cells exceeding 99% fidelity," reported
consistently across the vendor, technical coverage, and the open-access
record; the underlying device physics per arXiv:2410.15590]. Not one hero
device: a sampled population, all above the error-correction-relevant line.

But a quantum computer is not a population of unit cells; it is one array
in which *every* site must work *simultaneously*. And there the platform's
numbers change scale abruptly: the largest foundry-fabricated silicon spin
device operating as a qubit array is **eight qubits** (Diraq/imec, Nature
Communications, July 2026) [REPORTED: vendor and secondary]; Intel's
Tunnel Falls, processed on the same D1 line as its commercial logic, is a
**12-qubit** chip [REPORTED]. Chapters 2–4 of this dossier verified rival
platforms running 98 to 6,100 physical qubits, with below-threshold or
beyond-breakeven logical qubits on top. Silicon spin has the field's best
factory and, simultaneously, its smallest demonstrated arrays — both
halves verified, both load-bearing.

The platform's own literature names why scaling is not free even with a
perfect fab: solid-state reality — embedded and interfacial **defects**,
residual **nuclear spins**, lattice vibrations, and **crosstalk** from the
dense gate stack inadvertently steering idle neighbors [CITE:
arXiv:2509.24766, introduction]. Each is a per-site risk; an array
multiplies them.

## 03 · THE VERIFIED STATE OF THE ART

**Error correction machinery: arrived, at detection grade, in 2026.** Two
results this year moved the platform from "no QEC" to "QEC's first rungs":

- **Stabilizer-based error detection** — the measurement technique that
  fault-tolerant codes are built on — demonstrated for the first time in
  silicon: a donor-based processor of four phosphorus nuclear-spin qubits
  plus one electron ancilla detects an arbitrary single-qubit error in a
  circuit serving as a primitive of surface-code error detection, with a
  four-qubit GHZ state at 88.5(2.3)% fidelity; the stabilizer record
  enables post-processing correction and preserves entanglement [CITE:
  arXiv:2509.24766; published Nature Electronics (2026); SZIQA/SUSTech].
- **Universal logical operations** on encoded qubits: five phosphorus
  nuclear spins running the [[4,2,2]] error-*detecting* code — two logical
  qubits in four physical, the minimal fault-tolerance testbed — with
  universal logical operations and distillable magic states, using error
  mitigation (parity checks, symmetry verification) [CITE: Nature
  Nanotechnology (2026), doi 10.1038/s41565-026-02140-1, via its published
  coverage; Zhang et al.].

**The precision this dossier is obligated to draw** (as it drew for ions in
Chapter 4): these are error-*detected* logical qubits at few-qubit scale —
neither result claims fault-tolerant performance, and no silicon device
has shown a below-threshold or beyond-breakeven error-*corrected* logical
qubit of the kind Chapters 2–4 verified on atoms, superconductors, and
ions. (Earlier three-qubit phase-flip *correction* exists — RIKEN, Nature
2022 [CITE: Nature 608 lineage / arXiv:2201.08581] — but at
coherent-control grade, pre-stabilizer.) Chapter 1's leaderboard line "no
error-corrected logical qubit on this platform" therefore updates to: **no
error-corrected logical qubit; error-detected logical qubits with
universal operations since March 2026.** The wall is real and the first
rungs are now bolted to it.

**A finding inside the detection result that this dossier flags as
strategically large:** the silicon donor system's errors are **strongly
biased, with no state leakage** — the stabilizers measured it directly,
and the authors state these properties "call for tailored quantum-error
correction codes" [CITE: arXiv:2509.24766, abstract/discussion]. Readers
of this dossier's PREREG-1 campaign will recognize the shape: *what* a
platform's error budget is made of is worth more than how big it is —
biased, leakage-free noise is the cheapest kind to correct, and silicon
just measured that it has it.

**The record book, labeled.** Silicon's two-qubit fidelity record: 99.9%,
on an 11-qubit two-donor-register processor (SQC, Dec 2025) [REPORTED];
a four-qubit Grover's search at ~95% success with every operation above
threshold (SQC, Feb 2025) [REPORTED]. Hot-qubit operation near 1 kelvin —
a regime where cooling budgets are thousands of times friendlier than
millikelvin — demonstrated and central to the platform's integration story
[CITE: named among the field's milestones in arXiv:2509.24766's
introduction; vendor emphasis REPORTED]. Ecosystem breadth [all REPORTED]:
Intel's Tunnel Falls deployed to Argonne (Jan 2026); Quobly building on
STMicroelectronics' 28 nm FDSOI line with isotopically enriched silicon-28
entering that production line in December 2025; Equal1 shipping a 6-qubit
SiGe system; an 18-qubit germanium array (May 2026). Roadmaps [REPORTED —
vendor projections, interested parties]: Diraq targets thousands of qubits
by 2029 and more than a million by 2031.

## 04 · THE SCALING LAW — YIELD TO THE POWER OF N

Here is the platform's version of the law every chapter of this dossier
has had to write. Classical fabs think in per-device yield; a quantum array
compounds it: if each qubit *site* independently comes out usable with
probability y — the right electron count, workable valley structure,
tolerable charge noise, no killer defect — then a defect-intolerant
N-qubit array works with probability roughly **y^N**. The same exponential
that Chapter 2 wrote in time (exp(−N·T/τ)) and Chapter 5 wrote in distance
(transmission^elements), silicon writes in *fabrication space*.

What is actually measured today sits at the small-N end: unit cells at
N = 2 sampled across a wafer, all above the line [CITE: §02]; a working
N = 8 foundry array [REPORTED]; N = 12 processed at industrial volume
[REPORTED]. What the pitch requires is the exponent staying tame to
N = 10³–10⁶ — and that is precisely the range where the platform's
self-named per-site risks (defects, residual nuclear spins, crosstalk in a
sub-100-nm gate forest [CITE: §02]) have never been survived all at once.
The honest statement of the constraint: **the platform has demonstrated
that its factory can print excellent quantum devices; it has not yet
demonstrated that excellence survives exponentiation.** Mitigations exist —
tunable gates that trim away variability device-by-device, sparse arrays
with qubit shuttling between islands, redundancy-and-selection (print
extra sites, use the good ones — the classical industry's own trick)
[OPEN: mitigation taxonomy, composed from the platform literature] — and
every one of them spends control complexity to buy yield, which is the
next section's subject.

## 05 · THE TWIST — THE PLATFORM WHOSE FIXES LIVE ON ITS OWN CHIP

Every prior chapter's platform imports its fixes from somewhere else:
atoms import reload optics, superconductors import cryo-electronics and
photonics, ions import photonic networks. Silicon spin's distinguishing
bet is that **its fixes are made of the same stuff as its qubits.** The
control electronics that Chapter 3 showed strangling superconducting
machines — racks of room-temperature gear feeding per-qubit cables — can,
on this platform alone, plausibly move *onto the qubit die itself*:
spin qubits tolerate operation near 1 kelvin [CITE: §03], where cooling
budgets accommodate milliwatt-class on-chip CMOS control, and the vendors'
stated architecture is monolithic qubits-plus-control on one chip
[REPORTED: Diraq's stated GlobalFoundries 22 nm integration plan; the
cross-platform control-integration framing]. Add the measured noise
character — biased, leakage-free [CITE: §03] — and the platform's
end-state story is uniquely coherent: transistor-sized qubits, printed by
the million, controlled by their own neighbors, corrected by codes
tailored to a measured (and friendly) noise profile.

The gap between that story and the present tense is exactly two numbers
wide: **eight qubits, zero error-corrected logical qubits.** This dossier
declines to resolve the tension by narrative in either direction; §08
prices it instead. [OPEN: this section's framing is the chapter's
author-reviewed analytical claim.]

## 06 · THE FIX STACK — EVERY CANDIDATE, WITH STATUS

**Fix 1 — Foundry statistics as the instrument.** Sampled multi-device
fidelity studies on industrial wafers — the September 2025 result's real
content [CITE: §02]. Status: demonstrated at N = 2; the methodology, not
any single device, is the asset. Ceiling: says nothing yet about
simultaneous N-site arrays.

**Fix 2 — Tunability against variability.** Gate voltages trim each dot's
electron count and coupling, absorbing fabrication spread in software.
Status: standard practice [CITE: device operation throughout
arXiv:2410.15590]. Ceiling: each trimmed parameter is a control line and a
calibration — variability is paid for in the control budget.

**Fix 3 — On-chip / cryo-integrated control.** The 1 K operating window
plus CMOS-native fabrication makes co-located control the platform's
signature play [REPORTED: vendor architecture statements; hot-qubit
operation CITE-anchored per §03]. Ceiling: mixing milliwatt electronics
with nanovolt-sensitive qubits on one die is demonstrated nowhere at
array scale.

**Fix 4 — Sparse arrays and spin shuttling.** Move electrons between
distant sites so the array can be sparse where fabrication is risky and
dense where it must compute [REPORTED: architecture literature]. Ceiling:
shuttling fidelity per unit distance becomes a new per-operation error
channel — the platform's version of Chapter 2's transport toll.

**Fix 5 — Tailored codes for biased, leakage-free noise.** Named by the
error-detection paper itself as the indicated direction [CITE:
arXiv:2509.24766]. Ceiling: theory-to-hardware lag; but of all this
chapter's fixes it is the one with a fresh measurement underneath it.

**Fix 6 — Redundancy-and-selection.** Print more sites than needed, map
around the duds — the classical yield playbook, uniquely available to a
platform whose sites are transistor-cheap. Status: implicit in vendor
million-qubit roadmaps [REPORTED]. Ceiling: selection needs switching and
routing that themselves must work at scale.

## 07 · WHAT THIS DOES TO THE RACE — AND TO THIS DOSSIER'S RECORDS

**The constraint restated at bedrock.** Silicon spin's binding constraint
is not "no logical qubit" — that line is now stale by one rung (§03). It
is: **can per-site excellence survive exponentiation — can a platform
whose unit cells beat the threshold in sampled statistics hold that
quality across thousands of *simultaneous* sites, with control complexity
that its own on-chip integration story is supposed to absorb — before the
platforms already at logical scale make the race about logical
algorithms instead of physical arrays?** The factory is real; the
exponent is unmeasured; everything else is narrative.

**Chapter 1 inheritances, updated.** Ch1's card said "no error-corrected
logical qubit exists on this platform yet [REPORTED]" — now upgraded with
2026's two rungs: error-*detected* logical qubits with universal
operations exist [CITE: §03]; error-*corrected*, beyond-breakeven logical
qubits still do not. Ch1's "ride the trillion-dollar foundry" framing is
verified as the correct organizing question, and this chapter's answer is
that the foundry has been demonstrated as a *device* factory, not yet as
an *array* factory — the distinction the yield drill exists to make.

## 08 · THE CHAPTER'S BET — DEPOSITED TO THE REGISTRY

**B8 — The array clears its throat.** *By 2028-12-31, a silicon spin
platform publicly demonstrates repeated stabilizer-based quantum error
correction — at least two full syndrome-extraction rounds with mid-circuit
measurement on the same encoded logical qubit — on a device fabricated in
an industrial 300 mm (or equivalent production-line) process.* Resolution:
an arXiv preprint or journal paper reporting hardware data meeting the
italicized terms; resolves TRUE/FALSE on the date. Rationale: this is the
precise composition the platform is missing — its QEC machinery exists on
lab-grade donor devices [CITE: §03], its fidelity exists on foundry
devices [CITE: §02], and the bet demands they meet, with "repeated rounds"
chosen because single-shot detection is already done and repetition is
where crosstalk, readout back-action, and array-level yield actually get
tested. Probability: **~30%** [AI-drafted estimate (author-delegated
2026-07-17); the author may override]. The platform's own trajectory
(detection Jan 2026 → universal logical ops Mar 2026 → 8-qubit foundry
arrays Jul 2026) argues for higher; the standing pattern this dossier has
now verified on four platforms — *the composing experiment is always the
hard part* — argues for lower; ~30% is where those arguments meet.

## 09 · METHOD NOTE

Every CITE above was checked on 2026-08-24 against the named primary
source (arXiv abstract or full text, Nature-family publication record, or
consistent open-access mirrors, labeled in place). REPORTED items name
their non-primary provenance; vendor roadmaps are flagged as
interested-party projections. The y^N law in §04 is labeled analysis: the
independence assumption is a modeling choice, stated as such. Created with
heavy AI use, and limited human oversight, to test the capabilities of
contemporary state-of-the-art AI.

*Next: Chapter 7 — The engineered-qubit bets: topological and cat qubits.*
