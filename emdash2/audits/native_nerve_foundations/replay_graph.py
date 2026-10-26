#!/usr/bin/env python3
"""Replay the pinned native graph construction in an isolated owner copy."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from replay_realization import ROOT, REPO, digest, pinned_file

HERE = Path(__file__).resolve().parent


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout-seconds", type=int, default=90)
    parser.add_argument("--memory-mib", type=int, choices=(2048, 3072), default=2048,
                        help="explicit reviewed memory profile; default remains 2 GiB")
    parser.add_argument("--record", default="graph_verification.json",
                        help="pinned verification record in this audit directory")
    args = parser.parse_args()
    if not 1 <= args.timeout_seconds <= 3600:
        parser.error("timeout must be between 1 and 3600 seconds")
    record = json.loads(pinned_file(HERE, args.record).read_text())
    for name, expected in record["receiverInputs"].items():
        if digest(pinned_file(ROOT, name)) != expected:
            raise SystemExit(f"receiver source drift: {name}")
    for name, expected in record["artifactHashes"].items():
        if digest(pinned_file(HERE, name)) != expected:
            raise SystemExit(f"audit source drift: {name}")
    checker_dir = subprocess.check_output(
        [sys.executable, str(REPO / "scripts/verification-toolchain.py"), "batch-path"],
        cwd=REPO, text=True,
    ).strip()
    if digest(Path(checker_dir) / "lambdapi") != record["checker"]["sha256"]:
        raise SystemExit("checker differs from the reviewed toolchain")
    scratch = ROOT / "tmp/probes/native_nerve_foundations"
    scratch.mkdir(parents=True, exist_ok=True)
    package = Path(tempfile.mkdtemp(prefix="graph-replay-", dir=scratch))
    for name in record["receiverInputs"]:
        destination = package / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(pinned_file(ROOT, name), destination)
    for patch in record["ownerPatches"]:
        owner = pinned_file(package, patch["owner"])
        source = owner.read_text()
        if source.count(patch["anchor"]) != 1:
            raise SystemExit(f"owner anchor changed: {patch['owner']}")
        source = source.replace(
            patch["anchor"], pinned_file(HERE, patch["fragment"]).read_text()
            + "\n" + patch["anchor"], 1,
        )
        owner.write_text(source)
        if digest(owner) != patch["resultSha256"]:
            raise SystemExit(f"assembled owner differs: {patch['owner']}")
    for name, program in record["programs"].items():
        if Path(name).name != name or Path(name).suffix != ".lp":
            raise SystemExit(f"invalid generated program name: {name}")
        destination = package / name
        destination.write_text(program["prefix"] + program["separator"].join(
            pinned_file(HERE, part).read_text() for part in program["fragments"]
        ))
        if digest(destination) != program["sha256"]:
            raise SystemExit(f"assembled program differs: {name}")
    env = os.environ.copy()
    env.update({
        "PATH": checker_dir + os.pathsep + env.get("PATH", ""),
        "OCAMLRUNPARAM": "o=20,v=1024",
        "EMDASH_LAMBDAPI_WARNINGS": "1",
        "EMDASH_LAMBDAPI_FLAGS": "--too-long=0.5",
        "EMDASH_LP_MEMORY_MIB": str(args.memory_mib),
        "EMDASH_LP_FILE_MIB": "64",
        "EMDASH_LP_RESOURCE_BACKEND": "auto",
    })
    print(f"isolated package={package}; production sources unchanged", flush=True)
    return subprocess.run([
        sys.executable, str(ROOT / "scripts/run_lambdapi.py"),
        "--no-colors", "--quiet", "--timeout-ms", str(args.timeout_seconds * 1000),
        "--package-root", str(package), record["target"],
    ], cwd=REPO, env=env).returncode


if __name__ == "__main__":
    raise SystemExit(main())
