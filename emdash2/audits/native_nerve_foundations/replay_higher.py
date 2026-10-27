#!/usr/bin/env python3
"""Replay the staged higher-component comparison without changing production."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPO = ROOT.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_registry import input_hashes  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("integration", "instances", "without-bridge"),
                        default="integration")
    parser.add_argument("--assemble-only", action="store_true")
    args = parser.parse_args()
    record = json.loads((HERE / "higher_component_verification.json").read_text())
    mode = record["modes"][args.mode]
    for name, expected in record["artifacts"].items():
        if digest(HERE / name) != expected:
            raise SystemExit(f"higher-component artifact drift: {name}")
    parent = subprocess.run([
        sys.executable, str(HERE / record["baseReplay"]), "--assemble-only",
    ], cwd=REPO, capture_output=True, text=True, check=True)
    match = re.search(r"Exact candidate assembly verified: (.+)", parent.stdout)
    if not match:
        raise SystemExit("parent replay did not report its exact package")
    package = Path(match.group(1))
    fragment = (HERE / "higher_component_owner.lpfragment").read_text() + "\n"
    if args.mode == "without-bridge":
        marker = "// Identity-input component-first projection"
        if fragment.count(marker) != 1:
            raise SystemExit("higher projection removal marker changed")
        fragment = fragment[:fragment.index(marker)]
    core = package / "emdash3_2.lp"
    source = core.read_text()
    if source.count(record["coreAnchor"]) != 1:
        raise SystemExit("higher evaluation owner anchor changed")
    core.write_text(source.replace(record["coreAnchor"],
        fragment + record["coreAnchor"], 1))
    (package / record["newProgram"]).write_bytes(
        (HERE / "higher_component_readback.lpfragment").read_bytes())
    (package / record["instanceProgram"]).write_bytes(
        (HERE / "higher_component_instances.lpfragment").read_bytes() + b"\n")
    target = package / "native_nerve_section_review.lp"
    target.write_text(record["targetPrefix"] + target.read_text())
    if input_hashes([Path(mode["target"])], package) != mode["expectedInputs"]:
        raise SystemExit("assembled higher-component closure differs from its receipt")
    print(f"Exact {args.mode} assembly verified: {package}", flush=True)
    if args.assemble_only:
        return 0
    checker_dir = subprocess.check_output([
        sys.executable, str(REPO / "scripts/verification-toolchain.py"), "batch-path",
    ], cwd=REPO, text=True).strip()
    if digest(Path(checker_dir) / "lambdapi") != record["checker"]["sha256"]:
        raise SystemExit("checker differs from the recorded higher-component checks")
    env = os.environ.copy()
    env.update({
        "PATH": checker_dir + os.pathsep + env.get("PATH", ""),
        "OCAMLRUNPARAM": "o=20,v=1024", "EMDASH_LAMBDAPI_WARNINGS": "1",
        "EMDASH_LAMBDAPI_FLAGS": "--too-long=0.5", "EMDASH_LP_MEMORY_MIB": "2048",
        "EMDASH_LP_FILE_MIB": "64", "EMDASH_LP_RESOURCE_BACKEND": "auto",
    })
    return subprocess.run([
        sys.executable, str(ROOT / "scripts/run_lambdapi.py"), "--no-colors", "--quiet",
        "--timeout-ms", str(mode["timeoutMs"]), "--package-root", str(package), mode["target"],
    ], cwd=REPO, env=env).returncode


if __name__ == "__main__":
    raise SystemExit(main())
