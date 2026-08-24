# CHAPTER 5 — PHOTONICS: THE LOSS DRILL, WORSE
## The platform that traded every error for one error, and bet the factory on it
### DRAFT v3 (v2 superseded pre-commit: the executor caught v2 attributing the caveat quote jointly to two sources when the verbatim phrase appears only in the published Nature abstract; the arXiv v1 abstract carries a shorter form; v3 attributes each exactly) — every number below verified against the named primary source on 2026-08-24 unless labeled REPORTED.

Status legend: **CITE** = verified against the named primary source on
2026-08-24. **REPORTED** = interested-party or secondary source, recorded but
not adopted. **OPEN** = the author's own analytical claim. **FORECAST** = a
dated, falsifiable bet with a resolution mechanism.

This chapter is self-contained: nothing below requires reading any other
chapter.

---

## 01 · THE MACHINE, PHYSICALLY

A photonic quantum computer stores its qubits in particles of light. One
photon, guided through a glass-like channel (a silicon-nitride waveguide)
etched on a chip, can encode a qubit in which of two parallel channels it
travels ("dual-rail"), or — in the continuous-variable approach — a qubit
can live in the wave-like properties of a specially prepared pulse of
squeezed light (a "GKP" state, which hides a digital qubit inside an analog
waveform with error correction built into the encoding itself).

Three consequences of choosing light, before any engineering:

**No refrigerator for the qubits.** Photons don't need millikelvin. The
chips run at room temperature, with only the single-photon *detectors*
needing a cryostat at a few kelvin. **Networking is native.** The qubit *is*
the thing that already travels down telecom fiber — connecting modules means
plugging in a cable, not inventing a transducer. **And photons do not talk
to each other.** That is the platform's original sin: two photons crossing
paths ignore each other completely, so there is no direct two-qubit gate at
all. Every entangling operation is indirect — interfere photons on a beam
splitter, measure, and let quantum mechanics do the rest — and such "fusion"
operations *fail by design* a large fraction of the time, succeeding only
probabilistically. The architecture that embraces this is measurement-based:
manufacture huge entangled resource states, then compute by measuring them,
routing around every failed fusion with redundancy.

So the machine is not a processor in the usual sense. It is a **photon
factory**: sources firing billions of times per second, switches routing
survivors, detectors consuming everything, and the computation living in the
statistics of what got measured.

## 02 · WHAT "LOSS, WORSE" MEANS

Chapter 2 of this dossier drilled atom loss: an atom escapes its trap, the
qubit vanishes. Photonics has the same failure — a photon absorbed in a
waveguide, scattered at an interface, missed by a detector, is a qubit gone —
but three compounding features make it the platform's entire biography
rather than one line in its error budget:

**(a) Everything is loss.** A photon in flight barely decoheres, doesn't
crosstalk, and can't be heated — the error channels that fill other
platforms' budgets mostly don't exist here. What remains is loss, at every
single component the photon touches. The platform traded a zoo of errors for
one predator.

**(b) The gates volunteer to fail.** Fusion operations are probabilistic
even at zero loss. Loss doesn't just erase qubits; it multiplies against an
architecture already built on retrying, so redundancy costs compound —
which is why the platform's own descriptions speak of millions of photons
in flight to support the error-corrected computation [REPORTED: platform
descriptions in survey coverage].

**(c) Photons cannot wait.** Light in fiber moves about 20 centimeters
every nanosecond and cannot be parked. "Storing" a photonic qubit means
sending it down a delay line — and delay lines are made of the very medium
that eats photons. **On this platform, loss is a tax on time itself**: every
nanosecond of waiting is meters of glass, and meters of glass are percent
of qubit. That is the sense in which this is the loss drill, worse.

## 03 · THE VERIFIED STATE OF THE ART

