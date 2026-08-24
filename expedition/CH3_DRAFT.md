# CHAPTER 3 — SUPERCONDUCTING: THE WIRING DRILL
## The best qubits money can fabricate, strangled by their own umbilicals
### DRAFT v2 (supersedes v1 per erratum SR-6: v1 carried false verification dates; v1 retained in history) — every number below verified against the named primary source on 2026-08-24 unless labeled REPORTED.

Status legend: **CITE** = verified against the named primary source on
2026-08-24. **REPORTED** = interested-party or secondary source, recorded but
not adopted. **OPEN** = the author's own analytical claim. **FORECAST** = a
dated, falsifiable bet with a resolution mechanism.

This chapter is self-contained: nothing below requires reading any other
chapter.

---

## 01 · THE MACHINE, PHYSICALLY

A superconducting quantum computer is a fingernail-sized silicon chip,
patterned with aluminum and niobium circuits, hanging at the bottom of a
room-sized thermos. Cool certain metals far enough and electrical resistance
vanishes — current flows forever, losslessly. Build a small loop of such
metal, interrupt it with a "Josephson junction" (two superconductors
separated by an insulating film about a nanometer thick, through which
current quantum-mechanically tunnels), and the loop becomes an artificial
atom: a circuit with discrete energy levels you can use as 0 and 1. This is
the transmon, the workhorse qubit of Google and IBM.

Unlike a real atom, you can *print* it. Transmons are fabricated with the
same lithography family that makes classical chips — which is why this
platform scaled first, iterates fastest, and carries the industry's two
biggest balance sheets. The price of an artificial atom: it's big (hundreds
of micrometers), it's unique (no two come out identical), and it only behaves
quantum-mechanically when colder than deep space. The chip lives at the
bottom of a dilution refrigerator at 10–15 thousandths of a degree above
absolute zero, and every operation on every qubit is a precisely shaped
microwave pulse, individually generated, individually delivered.

Hold "individually delivered." That is this chapter's entire subject.

## 02 · WHAT THE WIRING PROBLEM IS — AND WHY IT ISN'T LIKE CLASSICAL WIRING

A classical chip with a billion transistors is controlled through a few
thousand pins, because the control logic lives *on the chip*. A
superconducting quantum chip enjoys no such luxury: the control electronics
are racks of room-temperature instruments, and each qubit needs its own
private microwave plumbing from that warm world down to the coldest plate —
drive lines to steer it, flux lines to tune it, readout lines to ask it
questions. Today's architecture pays three compounding costs for every line
[CITE: framing per arXiv:2512.10706, verified 2026-08-24]: the metal cable
conducts heat straight into the refrigerator; the signal attenuates over the
meters of descent, requiring attenuators at each stage that dump still more
heat exactly where cooling is scarcest; and the cables' physical bulk crowds
the finite cold real estate.

The bedrock arithmetic, from the group that engineered and published the
accounting [CITE: Krinner et al., arXiv:1806.07862, full text]: operating a
**50-qubit** processor with individual drive and flux control and multiplexed
readout requires **124 radio-frequency lines** — roughly 2.5 per qubit —
with the mixing chamber holding 14 mK, and their analysis concludes the same
cryostat could stretch to about **150 qubits** only if coaxial-line density
were tripled. Meanwhile the coldest stage's cooling budget is measured in
*millionths* of a watt — their cold plate offers about 400 µW, at a stage
already warmer than the qubits' plate. For calibration: a single LED uses
tens of thousands of times more power than the entire cooling budget of the
plate these chips live on.

And the demand side is not standing still. The most qubit-efficient
error-correcting codes — the qLDPC family this platform's roadmap bets on —
require qubits to talk to *distant* partners, connections a flat chip does
not natively have. More couplers, more control, more wiring, on a platform
already wire-bound. That is the wall: **not making qubits — feeding them.**

## 03 · THE VERIFIED STATE OF THE ART — WHAT THE PLATFORM HAS ACTUALLY SHOWN

