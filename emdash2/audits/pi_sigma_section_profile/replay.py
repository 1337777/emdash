#!/usr/bin/env python3
"""Replay the isolated Pi/Sigma profile correction with pinned sources."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPO = ROOT.parent
NATIVE = HERE.parent / "native_nerve_foundations"
sys.path.insert(0, str(ROOT / "scripts"))
from check_registry import input_hashes, local_file  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("core", "consumers", "generic-view", "reflexive",
                                           "central-cases", "nested", "native", "central"),
                        default="consumers")
    parser.add_argument("--timeout-seconds", type=int, default=90)
    parser.add_argument("--memory-mib", type=int, choices=(2048, 4096), default=2048)
    parser.add_argument("--source-revision",
                        help="Explicit Git revision of the pre-correction sources; all source pins still apply")
    parser.add_argument("--assemble-only", action="store_true",
                        help="Verify exact source assembly without launching a checker")
    args = parser.parse_args()
    if not 1 <= args.timeout_seconds <= 3600:
        parser.error("timeout must be between 1 and 3600 seconds")
    record = json.loads((HERE / "verification.json").read_text())
    mode = record["modes"][args.mode]
    if Path(mode["target"]).name != mode["target"] or Path(mode["target"]).suffix != ".lp":
        raise SystemExit("invalid generated target name")
    for name, expected in record["artifacts"].items():
        if digest(local_file(HERE, name)) != expected:
            raise SystemExit(f"audit artifact drift: {name}")
    inputs = dict(mode["receiverInputs"])
    for name, expected in record["patchInputs"].items():
        if name in inputs and inputs[name] != expected:
            raise SystemExit(f"conflicting source pin: {name}")
        inputs[name] = expected
    source_bytes = {}
    revision = None
    if args.source_revision:
        revision = subprocess.check_output([
            "git", "rev-parse", "--verify", "--end-of-options",
            args.source_revision + "^{commit}",
        ], cwd=REPO, text=True).strip()
    for name, expected in inputs.items():
        path = local_file(ROOT, name)
        content = (subprocess.check_output(
            ["git", "show", f"{revision}:emdash2/{name}"], cwd=REPO,
        ) if revision else path.read_bytes())
        if hashlib.sha256(content).hexdigest() != expected:
            raise SystemExit(f"receiver source drift: {name}")
        source_bytes[name] = content
    checker_dir = subprocess.check_output(
        [sys.executable, str(REPO / "scripts/verification-toolchain.py"), "batch-path"],
        cwd=REPO, text=True,
    ).strip()
    if digest(Path(checker_dir) / "lambdapi") != record["checker"]["sha256"]:
        raise SystemExit("checker differs from the reviewed toolchain")
    scratch = ROOT / "tmp/probes/native_nerve_foundations"
    scratch.mkdir(parents=True, exist_ok=True)
    package = Path(tempfile.mkdtemp(prefix=f"pi-sigma-{args.mode}-", dir=scratch))
    for name in inputs:
        destination = package / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(source_bytes[name])
    subprocess.run([
        "patch", "--batch", "--forward", "--silent", "-p2", "-d", str(package),
        "-i", str(HERE / "profile_correction.patch"),
    ], check=True)
    for name, expected in record["patchedOutputs"].items():
        if digest(local_file(package, name)) != expected:
            raise SystemExit(f"patched output differs: {name}")

    if args.mode == "native":
        for name, expected in mode["nativeArtifacts"].items():
            if digest(local_file(NATIVE, name)) != expected:
                raise SystemExit(f"native parent artifact drift: {name}")
        parent = json.loads(local_file(NATIVE, mode["parentRecord"]).read_text())
        for change in parent["ownerPatches"]:
            if change["fragment"] == "section_identity_presentation.lpfragment":
                continue
            owner = local_file(package, change["owner"])
            source = owner.read_text()
            if source.count(change["anchor"]) != 1:
                raise SystemExit(f"native owner anchor changed: {change['owner']}")
            fragment = local_file(NATIVE, change["fragment"]).read_text()
            if change["fragment"] == "native_section_totalization_owner.lpfragment":
                old = mode["identityViewOldBody"]
                if fragment.count(old) != 1:
                    raise SystemExit("native identity-view body changed")
                fragment = fragment.replace(old, "≔ s;", 1)
            owner.write_text(source.replace(change["anchor"], fragment + "\n" + change["anchor"], 1))
        for scope in parent.get("ownerPrefixes", []):
            owner = local_file(package, scope["owner"])
            source = owner.read_text()
            anchor = scope["throughAnchor"]
            if source.count(anchor) != 1:
                raise SystemExit("native prefix anchor changed")
            source = source[:source.index(anchor) + len(anchor)]
            for statement in scope["omittedImports"]:
                if source.count(statement + "\n") != 1:
                    raise SystemExit("native prefix import changed")
                source = source.replace(statement + "\n", "", 1)
            owner.write_text(source)
        for name, program in parent["programs"].items():
            if Path(name).name != name or Path(name).suffix != ".lp":
                raise SystemExit(f"invalid native program name: {name}")
            (package / name).write_text(program["prefix"] + program["separator"].join(
                local_file(NATIVE, part).read_text() for part in program["fragments"]
            ))
    elif mode.get("program"):
        (package / mode["target"]).write_bytes(
            local_file(HERE, mode["program"]).read_bytes() + mode.get("programSuffix", "").encode()
        )

    actual = input_hashes([Path(mode["target"])], package)
    if mode.get("expectedInputs") is not None and actual != mode["expectedInputs"]:
        raise SystemExit("assembled source closure differs from the recorded check")
    if args.assemble_only:
        print(f"mode={args.mode}; exact assembly verified; checker not run; package={package}")
        return 0
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
    print(f"mode={args.mode}; isolated package={package}; production unchanged", flush=True)
    return subprocess.run([
        sys.executable, str(ROOT / "scripts/run_lambdapi.py"), "--no-colors", "--quiet",
        "--timeout-ms", str(args.timeout_seconds * 1000), "--package-root", str(package),
        mode["target"],
    ], cwd=REPO, env=env).returncode


if __name__ == "__main__":
    raise SystemExit(main())
