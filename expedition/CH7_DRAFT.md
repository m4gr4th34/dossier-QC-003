# CHAPTER 7 — THE ENGINEERED-QUBIT BETS: TOPOLOGICAL AND CAT
## The existence drill: two platforms that redesign the qubit so the error-correction mountain gets smaller instead of climbing it
### DRAFT v1 — every number below verified against the named primary source on 2026-08-24 unless labeled REPORTED.

Status legend: **CITE** = verified against the named primary source on
2026-08-24. **REPORTED** = interested-party or secondary source, recorded but
not adopted. **OPEN** = the author's own analytical claim. **FORECAST** = a
dated, falsifiable bet with a resolution mechanism.

This chapter is self-contained: nothing below requires reading any other
chapter.

---

## 01 · THE MACHINE, PHYSICALLY

Two machines share this chapter, because they share one wager.

**The topological machine.** A hybrid nanowire: a semiconducting wire of
indium arsenide laid against a superconductor — aluminium in the first
generation, lead in the newest — cooled to millikelvin and tuned with gate
voltages and an in-plane magnetic field until, if the theory holds, the
wire enters a topological superconducting phase whose two ends host
*Majorana zero modes*: not particles you can point at, but a pair of
half-a-fermion excitations pinned at the wire's ends. The information is
the shared **fermion parity** of that pair — whether the two ends jointly
hold an even or odd number of electrons. Because the two halves sit
micrometres apart, no local disturbance can read or corrupt the parity;
protection is geometric, not corrective. Four such modes make a "tetron", the
unit intended to serve as one qubit. Readout is interferometric: tunnel-couple
the wire to quantum dots and watch the dots' quantum capacitance shift by up
to 1 femtofarad depending on parity [CITE: Microsoft Quantum, *Nature* 638,
651–655 (2025)].

**The cat machine.** A superconducting microwave resonator — an ordinary
electromagnetic mode — driven by a circuit that dissipates photons strictly
*in pairs*. That two-photon dissipation pins the field into a superposition
of two coherent states of opposite phase: Schrödinger's cat, made of a few
tens of photons. The two computational states are two *locations in phase
space*, and the further apart you push them (the more photons you put in),
the harder it is for local noise to carry the field from one to the other.
Here too the protection is non-locality — but in phase space rather than
real space, and engineered by dissipation rather than by a phase of matter
[CITE: Lescanne et al., *Nature Physics* 16, 509–513 (2020)].

