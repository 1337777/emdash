#!/usr/bin/env python3
"""Replay the checked native section pieces together; never run Lambdapi."""
import argparse
import hashlib
import json
from pathlib import Path
import re

OWNER_FRAGMENTS = (
    "fibcov_cart_core.lpfragment",
    "fibcov_cart_inclusion.lpfragment",
    "fibcov_cart_section_owner.lpfragment",
)
CONTROLS = (
    "fibcov_cart_core_controls.lpfragment",
    "fibcov_cart_inclusion_controls.lpfragment",
    "fibcov_cart_section_controls.lpfragment",
    "fibcov_cart_section_action_controls.lpfragment",
    "homd_u_peaks_precomp_observations.lpfragment",
    "homd_u_peaks_curry_observation.lpfragment",
)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pin_path = audit / "homd_native_section_assembly_inputs.json"
    pins = json.loads(pin_path.read_text())
    for name, expected in pins["sourceInputs"].items():
        assert digest((root / name).read_bytes()) == expected, (name, "changed source input")
    for source, receipt in pins["checkedSources"].items():
        check = json.loads((root / receipt).read_text())
        assert check["outcome"] == "passed-fresh"
        assert check["inputs"][source] == digest((root / source).read_bytes())
    donor = root / pins["donor"]
    source = donor.read_text()
    assert "symbol fibcov_cart_target " not in source
    owner_bodies = [(audit / n).read_text() for n in OWNER_FRAGMENTS]
    controls = [(audit / n).read_text() for n in CONTROLS]
    for body in controls:
        assert not re.search(r"(?m)^(?:rule|unif_rule|(?:injective |constant )?symbol)\b", body)
    assert sum(len(re.findall(r"(?m)^rule\b", b)) for b in owner_bodies) == 3
    assert not any(re.search(r"(?m)^unif_rule\b", b) for b in owner_bodies)
    prior_section = (root / "tmp/probes/fibcov_cart_section/combined_controls.lp").read_text()
    for body in owner_bodies + controls[:4]:
        assert body in prior_section, "body differs from checked section source"
    anchor = "// NON-LIBRARY direct identity ladder; all primitive Homd projection rules"
    assert source.count(anchor) == 1
    source = source.replace(anchor, "\n".join(owner_bodies) + "\n" + anchor)
    text = source + "\n" + "\n".join(controls)
    rules = re.findall(r"(?ms)^rule\b.*?;", owner_bodies[0])
    assert len(rules) == 3
    targets = {"combined_controls.lp": text}
    removals = {}
    for label, rule in zip(("root", "point", "component"), rules):
        assert text.count(rule) == 1, (label, "projection is not unique")
        name = "without_fibcov_" + label + ".lp"
        targets[name] = text.replace(rule, "")
        removals[name] = {"removedRuleSha256": digest(rule.encode()), "removedRule": rule}
    package = (root / "lambdapi.pkg").read_bytes()
    paths = [Path(__file__).resolve(), pin_path, *(root / n for n in pins["sourceInputs"])]
    manifest = {
        "status": "unchecked coexistence replay of checked native intermediate, FibCov, section and peak observations",
        "sourceInputs": {str(p.relative_to(root)): digest(p.read_bytes()) for p in paths},
        "donor": pins["donor"],
        "checkedSources": pins["checkedSources"],
        "ownerAnchor": anchor,
        "reusedOwnerFragments": list(OWNER_FRAGMENTS),
        "reusedControlFragments": list(CONTROLS),
        "outputs": {**{name: digest(body.encode()) for name, body in targets.items()}, "lambdapi.pkg": digest(package)},
        "exactRemovals": removals,
        "sourceAssertionCounts": {
            "positive": len(re.findall(r"(?m)^assert\b", text)),
            "negative": len(re.findall(r"(?m)^assertnot\b", text)),
        },
        "scope": [
            "Exact checked minimally guarded intermediate donor plus the same FibCov core/inclusion/section bodies at their existing owner anchor.",
            "No newly authored LP fragment, rule, unifier, or control; the three added runtime projections are copied unchanged from the checked FibCov core.",
            "All core/inclusion/section/action controls and both peak observation fragments coexist in one target.",
            "Old homd_id_src_sec remains unchanged; no legacywhole equality is appended or required.",
            "Adopting the actual derived body in old native owners with whole x/u compatibility is separate future work.",
            "Provisional Q/global Cartesian Prof profile and lift coherence limitations remain.",
        ],
        "checkerInvoked": False,
    }
    return root, targets, package, manifest

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--initialize-authoring", action="store_true")
    parser.add_argument("--check-authoring", action="store_true")
    parser.add_argument("--check-evidence", action="store_true")
    args = parser.parse_args()
    root, targets, package, manifest = build()
    path = Path(__file__).resolve().parent / "homd_native_section_assembly_verification.json"
    if args.initialize_authoring:
        assert not path.exists(), "preserve recorded evidence"
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
            assert digest((root / "tmp/probes/homd_native_section_assembly" / name).read_bytes()) == record["outputs"][name]
        print(f"{len(record.get('checks', {}))} recorded checks verified.")
    if not args.check_authoring and not args.check_evidence:
        output = root / "tmp/probes/homd_native_section_assembly"
        output.mkdir(parents=True, exist_ok=True)
        for name, text in targets.items():
            (output / name).write_text(text)
        (output / "lambdapi.pkg").write_bytes(package)
        (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"{len(targets)} native section assembly targets pinned; no checker run.")

if __name__ == "__main__":
    main()
