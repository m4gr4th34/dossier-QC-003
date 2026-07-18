#!/usr/bin/env python3
"""
PREREG-1 harness — loss-treatment sensitivity campaign.
Implements expedition/PREREG_1_LOSS_TREATMENT.md exactly. See prereg for design.

Model summary (documented choices, per prereg S2/S5):
- Base noise: standard circuit-level depolarizing at rate p_dep on cliffords,
  resets, measurements, and data idles (stim generated surface code circuit).
- Loss locations: (a) each qubit slot of each 2-qubit gate (CX), (b) each data
  qubit once per round (idle slot, attached at the round's measurement layer).
- A sampled loss event at a location, by treatment:
    T1 (unheralded Pauli, STAR-style): deterministic Y applied at the location
        in the sampled circuit; decoder = base decoder, no heralding.
    T2 (delayed erasure): physical event = uniformly random Pauli in {I,X,Y,Z}
        (the atom's state is gone -> maximally mixed on replacement); decoder
        is told (qubit, round) only: its model inserts DEPOLARIZE1(P_SPREAD)
        at EVERY candidate layer of that qubit in that round.
    T3 (immediate erasure): same physical event as T2; decoder is told the
        exact (location): its model inserts DEPOLARIZE1(P_ERASE) there.
- P_ERASE = 0.499 (max graphlike-safe stand-in for "known error here",
  weight ~ 0). P_SPREAD = 0.25 per candidate layer (documented design point;
  prereg S5 notes T2 is one point in the delayed-detection space).
- Budget split: total per-location physical error rate P_TOT fixed; loss share
  s => p_loss = s*P_TOT at loss locations, p_dep = (1-s)*P_TOT elsewhere.
  At s=0 all treatments are byte-identical (the control/self-test).
- Decoding: PyMatching from stim DEM (decompose_errors=True). Per-loss-shot
  decoder models are cached by (treatment, frozenset(locations)) — most loss
  shots have 1 event, so the cache converges to ~#locations entries.
"""
import argparse, json, time, hashlib, sys
from collections import OrderedDict
import numpy as np
import stim, pymatching

P_ERASE = 0.499
P_SPREAD = 0.25

def build_base(distance, rounds, p_dep, basis):
    c = stim.Circuit.generated(
        f"surface_code:rotated_memory_{basis}",
        distance=distance, rounds=rounds,
        after_clifford_depolarization=p_dep,
        after_reset_flip_probability=p_dep,
        before_measure_flip_probability=p_dep,
        before_round_data_depolarization=p_dep,
    ).flattened()
    return c

def enumerate_locations(circ):
    """Walk the flattened circuit; return loss locations and metadata.
    A location = (instr_index, qubit, round_idx, kind) where kind in
    {'cx','idle'}; insertion point = immediately AFTER instr_index."""
    locs = []
    round_idx = 0
    data_qubits = None
    # data qubits: targets of the final M/MX layer are the data qubits.
    last_meas_targets = None
    instrs = list(circ)
    for i, ins in enumerate(instrs):
        if ins.name in ("M", "MX"):
            last_meas_targets = [t.value for t in ins.targets_copy()]
    data_qubits = sorted(set(last_meas_targets or []))
    for i, ins in enumerate(instrs):
        if ins.name == "CX":
            ts = [t.value for t in ins.targets_copy()]
            for q in ts:
                locs.append((i, q, round_idx, "cx"))
        elif ins.name == "MR":  # ancilla measure+reset = round boundary
            for q in data_qubits:
                locs.append((i, q, round_idx, "idle"))
            round_idx += 1
    return locs, instrs, round_idx

def rebuild_with_inserts(instrs, inserts):
    """inserts: dict instr_index -> list of (gate_name, qubit, arg_or_None).
    Returns a new stim.Circuit with each list appended AFTER that index."""
    out = stim.Circuit()
    for i, ins in enumerate(instrs):
        out.append(ins)
        for name, q, arg in inserts.get(i, ()):
            if arg is None:
                out.append(name, [q])
            else:
                out.append(name, [q], arg)
    return out

def decoder_model_circuit(instrs, losses, treatment, locs_by_qr):
    """Build the DECODER's model circuit for a given loss pattern."""
    inserts = {}
    def add(i, name, q, arg):
        inserts.setdefault(i, []).append((name, q, arg))
    if treatment == "T3":
        for (i, q, r, kind) in losses:
            add(i, "DEPOLARIZE1", q, P_ERASE)
    elif treatment == "T2":
        seen = set()
        for (_, q, r, _) in losses:
            if (q, r) in seen: continue
            seen.add((q, r))
            for loc in locs_by_qr[(q, r)]:
                add(loc[0], "DEPOLARIZE1", q, P_SPREAD)
    return rebuild_with_inserts(instrs, inserts)