**The flagship result (the platform's crown, and the field's).** Google's
Willow processor, 105 qubits: two surface-code memories operating **below
threshold** — the regime where making the code bigger makes the logical
qubit *better*, exponentially [CITE: Google Quantum AI, Nature 638, 920–926
(2025); arXiv:2408.13687; abstract verified]. The numbers, all from the
paper's abstract: logical error suppressed by **Λ = 2.14 ± 0.02** per
distance step, a 101-qubit distance-7 code at **0.143% ± 0.003% error per
cycle**, logical memory **beyond break-even** (outliving its best physical
qubit by 2.4 ± 0.3×), and a **real-time decoder at 63 µs average latency**
sustained over a million cycles of 1.1 µs each. This is the platform's
answer to "does error correction work here": yes, demonstrably, in real time.
(A coincidence too good to omit: the neutral-atom flagship's below-threshold
factor is *also* 2.14 — Bluvstein et al., Nature 649 (2026), 2.14(13)×.
Unrelated experiments, unrelated mathematics, same digits. The universe has
a sense of humor about leaderboards.)

**The same paper's warning shot.** Running repetition codes to distance 29,
the Willow team found logical performance limited by **rare correlated error
events striking about once every hour** (once per ~3×10⁹ cycles) [CITE: same
abstract] — bursts, cosmic-ray-class events that hit many qubits at once and
momentarily break the independence assumption every code relies on. One
event per hour per chip is survivable; a data center of chips multiplies the
clock. This is the platform's *second* wall, recorded here and drilled when
the race chapter prices it.

**The roadmap side (vendor statements, labeled as such).** IBM's published
plan [REPORTED — vendor roadmap, primary source IBM's own blog, verified
2026-08-24 as *statements of plan*, not results]: Loon (2025) introduces
"c-couplers" for long-range on-chip connections that qLDPC codes need;
**Kookaburra (2026) is to be the first module storing information in a qLDPC
memory with an attached logical processing unit**; Cockatoo (2027) entangles
modules; Starling (2029) targets 200 logical qubits and 100 million gates,
with a claimed ~90% overhead reduction from qLDPC codes. Status verified
2026-08-24: Loon was delivered and announced (Nov 2025) alongside the
120-qubit Nighthawk [REPORTED: secondary coverage; qubit/coupler counts not
primary-verified], with IBM claiming demonstration of "the cornerstones
needed to scale qLDPC codes"; **no Kookaburra delivery announcement exists
yet** — this dossier's bet B3 (~60% that it ships as roadmapped by
2026-12-31, resolution: IBM public technical announcement plus independent
coverage) remains genuinely open, with IBM's on-cadence Loon delivery as the
main supporting datum and about four months on the clock.

**The efficiency claim already in this dossier's audit table.** IBM-lineage
"Tour de Gross" architecture: ~10× qubit efficiency versus surface-code
architectures [CITE: arXiv:2506.03094, abstract, from the committed Cycle-1
ledger]. Baseline self-chosen, per the ledger's standing finding.

## 04 · THE SCALING LAW — MULTIPLY IT OUT

Chapter 2's constraint had a clean formula (survival ~ exp(−N·T/τ)). This
platform's binding law is blunter — a ledger of per-qubit costs against
fixed ceilings:

**Lines.** At the measured ~2.5 lines per qubit [CITE: Krinner], a
10,000-physical-qubit machine — the general scale a few-hundred-logical-qubit
system implies under efficient codes — wants **~25,000 coaxial lines** into
a vessel whose published stretch goal was 150 qubits' worth. Two orders of
magnitude stand between the demonstrated and the required. Nobody plans to
close that gap with more coax; everything in §06 exists because of it.

**Heat.** Every line imports heat toward stages whose budgets are micro- to
milliwatts. Move the electronics cold to cut the lines, and the electronics
*become* the heat: demonstrated cryogenic CMOS controllers dissipate **a few
milliwatts per qubit at the 4-kelvin stage** [CITE: arXiv:2509.25768,
verified 2026-08-24] — so at ten thousand qubits, tens of watts at a stage
engineered for single-digit watts. The current scaling literature frames the
task explicitly as choosing multiplexing factors and stage-wise power budgets
to fit under these ceilings [CITE: arXiv:2601.03922, 2026 review, abstract].