**The shared wager, stated once.** Every other platform in this dossier's
serial accepts a fragile qubit and pays for error correction — hundreds of
physical qubits, syndrome rounds, decoders. These two platforms instead
**buy an exponent**: make one error type exponentially rare by construction,
and the error-correction bill collapses. Topological aims to suppress both
error types at once and need almost no code at all; cat suppresses bit flips
only and leaves phase flips to a one-dimensional repetition code, the
cheapest code there is [CITE: Lescanne et al., *Nature Physics* 16 (2020),
abstract: bit flips are "autonomously corrected", so "only phase-flips remain
to be corrected via a one-dimensional quantum error correction code"].

This chapter drills the one question that wager creates and no other chapter
in this serial has had to ask: **does the exponent exist, and has anyone
measured it doing the work the architecture spends it on?**

## 02 · WHAT THE EXISTENCE PROBLEM IS

Every previous constraint in this dossier's serial was an engineering
quantity: atoms escape, wires conduct heat, ions must be cooled, photons
attenuate, wafers yield. You can argue about the number; nobody argues about
what is being measured.

The engineered-qubit bets are different in kind, and in two different ways.

**Topological: a question of existence.** The architecture's protection is
inherited from a physical object — a pair of Majorana zero modes in a
topological phase. If the devices are not in that phase, the protection is
not weak; it is absent, and the measured signals are being produced by
ordinary, trivial states that mimic the signatures. This is not a
hypothetical failure mode: it has already happened once in this exact
research programme, in public. "Quantized Majorana conductance" [Zhang et
al., *Nature* 556, 74–79 (2018)] was **retracted on 8 March 2021**; the
retraction note records that data in two figures had been unnecessarily
corrected for charge jumps and a figure axis mislabeled, and that after
recalibration the conductance values sat about 8% above the plateau the
paper claimed to observe [CITE: Retraction Note, *Nature* 591, E30 (2021),
doi 10.1038/s41586-021-03373-x].

**Cat: a question of extrapolation.** Nothing about the cat qubit's
mechanism is in dispute — the exponential is measured, peer-reviewed, and
reproduced by two independent industrial groups (§04). What is in dispute,
or rather what is simply not yet measured, is whether the exponent survives
the trip from *one idle mode* to *a running logical qubit*: through the
gates, the ancilla measurements, the concatenation, and the scale. The
platform's headline resource numbers are the output of an architecture
analysis with stated assumptions, not of a machine.

So the chapter's constraint, named plainly: **for one of these platforms the
foundation is disputed and the payoff is uncontroversial; for the other the
foundation is measured and the payoff is an extrapolation.** Both are bets
that a physics claim can replace an engineering bill. Only one of them can
currently be checked by turning a knob.

## 03 · THE VERIFIED STATE OF THE ART — TOPOLOGICAL

**The flagship result, stated exactly.** Microsoft Quantum published an
interferometric single-shot parity measurement in indium arsenide–aluminium
hybrid devices: a gate-defined proximitized nanowire tunnel-coupled to
quantum dots, showing flux-periodic bimodality in the dots' quantum
capacitance with a signal-to-noise ratio of 1 in 3.6 microseconds, a dwell
time in the two states longer than 1 millisecond at in-plane fields near 2
tesla, and a parity measurement assignment error probability of 1% [CITE:
Microsoft Quantum (Aghaee et al.), "Interferometric single-shot parity
measurement in InAs–Al hybrid devices", *Nature* 638, 651–655 (2025), doi
10.1038/s41586-024-08445-2, published 19 February 2025].

**What the published paper claims about Majoranas — and what the preprint
claimed.** This dossier fetched both versions on 2026-08-24 and reports the
divergence, because it is the cleanest available measure of how the claim
moved under review. The preprint's abstract states that "these results are
consistent with a measurement of the fermion parity encoded in a pair of
Majorana zero modes that are separated by approximately 3 μm" [CITE:
arXiv:2401.09549v1 abstract]. The published abstract deletes that sentence
and replaces it with: "We discuss the interpretation of our measurements in
terms of both topologically trivial and non-trivial origins" [CITE: *Nature*
638, 651–655 (2025) abstract]. The measurement is the same; the claim
attached to it is not. (A second, smaller divergence, recorded for
completeness: the signal-to-noise figure reads 3.7 microseconds in the
preprint and 3.6 in the published version.)

**The journal said so itself.** The peer-review file accompanying the paper
carries an editorial statement that "the results in this manuscript do not
represent evidence for the presence of Majorana zero modes in the reported
devices" [CITE: *Nature* peer-review file for doi 10.1038/s41586-024-08445-2,
quoted in *Physics World*, 25 February 2025 — the peer-review file is the
primary document; the quotation is reproduced from technical coverage at
coverage grade, as this dossier has done elsewhere for paywalled primary
records].

**The dispute is peer-reviewed, in the same journal, on both sides.** On 24
June 2026 *Nature* published a Matters Arising and a Reply, back to back:

- Henry F. Legg (University of St Andrews / University of Basel), "On the
  robustness of topological gap detection via transport", *Nature* 654,
  E22–E26 (2026), doi 10.1038/s41586-026-10567-8 — argues that trivial
  states can mimic the expected signatures, that the topological gap
  protocol's verdict depends on data-processing choices rather than device
  properties, and that the regions of parameter space in which the parity
  readout was performed appear gapless and highly disordered in the public
  transport data [CITE].
- Microsoft Quantum, "Reply to: On the robustness of topological gap
  detection via transport", *Nature* 654, E27–E28 (2026), doi
  10.1038/s41586-026-10568-7 — maintains that the flux-periodic
  interferometric signal strongly indicates a topological origin, states
  explicitly that "our analysis of our CQ measurements does not assume the
  existence of a gap", and argues that a gapless system could not sustain
  the observed periodic signal because the interference contrast would wash
  out [CITE].

