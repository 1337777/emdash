#!/usr/bin/env python3
"""Emit a canonical strict-target FibCov audit; never invoke Lambdapi."""
import argparse
import hashlib
import json
from pathlib import Path
import re

FRAGMENTS = ("core", "inclusion", "core_controls", "inclusion_controls", "legacy_whole_boundary")

def digest(data):
    return hashlib.sha256(data).hexdigest()

def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pins_path = audit / "fibcov_cart_inputs.json"
    pins = json.loads(pins_path.read_text())
    for name, expected in pins["sourceInputs"].items():
        assert digest((root / name).read_bytes()) == expected, (name, "source pin changed")
    donor = root / pins["donor"]
    source = donor.read_text()
    prior_path = audit / "homd_u_normalization_verification.json"
    prior = json.loads(prior_path.read_text())
    assert digest(source.encode()) == prior["outputs"][donor.name]
    assert prior["checks"][donor.name]["outcome"] == "passed-fresh"
    paths = {n: audit / ("fibcov_cart_" + n + ".lpfragment") for n in FRAGMENTS}
    body = {n: p.read_text() for n, p in paths.items()}
    assert len(re.findall(r"(?m)^rule\b", body["core"])) == 3
    assert not re.search(r"(?m)^(?:rule|unif_rule)\b", body["inclusion"])
    anchor = "// NON-LIBRARY direct identity ladder; all primitive Homd projection rules"
    assert source.count(anchor) == 1
    core = source.replace(anchor, body["core"] + "\n" + anchor)
    full = source.replace(anchor, body["core"] + "\n" + body["inclusion"] + "\n" + anchor)
    targets = {
        "core_controls.lp": core + "\n" + body["core_controls"],
        "inclusion_owner.lp": full,
        "inclusion_controls.lp": full + "\n" + body["core_controls"] + "\n" + body["inclusion_controls"],
        "legacy_whole_boundary.lp": full + "\n" + body["legacy_whole_boundary"],
    }
    package = (root / "lambdapi.pkg").read_bytes()
    inputs = [Path(__file__).resolve(), pins_path, prior_path, donor, root / "lambdapi.pkg", *paths.values()]
    manifest = {
        "status": "unchecked canonical structural strict-target FibCov prototype",
        "sourceInputs": {str(p.relative_to(root)): digest(p.read_bytes()) for p in inputs},
        "donor": str(donor.relative_to(root)),
        "donorReceipt": prior["checks"][donor.name]["receipt"],
        "ownerAnchor": anchor,
        "outputs": {name: digest(text.encode()) for name, text in targets.items()},
        "assertionCounts": {name: {
            "positive": len(re.findall(r"(?m)^assert\b", text)),
            "negative": len(re.findall(r"(?m)^assertnot\b", text)),
        } for name, text in targets.items()},
        "scope": [
            "Canonical structural contract: strict I_x-to-E values for default-strict E, carried by one ambient-in-x whole FibCov map.",
            "Strict target and ambient target inclusion are actual definitions from existing hom_con, Rep_cart_func, Cartesian inclusion and generic pullback Hom action.",
            "Three projection rules only; no unification rule, generic FF admission, x-strictness, proof payload, coend derivation or Homd-section extension.",
            "Old donor FibCov declarations remain byte-identical; fresh ambient views have tested-intended y agreement but whole legacy equality is a separate positive boundary.",
            "Whole u-parameter action is retained by the source component functor; formation controls do not supply its further computation.",
            "Provisional Q/global Cartesian Prof donor profile remains; raw-preserving coefficient integration is not claimed.",
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
    path = Path(__file__).resolve().parent / "fibcov_cart_verification.json"
    if args.initialize_authoring:
        assert not path.exists(), "do not overwrite measured evidence"
        record = dict(manifest)
        record["checks"] = {}
        record["uncheckedTargets"] = list(targets)
        path.write_text(json.dumps(record, indent=2) + "\n")
    record = json.loads(path.read_text())
    for group in ("sourceInputs", "outputs"):
        assert record[group] == manifest[group], (group, "review changed source before refreshing")
    if args.check_evidence:
        for name, evidence in record.get("checks", {}).items():
            for field, pin in (("receipt", "receiptSha256"), ("log", "logSha256"), ("output", "outputSha256")):
                if field in evidence:
                    assert digest((root / evidence[field]).read_bytes()) == evidence[pin], (name, field)
            assert digest((root / "tmp/probes/fibcov_cart" / name).read_bytes()) == record["outputs"][name]
        print(f"{len(record.get('checks', {}))} recorded checks verified.")
    if not args.check_authoring and not args.check_evidence:
        output = root / "tmp/probes/fibcov_cart"
        output.mkdir(parents=True, exist_ok=True)
        for name, text in targets.items():
            (output / name).write_text(text)
        (output / "lambdapi.pkg").write_bytes(package)
        (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"{len(targets)} FibCov targets pinned; no checker run.")

if __name__ == "__main__":
    main()