**Helium.** Dilution refrigerators run on helium-3, a rare isotope with no
cheap source: roughly **20 liters per unit**, and a naive linear scaling to
100,000-qubit systems "would demand large fractions of the yearly world
production" [CITE: arXiv:2512.15001, Dec 2025 review]. The refrigerant
itself is a supply-chain constraint.

Plain form for the student: **each qubit drags an umbilical, each umbilical
costs heat, space, and money, and all three are capped.** The platform's
entire scaling program is a war on the umbilical.

## 05 · THE TWIST — THE CODE IS A WIRING FIX

Here is the part that makes this platform's story elegant rather than merely
hard: its most important wiring technology is *mathematics*.

Every physical qubit you don't need is 2.5 lines you don't run, milliwatts
you don't dissipate, and helium you don't buy. So when IBM claims its qLDPC
codes cut physical-qubit overhead ~90% [REPORTED: vendor], or the Tour de
Gross paper claims ~10× qubit efficiency [CITE: abstract], those are not just
error-correction claims — **they are wiring claims.** A 10× more efficient
code is a 10× smaller cable plant, a 10× lighter heat load, a 10× smaller
helium bill. Conversely, richer codes demand richer connectivity (the
c-coupler program exists precisely to give the chip the long-range edges the
code's math wants). Hardware and code are co-designing each other in public,
and the wiring ledger is the exchange rate between them. That co-design loop
— qubits bought back by mathematics, connectivity paid for in couplers — is
this platform's distinctive move in the race, and no other platform's
constraint trades against theory this directly. [OPEN: this framing is the
chapter's author-reviewed analytical claim.]

## 06 · THE FIX STACK — EVERY CANDIDATE, WITH STATUS

**Fix 1 — Multiplexing (share the lines).** Status: **demonstrated,
standard for readout** — 6–7 qubits per readout line in the measured
50-qubit accounting [CITE: Krinner]. Ceiling: drive and flux lines resist
sharing; readout multiplexing alone leaves the ~2 individually-wired control
lines per qubit untouched.

**Fix 2 — Cryogenic CMOS (move the electronics cold).** Status:
**demonstrated at few-qubit scale** [CITE: arXiv:2509.25768]. Ceiling: the
power wall of §04 — a few mW/qubit at 4 K buys back wiring by spending the
other capped resource. The 2026 scaling literature treats cryo-CMOS as one
tier of a heterogeneous stack, not a standalone answer [CITE:
arXiv:2601.03922].

**Fix 3 — Superconducting digital logic (colder, leaner electronics).**
Status: **proposed/lab-stage**, named in the same 2026 review as the 4 K
and/or millikelvin tier of the heterogeneous stack [CITE: arXiv:2601.03922].
Ceiling: an entire electronics ecosystem to rebuild.

**Fix 4 — Optical I/O (replace metal with light).** Status: **first
closed-loop demonstration, Dec 2025** — all control and readout signals for
multiple superconducting qubits delivered exclusively via optical photons:
frequency-multiplexed optical readout of two qubits through a traveling-wave
Brillouin microwave-optical transducer, fiber-delivered control, **no
measurable coherence degradation, and single-qubit gate fidelity only 0.19%
below standard microwave operation** [CITE: arXiv:2512.21199, abstract,
verified 2026-08-24]. Optical fiber conducts ~10,000× less heat than coax
and carries many channels per strand; the same paper names the endgame —
multiple refrigerators networked from centralized room-temperature control.
Ceiling: two qubits is a proof, not a plant; transducer efficiency and noise
at scale are the open front.

**Fix 5 — Density engineering (more coax per vessel).** Status:
**continuous industrial progress** — thinner cables (passive heat scales
with diameter squared [CITE: Krinner]), flex lines, bigger vessels (IBM's
System Two class). Ceiling: buys constants, never the two orders of
magnitude.

**Fix 6 — Modularity (many small chips, quantum links).** Status:
**components demonstrated / roadmap-central** — IBM's c-couplers delivered
on Loon [REPORTED], module-to-module entanglement scheduled for Cockatoo
2027 [REPORTED: vendor]; fridge-to-fridge microwave-waveguide entanglement
has been demonstrated in the research literature [REPORTED via citing
papers; primary verification deferred to the race chapter]. Ceiling: links
between modules are themselves scarce, lossy channels — modularity converts
the wiring problem into a networking problem and bets the exchange rate is
favorable.

**Fix 7 — The code itself (need fewer qubits).** Status: **the platform's
main bet** — see §05. Kookaburra is its first scheduled hardware test, and
this dossier's B3 rides on it.

**Fix 8 — Helium economics.** Status: **industrial/engineering** — reduced
heat load per qubit, alternative cooling (continuous adiabatic
demagnetization named in the literature), supply expansion [CITE:
arXiv:2512.15001]. Ceiling: cost curve, not physics.

## 07 · WHAT THIS DOES TO THE RACE — AND TO THIS DOSSIER'S RECORDS

**The constraint restated at bedrock.** Superconducting's binding constraint
is not "the fridge is cold" — cold is solved. It is: **can the platform cut
control-and-readout cost per qubit by roughly two orders of magnitude —
in lines, in heat, in helium — faster than its qubit demand grows, while
adding the long-range connectivity its own efficiency codes require?** The
platform's unmatched advantages (fabrication iteration speed, below-threshold
error correction with real-time decoding, two industrial balance sheets) all
press against this one ceiling.

**Chapter 1 inheritances, updated.** Chapter 1 carried "Google 1
below-threshold logical qubit on Willow" as REPORTED; today's verification
upgrades it to CITE with the full numbers (§03) — the leaderboard line was
accurate and understated. IBM roadmap dates remain REPORTED-vendor by
doctrine. Bet **B3 status-checked**: substrate confirmed (Loon delivered on
cadence Nov 2025; Kookaburra unannounced as of 2026-08-24; ~4 months
remain). The ~60% stands unmodified — on-cadence delivery of the predecessor
is mild support; an unannounced successor at mid-year is mild drag; neither
justifies moving a registered number mid-flight without a resolution-grade
event. [OPEN: this status paragraph is bookkeeping, not evidence of outcome.]

## 08 · THE CHAPTER'S BET — DEPOSITED TO THE REGISTRY

**B5 — The umbilical starts to disappear.** *By 2028-06-30, a hardware
experiment publicly demonstrates ≥ 20 superconducting qubits whose control
AND readout both reach the room-temperature world through shared or optical
I/O — i.e., zero per-qubit dedicated room-temperature coaxial lines — while
sustaining two-qubit gate fidelity ≥ 99% on the same device.* Resolution: an
arXiv preprint or journal paper reporting hardware data meeting the
italicized terms; resolves TRUE/FALSE on the date. Rationale: the
all-optical closed loop exists at 2 qubits with a 0.19% single-qubit penalty
[CITE: arXiv:2512.21199]; cryo-CMOS exists at few-qubit scale; 20 qubits
with a fidelity floor forces genuine integration rather than a hero demo.
Probability: **~35%** [AI-drafted estimate (author-delegated 2026-07-17);
the author may override]. The number is deliberately below coin-flip: both
candidate technologies must clear scale-up walls (transducer noise; cryo
power) that have historically eaten schedules.

## 09 · METHOD NOTE

Every CITE above was checked against the named primary source (arXiv
abstract or full text, journal page, or the vendor's own primary statement,
labeled as such) on 2026-08-24. REPORTED items name their non-primary
provenance; vendor projections are flagged as interested-party statements
even when sourced from the vendor's own primary channel. The line-count and
heat arithmetic in §04 composes cited measurements with stated targets and
is labeled analysis, not measurement. Created with heavy AI use, and limited
human oversight, to test the capabilities of contemporary state-of-the-art
AI.

*Next: Chapter 4 — Trapped ions. The clock-speed drill.*
