#!/usr/bin/env python3
"""Replay existing-owner Homd x consumers without invoking a checker."""
import argparse
import hashlib
import json
from pathlib import Path
import re

NAMES = (
    "target_controls", "section_y_comparison", "right_route_leaf",
    "identity_action_boundary", "route_coherence_boundary",
)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pins_path = audit / "homd_x_consumer_inputs.json"
    pins = json.loads(pins_path.read_text())
    for name, expected in pins["sourceInputs"].items():
        assert digest((root / name).read_bytes()) == expected, (name, "source pin changed")
    donor = root / pins["donor"]
    record_path = audit / "foundation_assembly_verification.json"
    prior = json.loads(record_path.read_text())
    source = donor.read_text()
    assert digest(source.encode()) == prior["outputs"][donor.name]
    assert prior["checks"][donor.name]["outcome"] == "passed-fresh"
    fragments = [audit / ("homd_x_consumer_" + name + ".lpfragment") for name in NAMES]
    targets = {}
    for name, path in zip(NAMES, fragments):
        # Preserve the separator bytes of the already checked targets while
        # keeping authoring fragments free of extra blank lines at EOF.
        body = path.read_text().rstrip("\n") + "\n\n"
        assert not re.search(r"(?m)^(?:rule|unif_rule|(?:injective |constant )?symbol)\b", body), path.name
        targets[name + ".lp"] = source + "\n" + body
    package = (root / "lambdapi.pkg").read_bytes()
    inputs = [Path(__file__).resolve(), pins_path, record_path, donor, root / "lambdapi.pkg", *fragments]
    manifest = {
        "status": "unchecked existing-owner identity Homd x consumer audit",
        "sourceInputs": {str(p.relative_to(root)): digest(p.read_bytes()) for p in inputs},
        "donor": str(donor.relative_to(root)),
        "donorReceipt": prior["checks"][donor.name]["receipt"],
        "outputs": {name: digest(body.encode()) for name, body in targets.items()},
        "newAssertionCounts": {name: {
            "positive": len(re.findall(r"(?m)^assert\b", path.read_text())),
            "negative": len(re.findall(r"(?m)^assertnot\b", path.read_text())),
        } for name, path in zip(NAMES, fragments)},
        "checkerInvoked": False,
        "scope": [
            "No new runtime rewrite, unification rule, primitive, or operational proof parameter.",
            "Homd_target action is existing ordinary Hom postcomposition; source section transport retains the stable postcomposition runtime head.",
            "The y-component observation applies generic equality action to the whole section comparison.",
            "The right-route ordinary leaf is computed through existing identity source/y/v/q projections and strict E action.",
            "Identity whole source-route action is a positive boundary; whole source/right equality is only an optional stronger diagnostic, not an ambient Homd requirement.",
            "Passing the target transport and leaf consumers does not establish identity Homd x coherence or represented lift triangle/composition.",
        ],
    }
    manifest["outputs"]["lambdapi.pkg"] = digest(package)
    return root, targets, package, manifest

def check_evidence(root, record):
    checked = 0
    for name, evidence in record.get("checks", {}).items():
        source = root / "tmp/probes/homd_x_consumer" / name
        assert digest(source.read_bytes()) == record["outputs"][name]
        for field, sha in (("receipt", "receiptSha256"), ("log", "logSha256"), ("output", "outputSha256")):
            if field in evidence:
                assert digest((root / evidence[field]).read_bytes()) == evidence[sha], (name, field)
        checked += 1
    return checked

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh-authoring", action="store_true")
    parser.add_argument("--check-authoring", action="store_true")
    parser.add_argument("--check-evidence", action="store_true")
    args = parser.parse_args()
    root, targets, package, manifest = build()
    path = Path(__file__).resolve().parent / "homd_x_consumer_verification.json"
    if args.refresh_authoring:
        assert not path.exists(), "preserve existing evidence; review an explicit successor"
        record = dict(manifest)
        record["checks"] = {}
        record["uncheckedTargets"] = list(targets)
        path.write_text(json.dumps(record, indent=2) + "\n")
    record = json.loads(path.read_text())
    for group in ("sourceInputs", "outputs"):
        assert record[group] == manifest[group], (group, "changed; review before refreshing evidence")
    if args.check_evidence:
        print(f"{check_evidence(root, record)} recorded receipts verified; no checker run.")
    if not args.check_authoring and not args.check_evidence:
        output = root / "tmp/probes/homd_x_consumer"
        output.mkdir(parents=True, exist_ok=True)
        for name, body in targets.items():
            (output / name).write_text(body)
        (output / "lambdapi.pkg").write_bytes(package)
        (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"{len(targets)} Homd x-consumer sources pinned; no checker run.")

if __name__ == "__main__":
    main()