This dossier records both at equal prominence and adopts neither. The
observable it *does* adopt is structural: **the flagship result and a
substantive challenge to it now both carry the same journal's peer-reviewed
imprimatur.** In this dossier's labeling scheme that is not a scandal; it is
what an unresolved existence question looks like when it is being handled
properly.

**Where the hardware actually is, mid-2026.** Microsoft's newest published
artifact is a preprint: an InAs–**lead** tetron device, swapping aluminium
for a higher-gap superconductor, in which the team brings up one device
inside a multi-tetron array and measures the parity of one of that tetron's
hybrid nanowires, observing flux-periodic bimodal quantum-capacitance shifts
and a characteristic parity switching time of about **20 seconds**, some
instances reaching minute scale — "orders of magnitude longer than typical
qubit operation times, which are on the order of μs" [CITE: Zimmerman et al.
(Microsoft Quantum), "20 Second Parity Lifetime in an InAs–Pb Tetron
Device", arXiv:2606.03884, submitted 2 June 2026 — **preprint, unrefereed**].
Coverage adds a topological gap of roughly 70 microelectronvolts against
about 30 in the earlier devices, and a characteristic parity lifetime near
22 seconds [REPORTED: trade coverage, 2 June 2026]. Trade press also reports
the specific data-processing objections behind the Nature exchange — a
plotting filter hardcoded to highlight only the largest purportedly
topological region, and an antisymmetrization performed on array index
rather than physical bias value — with Microsoft characterizing the latter
as "a minor off-by-one-pixel bug in our TGP processing" and stating "we stand
by our results and our roadmap" [REPORTED: trade coverage, 24 June 2026; the
peer-reviewed core of this dispute is the Matters Arising and Reply above].

**The roadmap, labeled.** Microsoft's published device roadmap runs four
generations: a single-qubit device for benchmarking, a two-qubit device using
measurement-based braiding for Clifford operations, an eight-qubit device
intended to demonstrate logical-qubit advantages, and a topological qubit
array supporting lattice surgery on two logical qubits [CITE: Aasen et al.,
"Roadmap to fault tolerant quantum computation using topological qubit
arrays", arXiv:2502.12252 — **preprint, unrefereed**; the roadmap's *targets*
are the authors' plan, not results].

**The precision this dossier is obligated to draw.** As of 2026-08-24, the
peer-reviewed record for this platform contains **a parity measurement and a
published dispute about what it means**. It does not contain a topological
qubit: no encoded qubit on which two non-commuting operations have been
performed, and no quoted single-qubit error rate. The 20-second parity
lifetime is a genuine and striking number, and it is a *lifetime of a
measured quantity*, in an unrefereed preprint — not a qubit benchmark
[OPEN: this dossier's own reading of the published record on the stated
date].

## 04 · THE VERIFIED STATE OF THE ART — CAT / BOSONIC

**The mechanism, measured.** Increasing the phase-space separation of the two
cat states produces "an exponential decrease of the bit-flip rate while only
linearly increasing the phase-flip rate" [CITE: Lescanne, Villiers, Peronnin,
Sarlette, Delbecq, Huard, Kontos, Mirrahimi, Leghtas, "Exponential suppression
of bit-flips in a qubit encoded in an oscillator", *Nature Physics* 16,
509–513 (2020), doi 10.1038/s41567-020-0824-x]. That single sentence is the
whole platform: one error channel bought down exponentially, the other paid
for linearly, and a repetition code — the simplest classical code there is —
left to mop up.

**The single-qubit record.** A cat qubit with **bit-flip times exceeding 10
seconds** — a four-order-of-magnitude improvement over prior implementations
— with **phase-flip times above 490 nanoseconds**, and with quantum phase
control demonstrated without breaking the bit-flip protection [CITE: Réglade
et al. (ENS/Inria/Alice & Bob), "Quantum control of a cat qubit with bit-flip
times exceeding ten seconds", *Nature* 629, 778–783 (2024), doi
10.1038/s41586-024-07294-3; arXiv:2307.06617]. Those two figures, taken at
face value, describe an idle qubit whose two error channels differ by roughly
seven orders of magnitude [OPEN: arithmetic on the two quoted figures; note
both are reported as bounds ("exceeding", "above"), so this is a
characterization of the quoted operating point, not a bound on the bias].

