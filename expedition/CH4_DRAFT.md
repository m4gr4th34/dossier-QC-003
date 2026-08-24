# CHAPTER 4 — TRAPPED IONS: THE CLOCK-SPEED DRILL
## The best qubits in physics, computing two percent of the time
### DRAFT v1 — every number below verified against the named primary source on 2026-08-24 unless labeled REPORTED.

Status legend: **CITE** = verified against the named primary source on
2026-08-24. **REPORTED** = interested-party or secondary source, recorded but
not adopted. **OPEN** = the author's own analytical claim. **FORECAST** = a
dated, falsifiable bet with a resolution mechanism.

This chapter is self-contained: nothing below requires reading any other
chapter.

---

## 01 · THE MACHINE, PHYSICALLY

A trapped-ion quantum computer stores its qubits in single charged atoms —
barium or ytterbium with one electron removed — floating in ultra-high vacuum,
pinned in place not by light but by oscillating electric fields from a
microchip beneath them. Because each ion is electrically charged, the trap
grips it fiercely, and because every barium ion in the universe is *exactly*
identical, there is no fabrication variation, no device-to-device spread:
nature manufactures the qubits, perfectly, for free.

The qubit lives in two hyperfine states of the ion — energy levels so stable
that coherence times run to **minutes** [CITE: arXiv:2605.22463, 2026], while
lasers perform every operation: cooling the ions to near stillness, flipping
their states, entangling neighbors through their shared vibrations (two ions
in one trap repel each other, so they swing like pendulums coupled by a
spring — push one quantum-mechanically and the other feels it), and reading
them out by making them fluoresce. The flagship machine of this platform,
Quantinuum's Helios, is a "QCCD" — a quantum charge-coupled device — in
which **98 barium-137 ions are physically shuttled, individually or in
pairs, between eight interaction zones** where all operations happen [CITE:
Quantinuum Helios Product Data Sheet v1.2, 2026; system paper: Nature 655,
81–86 (2026)]. Any ion can be brought next to any other: **all-to-all
connectivity**, the platform's structural superpower, and the thing every
flat superconducting chip envies.

The fidelity records are the platform's calling card, and they are now
Nature-verified: averaged over all of Helios's zones, single-qubit gate
infidelity **2.5(1)×10⁻⁵**, two-qubit **7.9(2)×10⁻⁴**, state preparation
and measurement **3.3(5)×10⁻⁴** — and the paper adds that none of these is
fundamentally limited [CITE: Nature 655, 81–86 (2026), abstract]. These are
the best all-around numbers on any commercial quantum computer.

So: perfect qubits, minutes of memory, everyone talks to everyone, best
fidelities in the business. The catch is the clock.

## 02 · WHAT THE CLOCK PROBLEM IS — AND WHERE THE TIME ACTUALLY GOES

A superconducting two-qubit gate takes tens of *nanoseconds*. A trapped-ion
two-qubit gate takes tens to hundreds of *microseconds* — a thousand to ten
thousand times longer [REPORTED: standard figures via secondary surveys;
the ratio, not the precise values, is load-bearing here]. That alone would
be a serious handicap. But the drill goes deeper, and what it finds is the
chapter's central fact:

**The gates are not where the time goes.** In the platform's own accounting
of a seminal QCCD demonstration: quantum gate pulses occupied **~2% of
system runtime; ion movement ~27%; cooling ~68%** [CITE: IonQ technical
blog, 2025-10-21, describing the published QCCD demonstration record]. The
same source explains the subtlety: ions can be moved fast, but movement is
deliberately slowed *to keep them cold* — so the transport bottleneck is
really a cooling bottleneck. Independent theory literature agrees on the
shape: circuit execution time is dominated by shuttling, often more than
half the total runtime, with large circuits requiring over 10,000 shuttling
operations [CITE: arXiv:2605.22463]; and conventional sympathetic cooling of
a mixed-species crystal can take **milliseconds per cooling step, per mode**
[CITE: Nature Communications 15, 1089 (2024), introduction].

