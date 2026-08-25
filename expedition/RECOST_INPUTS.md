# RECOST INPUTS — the verified input table for arc E's common ruler
## Every figure below verified against the named primary source on 2026-08-25

This file is the input to the recosting harness. It exists as a separate,
committed artifact so the recost is reproducible: a stranger can check the
inputs before checking the arithmetic, and any later correction to an input
is a diff on this file rather than a silent change inside a script.

**Provenance grades used here.** *Full text* = LaTeX source and/or rendered
PDF searched mechanically. *Abstract* = complete abstract read from the
primary listing. Per erratum SR-8, absence claims in this file rest only on
full-text-grade checks.

---

## 1 · Transversal STAR — arXiv:2509.18294v2

Ismail, Chen, Zhao, Weiss, Liu, Zhou, Wang, Sornborger, Kornjaca (QuEra / Los
Alamos). Published **PRX Quantum 7, 020343 (2026)**, 2026-05-29, doi
10.1103/j2fw-ccmy. *Full text.*

Absolute figures:
- ~10,000 physical qubits at physical error rate 1e-3 for the headline regime
- total simulation volume exceeding 600 (logical qubits x evolution timescale)
- equivalent to a fully fault-tolerant computation of >1e6-1e7 T gates
- resource table `tab:resource_summary` carries an explicit column headed
  "fixed connectivity / fully fault-tolerant" — the column the 250x is read off

Multipliers, each with the baseline named in its own sentence:
| Multiplier | Baseline as the paper states it |
|---|---|
| ~250x time + 2x space | "a fixed-connectivity, fully fault-tolerant scheme" |
| ~10x time + 2x space | "the original STAR architecture" |
| >100x space-time | "current, state-of-the-art protocols" (abstract) |
| 100-1000x space-time | "current, state-of-the-art fully-fault-tolerant protocols" |
| 2-4x | cultivation T-factories vs STAR injection |
| 10-20x space-time volume | per-T over STAR injection |
| ~30x | direct synthesis overhead |
| ~100x | limit via Hamming-weight phasing over transversal STAR |
| ~1000x | over fixed-connectivity architectures |
| ~5x additional space | high-rate transversal STAR |

## 2 · High-rate STAR — arXiv:2606.25011v1 (2026-06-23, no journal ref)

Ismail, Kornjaca, Hu, Maskara, Wang, Zhou, Zhao. *Full text.*

Absolute figures:
- 8x8 transverse-field Ising to T* ~ 8(zJ)^-1: **2,240 physical qubits, ~200 s
  per shot**
- 8x8 Fermi-Hubbard to T* ~ 4(zt)^-1: **~6,300 physical qubits, ~200 s per shot**

| Multiplier | Baseline as the paper states it |
|---|---|
| **~5.5x space (physical qubit count)** | **"a surface code STAR baseline" at comparable speed** |
| 5.5x and 5.7x qubit count | surface STAR, for TFIM and Fermi-Hubbard respectively |
| 100-1000x speedup | code-surgery approaches |
| >10x speedup | (unnamed in the extracted sentence) |
| 15-75x more physical qubits | fully fault-tolerant architectures |
| ~2.8-13x more bulky | BB/GB architectures |
| >=100x time-cost | "fixed connectivity T-based architectures" |
| ~10x / ~5x | vs distance-9 surface code / serial high-rate injection |

**Absence, full-text grade:** no 20x, 40x or 20-40x multiplier; no
"best-in-class", "previous best" or "state-of-the-art" phrasing. See SR-7.

## 3 · Q-NEXUS heterogeneous — arXiv:2604.06319 (2026-04-09)

Mundada, Khindanov, Wang, Edmunds, Coote, Biercuk, Baum, Hush. *Abstract +
listing.* Title states the headline: "Heterogeneous architectures enable a
138x reduction in physical qubit requirements for fault-tolerant quantum
computing under detailed accounting".

Baseline, fully specified — **the most recostable baseline in the set**:
1,000 logical qubits, homogeneous superconducting grid, nearest-neighbour
connectivity, **distance-15 surface code**, **1 us cycle time**, **physical
error rate 5e-4** → **~49 million physical qubits**.

Absolute figures:
- heterogeneous variant at 1,000 logical qubits: **~0.4 million physical qubits**
- RSA-2048: **381,000 physical qubits, 9.2 days** (demonstrated grid coupling)
- RSA-2048: **190,000 physical qubits** (hypothetical long-range coupling, qLDPC)
- algorithmic logical-error reduction: 551x (quantum adder), 59x (AQFT), both
  at 1,000 logical qubits

## 4 · NA/SC heterogeneous — arXiv:2601.10144

Fang, Ruan, Prabhu, Li, Humble, Tullsen, Ding. *Abstract.*

| Multiplier | Baseline as the paper states it |
|---|---|
| 752x speedup (average) | "NA-only baselines" |
| >10x physical qubit footprint | "SC-only systems" |
| 500-1000x speedup | MagicAcc over NA-only |
| 10.8x qubit reduction | MCSep vs SC-only |

Platform parameters the cost model assumes: SC gates 10-100 ns at 99.9%,
SC scaling limit 1e2-1e3 qubits; NA gates 0.1-1 us, NA transport 0.1-1 ms,
demonstrated NA scale 6,100 qubits (3,000 in continuous operation).

## 5 · Tour de Gross — arXiv:2506.03094

Yoder, Schoute, Rall, Pritchett, Gambetta, Cross, Carroll, Beverland.
*Abstract.*

Absolute figures:
- gross code: **288 physical, 12 logical, distance 12**
- two-gross code: **576 physical, distance 18**
- required physical error rate **7e-4**; module size under 1,000 physical qubits
- state transfer 98.8% over 0.6 m
- minimum estimate **~8,138 physical qubits**

Claim: "an order of magnitude larger logical circuits can be implemented with
a given number of physical qubits on a bicycle architecture than on surface
code architectures." **Direction matters** — this is circuit size at fixed
qubits, not qubit count at fixed circuit. Converting between the two requires
an assumption about how cost scales with circuit size that the paper does not
state, and the recost must either supply that assumption explicitly or leave
this row on its own axis. See erratum SR-7's companion correction to CM5.

## 6 · Routing codes — arXiv:2606.25330

Zhang, Chen, Duan, Li, Wei, Hou, Kong, Wu, Guo. *Abstract.*

- ~8x physical qubit overhead reduction "compared to surface codes achieving a
  same logical error rate"
- threshold ~0.5%
- logical error below 1e-12 at physical error rate 1e-4
- weight-7 instances; encoding rates comparable to bivariate bicycle codes

---

## What the ruler can and cannot be built from

**Recostable to a common scale.** Rows 3 and 6 state an absolute physical-qubit
count against a fully specified surface-code baseline including code distance
and physical error rate. Row 5 states code parameters and a required physical
error rate. Rows 1 and 2 state absolute physical-qubit counts at a stated
physical error rate for a stated task.

**Not recostable without a supplied assumption**, each of which the harness
must state rather than bury:
- the six operating points use **four different physical error rates**
  (1e-3, 7e-4, 5e-4, 1e-4). A common ruler must fix one and re-express the
  others, which requires a threshold-scaling model.
- three rows cost a **simulation task**, two cost a **1,000-logical-qubit
  machine**, and one costs **circuit size at fixed qubits**. These are three
  different quantities.
- row 4 reports **speed** against one baseline and **space** against another,
  in one abstract.

That list is not an obstacle to the chapter. It is most of the chapter's
result: the ruler's construction is where the incomparability becomes
quantitative instead of rhetorical.
