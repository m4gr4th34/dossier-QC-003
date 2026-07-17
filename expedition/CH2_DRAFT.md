# CHAPTER 2 — NEUTRAL ATOMS: THE LOSS DRILL
## From "atoms escape" to "the best-instrumented error in quantum computing"
### DRAFT v1 — every number below verified against the named primary source on 2026-07-17 unless labeled REPORTED.

Status legend: **CITE** = verified against the named primary source on
2026-07-17. **REPORTED** = interested-party or secondary source, recorded but
not adopted. **OPEN** = the author's own analytical claim. **FORECAST** = a
dated, falsifiable bet with a resolution mechanism.

This chapter is self-contained: nothing below requires reading any other
chapter.

---

## 01 · THE MACHINE, PHYSICALLY

A neutral-atom quantum computer is a vacuum chamber, some lasers, and a cloud
of individual atoms — usually rubidium or ytterbium. Each atom is held in
place by an "optical tweezer": a laser beam focused so tightly that its light
forms a tiny bowl of energy an atom settles into, the way a marble settles
into a dimple. Thousands of these bowls, arranged in a grid, each holding
exactly one atom, form the qubit register — a record-holding array now traps
6,100 atomic qubits in 12,000 tweezer sites [CITE: Manetsch et al., Nature,
2025; arXiv:2403.12021].

The qubit is the atom's internal state — two energy levels of its outermost
electron or its nucleus, playing the role of 0 and 1. To make two atoms
interact, lasers briefly promote them into a "Rydberg" state, where the
electron orbits so far from the nucleus that the atom swells thousands of
times over and physically shoves its neighbor's energy levels around — a
programmable, switchable interaction. And because the traps are made of light,
the atoms can be *moved* mid-computation: pick an atom up in a steerable
tweezer, carry it across the array, and any qubit can be made adjacent to any
other. That mobility is the platform's superpower.

It is also where this chapter's subject enters. Everything above shares one
failure mode that no other major platform has in the same form: **the atom can
simply leave.**

---

## 02 · WHAT LOSS IS, AND WHY IT IS NOT A BIT FLIP

Every quantum computer fights errors. Most errors are corruptions: the qubit
is still there, but its state flipped or blurred. Error-correcting codes are
built for exactly that — they detect and undo corruption using redundancy.

Atom loss is different in kind. The trap's energy bowl is shallow —
equivalent, in temperature units, to well under a thousandth of a degree above
absolute zero. Anything that gives the atom a modest kick sends it out of the
bowl and gone: not a flipped bit, a **missing** bit. The qubit hasn't taken a
wrong value; it has ceased to exist at its address. A code expecting to
measure that qubit gets, in effect, silence — and naive error correction
handles silence badly, because its whole machinery assumes there is a qubit
there to interrogate.

Hold that thought, because Section 05 inverts it: the same property that makes
loss alien to standard error correction — the qubit's *absence* — is
detectable in a way ordinary errors never are, and the platform's entire
2023–2026 research arc has been about cashing that in.

---

## 03 · WHERE THE ATOMS GO — MECHANISMS AND VERIFIED NUMBERS

Five mechanisms dominate. For each: the physics in plain terms, then the
measured number.

**(a) Background-gas collisions — the vacuum clock.** The chamber is a very
good vacuum, but not a perfect one. Stray room-temperature gas molecules
occasionally slam into a trapped atom; one hit ejects it. This sets a
"vacuum-limited lifetime" — the average survival time of a trapped atom doing
nothing at all. Typical working systems: **about 60 seconds** [CITE: Chiu et
al., Nature 646, 1075 (2025), which states its storage array's trap lifetime
as ~60 s]. Room-temperature record: **22.9(1) minutes** [CITE: Manetsch et
al.; same 6,100-qubit apparatus]. Cryogenic systems, where the cold chamber
walls themselves pump away residual gas: **~3,000 seconds** [CITE:
arXiv:2412.09780] and a July 2026 platform reporting a **2-hour trap
lifetime** [CITE: arXiv:2607.12988, posted 2026-07-14].

