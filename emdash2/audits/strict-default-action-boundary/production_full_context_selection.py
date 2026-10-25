#!/usr/bin/env python3
"""Prepare all central diagnostics with the approved whole terminal contract.

Non-library replay. No assertion is omitted. The former except-terminal
filename remains an import shim for historical regression drivers.
"""
from __future__ import annotations
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import foundation_terminal_contract as terminal_contract

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_check_catalog import parse_checks, read_lines


def prepare(package: Path) -> dict:
    package = package.resolve()
    source = package / "emdash3_2_checks.lp"
    before = parse_checks(read_lines(source))
    terminal_contract.apply(package)
    target = package / "central_full_context.lp"
    selected = parse_checks(read_lines(target))
    assert len(before) == len(selected)
    assert source.read_bytes() == target.read_bytes()
    return {
        "source": str(source.relative_to(ROOT)),
        "sourceSha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "target": str(target.relative_to(ROOT)),
        "targetSha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "assertions": len(selected),
        "polarities": dict(Counter(c.first_line.split()[0] for c in selected)),
        "approvedWholeTerminalComparisons": 5,
        "excludedObligations": [],
    }


if __name__ == "__main__":
    print(json.dumps(prepare(ROOT / "tmp/probes/production_owner_migration/package"),
                     indent=2))
