# QC003 — FOUNDING HANDOFF
## An exploratory dossier: AI-led scouting of breakthrough arcs in fault-tolerant quantum computing

Date: 2026-07-14. Author: Irfan Ali Khan (m4gr4th34). Drafted by the
Strategy Room at the close of dossier-QC-Accelerate-002. This document is
the seed context for QC003's first session and its Chapter 1
(reconnaissance, non-DOI). It carries: lineage, the verified 2026
landscape, the mission and autonomy contract, the publishing doctrine,
the candidate arc portfolio, and the operating protocol.

---

## 1. LINEAGE

Predecessors: dossier-QC-Accelerate (Ch1 DOI 10.5281/zenodo.20838233) and
dossier-QC-Accelerate-002, concluded 2026-07-14 at Chapter 5 (v5.0.0, DOI
10.5281/zenodo.21360979; concept DOI 10.5281/zenodo.21270186). What -002
proved and left behind:
- Proof of principle: an automated search loop's code beat the matched-
  efficiency human benchmark 4.6x per-logical at a hardware-calibrated
  circuit-level operating point — measured, certified, sealed.
- The measurement lesson: cheap proxies for logical performance fail in
  documented, mechanistic ways; honest grading costs ~100x the field-
  standard budget; six certified operating-point truths exist as a
  calibration set; the rep-13 floor (2.31e-8) is a standing challenge.
- The decoder lesson: quantum trapping sets surfaced at circuit level;
  the decoder-created failure share is a code-decoder interaction
  spanning 8.5-63%.
- The machinery: two-agent architecture (Strategy Room decides/drafts;
  Code executes/verifies), pre-registration with mechanical resolution,
  append-only records, OpenTimestamps + optional Zenodo sealing, a
  16-catch error ledger proving the system audits its own author.
- Three live forward bets scoring at their signposts (2026-08-15,
  2026-08-31, 2026-12-31) — the honest priority-claim mechanism QC003
  should industrialize.
Template: github.com/m4gr4th34/open-dossier-template. Known template
lessons to pre-apply in the new repo: the jq boolean bug (fixed at
template level — verify), and the DEPLOY.md rule added at -002's close:
reset provenance.version_doi to "" before each release so a freeze never
seals a stale DOI.

---

## 2. THE VERIFIED LANDSCAPE (searches run 2026-07-14; re-verify on use)