**The manufacturability landmark (PsiQuantum, Omega).** Published in Nature
641, 876–883 (2025) (doi: 10.1038/s41586-025-08820-7; arXiv:2404.17570;
online Feb 2025): a photonic chipset fabricated
in GlobalFoundries' commercial 300 mm silicon-photonics fab — sources,
superconducting single-photon detectors, and switching integrated on
industry-standard wafers. The benchmark fidelities [CITE: Nature paper via
its published figures, cross-reported identically in Optica/OPN and
technical coverage]: **99.98% ± 0.01% state preparation and measurement**
for dual-rail qubits, **99.5% quantum-interference visibility** between
independent sources, **99.22% ± 0.12% two-qubit fusion-gate fidelity**, and
**99.72% ± 0.04% chip-to-chip interconnect fidelity over 42 meters of
fiber**. And the caveat this dossier considers the most important sentence
in the paper — with its provenance stated exactly, because the two public
versions differ: the **published Nature abstract** states, verbatim, that
these fidelities are **"conditional on photon detection and not accounting
for loss"** [CITE: Nature 641, 876–883 abstract at nature.com, mirrored at
ADS, verified 2026-08-24], while the **arXiv v1 abstract** (2404.17570)
carries only the shorter "not accounting for loss" [CITE: arXiv abstract,
verified 2026-08-24]. Peer review *strengthened* the caveat — the journal
version is the more explicit about what the record numbers exclude, which
this dossier notes with approval. Read the caveat twice: the record numbers describe the
photons that *survived*. Loss is not inside those fidelities; loss is the
thing that decides how many photons get to have a fidelity at all.

**The component loss ledger (same platform, next-generation parts)** [CITE:
reported figures from the Nature-paper coverage]: silicon-nitride waveguides
at **0.5 ± 0.3 dB per meter**; photon-number-resolving detectors at **98.9%
median efficiency**; electro-optic (barium titanate) switching at a
loss-voltage product of **0.33 dB·V**; edge couplers at **52 ± 12
millidecibels** (~1.2% loss) to fiber — the abstract names this
next-generation suite (SiN waveguides, PNRDs, BTO switching, low-loss
chip-to-fibre coupling) as the paper's preview toward the fault-tolerant
regime [CITE: abstract]; the specific figures are from the paper's body as
reproduced in technical coverage [CITE at that grade]. The vendor's own framing of the
interface war: chip-to-fiber coupling losses cut from an industry-standard
~50% to **~1%**, "enabling die-to-die networking at error-correction-
compatible levels," and on-chip interferometers at up to 99.999% fidelity
[REPORTED: vendor technology pages — interested party, but *primary* for
what the vendor claims its own budget must be; note the vendor's ~1%
standard is itself the clearest public statement of the per-interface loss
scale the architecture demands].

**The system landmark (Xanadu, Aurora).** Published in Nature 638 (2025): a
modular photonic machine — **12 qubits across 35 photonic chips in four
server racks, interconnected by 13 km of optical fiber, at room
temperature, running real-time error-correction decoding** on GKP-encoded
qubits [CITE: Nature 638 / arXiv record and the company's announcement].
The honest asterisk, carried in the technical coverage: **the GKP state
quality remains above (worse than) the fault-tolerance threshold**
[REPORTED: technical survey coverage] — the architecture ran end-to-end;
the qubits are not yet good enough for the error correction to win.
Follow-ups: first **on-chip generation of optical GKP states** (Nature,
June 2025) [REPORTED: multiple secondary]; a claimed **60% optical-loss
reduction in 2025 and 20× over three years** [REPORTED: company statements
at listing].

**Money and roadmaps, labeled.** PsiQuantum: $1B Series E at ~$7B valuation
(Sept 2025), DARPA US2QC Phase 3 selection, quantum compute centers
breaking ground in Chicago and Brisbane; aggregator claims of "1 million
physical qubits targeting 2027" [REPORTED: vendor projections and
secondary tracking — interested parties, recorded not adopted]. Xanadu:
public listing (2026, ~$302M gross), DARPA QBI Stage B [REPORTED]. This
platform now carries the largest private capital in quantum computing
[REPORTED] — a fact the race chapter must weigh, and this chapter merely
records.

**What does not exist.** As of the March 2026 survey framing, **no photonic
platform has demonstrated a below-threshold logical qubit** [REPORTED:
tracker standard; Aurora's 12 error-decoded GKP qubits are the closest
approach and are above threshold per the coverage]. Chapters 2–4 verified
below-threshold or beyond-breakeven logical qubits on atoms, superconductors,
and ions; photonics is the front-runner platform by capital and the
rear-runner by that specific, decisive metric.

## 04 · THE SCALING LAW — DECIBELS COMPOUND

