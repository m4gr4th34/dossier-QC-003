#!/usr/bin/env python3
"""
check_retracted.test.py — tests for the retracted-claim sentinel.

Doctrine of these tests, same as the gate they cover: stdlib only, no network,
no fixtures on disk beyond tempfiles, fail loud. They exercise the property that
matters — that an ALLOWLISTED file is still guarded, because budget-not-allowlist
is the whole design.
"""
import importlib.util
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cr", os.path.join(HERE, "check_retracted.py"))
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)

FAILED = []


def check(name, cond):
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        FAILED.append(name)


def write(dirpath, rel, text):
    path = os.path.join(dirpath, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return (rel, path)


ENTRY = {
    "id": "T1",
    "erratum": "SR-TEST",
    "retracted_on": "2026-08-25",
    "note": "test",
    "pattern": r"20\s*[-–]\s*40\s*[x×]",
    "budget": {"errata.md": 1},
}

with tempfile.TemporaryDirectory() as tmp:
    errata = write(tmp, "errata.md", "we retracted the 20-40x figure\n")
    clean = write(tmp, "notes.md", "nothing retracted here\n")
    stale = write(tmp, "draft.md", "the paper reports 20-40x savings\n")

    v, counts = cr.scan([ENTRY], files=[errata, clean])
    check("in-budget errata file passes", v == [])
    check("counts record the errata occurrence", counts["T1"]["errata.md"] == 1)

    v, _ = cr.scan([ENTRY], files=[errata, stale])
    check("stale copy in an unlisted file fails", any(x[1] == "draft.md" for x in v))

    # The property an allowlist cannot give: a listed file is still guarded.
    write(tmp, "errata.md", "we retracted the 20-40x figure\nand here it is again 20-40x\n")
    v, _ = cr.scan([ENTRY], files=[errata])
    check("re-introduction INSIDE a budgeted file fails",
          any(x[1] == "errata.md" and x[2] == 2 and x[3] == 1 for x in v))

    # En-dash and multiplication-sign spellings are the same claim.
    write(tmp, "draft.md", "reports 20–40× savings\n")
    v, _ = cr.scan([ENTRY], files=[stale])
    check("en-dash and multiplication-sign spelling is caught", len(v) == 1)

    # Case-insensitivity, on a word pattern.
    word = dict(ENTRY, id="T2", pattern=r"best[-\s]in[-\s]class", budget={})
    write(tmp, "draft.md", "the previous BEST-IN-CLASS architecture\n")
    v, _ = cr.scan([word], files=[stale])
    check("word pattern matches case-insensitively", len(v) == 1)

# Scan scope: .github is walked (workflow files are authored text), .git is not.
scanned = {rel for rel, _ in cr.iter_files()}
check("workflow files are inside the scan",
      any(r.startswith(".github/") for r in scanned))
check("the git directory is outside the scan",
      not any(r.startswith(".git/") for r in scanned))
check("this gate's own machinery is exempt by name",
      not (scanned & cr.SELF) and len(cr.SELF) == 2)

# The live registry must parse and every entry must be well formed.
try:
    entries = cr.load_registry()
    check("live registry parses", isinstance(entries, list) and len(entries) > 0)
    check("live registry entries are well formed",
          all(set(("id", "pattern", "erratum", "budget")) <= set(e) for e in entries))
except Exception as exc:  # noqa: BLE001 - a broken registry is a test failure
    check("live registry parses (%s)" % exc, False)

# A malformed registry must raise rather than silently pass.
with tempfile.TemporaryDirectory() as tmp:
    bad = os.path.join(tmp, "bad.json")
    with open(bad, "w", encoding="utf-8") as handle:
        json.dump({"retracted": [{"id": "x", "pattern": "y"}]}, handle)
    try:
        cr.load_registry(bad)
        check("malformed registry raises", False)
    except ValueError:
        check("malformed registry raises", True)

print("")
print("SUMMARY: %d failed" % len(FAILED))
sys.exit(1 if FAILED else 0)
