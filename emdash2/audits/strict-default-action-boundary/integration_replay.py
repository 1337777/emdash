#!/usr/bin/env python3
"""Prepare source-pinned consumer packages and the Cartesian-boundary audit.

This is source assembly only. Run Lambdapi through the normal resource guard.
"""

import hashlib
import json
from pathlib import Path
import runpy
import shutil
import sys


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    sys.path.insert(0, str(root / "scripts"))
    from check_registry import input_hashes

    runpy.run_path(str(audit / "replay.py"), run_name="__main__")
    output = root / "tmp/probes/strict_default_action"
    onecat = root / "emdash3_2_one_cat_action_paths.lp"
    text = onecat.read_text()
    owner = "symbol one_cat_composition_path"
    end = "\nsymbol one_cat_component_naturality_path"
    if text.count(owner) != 1 or text.count(end) != 1:
        raise SystemExit("one-category composition owner changed")
    start = text.index("≔ @eq_trans", text.index(owner))
    finish = text.index(end, start)
    replacement = (audit / "one_cat_composition_body.lpfragment").read_text()
    adapted = text[:start] + replacement + text[finish:]
    packages = {}
    for target, variants in (
        ("emdash3_2_represented_comma_families.lp", ("baseline", "capped", "whole", "intrinsic", "evaluated", "evaluated_rhs")),
        ("emdash3_2_checks.lp", ("evaluated",)),
    ):
        inputs = input_hashes([Path(target)], root)
        for variant in variants:
            name = "diagnostic_evaluated" if target == "emdash3_2_checks.lp" else "comma_" + variant
            package = output / name
            package.mkdir(exist_ok=True)
            if any(package.rglob("*.lpo")):
                raise SystemExit("compiled objects present in source-only replay: " + str(package))
            for rel in inputs:
                dest = package / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                if rel == "emdash3_2.lp":
                    # Baseline has no candidates; other stages use exact owner edits.
                    base_variant = "evaluated" if variant == "evaluated_rhs" else variant
                    source = root / rel if variant == "baseline" else output / ("source_" + base_variant + ".lp")
                    if variant == "evaluated_rhs":
                        clause = (audit / "intrinsic_rule.lpfragment").read_text()
                        candidate = source.read_text()
                        if candidate.count(clause) != 1:
                            raise SystemExit("intrinsic clause changed")
                        dest.write_text(candidate.replace(clause, clause.replace(
                            "functord_transport_lhs_func", "functord_transport_rhs_func")))
                    else:
                        shutil.copyfile(source, dest)
                elif rel == onecat.name and variant != "baseline":
                    dest.write_text(adapted)
                else:
                    shutil.copyfile(root / rel, dest)
            packages[name] = {
                "target": target, "originalInputs": inputs,
                "candidateInputs": input_hashes([Path(target)], package),
            }

    # The unsafe commuting-square construction needs only the first capped
    # strictness rule; it does not use Homd or an identity-compositor clause.
    counter = output / "evaluation_naturality_capped.lp"
    counter.write_text((output / "source_capped.lp").read_text() + "\n" +
                       (audit / "evaluation_naturality_audit.lpfragment").read_text())
    cart = output / "package_evaluated/cartesian_profile.lp"
    cart.write_text((audit / "cartesian_profile.lpfragment").read_text())
    manifest = {
        "status": "non-library; unrestricted Cartesian evaluation rejects blanket promotion",
        "authoringInputs": {str(p.relative_to(root)): digest(p) for p in sorted(audit.iterdir())
                            if p.suffix in (".py", ".lpfragment")},
        "packages": packages,
        "counterexample": {"target": str(counter.relative_to(root)), "sha256": digest(counter)},
        "cartesianProfile": {"target": str(cart.relative_to(root)), "sha256": digest(cart)},
    }
    (output / "integration_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print("Prepared source-only consumer packages and the Cartesian-boundary audit.")


if __name__ == "__main__":
    main()
