#!/usr/bin/env python3
"""Replay the native realization in an isolated, pinned owner-position copy."""
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
ROOT = HERE.parents[1]
REPO = ROOT.parent
TARGET = "native_nerve_realization_review.lp"
ANCHOR = "// Strict default maps preserve represented postcomposition. Whole functors\n"
IMPORTS = (
    "require open emdash.audits.native_nerve_foundations.walking_observer;\n"
    "require open emdash.emdash3_2_arrow_diagram_families;\n"
)

sys.path.insert(0, str(ROOT / "scripts"))
from check_registry import local_file  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pinned_file(root: Path, name: str) -> Path:
    path = local_file(root, name)
    if path.relative_to(root).as_posix() != name:
        raise SystemExit(f"noncanonical pinned path: {name}")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("candidate", "units-baseline", "without-units"),
                        default="candidate")
    parser.add_argument("--timeout-seconds", type=int, default=90)
    parser.add_argument("--timing", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.timeout_seconds <= 3600:
        parser.error("timeout must be between 1 and 3600 seconds")

    record = json.loads((HERE / "realization_verification.json").read_text())
    for name, expected in record["receiverInputs"].items():
        if digest(pinned_file(ROOT, name)) != expected:
            raise SystemExit(f"receiver source drift: {name}; review before replay")
    for name, expected in record["artifactHashes"].items():
        if digest(pinned_file(HERE, name)) != expected:
            raise SystemExit(f"audit source drift: {name}; review before replay")

    checker_dir = subprocess.check_output(
        [sys.executable, str(REPO / "scripts/verification-toolchain.py"), "batch-path"],
        cwd=REPO, text=True,
    ).strip()
    if digest(Path(checker_dir) / "lambdapi") != record["checker"]["sha256"]:
        raise SystemExit("checker bytes differ from the reviewed verification toolchain")

    scratch = ROOT / "tmp/probes/native_nerve_foundations"
    scratch.mkdir(parents=True, exist_ok=True)
    package = Path(tempfile.mkdtemp(prefix=f"realization-{args.mode}-", dir=scratch))
    for name in record["receiverInputs"]:
        destination = package / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(pinned_file(ROOT, name), destination)

    if args.mode != "without-units":
        core = package / "emdash3_2.lp"
        source = core.read_text()
        if source.count(ANCHOR) != 1:
            raise SystemExit("postcomposition owner anchor changed")
        core.write_text(source.replace(
            ANCHOR, (HERE / "total_dual_postcomp_units.lpfragment").read_text() + "\n" + ANCHOR,
            1,
        ))

    program = IMPORTS if args.mode == "units-baseline" else (
        HERE / "walking_realization.lpfragment"
    ).read_text()
    (package / TARGET).write_text(program)
    env = os.environ.copy()
    env.update({
        "PATH": checker_dir + os.pathsep + env.get("PATH", ""),
        "OCAMLRUNPARAM": "o=20,v=1024",
        "EMDASH_LAMBDAPI_WARNINGS": "1",
        "EMDASH_LAMBDAPI_FLAGS": "--too-long=0.5" if args.timing else "",
        "EMDASH_LP_MEMORY_MIB": "2048",
        "EMDASH_LP_FILE_MIB": "64",
        "EMDASH_LP_RESOURCE_BACKEND": "auto",
    })
    print(f"mode={args.mode}; isolated package={package}", flush=True)
    print("Production files are unchanged; the existing serial/no-swap guard owns execution.",
          flush=True)
    result = subprocess.run([
        sys.executable, str(ROOT / "scripts/run_lambdapi.py"),
        "--no-colors", "--quiet", "--timeout-ms", str(args.timeout_seconds * 1000),
        "--package-root", str(package), TARGET,
    ], cwd=REPO, env=env)
    # In omission mode a failed type-preservation check is an expected control,
    # but its real exit status is retained rather than relabeled a passing run.
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
