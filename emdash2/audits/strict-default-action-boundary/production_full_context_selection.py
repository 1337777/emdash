#!/usr/bin/env python3
"""Prepare the explicit all-import diagnostic scope; never edit its source.

Non-library R10/R12 audit. The five terminal runtime observations remain
required in emdash3_2_checks.lp and are excluded only from this named target.
Run production_owner_migration.py first after changing its authoring inputs.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_check_catalog import parse_checks, read_lines


def prepare(package: Path) -> dict:
    source = package / "emdash3_2_checks.lp"
    original = source.read_text()
    raw = original.splitlines(keepends=True)
    checks = parse_checks(read_lines(source))
    omitted = parse_checks(read_lines(
        package / "central_public_homd_terminal_obligations.lp"))
    assert len(checks) == 2440 and len(omitted) == 5
    remaining = Counter(c.statement for c in omitted)
    dispositions = []
    for check in checks:
        if not remaining[check.statement]:
            continue
        start = check.line - 1
        end = start
        while not raw[end].strip().endswith(";"):
            end += 1
        for i in range(start, end + 1):
            raw[i] = "// R01-R03 unresolved runtime obligation: " + raw[i]
        dispositions.append({"originalAssertion": check.index,
                             "line": check.line, "statement": check.statement})
        remaining[check.statement] -= 1
    assert not +remaining and len(dispositions) == 5
    target = package / "central_full_context_except_terminal.lp"
    target.write_text("".join(raw))
    selected = parse_checks(read_lines(target))
    assert len(selected) == 2435
    assert (Counter(c.statement for c in selected)
            + Counter(c.statement for c in omitted)
            == Counter(c.statement for c in checks))
    imports = lambda text: re.findall(r"(?m)^require\b.*?;", text, re.S)
    assert imports(original) == imports(target.read_text())
    symbols = lambda text: re.findall(
        r"(?m)^\s*(?:(?:constant|injective|opaque|private|protected)\s+)*"
        r"symbol\s+([^\s\[:(]+)", text)
    assert symbols(original) == symbols(target.read_text())
    assert len(symbols(original)) == 66
    return {
        "source": str(source.relative_to(ROOT)),
        "sourceSha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "target": str(target.relative_to(ROOT)),
        "targetSha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "assertions": len(selected),
        "polarities": dict(Counter(c.first_line.split()[0] for c in selected)),
        "unchangedDeclarations": len(symbols(original)),
        "unchangedImportOrder": True,
        "excludedObligations": dispositions,
    }


if __name__ == "__main__":
    print(json.dumps(prepare(ROOT / "tmp/probes/production_owner_migration/package"),
                     indent=2))
