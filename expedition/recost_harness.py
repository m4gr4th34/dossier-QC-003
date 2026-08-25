#!/usr/bin/env python3
"""
recost_harness.py — arc E's recosting harness: the committed, rerunnable
arithmetic behind Chapter 8.

What this is. The six headline multipliers audited in Chapter 1 sec 03 were
re-verified against primary sources on 2026-08-25 (expedition/RECOST_INPUTS.md,
errata SR-7/SR-8). This script takes ONLY figures from that verified input
table plus the surface-code memory simulated in the 2:1 qLDPC result (Ch1's
CITE'd memory landmark) and does three things:

  1. AXES — classifies each claim by the quantity it actually measures. Claims
     on different axes cannot be ordered against each other by any recosting;
     they are different experiments, not different answers.
  2. RULER — for the one axis several claims share (physical-qubit overhead
     per logical qubit), re-expresses them at one target logical error rate
     under one stated error-suppression model, at each paper's own physical
     error rate and at a common one.
  3. DIALS — computes the sensitivity of that ruler to its three assumptions:
     the physical-error-rate normalization, the suppression-model constants,
     and the accounting scope (memory-only vs full computation). A pairwise
     ordering is called RESOLVABLE only if the separation between two claims
     exceeds the combined normalization sensitivity.

The error model, stated once and varied: LER(d) = A * (p / p_th)^((d+1)/2),
the standard surface-code suppression heuristic. Defaults A = 0.1,
p_th = 1e-2; the DIALS section varies A over [0.03, 0.3] and p_th over
[5e-3, 1e-2] and reports the swing. Every number downstream of this model is
OPEN-CAVEATED: true under the stated model, and closing the caveat is more
verification work (circuit-level simulation per code), not a contingent fact.

Doctrine: stdlib only, no network, deterministic (no clock, no RNG). Output
is written to expedition/recost_results.json; the committed copy must match a
rerun byte-for-byte (enforced by recost_harness.test.py). A stranger reruns
this and gets the same table or a bug report.

    python3 expedition/recost_harness.py            # print + rewrite json
    python3 expedition/recost_harness.py --check    # verify committed json
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "recost_results.json")

# ---------------------------------------------------------------- inputs ---
# Every figure below is copied from expedition/RECOST_INPUTS.md (verified
# 2026-08-25) or, for the 2:1 memory row, from the Ch1 CITE (qmem card).
# Nothing here is recalled; change RECOST_INPUTS.md first, this second.

CLAIMS = [
    dict(id="star250", paper="arXiv:2509.18294v2 / PRX Quantum 7, 020343",
         claim="~250x time + 2x space", axis="time+space",
         baseline="a fixed-connectivity, fully fault-tolerant scheme",
         p=1e-3, task="Hamiltonian simulation (megaquop)"),
    dict(id="hqa752", paper="arXiv:2601.10144",
         claim="752x speedup; >10x footprint", axis="time|space (two baselines)",
         baseline="NA-only (speed); SC-only (space)",
         p=None, task="end-to-end cost model"),
    dict(id="qnexus138", paper="arXiv:2604.06319",
         claim="138x fewer physical qubits", axis="space (full machine)",
         baseline="monolithic SC grid, d=15 surface, p=5e-4, 1e3 logical",
         p=5e-4, task="1,000-logical-qubit machine / RSA-2048"),
    dict(id="hrstar55", paper="arXiv:2606.25011v1",
         claim="~5.5x fewer physical qubits", axis="space",
         baseline="a surface code STAR baseline (comparable speed)",
         p=1e-3, task="8x8 TFIM / Fermi-Hubbard simulation"),
    dict(id="tdg10", paper="arXiv:2506.03094",
         claim="~10x larger circuits at fixed qubits", axis="circuit-size",
         baseline="surface code architectures",
         p=7e-4, task="end-to-end modular architecture"),
    dict(id="routing8", paper="arXiv:2606.25330",
         claim="~8x qubit overhead reduction", axis="space",
         baseline="surface codes at same logical error rate",
         p=1e-4, task="circuit-level memory simulation"),
]

# The memory landmark from Ch1 (CITE, qmem): rate > 1/2 qLDPC memory, ~2
# physical per logical, LER ~1.3e-13 per round at p = 1e-3 — simulation.
QMEM = dict(id="qldpc21", paper="QuEra/Harvard/MIT preprint (April 2026)",
            phys_per_logical=2.04, p=1e-3, scope="memory-only simulation")

# Q-NEXUS's own two figures for the SAME machine class (from its baseline
# spec): full-computation accounting vs memory-only accounting of d=15.
QNEXUS_FULL_PER_LOGICAL = 49e6 / 1000.0     # ~49,000
QNEXUS_D = 15

TARGET_LER = 1e-12
A_DEFAULT, PTH_DEFAULT = 0.1, 1e-2
A_RANGE, PTH_RANGE = (0.03, 0.3), (5e-3, 1e-2)
P_POINTS = [1e-3, 7e-4, 5e-4, 1e-4]         # the four operating points in use


# ----------------------------------------------------------------- model ---
def d_required(p, target=TARGET_LER, A=A_DEFAULT, p_th=PTH_DEFAULT):
    """Smallest odd distance d with A*(p/p_th)^((d+1)/2) <= target."""
    if p >= p_th:
        return None  # above threshold: no distance suffices
    # ceil with an epsilon guard: at p = 1e-3 the exact ratio is 11.0, and
    # bare ceil() over floating point returns 12 (log rounding), silently
    # inflating d from 21 to 23. Caught by recost_harness.test.py's
    # independently-derived spot checks; fixed here, never in the test.
    k = math.ceil(math.log(target / A) / math.log(p / p_th) - 1e-9)
    k = max(k, 1)
    d = 2 * k - 1
    return d if d % 2 == 1 else d + 1


def surface_overhead(p, **kw):
    """Memory-only physical qubits per logical: 2*d^2 (data + measure)."""
    d = d_required(p, **kw)
    return None if d is None else 2 * d * d


# ------------------------------------------------------------------ runs ---
def build():
    out = {"_generated_by": "expedition/recost_harness.py",
           "_inputs": "expedition/RECOST_INPUTS.md (verified 2026-08-25)",
           "_model": {"form": "LER(d) = A*(p/p_th)^((d+1)/2)",
                      "A": A_DEFAULT, "p_th": PTH_DEFAULT,
                      "target_LER": TARGET_LER,
                      "status": "OPEN-CAVEATED: results hold under this stated model"}}

    # 1 · AXES
    axes = {}
    for c in CLAIMS:
        axes.setdefault(c["axis"], []).append(c["id"])
    out["axes"] = {
        "classification": {c["id"]: {"axis": c["axis"], "claim": c["claim"],
                                     "baseline": c["baseline"], "p": c["p"],
                                     "task": c["task"]} for c in CLAIMS},
        "distinct_axes": sorted(axes),
        "shared_space_axis": sorted(axes.get("space", [])),
        "finding": ("The six claims measure at least four distinct quantities "
                    "across four physical error rates and three task classes. "
                    "Only the 'space' claims can be ordered against each other "
                    "at all; orderings across axes are UNDEFINED, not merely "
                    "uncertain."),
    }

    # 2 · RULER — surface-code memory overhead at each operating point
    ruler = {}
    for p in P_POINTS:
        d = d_required(p)
        ruler["p=%g" % p] = {"d_required": d, "phys_per_logical_2d2": 2 * d * d}
    spread = (ruler["p=0.001"]["phys_per_logical_2d2"] /
              ruler["p=0.0001"]["phys_per_logical_2d2"])
    out["ruler"] = {
        "surface_memory_overhead_at_target": ruler,
        "p_normalization_spread": round(spread, 2),
        "note": ("The identical surface code, held to the identical logical "
                 "error target, costs this much more per logical qubit at the "
                 "loosest operating point in use than at the tightest. Any "
                 "cross-paper comparison spanning these p's inherits this "
                 "factor before any architecture difference is measured."),
    }

    # Normalized space-axis table at p = 1e-3 (memory scope, stated model).
    # Tour de Gross is deliberately NOT in this table: its 288-physical /
    # 12-logical gross code is the paper's own figure at ITS distance (12),
    # which does not reach the 1e-12 target, and the abstract gives no
    # scaling to that target — placing 24 next to at-target numbers would
    # manufacture exactly the mixed-conditions comparison this audit exists
    # to expose. Its claim stays on the circuit-size axis where it was made.
    surf_1e3 = surface_overhead(1e-3)
    out["space_axis_at_p1e-3_memory_scope"] = {
        "surface_code": surf_1e3,
        "routing_codes_via_8x": round(surf_1e3 / 8.0, 1),
        "qldpc_rate_half_memory": QMEM["phys_per_logical"],
        "memory_axis_total_span": round(surf_1e3 / QMEM["phys_per_logical"], 0),
        "excluded": {"tour_de_gross": "own figure 288/12 = 24 phys per logical "
                     "is at d=12, not at the 1e-12 target; not placeable here "
                     "from the published abstract"},
    }

    # 3 · DIALS
    d_at = lambda **kw: surface_overhead(1e-3, **kw)
    dial_pth = d_at(p_th=PTH_RANGE[0]) / d_at(p_th=PTH_RANGE[1])
    dial_A = d_at(A=A_RANGE[1]) / d_at(A=A_RANGE[0])
    accounting = QNEXUS_FULL_PER_LOGICAL / (2.0 * QNEXUS_D * QNEXUS_D)
    out["dials"] = {
        "p_normalization": {"factor": round(spread, 2),
                            "meaning": "choice of physical error rate (1e-3 vs 1e-4)"},
        "threshold_constant": {"factor": round(dial_pth, 2),
                               "meaning": "p_th chosen at 0.5% vs 1%"},
        "prefactor_A": {"factor": round(dial_A, 2),
                        "meaning": "A chosen at 0.3 vs 0.03"},
        "accounting_scope": {
            "factor": round(accounting, 1),
            "meaning": ("physical qubits per logical for the SAME d=15 surface "
                        "code: full-computation accounting (Q-NEXUS's own "
                        "baseline, ~49,000) vs memory-only (2d^2 = 450)"),
        },
        "resolvability_threshold": round(spread, 2),
        "note": ("A pairwise ordering on the shared axis is called RESOLVABLE "
                 "only when the claimed separation exceeds the p-normalization "
                 "factor, the largest dial that applies WITHIN one accounting "
                 "scope. The accounting dial is larger than every audited "
                 "multiplier except the 250x and dwarfs all inter-architecture "
                 "separations; comparisons that mix scopes are meaningless."),
    }

    # Pairwise verdicts. Each claim is compared only against its OWN stated
    # baseline on its OWN axis; cross-claim orderings are attempted only where
    # an explicit, stated assumption can bridge the axes, and the bridge is
    # named in the verdict.
    sep_tdg_routing = 10.0 / 8.0
    out["pairwise_verdicts"] = {
        "surface_vs_routing(8x)": {
            "separation": 8.0, "threshold": round(spread, 2),
            "verdict": "RESOLVABLE on the qubit-overhead axis — but with a "
                       "margin of only ~2.2x over the normalization sensitivity"},
        "surface_vs_tour_de_gross(10x)": {
            "separation": 10.0, "threshold": round(spread, 2),
            "verdict": "RESOLVABLE on the paper's own circuit-size axis (the "
                       "direction survives the dials); NOT transferable to the "
                       "qubit-overhead axis without a cost-linearity assumption "
                       "the paper does not state"},
        "tour_de_gross_vs_routing": {
            "separation": round(sep_tdg_routing, 2), "threshold": round(spread, 2),
            "verdict": "NOT RESOLVABLE — the claims live on different axes "
                       "(circuit-size vs qubit-overhead); under the unstated "
                       "linearity bridge their separation is ~1.25x, far inside "
                       "the ~3.6x normalization sensitivity. These two cannot "
                       "be ordered from the published record"},
        "qldpc_memory_vs_everything": {
            "separation": round(surf_1e3 / QMEM["phys_per_logical"], 0),
            "threshold": round(spread, 2),
            "verdict": "RESOLVABLE, robustly — two orders of magnitude of margin"},
        "cross_axis_claims(250x,752x,138x,5.5x)": {
            "verdict": "UNDEFINED — different quantities against different "
                       "baselines; no recosting orders them without assumptions "
                       "whose defensible ranges exceed the separations"},
    }

    # 4 · KILL CONDITION (pre-registered in the scouting ledger, arc E)
    out["kill_condition"] = {
        "preregistered": ("if no headline multiplier's ordering changes by more "
                          "than its own stated uncertainty under the common "
                          "baseline, arc E is reported as a negative result and "
                          "closed"),
        "verdict": "FIRES",
        "detail": ("On the one axis where orderings exist, none changes under "
                   "recosting: the qLDPC-family claims beat the surface code by "
                   "roughly their stated factors, and the memory landmark beats "
                   "everything, robustly. The orderings the field might have "
                   "gotten wrong turn out not to exist at all (cross-axis) "
                   "rather than to be wrong. Arc E closes as a negative result "
                   "at full grade, with its incidental findings — SR-7, SR-8, "
                   "the accounting-scope factor, the resolvability threshold — "
                   "standing on their own."),
    }

    # 5 · THE RACE, QUANTIFIED — Chapter 1's thesis in two numbers
    out["memory_vs_compute"] = {
        "memory_axis_span": round(surf_1e3 / QMEM["phys_per_logical"], 0),
        "compute_inclusive_span": "8-12x",
        "meaning": ("The storage half of the problem offers verified-simulation "
                    "wins of two orders of magnitude; every end-to-end "
                    "(compute-inclusive) multiplier on the shared axis "
                    "compresses to about one order. The memory-to-compute gap "
                    "is not a slogan; at the current published record it is "
                    "the difference between ~430x and ~10x."),
    }
    return out


def main(argv):
    result = build()
    blob = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if "--check" in argv:
        with open(OUT, "r", encoding="utf-8") as fh:
            committed = fh.read()
        if committed != blob:
            print("recost_harness --check: committed results DIFFER from a rerun")
            return 1
        print("recost_harness --check: committed results match a rerun byte-for-byte")
        return 0
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(blob)
    print(blob)
    print("wrote %s" % os.path.relpath(OUT, os.getcwd()))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
