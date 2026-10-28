#!/usr/bin/env python3
"""Replay the native triangle, higher shape/families and explicit pending boundary."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REPO = ROOT.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_registry import input_hashes  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("baseline", "qualification", "unit-pending",
                                          "higher-recursion", "higher-family",
                                          "higher-qualification", "higher-dependencies",
                                          "vertices-pending", "coefficient-boundary-pending",
                                          "boundary-qualification", "constant-total-pending",
                                          "constant-qualification", "endpoints-qualification",
                                          "shared-edge-pending", "universal-qualification",
                                          "projection-law-proof", "projection-qualification",
                                          "projection-omission", "sigma-totalization",
                                          "sigma-unit-view", "sigma-unit-omission",
                                          "sigma-unit-derived", "arrow-total-duality",
                                          "arrow-duality-omission", "arrow-duality-boundary-proof",
                                          "arrow-duality-unit-pending", "triangle-connecting",
                                          "family-duality-proof", "family-duality-view-omission",
                                          "triangle-endpoints-pending", "duality-view-broad-regression"),
                        default="qualification")
    parser.add_argument("--assemble-only", action="store_true")
    args = parser.parse_args()
    record = json.loads((HERE / "verification.json").read_text())
    mode = record["modes"][args.mode]
    for name, expected in record["artifacts"].items():
        if digest(HERE / name) != expected:
            raise SystemExit(f"simplex artifact drift: {name}")
    for name, expected in record["activeSources"].items():
        if digest(ROOT / name) != expected:
            raise SystemExit(f"simplex active-source drift: {name}")
    destination = ROOT / "tmp/probes/native_nerve_foundations"
    destination.mkdir(parents=True, exist_ok=True)
    package = Path(tempfile.mkdtemp(prefix="simplex-core-", dir=destination))
    for name in record["activeSources"]:
        target = package / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
    (package / "lambdapi.pkg").write_text(record["packageText"])

    def fragment(name: str) -> str:
        return (HERE / name).read_text() + record["artifactSuffixes"].get(name, "")

    for insertion in mode["ownerInsertions"]:
        target = package / insertion["owner"]
        if digest(target) != insertion["parentSha256"]:
            raise SystemExit(f"simplex insertion parent drift: {insertion['owner']}")
        content = target.read_text()
        anchor = insertion["before"]
        if content.count(anchor) != 1:
            raise SystemExit(f"simplex insertion anchor is not unique: {anchor!r}")
        target.write_text(content.replace(anchor, fragment(insertion["fragment"]) + anchor, 1))
    programs = {**record["programs"], **mode.get("programOverrides", {})}
    for target, source in programs.items():
        content = fragment(source)
        stop = mode.get("programPrefixBefore", {}).get(target)
        if stop:
            if content.count(stop) != 1:
                raise SystemExit(f"simplex program prefix is not unique: {stop!r}")
            content = content.split(stop, 1)[0]
        destination = package / target
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content)
    if input_hashes([Path(mode["target"])], package) != mode["expectedInputs"]:
        raise SystemExit("simplex assembly differs from the recorded input snapshot")
    print(f"Exact simplex {args.mode} assembly verified: {package}", flush=True)
    if args.assemble_only:
        return 0
    checker_dir = Path(subprocess.check_output([
        sys.executable, str(REPO / "scripts/verification-toolchain.py"), "batch-path",
    ], cwd=REPO, text=True).strip())
    if digest(checker_dir / "lambdapi") != record["checker"]["sha256"]:
        raise SystemExit("simplex checker drift")
    env = os.environ.copy()
    env.update({
        "PATH": str(checker_dir) + os.pathsep + env.get("PATH", ""),
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
