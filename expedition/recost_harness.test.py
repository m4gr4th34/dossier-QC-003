#!/usr/bin/env python3
"""recost_harness.test.py — the committed results must match a rerun, and the
model arithmetic must hold at spot-checked points. Stdlib only, fail loud."""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "rh", os.path.join(HERE, "recost_harness.py"))
rh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rh)

FAILED = []
def check(name, cond):
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        FAILED.append(name)

# Determinism: committed json == rerun (the harness's own --check contract).
with open(os.path.join(HERE, "recost_results.json"), encoding="utf-8") as fh:
    committed = fh.read()
rerun = json.dumps(rh.build(), indent=2, sort_keys=True) + "\n"
check("committed results match a rerun byte-for-byte", committed == rerun)

# Model spot checks, independently computed: A*(p/pth)^((d+1)/2) <= 1e-12.
check("d_required(1e-3) == 21", rh.d_required(1e-3) == 21)
check("d_required(1e-4) == 11", rh.d_required(1e-4) == 11)
check("d_required at threshold is None", rh.d_required(1e-2) is None)
check("overhead(1e-3) == 882", rh.surface_overhead(1e-3) == 882)
check("overhead(1e-4) == 242", rh.surface_overhead(1e-4) == 242)

# The suppression inequality actually holds at the returned distance and
# fails one distance step earlier (minimality).
for p in (1e-3, 7e-4, 5e-4, 1e-4):
    d = rh.d_required(p)
    # Relative tolerance: at p = 1e-3 the model value EQUALS the target
    # exactly (0.1 * 0.1^11 = 1e-12) and float noise puts it a hair above;
    # exact equality is admissible, so compare with a 1e-6 relative guard.
    ok_at = (rh.A_DEFAULT * (p / rh.PTH_DEFAULT) ** ((d + 1) / 2)
             <= rh.TARGET_LER * (1 + 1e-6))
    ok_below = (rh.A_DEFAULT * (p / rh.PTH_DEFAULT) ** ((d - 1) / 2)
                > rh.TARGET_LER * (1 + 1e-6))
    check("model inequality tight at p=%g (d=%d)" % (p, d), ok_at and ok_below)

# Headline derived figures.
r = rh.build()
check("p-normalization spread ~3.6x",
      r["ruler"]["p_normalization_spread"] == round(882 / 242, 2))
check("accounting dial ~109x",
      abs(r["dials"]["accounting_scope"]["factor"] - round(49000 / 450.0, 1)) < 1e-9)
check("kill condition verdict recorded", r["kill_condition"]["verdict"] == "FIRES")
check("memory span ~432x",
      r["memory_vs_compute"]["memory_axis_span"] == round(882 / 2.04, 0))

print("")
print("SUMMARY: %d failed" % len(FAILED))
sys.exit(1 if FAILED else 0)
