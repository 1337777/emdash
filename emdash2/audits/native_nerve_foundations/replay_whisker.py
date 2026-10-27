#!/usr/bin/env python3
"""Replay the native whole post-cell candidate at its recorded prefix."""
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
    parser.add_argument("--assemble-only", action="store_true")
    args = parser.parse_args()
    record = json.loads((HERE / "whisker_verification.json").read_text())
    for name, expected in record["artifacts"].items():
        if digest(HERE / name) != expected:
            raise SystemExit(f"candidate artifact drift: {name}")
    base = record["baseReplay"]
    result = subprocess.run([
        sys.executable, str(HERE / base["script"]),
        "--mode", base["mode"], "--source-revision", base["sourceRevision"],
        "--assemble-only",
    ], cwd=REPO, capture_output=True, text=True, check=True)
    match = re.search(r"package=(.+)", result.stdout)
    if not match:
        raise SystemExit("parent replay did not report its verified package")
    package = Path(match.group(1))
    owner = package / "emdash3_2.lp"
    source = owner.read_text()
    anchor = record["coreAnchor"]
    if source.count(anchor) != 1:
        raise SystemExit("core owner anchor changed")
    owner.write_text(source.replace(anchor,
        (HERE / "whisker_owner.lpfragment").read_text() + "\n" + anchor, 1))
    subprocess.run([
        "patch", "--batch", "--forward", "--silent", "-p1", "-d", str(package),
        "-i", str(HERE / "whisker_native_owner.patch"),
    ], check=True)
    (package / record["addedProgram"]).write_bytes(
        (HERE / "whisker_functor.lpfragment").read_bytes())
    (package / record["addedControls"]).write_bytes(
        (HERE / "whisker_controls.lpfragment").read_bytes())
    target = package / record["target"]
    target.write_text(target.read_text() + record["targetSuffix"])
    if input_hashes([Path(record["target"])], package) != record["expectedInputs"]:
        raise SystemExit("candidate closure differs from the checked inputs")
    print(f"Exact candidate assembly verified: {package}", flush=True)
    if args.assemble_only:
        return 0
    checker_dir = subprocess.check_output([
        sys.executable, str(REPO / "scripts/verification-toolchain.py"), "batch-path",
    ], cwd=REPO, text=True).strip()
    if digest(Path(checker_dir) / "lambdapi") != record["checker"]["sha256"]:
        raise SystemExit("checker differs from the qualified candidate")
    env = os.environ.copy()
    env.update({
        "PATH": checker_dir + os.pathsep + env.get("PATH", ""),
        "OCAMLRUNPARAM": "o=20,v=1024", "EMDASH_LAMBDAPI_WARNINGS": "1",
        "EMDASH_LAMBDAPI_FLAGS": "--too-long=0.5", "EMDASH_LP_MEMORY_MIB": "2048",
        "EMDASH_LP_FILE_MIB": "64", "EMDASH_LP_RESOURCE_BACKEND": "auto",
    })
    return subprocess.run([
        sys.executable, str(ROOT / "scripts/run_lambdapi.py"), "--no-colors", "--quiet",
        "--timeout-ms", "180000", "--package-root", str(package), record["target"],
    ], cwd=REPO, env=env).returncode


if __name__ == "__main__":
    raise SystemExit(main())
