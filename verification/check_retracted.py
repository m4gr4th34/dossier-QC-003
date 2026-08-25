#!/usr/bin/env python3
"""
check_retracted.py — retracted-claim sentinel.

Why this exists: the constitution says any change to a number updates every copy
in lockstep. Erratum SR-7 proved that rule was unenforced. A false CITE was
corrected on the live edition and in the claim ledger, and a stale copy of the
retracted claim survived in a working draft under expedition/ — the drafting
file for the very chapter the erratum corrects. No gate caught it, because
check_placeholders.py scans publication surfaces only and this was a draft.

This gate closes that hole for the one class of string that must never drift:
text this dossier has publicly RETRACTED. Unlike check_placeholders.py it is NOT
gated on release state. A placeholder is allowed to be drafty; a retracted claim
is wrong at every stage, in every file, including notes nobody publishes.

How it works — occurrence budgets, not an allowlist. A retracted claim
legitimately survives inside the erratum that retracts it: you cannot record
"the paper does not say X" without writing X. So the registry records, per
pattern, exactly how many times it may appear in each file. Any occurrence in an
unlisted file fails, and so does any INCREASE in a listed one. That is the
property an allowlist cannot give: allowlisting the manuscript wholesale would
let the false claim be re-introduced into the manuscript unnoticed, which is the
exact failure this gate exists to prevent.

Editing errata prose therefore requires deliberately updating a budget. That is
intended friction: the errata are the record, and the record should not move by
accident.

Registry: verification/retracted_claims.json
Stdlib only, fail-loud, same doctrine as the gates around it.

    python3 verification/check_retracted.py

Exit 0 if every pattern is within budget everywhere; exit 1 otherwise.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, "verification", "retracted_claims.json")

# Text surfaces worth scanning. Vendored runtimes and dependency trees are
# skipped: this dossier does not author them and cannot retract claims in them.
SCAN_EXT = {".md", ".html", ".csv", ".json", ".txt", ".js", ".py", ".yml", ".yaml"}
SKIP_DIRS = {"node_modules", "katex", "__pycache__"}

# Dot-directories are skipped by default — .git alone would swamp the walk — but a
# gate whose premise is "every file, every stage" cannot afford a silent blind spot,
# and workflow files are authored text like any other. .github is therefore scanned
# explicitly. Any future dot-directory holding authored prose belongs in this set.
DOT_SCAN = {".github"}

# This gate's own machinery is not scanned, and the exemption is deliberately two
# named files rather than a glob. Both MUST quote the retracted patterns in order
# to work at all: the registry defines them, and the test file feeds them to the
# matcher as fixtures. Nothing else is exempt — not drafts, not notes, not README.
# (The exemption exists because the gate flagged its own test file on first run,
# which is the behaviour working, not failing.)
SELF = {
    "verification/retracted_claims.json",
    "verification/check_retracted.test.py",
}


def iter_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in sorted(dirnames)
                       if d not in SKIP_DIRS
                       and (not d.startswith(".") or d in DOT_SCAN)]
        for name in sorted(filenames):
            if os.path.splitext(name)[1].lower() not in SCAN_EXT:
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
            if rel in SELF:
                continue
            yield rel, path


def load_registry(path=REGISTRY):
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    entries = data.get("retracted", [])
    if not isinstance(entries, list):
        raise ValueError("retracted_claims.json: 'retracted' must be a list")
    for entry in entries:
        for key in ("id", "pattern", "erratum", "budget"):
            if key not in entry:
                raise ValueError(
                    "retracted_claims.json: entry %r missing %r" % (entry.get("id"), key))
        if not isinstance(entry["budget"], dict):
            raise ValueError(
                "retracted_claims.json: %s budget must be an object" % entry["id"])
    return entries


def scan(entries, files=None):
    """Return (violations, counts). A violation is (entry_id, rel, found, allowed)."""
    compiled = [(e, re.compile(e["pattern"], re.IGNORECASE)) for e in entries]
    counts = {e["id"]: {} for e in entries}
    corpus = list(files) if files is not None else list(iter_files())
    for rel, path in corpus:
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as handle:
                text = handle.read()
        except OSError:
            continue
        for entry, rx in compiled:
            n = len(rx.findall(text))
            if n:
                counts[entry["id"]][rel] = n
    violations = []
    for entry, _ in compiled:
        budget = entry["budget"]
        for rel, n in sorted(counts[entry["id"]].items()):
            allowed = budget.get(rel, 0)
            if n > allowed:
                violations.append((entry["id"], rel, n, allowed))
    return violations, counts


def main():
    try:
        entries = load_registry()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("check_retracted: cannot read registry: %s" % exc)
        return 1

    if not entries:
        print("check_retracted: registry empty — nothing retracted yet, nothing to guard.")
        return 0

    violations, counts = scan(entries)

    print("=" * 72)
    print("RETRACTED-CLAIM SENTINEL — a retracted claim is wrong in every file, at every stage")
    print("=" * 72)
    for entry in entries:
        seen = counts[entry["id"]]
        total = sum(seen.values())
        print("[%s] %s" % (entry["id"], entry.get("note", "")))
        print("     erratum %s · retracted %s · %d occurrence(s) in %d file(s)"
              % (entry["erratum"], entry.get("retracted_on", "?"), total, len(seen)))

    if violations:
        print("")
        print("FAIL — retracted text found outside its recorded budget:")
        for entry_id, rel, found, allowed in violations:
            print("  %s  %s: found %d, budget %d" % (entry_id, rel, found, allowed))
        print("")
        print("Fix the file, or — if this occurrence is a deliberate addition to the")
        print("errata record — raise that file's budget in verification/retracted_claims.json")
        print("in the same commit. Never raise a budget to silence a stale copy.")
        print("=" * 72)
        return 1

    print("")
    print("PASS — every retracted claim appears only in the errata that retract it.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
