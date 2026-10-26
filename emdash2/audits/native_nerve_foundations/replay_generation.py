#!/usr/bin/env python3
"""Replay walking source generation and whole oplax-family reconstruction."""
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
TARGET = "native_nerve_generation_review.lp"
OWNER = "emdash3_2_walking_arrow_introduction.lp"
ANCHOR = "// Postcomposition of the free walking-arrow introduction. A strict functor\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--without-generation", action="store_true")
    parser.add_argument("--timeout-seconds", type=int, default=90)
    args = parser.parse_args()
    if not 1 <= args.timeout_seconds <= 3600:
        parser.error("timeout must be between 1 and 3600 seconds")
    record = json.loads((HERE / "generation_verification.json").read_text())
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
    package = Path(tempfile.mkdtemp(prefix="walking-generation-", dir=scratch))
    for name in record["receiverInputs"]:
        destination = package / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(pinned_file(ROOT, name), destination)
    if not args.without_generation:
        owner = package / OWNER
        source = owner.read_text()
        if source.count(ANCHOR) != 1:
            raise SystemExit("walking introduction owner anchor changed")
        source = source.replace(
            ANCHOR, (HERE / "walking_generation_self.lpfragment").read_text()
            + "\n" + ANCHOR, 1,
        )
        owner.write_text(source)
        if digest(owner) != record["isolatedOwnerSha256"]:
            raise SystemExit("assembled owner differs from the qualified input")
    (package / TARGET).write_bytes((HERE / "walking_generation.lpfragment").read_bytes())
    env = os.environ.copy()
    env.update({
        "PATH": checker_dir + os.pathsep + env.get("PATH", ""),
        "OCAMLRUNPARAM": "o=20,v=1024",
        "EMDASH_LAMBDAPI_WARNINGS": "1",
        "EMDASH_LAMBDAPI_FLAGS": "--too-long=0.5",
        "EMDASH_LP_MEMORY_MIB": "2048",
        "EMDASH_LP_FILE_MIB": "64",
        "EMDASH_LP_RESOURCE_BACKEND": "auto",
    })
    print(f"isolated package={package}; production sources unchanged", flush=True)
    return subprocess.run([
        sys.executable, str(ROOT / "scripts/run_lambdapi.py"),
        "--no-colors", "--quiet", "--timeout-ms", str(args.timeout_seconds * 1000),
        "--package-root", str(package), TARGET,
    ], cwd=REPO, env=env).returncode


if __name__ == "__main__":
    raise SystemExit(main())