**(b) Heating by the trap's own light and the finite bowl.** The trapping
laser itself jiggles the atom — photon recoil and intensity noise steadily
heat it — and because the bowl is finite, a hot-enough atom boils out even
before its average energy reaches the rim [CITE: mechanism as described in
arXiv:2412.09780]. This is why atoms need periodic re-cooling, and re-cooling
has its own price: a measured loss of **1.1(1)×10⁻⁴ per cooling pulse** in the
cryogenic system above [CITE: arXiv:2412.09780].

**(c) Imaging.** Reading out or checking atoms means scattering light off
them, which heats them and can excite them into states the trap repels.
Measured per-image loss spans two orders of magnitude across systems: **1.5%
per image** in one ytterbium setup, with ~0.9 points of that from off-resonant
scattering and photoionization [CITE: IOP Quantum Sci. Technol.,
10.1088/2058-9565/adf7cf], down to a record steady-state imaging survival of
**99.98952(1)% per 80-ms image** — about 1 loss per 10,000 images, itself
mostly the vacuum clock ticking [CITE: Manetsch et al.].

**(d) Gates — the Rydberg toll.** Entangling gates require exciting atoms to
Rydberg states, which the tweezers do not confine (for ground-state traps the
Rydberg atom is typically *anti*-trapped), and from which the atom can decay
into states outside the qubit space — leakage that frequently ends in loss.
This is the toll booth every two-qubit gate passes through, and it is why gate
fidelity and loss are entangled subjects on this platform. Reference numbers:
metastable-ytterbium two-qubit gates at **0.980(1)** fidelity with mid-circuit
erasure conversion (2023) [CITE: Ma et al., arXiv:2305.05493 / Nature 622, 279
(2023)]; current vendor-reported two-qubit fidelities **>99.2%** [REPORTED:
QuEra figure via secondary coverage; not independently verified today].