**Layer 1 — Codes: solved and industrializing.** qLDPC overheads
collapsing: surface ~100:1; IBM bivariate-bicycle ~8:1 era; QuEra
ultra-high-rate qLDPC memory at 2:1 physical:logical (2026, memory
baseline only); "routing codes" (arXiv:2606.25330) match BB rates with
parallel non-local couplings buildable on BOTH superconductors and
neutral atoms, ~8x overhead reduction vs surface at equal logical error.
qLDPC is platform-agnostic in principle; the binding constraint is
non-local connectivity, solved differently per platform: atom shuttling
(neutral atoms), long-range couplers + multilayer wiring (IBM Loon),
all-to-all (ions), optical links (photonics), phase-flip LDPC-cat (cat
qubits — -002's old lane).

**Layer 2 — Memory-to-compute: THE structural gap.** The field stores
logical qubits cheaply and cannot yet compute on them cheaply. QuEra's
own caveat: logical gates on high-rate codes remain open. The gate
theory space is elite-crowded (code surgery, universal adapters
[PRX Quantum 2026], gauging logical operators [Nature Physics 2026],
transversal non-Clifford via sheaves/products, addressability problem,
fresh no-go theorems [arXiv:2602.13395, Gottesman group]). Pure theory
here: bad edge-fit for a solo AI loop. What is NOT crowded: honest
circuit-level measurement of the gadget zoo (Layer 4).

**Layer 3 — Real-time decoding: open but industrially swarmed.** BP-OSD
accuracy-leading but OSD worst-case cubic; real-time speed+accuracy for
qLDPC still open. Incumbents: IBM Relay-BP (disordered-memory BP that
damps the symmetric trapping sets that trap standard BP — the exact
mechanism -002 Entry 011 dissected), NVIDIA cudaq-qec, FPGA-tailored
decoders, ML decoders incl. Google AlphaQubit (Nature-published,
accuracy-leading, too slow for live correction; REPORTED claims of
2025-26 productionization are low-quality-source and unverified).
Edge-fit: moderate — trapping-set expertise is load-bearing, but
out-engineering IBM/NVIDIA on hardware decoders is not the lane.

**Layer 4 — The honest-measurement layer: verified thin. THE LANE.**
The gadget zoo (surgery schemes, adapters, dimension jumps, shuttling
choreographies, hybrid architectures like NA-memory + SC-compute
[arXiv:2601.10144, 752x-speedup cost-model claims]) is compared on
asymptotics and toy analyses. No certified circuit-level operating-point
leaderboard of LOGICAL OPERATIONS on high-rate codes exists. Referee
work is career-unrewarded and falls between theory and hardware — a
verified crowd-absence, and exactly -002's apparatus one level up.
Adjacent rulers now exist to gate, not to trust: failure-spectrum ansatz
(arXiv:2511.15177), circuit-level splitting (arXiv:2509.13678), the
Bravyi-Vargo lineage (PRA 88, 062308).

**Layer 5 — AI-for-QC: the thesis is live and under-verified.** Learned
components beat classical on real hardware data (AlphaQubit); AI code
search still grades at code capacity (-002's sealed, DOI'd finding);
"AI as accelerant, honestly graded" remains near-empty.

**Platform verdict:** neutral atoms lead (structural connectivity
advantage, 2:1 memory demonstrated, the compute gap wide open), with
cross-platform code families (routing codes) hedging the bet.

---

## 3. MISSION AND AUTONOMY CONTRACT

QC003 is EXPLORATORY. The AI (Strategy Room) leads arc-scouting and is
expected to operate without being babied:

- **Self-triage:** the AI generates candidate arcs, runs its own
  prior-art verification, scores each on the five axes below, and KILLS
  mundane ones autonomously — recording one-line kills in an
  append-only scouting ledger without asking permission per kill. Only
  arcs scoring breakthrough-shaped are surfaced for author decision.
- **The five axes** (all scored, in the ledger, per arc):
  1. Breakthrough-shaped: a win changes what others do, not a number.
  2. Edge-fit: computation/reasoning-heavy, no lab, exploits the
     verified two-agent loop and the -002 machinery.
  3. Underpriced-why: a NAMED reason the crowd is absent (between
     fields, career-unrewarded, discipline-scarce). "Nobody thought of
     it" is not a reason; verify absence by search.
  4. Mechanically verifiable: a stranger can check the claim by
     rerunning committed artifacts.
  5. Pull: would the author stay up for it. The author retains absolute
     authority on this axis; the AI must ask rather than infer.
- **Standing bar:** if an arc's honest ceiling is coefficient-polishing,
  it dies in the ledger. -002 was concluded over exactly this; QC003
  does not relitigate it per-arc.
- **Author authority retained:** forecast percentages, author-position
  statements, AI-use disclosure wording, scope exclusions (weapons-
  adjacent comparisons excluded; macro-economic topics out of scope),
  publication/DOI decisions, and the Pull axis.

---

## 4. THE PRODUCTIVITY QUESTION, ANSWERED HONESTLY

**Field-wide (all tools):** the fastest routes to fault tolerance right
now are (a) closing the memory-to-compute gap on high-rate codes —
logical gadgets, their schedules, and their honest costs; (b) real-time
decoders that keep pace with syndrome streams at qLDPC block sizes;
(c) architecture-level co-design (hybrid memory/compute, movement
scheduling, interconnects) graded by measurement rather than cost
models; (d) magic-state / non-Clifford supply chains at constant-ish
overhead. All four are simulation-verifiable long before hardware.

**The Claude-only lane (no lab, no experiments):** everything above
EXCEPT hardware demonstration is in reach, because the grading
instruments are classical simulations: stim-class circuit simulators,
BP/OSD-class decoders, exact enumeration, rare-event methods. A no-lab
researcher with a verified AI loop can:
  1. Build referees (frozen, gated, calibrated to published hardware
     noise) — the field's missing infrastructure.
  2. Produce certified measurements and leaderboards others must cite.
  3. Design and verify in silico: codes, gadgets, schedules, decoders —
     with honest grading the designers themselves rarely pay for.
  4. Register dated, falsifiable forecasts about which approaches win —
     the honest priority-claim instrument.
  5. Publish negative results and kills at full grade — the discipline
     institutions cannot afford and the record rewards.
This is not a consolation lane. It is the lane the field is worst at.

---

## 5. PUBLISHING DOCTRINE (recommended; author decides)

The author's goal — volume of DOI'd output creating unavoidable credit —
is adopted with one bar, for effectiveness rather than propriety:

- **Bare idea lists earn nothing.** In 2026 anyone can generate ideas
  with an LLM; unexecuted speculation is uniteable, unciteable, and
  would spend down the lineage's hard-won credibility. Priority
  attaches to demonstrated or falsifiably-registered claims.
- **Therefore the publishable unit is the SCOUTED CLAIM:** an idea plus
  at least one of (i) a derivation, (ii) a simulation/measurement with
  committed artifacts, or (iii) a pre-registered, dated, falsifiable
  forecast with a stated resolution mechanism. Each unit carries its
  prior-art table (what is established / adjacent / open, verified by
  search on a stated date).
- **Volume comes from the loop's throughput, not from lowering the
  bar:** batches of scouted claims can seal as non-DOI chapters
  (OTS-anchored) continuously, with DOI minting reserved for chapters
  the author judges citable. The forward-bet ledger scores everything
  at its signposts, attended or not — that is the "pip": dated,
  falsifiable, timestamped priority the field can check.
- Chapter 1 of QC003 (this reconnaissance, expanded) seals non-DOI.

---

## 6. CANDIDATE ARC PORTFOLIO (seed set — the AI extends and re-scores)

**A. THE LOGIC REFEREE (flagship candidate).** Build the frozen
circuit-level referee for logical operations on high-rate codes under
neutral-atom noise (shuttling, loss, 2:1-era codes); produce the first
certified gate-level truths; then arm the loop to search the
gadget/schedule space against it. Ceiling: "AI discovers a measurably
better way to compute on qLDPC codes." Scores: breakthrough-shaped
HIGH / edge-fit HIGH / underpriced VERIFIED (referee work) /
verifiable HIGH / pull: AUTHOR TO SCORE.

**B. Trapping-set-aware decoder co-design.** Port -002's decoder-trap
census + gap-share machinery to BB/routing codes; feed Relay-BP-class
decoders. Edge-fit high, but incumbent-crowded; ceiling likely
component-grade. Scores: breakthrough MED / edge HIGH / underpriced
WEAK / verifiable HIGH.

**C. Hybrid-architecture honest grading.** Re-grade the NA-memory +
SC-compute cost-model claims (752x etc.) by measurement-grade
simulation. Breakthrough MED-HIGH if claims re-order; underpriced
MED (very new, may crowd fast).

**D. The forecast engine.** Industrialize the forward-bet ledger:
regular batches of registered, dated predictions about which codes/
gadgets/decoders win at stated operating points, each backed by a
scouting simulation. Pure Layer-5 play; compounds with A. Breakthrough
as a BODY of work rather than a single result.

**E. Wildcards lane (standing).** Each scouting cycle must include at
least one arc from OUTSIDE the QEC frame (e.g., verification tooling
the field lacks, cross-field imports), so the exploration never
collapses into the prior dossier's groove.

---

## 7. OPERATING PROTOCOL (carried from -002, condensed)

Two-agent split: Strategy Room decides/drafts/ships .txt files with
sha256 guards + paste-ready blocks; Code executes with HEAD guards,
diff gates, independent fact-checks; author approves commits with "go"
relayed in the Code tab. Never git add -A; stage explicitly. Never edit
verified bytes; reissue with fresh hash. Numbers pasted from committed
artifacts only. Preregs before runs; dated addenda for mid-campaign
changes; kills and self-catches are first-class findings. Long reports
via review branch (chat attachments are lossy). In-browser functional
checks are mandatory for anything CI cannot see. Session hygiene: long
focused sessions, fresh session per arc, handoff refreshed at close.
Canonical env (re-pin in QC003): Python 3.12, numpy 2.5.x, stim 1.16+,
ldpc 2.4+, pymatching 2.4+.

---

## 8. FIRST-SESSION AGENDA (QC003, fresh repo)

1. Repo from template; apply template lessons (jq fix verify;
   version_doi-reset rule in DEPLOY.md from day one).
2. Author sets: dossier name/scope line, AI-use disclosure (author's
   own words), publishing-doctrine sign-off (Section 5), Pull scores
   on the seed portfolio (Section 6).
3. AI runs Scouting Cycle 1: extend the portfolio (target: 8-12 arcs
   incl. the wildcards lane), verify prior-art absences by search,
   score, kill, surface the survivors.
4. Chapter 1 drafted: this reconnaissance + Cycle 1, sealed non-DOI.
5. Author picks the first arc worthy of instruments.

---