def matcher_from(circ):
    dem = circ.detector_error_model(decompose_errors=True, ignore_decomposition_failures=True)
    return pymatching.Matching.from_detector_error_model(dem)

def run_cell(distance, rounds, basis, p_tot, share, treatment, shots, seed, report_every=None):
    rng = np.random.default_rng(seed)
    p_loss_loc = share * p_tot
    p_dep = (1.0 - share) * p_tot
    base = build_base(distance, rounds, p_dep, basis)
    locs, instrs, nrounds = enumerate_locations(base)
    locs_by_qr = {}
    for L in locs:
        locs_by_qr.setdefault((L[1], L[2]), []).append(L)
    base_matcher = matcher_from(base)
    base_sampler = base.compile_detector_sampler(seed=int(rng.integers(2**31)))

    n_loc = len(locs)
    fails = 0
    # Bulk path: shots with zero loss events.
    # P(no loss) = (1-p_loss_loc)^n_loc
    p_none = (1.0 - p_loss_loc) ** n_loc if p_loss_loc > 0 else 1.0
    n_none = int(rng.binomial(shots, p_none)) if p_loss_loc > 0 else shots
    n_lossy = shots - n_none
    if n_none:
        dets, obs = base_sampler.sample(n_none, separate_observables=True)
        preds = base_matcher.decode_batch(dets)
        fails += int(np.sum(np.any(preds != obs, axis=1)))
    # Lossy path: sample number of events per shot conditioned on >=1.
    cache = OrderedDict(); CACHE_MAX = 4096
    t0 = time.time()
    for s_i in range(n_lossy):
        k = 0
        while k == 0:
            k = rng.binomial(n_loc, p_loss_loc)
        idxs = rng.choice(n_loc, size=k, replace=False)
        losses = [locs[j] for j in idxs]
        # physical circuit for this shot
        inserts = {}
        for (i, q, r, kind) in losses:
            if treatment == "T1":
                inserts.setdefault(i, []).append(("Y", q, None))
            else:
                pauli = rng.integers(4)  # 0=I,1=X,2=Y,3=Z
                if pauli:
                    inserts.setdefault(i, []).append((("X","Y","Z")[pauli-1], q, None))
        phys = rebuild_with_inserts(instrs, inserts)
        det, ob = phys.compile_detector_sampler(seed=int(rng.integers(2**31))).sample(1, separate_observables=True)
        # decoder for this shot
        if treatment == "T1":
            m = base_matcher
        else:
            key = (treatment, frozenset((L[0], L[1]) for L in losses))
            m = cache.get(key)
            if m is None:
                m = matcher_from(decoder_model_circuit(instrs, losses, treatment, locs_by_qr))
                cache[key] = m
                if len(cache) > CACHE_MAX: cache.popitem(last=False)
            else:
                cache.move_to_end(key)
        pred = m.decode_batch(det)
        fails += int(np.any(pred != ob))
        if report_every and (s_i+1) % report_every == 0:
            print(f"    lossy {s_i+1}/{n_lossy} ({time.time()-t0:.0f}s)", flush=True)
    ler = fails / shots
    ci = 1.96 * np.sqrt(max(ler*(1-ler), 1e-12) / shots)
    return {"d": distance, "rounds": rounds, "basis": basis, "p_tot": p_tot,
            "share": share, "treatment": treatment, "shots": shots,
            "n_lossy_shots": n_lossy, "n_loss_locations": n_loc,
            "fails": fails, "ler": ler, "ci95": ci, "seed": seed,
            "versions": {"stim": stim.__version__, "pymatching": pymatching.__version__,
                          "numpy": np.__version__, "python": sys.version.split()[0]}}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--d", type=int, required=True)
    ap.add_argument("--p", type=float, default=1e-3)
    ap.add_argument("--share", type=float, required=True)
    ap.add_argument("--treatment", choices=["T1","T2","T3"], required=True)
    ap.add_argument("--basis", choices=["z","x"], default="z")
    ap.add_argument("--shots", type=int, required=True)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    res = run_cell(a.d, a.d, a.basis, a.p, a.share, a.treatment, a.shots, a.seed)
    line = json.dumps(res)
    print(line)
    if a.out:
        with open(a.out, "a") as f: f.write(line + "\n")

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------
# FAST PATH (v2): statistically identical regrouping of the lossy-shot loop.
# Shots with exactly ONE loss event are exchangeable within a (location, pauli)
# class: allocate their counts multinomially and batch-sample/batch-decode one
# circuit per class. Shots with >=2 events keep the per-shot slow path.
# ---------------------------------------------------------------------------
def run_cell_fast(distance, rounds, basis, p_tot, share, treatment, shots, seed):
    rng = np.random.default_rng(seed)
    p_loss_loc = share * p_tot
    p_dep = (1.0 - share) * p_tot
    base = build_base(distance, rounds, p_dep, basis)
    locs, instrs, _ = enumerate_locations(base)
    locs_by_qr = {}
    for L in locs:
        locs_by_qr.setdefault((L[1], L[2]), []).append(L)
    base_matcher = matcher_from(base)
    n_loc = len(locs)
    fails = 0
    if p_loss_loc <= 0:
        dets, obs = base.compile_detector_sampler(seed=int(rng.integers(2**31))).sample(shots, separate_observables=True)
        preds = base_matcher.decode_batch(dets)
        fails = int(np.sum(np.any(preds != obs, axis=1)))
        n_lossy = 0; n_multi = 0
    else:
        # exact per-shot event-count distribution: k ~ Binomial(n_loc, p_loss_loc)
        p0 = (1.0 - p_loss_loc) ** n_loc
        p1 = n_loc * p_loss_loc * (1.0 - p_loss_loc) ** (n_loc - 1)
        counts = rng.multinomial(shots, [p0, p1, max(0.0, 1.0 - p0 - p1)])
        n_none, n_one, n_multi = int(counts[0]), int(counts[1]), int(counts[2])
        n_lossy = n_one + n_multi
        if n_none:
            dets, obs = base.compile_detector_sampler(seed=int(rng.integers(2**31))).sample(n_none, separate_observables=True)
            preds = base_matcher.decode_batch(dets)
            fails += int(np.sum(np.any(preds != obs, axis=1)))
        # single-event shots: allocate over (location, pauli-class)
        if n_one:
            if treatment == "T1":
                per_loc = rng.multinomial(n_one, [1.0/n_loc]*n_loc)
                classes = [(li, "Y") for li in range(n_loc)]
                alloc = {c: int(per_loc[i]) for i, c in enumerate(classes)}
            else:
                nclass = n_loc * 4
                per = rng.multinomial(n_one, [1.0/nclass]*nclass)
                paulis = ("I","X","Y","Z")
                alloc = {}
                for j in range(nclass):
                    if per[j]:
                        alloc[(j // 4, paulis[j % 4])] = int(per[j])
            for (li, pauli), m_shots in alloc.items():
                if m_shots == 0: continue
                L = locs[li]
                inserts = {}
                if pauli != "I":
                    inserts[L[0]] = [(pauli, L[1], None)]
                phys = rebuild_with_inserts(instrs, inserts)
                det, ob = phys.compile_detector_sampler(seed=int(rng.integers(2**31))).sample(m_shots, separate_observables=True)
                if treatment == "T1":
                    m = base_matcher
                else:
                    m = matcher_from(decoder_model_circuit(instrs, [L], treatment, locs_by_qr))
                pred = m.decode_batch(det)
                fails += int(np.sum(np.any(pred != ob, axis=1)))
        # multi-event shots: slow per-shot path, conditioned k>=2
        cache = OrderedDict(); CACHE_MAX = 4096
        for _ in range(n_multi):
            k = 0
            while k < 2:
                k = rng.binomial(n_loc, p_loss_loc)
            idxs = rng.choice(n_loc, size=k, replace=False)
            losses = [locs[j] for j in idxs]
            inserts = {}
            for (i, q, r, kind) in losses:
                if treatment == "T1":
                    inserts.setdefault(i, []).append(("Y", q, None))
                else:
                    pauli = rng.integers(4)
                    if pauli:
                        inserts.setdefault(i, []).append((("X","Y","Z")[pauli-1], q, None))
            phys = rebuild_with_inserts(instrs, inserts)
            det, ob = phys.compile_detector_sampler(seed=int(rng.integers(2**31))).sample(1, separate_observables=True)
            if treatment == "T1":
                m = base_matcher
            else:
                key = (treatment, frozenset((L[0], L[1]) for L in losses))
                m = cache.get(key)
                if m is None:
                    m = matcher_from(decoder_model_circuit(instrs, losses, treatment, locs_by_qr))
                    cache[key] = m
                    if len(cache) > CACHE_MAX: cache.popitem(last=False)
            pred = m.decode_batch(det)
            fails += int(np.any(pred != ob))
    ler = fails / shots
    ci = 1.96 * np.sqrt(max(ler*(1-ler), 1e-12) / shots)
    return {"d": distance, "rounds": rounds, "basis": basis, "p_tot": p_tot,
            "share": share, "treatment": treatment, "shots": shots,
            "n_lossy_shots": n_lossy, "n_multi_shots": n_multi,
            "n_loss_locations": n_loc, "fails": fails, "ler": ler, "ci95": ci,
            "seed": seed, "path": "fast",
            "versions": {"stim": stim.__version__, "pymatching": pymatching.__version__,
                          "numpy": np.__version__, "python": sys.version.split()[0]}}