**(e) Transport.** Moving atoms — the superpower — shakes them. Acceleration
heats; heating compounds mechanism (b). The best current architectures fold
transport costs into their error budgets, and one flagship theory paper prices
transport loss as an explicit channel (`p_move,loss`) [CITE: transversal STAR,
arXiv:2509.18294, full text verified in this dossier's committed ledger].

---

## 04 · THE SCALING LAW — WHY A LEAKY BUCKET GETS WORSE FASTER THAN IT LOOKS

The cruel arithmetic: if one atom survives a duration T with probability
close to 1, an array of N atoms *all* surviving is that probability raised to
the Nth power. Survival decays like exp(−N·T/τ), where τ is the lifetime from
mechanism (a). Losses anywhere in a code block are everyone's problem.

The record-holding array states this about itself: with 6,100 atoms and a
22.9-minute lifetime, **the chance of losing at least one atom somewhere in
the array passes 50% within about 100 milliseconds** [CITE: Manetsch et al.,
who give exactly this framing]. One hundred milliseconds — against algorithms
whose useful runs are minutes to hours. And that is the *record* apparatus,
doing *nothing*: no imaging, no gates, no moves, each of which adds its toll
from Section 03.

This is the bedrock form of the constraint. Not "atoms sometimes escape" but:
**the product N·T is on a budget set by the vacuum, and every useful direction
— more qubits, deeper circuits — spends it.** A fault-tolerant machine wants
both factors large simultaneously. Something has to give, and Sections 05–06
are the field's answer to what.

---

## 05 · THE TWIST — LOSS IS THE BEST-INSTRUMENTED ERROR IN THE BUILDING

Here the story turns, and this is the part casual coverage misses.

An ordinary qubit error is invisible: you cannot check "did this qubit flip?"
without disturbing it, so codes must *infer* errors indirectly, and every
inference is statistical. But "is there an atom here at all?" is a question
you **can** ask — shine light structured so that an atom answers and an
absence stays dark, without reading the quantum state of the survivors. An
error whose *location* is known is called an **erasure**, and erasures are the
gold-standard error: a code of distance d can correct roughly **twice as many
located erasures as unlocated errors**. Loss, uniquely among this platform's
failure modes, is convertible into exactly that gold standard.

The field has spent three years industrializing the conversion, and the
receipts are now published:

- **Erasure conversion at the qubit level.** Encode the qubit in a metastable
  level of ytterbium-171 so that the dominant gate errors kick the atom into
  *disjoint, observable* states — errors become flagged departures. Proposed
  in 2022 [CITE: Wu, Kolkowitz, Puri, Thompson, Nat. Commun. 13, 4657 (2022)],
  demonstrated with mid-circuit detection in 2023, with the detection itself
  disturbing surviving qubits at below the 10⁻⁵ level [CITE: Ma et al.], and
  extended in 2026 to full **logical qubits with erasure conversion**: a
  [[4,2,2]] code too small to correct even one unlocated error nevertheless
  corrected errors during decoding, because erasure location information did
  the work distance couldn't — improved logical performance with **no
  postselection** [CITE: Zhang et al., Nature Physics 22, 910–916 (2026);
  arXiv:2506.13724].
- **Loss-aware decoding theory.** A general framework for loss in logical
  algorithms — including a "delayed-erasure decoder" that exploits loss
  detected only later, when the exact moment of loss is unknown — with the
  sharp definitional split this chapter uses: a *loss* leaves the qubit
  unavailable until detected and replaced; an *erasure* is a loss caught at
  the very gate layer it happened, location and time both known [CITE:
  Baranes, Cain, Bonilla Ataides, Bluvstein, Sinclair, Vuletić, Zhou, Lukin,
  Phys. Rev. X 16, 011002, published 2026-01-02; arXiv:2502.20558]. The same
  paper's structural finding: algorithm subroutines heavy in gate
  teleportation *naturally* replace qubits as they go — loss handling for
  free where the algorithm already teleports.
- **Loss detection inside the flagship experiment.** The platform's headline
  fault-tolerance result — 448 atoms implementing the key elements of a
  universal fault-tolerant architecture — achieved its **2.14(13)× below-
  threshold** error suppression explicitly "by leveraging atom loss detection
  and machine learning decoding" [CITE: Bluvstein et al., Nature 649, 39–46
  (2026); arXiv:2506.20661; abstract verified]. Loss handling is not a
  side-quest; it is *in the headline number* of the platform's best result.
- **Leakage-to-erasure circuits** for species without convenient metastable
  structure [CITE: Chow et al., PRX Quantum 5, 040343 (2024)], and a growing
  loss-tolerant code/decoder literature [CITE: e.g. arXiv:2603.04156,
  optimal-distance atom-loss correction via Pauli envelope, 2026; Kuo &
  Ouyang, npj Quantum Inf. 12, 75 (2026), degenerate erasure decoding].

Plain-language summary a student can carry: **on this platform, the scariest
error is also the only one that announces itself.** The research program is:
make it announce itself earlier, louder, and more cheaply.

---

## 06 · THE FIX STACK — EVERY CANDIDATE, WITH STATUS

Bedrock means listing all of them, with what each has actually shown.

**Fix 1 — Better vacuum, colder walls (attack τ).** Status: **demonstrated,
compounding.** 60 s typical → 22.9 min room-temp record [CITE: Manetsch] →
~3,000 s and ~2 h in cryogenic platforms [CITE: arXiv:2412.09780;
arXiv:2607.12988]. Ceiling: engineering-bounded, buys a constant factor —
powerful but never removes the exp(−N·T/τ) form.

