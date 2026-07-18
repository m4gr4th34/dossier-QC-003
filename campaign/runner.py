#!/usr/bin/env python3
"""
PREREG-1 canonical sweep runner. Run on the canonical machine ONLY after the
two gates pass (see README): (1) fast-vs-slow equivalence, (2) 0%-loss control.

Usage:
  python3 runner.py --out results.jsonl [--master-seed 20260717] [--cell-cap-hours 3]

Resumable: completed cells (matching keys in the out file) are skipped.
Every chunk appends a JSON line; the final line per cell has "final": true.
"""
import argparse, json, os, time, hashlib
from harness import run_cell_fast

CELLS = []
for d in (3, 5):
    bases = ("z", "x") if d == 3 else ("z",)  # d=5 x-basis: cap-budget extra, see ADDENDUM A1.5
    for basis in bases:
        for share in (0.0, 0.25, 0.5, 0.75):
            for t in ("T1", "T2", "T3"):
                CELLS.append((d, basis, share, t))
# d=5 x-basis appended last, run if budget allows:
for share in (0.0, 0.25, 0.5, 0.75):
    for t in ("T1", "T2", "T3"):
        CELLS.append((5, "x", share, t))

P_TOT = 1e-3
CHUNK = 100_000
CI_FRACTION = 0.15
SHOT_CAP = 100_000_000

def cell_seed(master, d, basis, share, t):
    h = hashlib.sha256(f"{master}|{d}|{basis}|{share}|{t}".encode()).digest()
    return int.from_bytes(h[:4], "big")

def done_cells(path):
    done = set()
    if os.path.exists(path):
        for line in open(path):
            try:
                r = json.loads(line)
                if r.get("final"):
                    done.add((r["d"], r["basis"], r["share"], r["treatment"]))
            except Exception:
                pass
    return done

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--master-seed", type=int, default=20260717)
    ap.add_argument("--cell-cap-hours", type=float, default=3.0)
    a = ap.parse_args()
    skip = done_cells(a.out)
    for (d, basis, share, t) in CELLS:
        if (d, basis, share, t) in skip:
            print(f"skip done: d={d} {basis} s={share} {t}"); continue
        seed0 = cell_seed(a.master_seed, d, basis, share, t)
        tot_shots = 0; tot_fails = 0; chunk_i = 0
        t0 = time.time()
        status = "OK"
        while True:
            r = run_cell_fast(d, d, basis, P_TOT, share, t, CHUNK, seed=seed0 + chunk_i)
            chunk_i += 1
            tot_shots += r["shots"]; tot_fails += r["fails"]
            ler = tot_fails / tot_shots
            ci = 1.96 * (max(ler * (1 - ler), 1e-15) / tot_shots) ** 0.5
            rec = dict(r); rec.update({"cum_shots": tot_shots, "cum_fails": tot_fails,
                                       "cum_ler": ler, "cum_ci95": ci, "final": False})
            with open(a.out, "a") as f: f.write(json.dumps(rec) + "\n")
            met_ci = tot_fails >= 5 and ci <= CI_FRACTION * ler
            hit_shots = tot_shots >= SHOT_CAP
            hit_time = (time.time() - t0) >= a.cell_cap_hours * 3600
            if met_ci or hit_shots or hit_time:
                if not met_ci: status = "CI-SHORT"
                break
        final = {"d": d, "basis": basis, "share": share, "treatment": t,
                 "cum_shots": tot_shots, "cum_fails": tot_fails,
                 "cum_ler": tot_fails / tot_shots,
                 "cum_ci95": ci, "status": status,
                 "wall_s": round(time.time() - t0, 1),
                 "master_seed": a.master_seed, "cell_seed": seed0, "final": True}
        with open(a.out, "a") as f: f.write(json.dumps(final) + "\n")
        print(json.dumps(final), flush=True)

if __name__ == "__main__":
    main()