Loss in optics is measured in decibels, and decibels *add* along a photon's
path — which means the surviving fraction *multiplies*. The student
arithmetic, from the cited components: a waveguide at 0.5 dB/m costs ~11%
of photons per meter traveled; every chip-to-fiber interface at the
achieved ~52 mdB costs ~1.2%; a 98.9%-efficient detector costs 1.1% at the
finish line. A photon that must traverse a source, meters of routing, a
switch network, a fusion, and a detector spends a budget of order **single
percent per element against a total the architecture's own vendor pegs at
~1%-per-interface "error-correction-compatible" levels** [OPEN: composition
of cited figures; the per-element numbers are CITE, the budget framing is
the vendor's own standard]. Then the probabilistic-gate multiplier stacks
on top: every failed fusion means the redundancy machinery spends more
photons, each of which pays the same loss gauntlet.

Written as a law: **yield ∝ (transmission)^(path elements), and resource
cost ∝ 1/yield — the machine's economics are exponential in path length.**
This is why the platform's history is a war on tenths of a decibel, why a
"60% loss reduction" is a headline [REPORTED], and why photonics is the
only platform whose scaling metric is a unit of *attenuation*. Chapter 2's
atoms lose exp(−N·T/τ) to time; photons lose exponentially to *distance
traveled* — and since waiting is traveling (§02c), they lose to time too,
at the speed of light.

## 05 · THE TWIST — ONE ENEMY, FULLY INSTRUMENTED, AND A FACTORY TO FIGHT IT

Here is the platform's elegant counter-story, and it rhymes with Chapter 2's
twist so precisely that this dossier flags the rhyme as a finding:

**Loss is the best-behaved catastrophic error in quantum computing.** A lost
photon is heralded at the detector — photon-number-resolving detectors
[CITE: 98.9% median efficiency] literally count what arrived, so an absence
is *data*, exactly the located-erasure gold standard Chapter 2 drilled.
Photons that do arrive are pristine: no decoherence budget, no crosstalk
matrix, no leakage zoo — which is precisely why the platform's conditional
fidelities (§03) can carry four nines while the machine's completion metric
lags. And the GKP encoding goes one step further: it builds a first layer of
error correction *inside each light pulse*, so the qubit arrives wearing its
own armor [CITE: architecture as published in the Aurora paper's framing].

The platform's wager, stated plainly: **reduce the fight to a single scalar
(dB), then win it with the largest manufacturing base on earth.** The chips
come off the same 300 mm commercial lines as classical silicon photonics
[CITE: Omega, fabricated at GlobalFoundries]; iteration speed is fab-cadence,
not lab-cadence; and the roadmap is datacenters of racks joined by telecom
fiber [CITE: Aurora's 13 km, four racks; vendor compute-center plans
REPORTED]. Every other platform fights a vector of enemies with bespoke
apparatus; this one fights a scalar with a foundry. Whether that trade wins
is exactly the open question §07 sharpens — but it is a *coherent* trade,
and the only one in the race whose limiting resource is industrial process
control rather than new physics. [OPEN: this framing paragraph is the
chapter's author-reviewed analytical claim.]

## 06 · THE FIX STACK — EVERY CANDIDATE, WITH STATUS

**Fix 1 — The decibel war (fabrication).** Status: **the main event,
measurably moving**: 0.5 ± 0.3 dB/m waveguides [CITE], interfaces cut
~50% → ~1% [REPORTED-vendor], a claimed 20× platform-loss improvement in
three years [REPORTED]. Ceiling: asymptotic — every tenth of a dB is harder
than the last, and the exponent (§04) never forgives.

**Fix 2 — Multiplex and switch.** Fire many probabilistic attempts in
parallel, then route the successes onward with fast, low-loss switches —
the vendor names this the key to overcoming nondeterminism [REPORTED-vendor;
the barium-titanate switch component is CITE at 0.33 dB·V]. Ceiling: the
switch itself is in the loss path; multiplexing spends hardware to buy
determinism.

**Fix 3 — Encoded fusion / architectural redundancy.** Fusion-based quantum
computing encodes each fusion attempt so that failures and losses are
correctable events rather than fatal ones [REPORTED: architecture
literature]. Ceiling: redundancy is photons, photons pay the gauntlet.

**Fix 4 — GKP and bosonic encoding.** Error correction inside the pulse;
demonstrated on-chip generation (Nature, June 2025) [REPORTED]; a published
protocol for implementing arbitrary codes over GKP qubits with reduced
physical overhead [REPORTED: PRL 2025 via secondary]. Ceiling: **state
quality is the whole game and is currently above threshold** [REPORTED] —
this is the platform's version of every other chapter's "the composing
experiment is the hard part."

**Fix 5 — Detectors.** 98.9% median-efficiency photon-number resolution,
integrated on-chip [CITE]. Ceiling: the last percent, forever.

**Fix 6 — The factory itself.** Commercial-foundry fabrication at
standard-semiconductor yields [CITE: Omega at GlobalFoundries; vendor yield
claims REPORTED]. Not a physics fix — the platform's bet that it doesn't
need one.

## 07 · WHAT THIS DOES TO THE RACE — AND TO THIS DOSSIER'S RECORDS

**The constraint restated at bedrock.** Photonics' binding constraint is
not "photons get lost" — that is the platform's chosen, singular battlefield.
It is: **can industrial decibel-reduction and GKP state quality cross their
thresholds before the platforms that already have below-threshold logical
qubits compound their lead — with the added asymmetry that photonics'
progress metric (dB, foundry yield) improves on manufacturing cadence while
its rivals' improves on physics cadence?** The platform holds the race's
best factory story, its most capital, and — uniquely — zero demonstrated
below-threshold logical qubits. Both halves of that sentence are load-
bearing, and this dossier declines to resolve them by vibes.

**The map-dossier conviction, checked but not scored.** The author's prior
publication registers a tracked conviction (QCF8) that quantum computing's
long-term endpoint is optical. This chapter is the drill that conviction was
waiting for, and the drill returns a split verdict: the endpoint logic
(native networking, room temperature, foundry scaling) verified stronger
than the map assumed; the present-tense standing (no below-threshold
logical qubit; conditional-on-detection records) verified weaker. QCF8
belongs to the map dossier's registry and is graded there, on its own
timeline — recorded here, deliberately unscored. [OPEN: cross-dossier note.]

**Chapter 1 inheritances.** Ch1's platform card said the whole platform
"lives or dies on driving optical loss below the fault-tolerance
threshold" — this chapter verifies that framing and sharpens it: the
threshold fight is currently being *lost at the GKP-quality layer*
[REPORTED] while being *won at the component layer* [CITE], and the race
between those two layers is the platform's actual clock.

## 08 · THE CHAPTER'S BET — DEPOSITED TO THE REGISTRY

**B7 — The pulse crosses the line.** *By 2028-12-31, a photonic platform
publicly reports optical GKP states, generated on an integrated (on-chip)
platform, whose measured quality the publishing team itself states to be at
or below the relevant fault-tolerance threshold of its stated architecture.*
Resolution: an arXiv preprint or journal paper making the italicized claim
in its own text, plus at least one independent secondary report; resolves
TRUE/FALSE on the date. Rationale: this is the platform's named missing
piece (§03, §06-Fix-4) — the below-threshold moment that Chapters 2–4's
platforms each already had — and the claimed loss trajectory [REPORTED:
60%/year] makes two and a half years a real but unsafe runway. Probability:
**~35%** [AI-drafted estimate (author-delegated 2026-07-17); the author may
override]. Below coin-flip because the last decibels are the hardest ones,
and because "the team itself states below-threshold" is a deliberately hard
resolution bar that vendor communications have every incentive to blur —
the bet is designed so that blur resolves FALSE.

## 09 · METHOD NOTE

Every CITE above was checked on 2026-08-24 against the named primary source
or, where flagged, against technical coverage that reproduces the paper's
figures; the distinction is labeled in place. The Omega caveat's two public
versions (published Nature abstract vs arXiv v1) are quoted separately at
their exact wording — a pre-commit catch by the executor, recorded in the
version header. REPORTED items name
their non-primary provenance; vendor claims are flagged as interested-party
statements even when the vendor is the only primary source for its own
standard. The §04 composition is labeled analysis. The QCF8 note is
cross-dossier bookkeeping, not a score. Created with heavy AI use, and
limited human oversight, to test the capabilities of contemporary
state-of-the-art AI.

*Next: Chapter 6 — Silicon spin. The yield drill.*
