#!/usr/bin/env python3
"""Emit the coefficient countercheck before the evaluation/curry owners.

NON-LIBRARY: a successful adverse construction shows why changing only
Eval cannot repair the strict-default migration. The baseline must reject
the strictness lemma. No output is imported by the library.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pin = "f8af1fca472657ff1598c639eb29c0566e7b2ec0"
    source = subprocess.check_output(
        ["git", "show", pin + ":emdash2/emdash3_2.lp"], cwd=root, text=True)
    expected = "6a980df34be718a23a6be121d170153650830a49f54b7e0eca415705ffb2068a"
    assert digest(source) == expected, "Historical source changed"
    rule = (audit / "composition_rule.lpfragment").read_text()
    fragment = (audit / "coefficient_naturality_audit.lpfragment").read_text()
    assert not re.search(r"\b(?:Eval_\w*|curry_\w*|homd_\w*|Op_\w*)\b", fragment)
    owner = "/*\n  The former capped composition cut and detached all-components law are\n"
    insertion = "// 7a. Internalized product formation and product maps"
    assert source.count(owner) == source.count(insertion) == 1
    assert source.index(insertion) < source.index("symbol Eval_func ")
    output = root / "tmp/probes/strict_default_coefficient"
    output.mkdir(parents=True, exist_ok=True)
    records = {}
    for variant in ("baseline", "capped", "no_cat_component"):
        candidate = source
        if variant != "baseline":
            candidate = candidate.replace(owner, rule + "\n" + owner)
        if variant == "no_cat_component":
            pattern = (r"(?m)^rule @tapp0_fapp0\s+_ _\s+_ _\s+\$i\s+"
                       r"\(@comp_prod_fapp1_fapp0 Cat_cat[\s\S]*?;\n")
            candidate, count = re.subn(pattern, "// Control: Cat composition component beta omitted.\n", candidate)
            assert count == 1, count
        candidate = candidate.replace(insertion, fragment + "\n" + insertion)
        target = output / (variant + ".lp")
        target.write_text(candidate)
        records[variant] = {"path": str(target.relative_to(root)), "sha256": digest(candidate)}
    manifest = {"status": "non-library adverse construction", "sourcePin": pin,
                "sourceSha256": expected,
                "fragmentSha256": digest(fragment), "strictRuleSha256": digest(rule),
                "authoringInputs": {
                    str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in (Path(__file__), audit / "coefficient_naturality_audit.lpfragment",
                              audit / "composition_rule.lpfragment")},
                "outputs": records}
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print("Emitted coefficient audit and controls before evaluation/curry.")


if __name__ == "__main__":
    main()
