#!/usr/bin/env python3
"""Emit a derived FibCov-lift section audit; no checker or new rules."""
import argparse
import hashlib
import json
from pathlib import Path
import re

def digest(data):
    return hashlib.sha256(data).hexdigest()

def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pins_path = audit / "fibcov_cart_section_inputs.json"
    pins = json.loads(pins_path.read_text())
    for name, expected in pins["sourceInputs"].items():
        assert digest((root / name).read_bytes()) == expected, (name, "changed input")
    donor = root / pins["donor"]
    receipt = root / pins["donorReceipt"]
    check = json.loads(receipt.read_text())
    assert check["outcome"] == "passed-fresh"
    assert check["inputs"][pins["donor"]] == digest(donor.read_bytes())
    names = ("owner", "controls", "action_controls")
    paths = [audit / ("fibcov_cart_section_" + n + ".lpfragment") for n in names]
    bodies = dict(zip(names, (p.read_text() for p in paths)))
    assert not any(re.search(r"(?m)^(?:rule|unif_rule)\b", b) for b in bodies.values())
    assert len(re.findall(r"(?m)^symbol\b", bodies["owner"])) == 1
    source = donor.read_text()
    anchor = "// NON-LIBRARY direct identity ladder; all primitive Homd projection rules"
    assert source.count(anchor) == 1
    prefix = source.replace(anchor, bodies["owner"] + "\n" + anchor)
    targets = {
        "section_controls.lp": prefix + "\n" + bodies["controls"],
        "action_controls.lp": prefix + "\n" + bodies["action_controls"],
        "combined_controls.lp": prefix + "\n" + bodies["controls"] + "\n" + bodies["action_controls"],
    }
    package = (root / "lambdapi.pkg").read_bytes()
    inputs = [Path(__file__).resolve(), pins_path, donor, receipt, root / "lambdapi.pkg", *paths]
    manifest = {
        "status": "unchecked section definition through the existing whole represented lift",
        "sourceInputs": {str(p.relative_to(root)): digest(p.read_bytes()) for p in inputs},
        "donor": pins["donor"],
        "donorReceipt": pins["donorReceipt"],
        "outputs": {n: digest(s.encode()) for n, s in targets.items()},
        "newAssertionCounts": {n: {
            "positive": len(re.findall(r"(?m)^assert\b", bodies[n])),
            "negative": len(re.findall(r"(?m)^assertnot\b", bodies[n])),
        } for n in ("controls", "action_controls")},
        "scope": [
            "One section definition with actual Homd_section_cat type; no new primitive, runtime rule, unifier or equality payload.",
            "The actual lift consumes the canonical structural strict-Y FibCov value; whole x strictness is not asserted.",
            "Consumers follow native y/v/f projections and whole/capped native y-action to the already selected lift R.",
            "No equality with the legacy homd_id_src_sec or independent FibCov root is required or supplied.",
            "This proposal does not yet migrate existing Homd names or qualify whole x/u compatibility, extracted laxity, lift triangle/composition, or raw-preserving Q integration.",
        ],
        "checkerInvoked": False,
    }
    manifest["outputs"]["lambdapi.pkg"] = digest(package)
    return root, targets, package, manifest

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--initialize-authoring", action="store_true")
    parser.add_argument("--check-authoring", action="store_true")
    parser.add_argument("--check-evidence", action="store_true")
    args = parser.parse_args()
    root, targets, package, manifest = build()
    path = Path(__file__).resolve().parent / "fibcov_cart_section_verification.json"
    if args.initialize_authoring:
        assert not path.exists(), "preserve measured evidence"
        record = dict(manifest)
        record["checks"] = {}
        record["uncheckedTargets"] = list(targets)
        path.write_text(json.dumps(record, indent=2) + "\n")
    record = json.loads(path.read_text())
    for key in ("sourceInputs", "outputs"):
        assert record[key] == manifest[key], (key, "changed authoring")
    if args.check_evidence:
        for name, check in record.get("checks", {}).items():
            for field, pin in (("receipt", "receiptSha256"), ("log", "logSha256"), ("output", "outputSha256")):
                if field in check:
                    assert digest((root / check[field]).read_bytes()) == check[pin], (name, field)
            assert digest((root / "tmp/probes/fibcov_cart_section" / name).read_bytes()) == record["outputs"][name]
        print(f"{len(record.get('checks', {}))} recorded checks verified.")
    if not args.check_authoring and not args.check_evidence:
        output = root / "tmp/probes/fibcov_cart_section"
        output.mkdir(parents=True, exist_ok=True)
        for name, text in targets.items():
            (output / name).write_text(text)
        (output / "lambdapi.pkg").write_bytes(package)
        (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"{len(targets)} derived section targets pinned; no checker run.")

if __name__ == "__main__":
    main()