**The logical-qubit result.** The strongest hardware result on this platform
is a memory: cat qubits concatenated with an outer distance-5 repetition
code, ancilla transmons performing syndrome measurement, a stabilizing
circuit passively protecting against bit flips, and a cat–transmon
noise-biased two-qubit gate. The phase-flip-correcting repetition code
**operates below threshold**, and the logical bit-flip error is suppressed as
the cat mean photon number increases. The minimum measured logical error per
cycle is **1.75(2)% for the distance-3 code sections and 1.65(3)% for the
distance-5 code** [CITE: Putterman et al. (AWS Center for Quantum Computing /
Caltech), "Hardware-efficient quantum error correction via concatenated
bosonic qubits", *Nature* 638, 927–934 (2025), doi 10.1038/s41586-025-08642-7,
published 26 February 2025 — the Ocelot device].

**The theory the resource claims come from.** The repetition-cat architecture
was proposed as a route to "a universal set of fully protected logical gates"
that avoids magic-state preparation, distillation and injection [CITE:
Guillaud & Mirrahimi, "Repetition Cat Qubits for Fault-Tolerant Quantum
Computation", *Phys. Rev. X* 9, 041053 (2019)]. Its best-known costing:
Shor's algorithm on a 256-bit elliptic-curve discrete logarithm in **9 hours
with 126,133 cat qubits**, at 19 average photons per cat state, a 500-nanosecond
cycle, and an **assumed ratio of single-photon to two-photon losses of 1 part
in 100,000** [CITE: Gouzien, Ruiz, Le Régent, Guillaud, Sangouard, *Phys. Rev.
Lett.* 131, 040602 (2023), doi 10.1103/PhysRevLett.131.040602, published 24
July 2023]. This is a performance analysis of an architecture. Its headline
number is an output of that assumed loss ratio, and the paper says so.

**The 2026 code work.** A 2D local code construction for biased noise —
inner repetition phase-flip codes concatenated with outer high-rate bit-flip
codes — reported to outperform rectangular surface and XZZX codes for noise
bias at or above 7×10⁴, cutting qubit overhead by over 50% at the stated
operating point to reach a logical error rate of one part in a trillion
[CITE: Shanahan & Ruiz, "Elevator Codes: Concatenation for resource-efficient
quantum memory under biased noise", arXiv:2601.10786, 19 January 2026 —
**preprint; theory and numerics, no hardware**].

**Vendor position, labeled.** Alice & Bob shipped "Helium" on 11 June 2026 as
an on-premise cat-qubit system, and states 18 physical cat qubits per logical
qubit and up to 200× overhead reduction against transmon surface-code
approaches; the 18-qubit figure is the company's own theoretical calculation
and has not been independently verified against the shipped hardware. The
company also reports a September 2025 preliminary single-qubit bit-flip
lifetime of 33 to 60 minutes at 95% confidence. Its published roadmap runs
five chip generations to 100 logical qubits at a logical error rate of one in
a million by 2030, and places the company today at milestone 2: one logical
qubit at a logical error rate of about one in a hundred [all REPORTED: vendor
announcements, vendor roadmap, and trade coverage, 2026-08-24].

## 05 · THE SCALING LAW — THE EXPONENT NOBODY HAS MEASURED IN PLACE

Every chapter of this dossier's serial has had to write a law that makes
things worse as the machine grows. This chapter's law is the one that is
supposed to make things *better* — and both platforms' versions have the same
defect.

**The cat law.** Bit-flip rate falls exponentially in the cat's mean photon
number; phase-flip rate rises linearly in it [CITE: *Nature Physics* 16
(2020)]. So there is no free lunch and no unbounded win: there is an optimum,
and past it you are buying bit-flip immunity with phase-flip errors that the
repetition code must then correct. The architecture's savings all live in how
steep the exponential is *relative to* the linear cost — which is exactly the
assumed loss ratio that the 126,133-qubit costing takes as input [CITE:
*Phys. Rev. Lett.* 131, 040602 (2023)].

**The topological law.** Protection falls off exponentially in the ratio of
wire length to the coherence length, and in the ratio of the topological gap
to temperature. Every downstream promise — the near-codeless qubit, the small
array — is priced from that gap. And the gap is precisely the quantity the
published dispute is about: whether the parameter regions used are gapped at
all [CITE: *Nature* 654, E22–E26 (2026)], against the position that the
interference signal itself indicates a topological origin and that the
analysis does not assume a gap [CITE: *Nature* 654, E27–E28 (2026)].

**The law stated in one sentence, for both:** *the exponent is the product,
and in both cases the exponent's value in a working logical qubit is either
disputed or unmeasured.*

**The one place the law has been measured end to end, and what it gave.**
Take the strongest hardware datum on either platform: Ocelot's logical error
per cycle, 1.75% at distance 3 and 1.65% at distance 5 [CITE: *Nature* 638,
927–934 (2025)]. Improving the code distance by two steps improved the
logical error by a factor of about **1.06** [OPEN: arithmetic on the two
published figures]. For scale — and stated fresh here rather than by
reference — Google Quantum AI's Willow processor reported surface-code
memories below threshold with logical error suppressed by a factor
Λ = 2.14 ± 0.02 **per single distance step**, a 101-qubit distance-7 code at
0.143% ± 0.003% per cycle, and memory beyond break-even at 2.4 ± 0.3× its
best physical qubit [CITE: Google Quantum AI, *Nature* 638, 920–926 (2025)].
The two are different codes solving different halves of the problem — a
phase-flip repetition code riding on bosonic bit-flip protection versus a
full surface code — so this is not a like-for-like ranking. It is a
like-for-like statement of *demonstrated suppression per unit of added
distance*, and on that one axis the engineered-qubit platform's measured
figure is about 1.06 and the transmon platform's is about 2.14 [OPEN: this
comparison and its stated caveat are the chapter's own analytical claim].

Both numbers are below threshold. Both are real. The gap between them is
where this chapter's bet lives.

## 06 · THE TWIST — THE TWO BETS FAIL AT OPPOSITE ENDS

Set them side by side and the symmetry is exact, and it is the most useful
thing in this chapter.

**Topological is disputed at the foundation and clean at the payoff.** If
Majorana zero modes exist in these devices as claimed, nobody argues about
what follows: a qubit with a 20-second parity lifetime against microsecond
operations is an extraordinary machine, and the error-correction bill really
does mostly vanish. The whole risk is concentrated in a single yes/no about
physics — and that yes/no is currently being argued in peer review, by both
sides, in the same journal [CITE: *Nature* 654, E22–E26 and E27–E28 (2026)].

**Cat is clean at the foundation and disputed at the payoff.** Nobody argues
that the exponential exists; it was measured in 2020, reproduced at
ten-second bit-flip scale in 2024, and carried into a below-threshold logical
memory in 2025 by a different company on a different continent [CITE:
*Nature Physics* 16 (2020); *Nature* 629, 778–783 (2024); *Nature* 638,
927–934 (2025)]. The risk is spread thinly across everything downstream: the
loss ratio the costings assume, the gates that must not break the bias, the
ancillas that must not import bit flips, and a measured distance-scaling
factor near 1.06 that the roadmaps need to become something much larger.

**Which is the better risk is not this dossier's to declare — but the
asymmetry has a practical consequence worth naming.** A disputed foundation
is settled by *one* decisive experiment, and could be settled quickly. A thin
extrapolation is settled by *many* incremental ones, and settles slowly but
almost never surprises you. A portfolio that wanted one high-variance and one
low-variance engineered-qubit position would hold exactly these two. [OPEN:
this section's framing is the chapter's author-reviewed analytical claim.]

**And the finding that generalizes past this chapter.** Every platform in this
serial has been graded on a number it can improve. These two must first be
graded on a claim that is either true or false. This dossier's labeling
discipline was built for exactly that distinction, and this is the chapter
where it earns its keep: *nothing above was upgraded because a machine is
impressive, and nothing was downgraded because a claim is contested.*

## 07 · THE FIX STACK — EVERY CANDIDATE, WITH STATUS

**Fix 1 — Raise the gap (topological).** Replace aluminium with a
higher-gap superconductor; lead is the demonstrated substitution, reported
with a roughly 20-second characteristic parity switching time [CITE:
arXiv:2606.03884, preprint]. Ceiling: a larger gap strengthens the
protection *if the phase is topological* — it does not by itself answer the
existence question the Nature exchange is about.

**Fix 2 — Better bring-up metrology (topological).** The radio-frequency
technique introduced with the lead tetrons resolves low-energy wire-end
states and measures their energy splitting to microelectronvolt precision,
aimed at fast, precise device bring-up at array scale [CITE:
arXiv:2606.03884, preprint]. Ceiling: this is the strongest *methodological*
answer to the disorder critique on the table, and it is unrefereed.

**Fix 3 — Move up the roadmap to operations (topological).** The published
plan's second generation performs measurement-based braiding for Clifford
operations on two qubits [CITE: arXiv:2502.12252, preprint]. Ceiling: this is
the fix that would settle the argument, because a working braided operation
is much harder to reproduce with trivial states than a bimodal signal is.
Status: not demonstrated in the peer-reviewed record as of 2026-08-24 [OPEN].

**Fix 4 — Push the photon number (cat).** More photons, exponentially fewer
bit flips [CITE: *Nature Physics* 16 (2020)], with the logical bit-flip error
observed to fall as mean photon number rises on a working logical device
[CITE: *Nature* 638, 927–934 (2025)]. Ceiling: phase flips rise linearly, so
this trade saturates; it moves the optimum, it does not remove it.

**Fix 5 — Noise-biased gates and ancillas (cat).** The bias is only worth
what survives the operations; the cat–transmon noise-biased two-qubit gate is
the demonstrated instance [CITE: *Nature* 638, 927–934 (2025)]. Ceiling: every
new operation added to the set must be re-shown not to break the bias, which
makes the gate set — not the qubit — the platform's real scaling frontier.

**Fix 6 — Better biased-noise codes (cat).** Concatenated constructions
tailored to very high bias, reported to cut overhead by more than half at
their stated operating point [CITE: arXiv:2601.10786, preprint, theory and
numerics]. Ceiling: theory-to-hardware lag, and the constructions assume bias
figures well above what a *running* logical qubit has been shown to sustain.

**Fix 7 — Buy the exponent from someone else.** Biased-noise and
erasure-style tricks are not exclusive to these two platforms; other
architectures are increasingly designed to exploit whatever structure their
noise already has. Ceiling — and this is the strategic risk to both bets:
**if structured noise can be manufactured cheaply on mature platforms, the
engineered qubit loses its moat while keeping its physics risk.** [OPEN:
this dossier's own analytical claim.]

## 08 · WHAT THIS DOES TO THE RACE — AND TO THIS DOSSIER'S RECORDS

**The constraint restated at bedrock.** For topological: **can the existence
of the protecting object be established to the field's satisfaction — not
asserted, not defended, but settled by a demonstration that trivial states
cannot mimic — before the decade of capital behind it runs out?** For cat:
**can the measured single-mode exponent be shown to survive gates, ancillas,
concatenation and distance, at a suppression factor the roadmaps' arithmetic
actually requires, rather than the factor near 1.06 that hardware has so far
delivered [CITE: *Nature* 638, 927-934 (2025)]?** Both are the same wager priced differently: a physics claim
substituting for an engineering bill.

**Chapter 1 inheritances, updated — one upgraded, one sharpened.** Chapter 1
recorded, as REPORTED, that "the reviewers of the flagship result noted it
does not by itself evidence the underlying Majorana modes". That is now
**CITE-grade and stronger than recorded**: the statement is the journal's own
editorial note in the peer-review file, and the dispute has since been
published in *Nature* itself as a Matters Arising with a Reply [CITE: *Nature*
654, E22–E26 and E27–E28 (2026)]. Chapter 1 also framed the cat bet as
turning on "whether single-mode suppression scales as projected"; this chapter
sharpens that from a question into a measured baseline — the scaling has been
demonstrated below threshold, at a distance-suppression factor of about 1.06
[CITE: *Nature* 638, 927–934 (2025); OPEN: the arithmetic]. The Chapter 1
constraint choice — "existence and extrapolation" — survives the drill
unchanged: this chapter elaborates it and does not correct it.

**What it does to the race.** Neither platform currently competes on the
leaderboard the other five are on, and this dossier declines to place them
on it by analogy. Cat has a below-threshold logical memory and no logical
gates on it; topological has neither, and has a live argument about whether
its qubit exists. What both have is the only thing that could make the
rest of the leaderboard irrelevant: a route in which the overhead never has
to be paid.

## 09 · THE CHAPTER'S BETS — DEPOSITED TO THE REGISTRY

Two platforms, two bets — because one signpost cannot resolve two different
kinds of uncertainty.

**B9 — The qubit, not the parity.** *By 2029-06-30, a peer-reviewed journal
publication reports a topological (Majorana-based) qubit on which at least
two non-commuting logical operations are performed on the same encoded qubit,
with a quantitative error rate stated for at least one of them.* Resolution: a
peer-reviewed journal publication meeting the italicized terms; preprints do
not resolve it, and the peer-review requirement is deliberate and load-bearing
given this chapter's record. Resolves TRUE/FALSE on the date. Rationale: the
platform's published record today is a parity measurement plus a published
dispute over its interpretation; its own roadmap places single-qubit
benchmarking as the first of four generations [CITE: arXiv:2502.12252]. The
20-second parity lifetime and the higher-gap lead devices are exactly the
precondition for measurement-based operations, which argues for yes; the bet's
binding term is peer review, and the flagship result drew a Matters Arising in
the same journal, which argues for no. Probability: **~20%** [AI-drafted
estimate (author-delegated 2026-07-17); the author may override].

**B10 — The exponent shows up in the logical error.** *By 2028-12-31, a
cat-qubit or comparable bosonic-plus-repetition platform publicly reports a
logical qubit memory whose measured logical error per cycle improves by a
factor of at least 2 between two code distances measured on the same device.*
Resolution: an arXiv preprint or journal paper reporting measured logical
error per cycle at two or more code distances on one device, with a ratio of
at least 2; resolves TRUE/FALSE on the date. Rationale: the current
published figure is about 1.06 across two distance steps [CITE: *Nature* 638,
927–934 (2025); OPEN: the arithmetic], which places the demonstrated operating
point just barely below threshold; a factor of 2 requires the physical error
rate to sit roughly a factor of 2 under the code's threshold, which is a
concrete, fundable engineering target rather than a new physical principle —
and it is the number every published cat costing implicitly assumes.
Probability: **~35%** [AI-drafted estimate (author-delegated 2026-07-17); the
author may override]. Two well-capitalized industrial groups are working the
problem on two continents, which argues for higher; the standing pattern this
dossier has now verified on six platforms — *the composing experiment is
always the hard part* — argues for lower.

## 10 · METHOD NOTE

Every CITE above was checked on 2026-08-24 against the named primary source
(arXiv abstract page, Nature-family publication record, or publisher abstract
page), with two exceptions labeled in place: the *Nature* peer-review file
quotation, reproduced at coverage grade from technical coverage because the
file itself is not openly retrievable, and specific device figures reproduced
from trade coverage, marked REPORTED. Preprints are labeled as preprints
everywhere they appear, including Microsoft's roadmap and lead-tetron results
and Alice & Bob's code work, because on this platform above all the
refereed/unrefereed line is the thing under discussion. The scaling
comparison in §05 is labeled analysis: it compares demonstrated suppression
per unit of added code distance across two different codes, and states that
caveat rather than burying it. Both sides of the topological dispute are
recorded at equal prominence and neither is adopted. Created with heavy AI
use, and limited human oversight, to test the capabilities of contemporary
state-of-the-art AI.

*Next: Chapter 8 — the recost. Every platform in this serial on one ruler, and an answer to "which one".*