Why does everything need re-cooling? The two-qubit gates couple ions through
their shared motion — which only works if that motion starts near its
quantum ground state. Every transport, every trap wobble, every stray field
heats the ions, and hot ions gate badly. So the machine's inner loop is:
move, cool, gate, move, cool, gate — with "cool" eating the schedule. **A
trapped-ion computer is a superb quantum processor wrapped in a
refrigeration workflow, and the workflow is the clock.**

## 03 · THE VERIFIED STATE OF THE ART

**The logical-qubit result (the platform's flank of the race).** On Helios,
Quantinuum reports — in a March 2026 preprint — computations using **94
error-detected and 48 error-corrected logical qubits from 98 physical
ions**, via "iceberg" codes ([[k+2,k,2]], two ancillas per block)
concatenated into distance-4 error-correcting codes, with logical error
rates 10–100× below physical across benchmarks and a 94-logical-qubit GHZ
state at 94.9% fidelity [REPORTED: arXiv preprint per Quantum Computing
Report and vendor announcement; preprint-level, not yet peer-reviewed]. Two
precision notes this dossier is obligated to make, because its own bet
registry rides on them: (i) 48 from 98 is an encoding rate of **0.49 —
just under** the ≥ 1/2 threshold of registered bet B1; (ii) iceberg codes
have stabilizers that touch *every* qubit in the block — they are
**not** low-density parity-check codes, so B1's "qLDPC" condition is not
met either. B1 remains genuinely open. What the result does establish: the
all-to-all connectivity that makes high-rate codes natural is not a
neutral-atom monopoly — ions run hardware logical operations at ~2:1 too,
and did it on a shipping commercial machine.

**Module-linking, both flavors, demonstrated.** Matter-link: ions physically
transferred between adjacent microchip modules at **2,424 per second with
transport-loss infidelity below 7×10⁻⁸**, without measurable phase-coherence
impact [CITE: Nature Communications 14, 531 (2023), abstract]. Photon-link:
two trapped-ion modules two meters apart running a *distributed algorithm* —
a teleported controlled-Z gate at **86% fidelity**, Grover's search across
modules at 71% success [CITE: Nature 638, 383–388 (2025); arXiv:2407.00835].
Reported rates elsewhere in the literature reach ~250 entangled pairs/second
with continuous cooling, and 1.2 km multiplexed links at 95.9% fidelity
[REPORTED: PRL 2024 and arXiv:2510.20392 via secondary survey]. The honest
gap, stated by the field's own July 2026 synthesis: **remote entanglement
trails local gates by about two orders of magnitude in both rate and
fidelity** [CITE: arXiv:2607.18387, abstract], with an architecture
projecting — not demonstrating — 99.9% Bell pairs at fault-tolerance-
compatible rates.

**Vendors and roadmaps, labeled.** Quantinuum: Helios shipping (98 ions,
above numbers CITE); roadmap Sol (hundreds of qubits, ~2027) then Apollo
(thousands, fault-tolerant, ~2029); the Sol→Apollo jump is the roadmap's
acknowledged largest step and its method is not yet public [REPORTED].
IonQ: Tempo (64 algorithmic qubits, barium) shipping; a 2025 world-record
**99.99%+ two-qubit fidelity without ground-state cooling** via the Oxford
Ionics "smooth gate" technique — significant here precisely because it
attacks the *cooling* bottleneck, not just fidelity [REPORTED: vendor
announcement + preprint]; roadmap claims of 256-qubit prototypes in 2026
and millions of qubits by 2030 [REPORTED: vendor projections, interested
party, recorded not adopted].

## 04 · THE SCALING LAW — THE USEFUL-WORK FRACTION

Chapter 2's law was exp(−N·T/τ); Chapter 3's was a per-qubit cost ledger
against fixed ceilings. This platform's law is an efficiency ratio:

**W = the fraction of wall-clock spent doing quantum gates.** Measured
QCCD accounting puts W at roughly **2%** (§02) — the other ~98% is moving
and re-chilling atoms. And the platform's error-correction cycle — the
heartbeat of any fault-tolerant machine — runs at millisecond scale once
shuttling and cooling are included, against the ~1.1 microsecond cycle
Chapter 3 verified for superconducting hardware [CITE for the SC figure:
Nature 638, 920–926; the ion ms-scale is composed from the CITE'd cooling
and shuttling figures above and labeled analysis]. The arithmetic a student
can do: **a fault-tolerant computation that a superconducting machine
finishes in a day would, at a ~1000× slower error-correction heartbeat and
equal cycle count, run for roughly three years on ions** [OPEN: illustrative
composition of cited figures; equal-cycle-count is generous to no one and
real algorithms differ — the point is the order of magnitude, and it is the
platform's own stated reason for attacking the cooling bottleneck].

What buys this back: fidelity and connectivity mean ions need *fewer*
cycles — smaller codes at equal logical error, high-rate codes run
natively, minutes of coherence mean the clock pressure is about throughput,
not survival. The race question this chapter sharpens: **is a 10× saving in
qubits and cycles worth a 1000× slower heartbeat?** For small, deep-value
computations (the current era), demonstrably yes — ions hold the
logical-qubit efficiency records on hardware. For long algorithms (the
destination era), no known code discount covers three orders of magnitude
of clock. The platform's own leaders act like they agree: the record they
chose to chase in 2025 was a *cooling-free gate*.

## 05 · THE TWIST — THE CLOCK PROBLEM IS A REFRIGERATION PROBLEM

The naive reading of "ions are slow" blames the gates. The measured reading
(§02) says the gates are innocent bystanders at 2% — **the platform is slow
because it spends its life re-cooling atoms that its own operations heat
up.** That reframing matters because refrigeration workflows, unlike laser
physics, have engineering headroom:

- **Exchange cooling** replaces the slow two-species sympathetic scheme with
  a bank of pre-chilled same-species "coolant" ions swapped in on demand:
  demonstrated with the full transport in **107 µs — an order of magnitude
  faster than typical sympathetic cooling — removing over 96% of the motional
  energy** [CITE: Nature Communications 15, 1089 (2024)].
- **Cooling-free gates**: the 2025 record two-qubit gate that simply *does
  not require* ground-state cooling (§03) — if it scales, it deletes the
  68% line item rather than shrinking it [REPORTED: vendor + preprint].
- **Gate-integrated transport scheduling** (the compiler's share): shuttling
  research treats schedule optimization as a first-class runtime lever
  [CITE: arXiv:2605.22463].

None of these is speculative physics; all are demonstrated or shipping
techniques aimed at the measured 95–98% overhead. That is why this chapter's
bet (§08) is a clock bet, not a fidelity bet.

## 06 · THE FIX STACK — EVERY CANDIDATE, WITH STATUS

**Fix 1 — Kill the cooling tax.** Exchange cooling (demonstrated, 107 µs
[CITE]); cooling-free record gates (demonstrated at two-ion scale,
vendor-reported [REPORTED]); continuous sympathetic cooling during photonic
entanglement [REPORTED]. Ceiling: integration into full QCCD workflows at
scale — every technique is demonstrated *separately* (a pattern this
dossier has now seen on three platforms).

**Fix 2 — Stop shuttling so much.** Grid/2D QCCD architectures with junction
transport and small optimal chain sizes (~15–25 ions per zone) [REPORTED:
architecture literature]; more parallel gate zones (Helios: 8 interaction
zones for 98 ions — parallelism, not just capacity, is the scarce resource
[CITE: data sheet]).

**Fix 3 — Electronic control (fire the lasers).** Microwave near-field gates
steered by chip voltages — no per-ion laser beams — pioneered academically
and now the core of IonQ/Oxford Ionics' "electronic qubit control" scaling
story [REPORTED]. Removes the optics-bench scaling wall (each laser-driven
ion needs precision beam delivery; a million ions cannot mean a million
aligned beams). Ceiling: the technique must hold record fidelities beyond
few-ion demonstrations; the platform's whole million-qubit roadmap leans on
it [REPORTED-vendor].

**Fix 4 — Modularity, matter flavor.** Chip-to-chip ion transfer at 2,424/s
with <7×10⁻⁸ loss [CITE: Nat. Commun. 2023]. Effectively extends one QCCD
across chips; inherits the same cooling economics.

**Fix 5 — Modularity, photon flavor.** Distributed gates across modules
demonstrated (86% CZ, Grover 71% [CITE: Nature 2025]); the two-orders-of-
magnitude rate/fidelity gap to local operations is named in print, with
integrated-photonics architectures projecting closure [CITE:
arXiv:2607.18387]. This is also the platform's answer to the optics-scale
wall: many small modules instead of one impossible bench.

**Fix 6 — Faster primitive gates.** Ultrafast pulsed schemes aim at the raw
µs→ns gap [REPORTED]; secondary today, because §02 says the gate is 2% of
the problem.

## 07 · WHAT THIS DOES TO THE RACE — AND TO THIS DOSSIER'S RECORDS

**The constraint restated at bedrock.** Trapped ions' binding constraint is
not "slow gates" — that framing misreads the platform's own accounting. It
is: **can the refrigeration-and-transport workflow that consumes ~95–98% of
wall-clock be engineered down by two to three orders of magnitude — via
cooling-free gates, exchange cooling, parallel zones, and electronic
control — before the fast platforms' fidelity catches up to where the ion
quality advantage stops paying?** Both sides of that race are moving:
Chapter 3 verified superconducting fidelity climbing under error correction;
this chapter verified the ion clock attack beginning at the exact line item
the measurements indict.

**Chapter 1 inheritances, updated.** Ch1 carried "Quantinuum 48 logical
qubits from 98 ions" as REPORTED; now anchored: the *system* and its
fidelities are Nature-verified [CITE: Nature 655, 81–86 (2026)]; the 48-LQ
iceberg result stands at preprint grade [REPORTED], with the B1-bearing
precision drawn in §03 (rate 0.49 < 1/2; iceberg ≠ LDPC; **B1 and B2
unchanged** — though B2's implicit story, neutral atoms first to high-rate
qLDPC gates, now has ions visibly close behind at 0.49 on shipping
hardware; the registered 45% is under honest pressure and moves only on a
resolution-grade event, per this registry's standing rule).

## 08 · THE CHAPTER'S BET — DEPOSITED TO THE REGISTRY

**B6 — The heartbeat accelerates.** *By 2028-06-30, a trapped-ion
experiment publicly demonstrates a complete quantum-error-correction cycle
(full syndrome extraction round on at least one error-corrected logical
qubit, including all required transport and cooling) with total wall-clock
time ≤ 100 microseconds.* Resolution: an arXiv preprint or journal paper
reporting hardware data meeting the italicized terms; resolves TRUE/FALSE
on the date. Rationale: this is a ~10× cut from the millisecond-scale
status quo, aimed exactly where the measured overhead lives; the
ingredients exist separately (107 µs exchange cooling [CITE], cooling-free
gates [REPORTED], parallel zones [CITE: data sheet]) and — a pattern this
dossier has verified on every platform so far — *the composing experiment
is always the hard part*. Probability: **~30%** [AI-drafted estimate
(author-delegated 2026-07-17); the author may override]. Below coin-flip
for the same reason B5 is: integration walls eat schedules.

## 09 · METHOD NOTE

Every CITE above was checked against the named primary source (arXiv
abstract or full text, Nature abstract, Nature Communications abstract, or
the vendor's own primary document, labeled as such) on 2026-08-24. REPORTED
items name their non-primary provenance; vendor projections are flagged as
interested-party statements. The three-year arithmetic in §04 is labeled
illustrative composition, not measurement. Created with heavy AI use, and
limited human oversight, to test the capabilities of contemporary
state-of-the-art AI.

*Next: Chapter 5 — Photonics. The loss drill, worse.*