**Fix 2 — Continuous reloading (refuse to let N·T/τ be the budget).** Status:
**demonstrated at scale, September 2025 — the conceptual break.** A dual
"optical conveyor belt" of lattices ferries reservoirs of fresh cold atoms
into the science region; tweezers pluck replacements without disturbing the
coherence of stored neighbors. Measured: **300,000 atoms/s reloaded into
tweezers, >30,000 initialized qubits/s** (15,000/s with rearrangement), an
array of **>3,000 atoms maintained for more than 2 hours** — versus its own
~60 s trap lifetime — with stored qubits held in superposition states while
neighbors were swapped in, operation "in principle, indefinite" [CITE: Chiu
et al., Nature 646, 1075 (2025); arXiv:2506.20660; per-figure rates verified
in the paper's own text]. In parallel, a Princeton demonstration of **fast,
continuous and coherent atom replacement** in a qubit array [CITE: Li, Bao,
Peper, Li, Thompson, arXiv:2506.15633; preprint]. What it changes: the
scaling law's τ stops being the wall; the wall moves to *reload rate versus
loss rate*. What it has NOT yet shown: reloading woven into **repeated
error-correction rounds on a logical qubit** — coherent storage during
replacement is demonstrated; logical QEC during replacement is the open step.
That gap is precisely bet B4 below.

**Fix 3 — Erasure conversion (make every loss a located loss).** Status:
**demonstrated through logical level** [CITE: Zhang et al., Nature Physics
2026, above]. Ceiling: conversion coverage — the fraction of all error events
that end up flagged — and the species tax: the best conversion story lives in
ytterbium's metastable levels, while the largest arrays and the continuous-
reload demonstration live in rubidium. The platform's two crown jewels
currently sit on different atoms [OPEN: this analytical observation is the
author-reviewed claim of this chapter; the platform chapters on other species
will not resolve it — a unification demo would].

**Fix 4 — Loss-aware decoding (spend information instead of qubits).**
Status: **theory published at top venue, already load-bearing in the flagship
experiment** [CITE: Baranes PRX X 16, 011002; Bluvstein Nature 649]. Ceiling:
decoder runtime and the delay penalty — the later a loss is detected, the
more of its damage is unlocated.

**Fix 5 — Architect around it (teleport instead of persist).** Gate-
teleportation-heavy circuit structures replace qubits as a side effect of
computing [CITE: Baranes et al., structural finding]. A 2026 preprint carries
this to its logical end: **Shor's algorithm with as few as ~10,000
reconfigurable atomic qubits** in a loss-managed architecture [CITE as
existence + claim, not as verified resource count: arXiv:2603.28627 — Picard,
Levine, Endres, Preskill, Huang, Bluvstein among authors; preprint,
unrefereed; the number is the paper's claim].

**Fix 6 — Price it honestly in the noise model.** Not a hardware fix — a
truth-in-advertising fix, and this dossier's own lane. See Section 07.

---

## 07 · THE MODELING QUESTION — WHERE THIS DOSSIER'S AUDIT BITES

The committed scouting ledger of this dossier (Cycle 1, arc E) pre-registered
a noise-model fidelity audit, and this chapter now states its neutral-atom
instance precisely.

The platform's flagship *architecture* paper prices atom loss as an
**unheralded effective Pauli-Y channel** during gates and transport [CITE:
transversal STAR, arXiv:2509.18294; full-text verification in the committed
ledger]. The platform's flagship *experiments and theory*, per Section 05,
treat loss as **detectable, locatable, and exploitable** — that is the entire
content of erasure conversion, delayed-erasure decoding, and
loss-detection-assisted below-threshold performance. Both choices are
defensible; they are not the same physics, and they should not price the same.
An erasure-aware treatment knows *where* the failure sits (worth roughly a
factor-two in correctable weight); a Pauli-Y treatment pays no detection
machinery and no delay penalty. Which way the resource multiplier moves when
the treatment varies across this defensible range is a computable,
falsifiable question — and to this dossier's knowledge, as of 2026-07-17, no
published recosting of a headline neutral-atom architecture claim across the
loss-treatment range exists [OPEN: absence claim, held to the standard "to our
knowledge," searched today].

**SCOUTED CLAIM (pre-registered simulation campaign, this dossier's next
instrument if the author greenlights it):** re-simulate a transversal-
architecture logical operation at fixed physical error budget under three
loss treatments — (i) unheralded Pauli-Y (the STAR choice), (ii) end-of-round
delayed erasure (the Baranes decoder's regime), (iii) idealized immediate
erasure — and report the logical error rate and resource multiplier
sensitivity across (i)–(iii). Committed artifacts; a stranger reruns the
repo and gets the table. This claim ships as a registered campaign, not a
result: no number is asserted here.

---

## 08 · WHAT THIS DOES TO THE RACE — AND TO THIS DOSSIER'S OWN RECORDS

**The constraint restated at bedrock.** Neutral atoms' binding constraint is
not "atoms are lost" — that framing is five years stale. It is: **can the
platform's loss-instrumentation stack (detect → locate → decode → replace)
run inside deep logical circuits at rates that beat the loss it manages,
on one atomic species, at scale?** Every piece is separately demonstrated;
no demonstration yet composes them all.

**Chapter 1 inheritances, updated.** Chapter 1 of this dossier carried, as
REPORTED, a leaderboard line "QuEra 96 logical qubits from 448 physical."
Today's verification: the underlying paper exists and is stronger than the
leaderboard line suggests — Nature 649, 39–46 (2026), online 2025-11-10,
implementing the key elements of a universal fault-tolerant architecture on
up to 448 atoms, 2.14(13)× below threshold, transversal gates, lattice
surgery, and universal logic via transversal teleportation with [[15,1,3]]
codes [CITE: abstract verified]. The specific "96 logical qubits" count and
the "[[16,6,4]]" code identification circulate in the vendor's own blog and
secondary trackers but are not in the paper's abstract; they remain
**REPORTED at that level of detail** pending full-text verification. The
registration note attached to this dossier's bet B1 — which raised B1's
threshold because a January 2026 result likely already cleared the old bar —
is now supported at Nature-paper level rather than aggregator level: hardware
logical two-qubit operations on high-rate codes exist; B1's live threshold
(encoding rate ≥ 1/2) remains genuinely open.

---

## 09 · THE CHAPTER'S BET — DEPOSITED TO THE REGISTRY

**B4 — Reloading meets error correction.** *By 2027-12-31, a hardware
experiment publicly demonstrates repeated quantum-error-correction rounds on
at least one logical qubit while lost atoms are replaced mid-experiment by
continuous or mid-circuit reloading — i.e., a logical qubit whose protected
lifetime is not bounded by the apparatus's single-atom trap lifetime.*
Resolution: an arXiv preprint or journal paper reporting hardware data
meeting the italicized terms; resolves TRUE/FALSE on the date. Rationale for
the number: every component exists separately (continuous reload at 300k
atoms/s with coherence preserved [CITE: Chiu]; coherent replacement [CITE:
Li/Thompson]; loss-aware QEC decoding in hardware [CITE: Bluvstein]); the
composing experiment is the obvious next flagship for at least two groups;
eighteen months is one flagship-paper cycle. Probability: **~55%**
[AI-drafted estimate (author-delegated 2026-07-17); the author may override
any number].

---

## 10 · METHOD NOTE

Every CITE above was checked against the named primary source (arXiv
abstract, arXiv full text, or journal page) on 2026-07-17. REPORTED items
name their non-primary provenance. The scaling-law framing in §04 is the
cited paper's own. This chapter's one absence claim (§07) is held to
"to our knowledge, searched on the stated date" and is posted as an open
challenge: the first person to produce a published loss-treatment recosting
of a headline neutral-atom architecture claim gets named credit in the next
version. Created with heavy AI use, and limited human oversight, to test the
capabilities of contemporary state-of-the-art AI.

*Next: Chapter 3 — Superconducting. The wiring drill.*
