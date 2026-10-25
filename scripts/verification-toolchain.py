#!/usr/bin/env python3
"""Capture, verify, or install the pinned formal verification environment."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "toolchains/verification.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def batch_profile(manifest):
    """Identify the reviewed source patch separately from the installed opam pin."""
    pin = manifest["lambdapi"]
    patch = pin["batchPatch"]
    if not re.fullmatch(r"[0-9a-f]{40}", pin["commit"]):
        raise ValueError("invalid Lambdapi source commit")
    patch_path = (ROOT / patch["path"]).resolve()
    if not patch_path.is_relative_to(ROOT.resolve()) or digest(patch_path) != patch["sha256"]:
        raise ValueError("batch patch path/checksum mismatch")
    before, after = patch["upstreamSources"], patch["patchedSources"]
    if not before or set(before) != set(after):
        raise ValueError("batch patch source inventory mismatch")
    for name in before:
        path = Path(name)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("batch source path must stay within its checkout")
        if any(not re.fullmatch(r"[0-9a-f]{64}", values[name]) for values in (before, after)):
            raise ValueError("invalid batch source checksum")
    profile = hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()
    return profile, patch_path


def batch_directory(manifest, directory=None):
    profile, _ = batch_profile(manifest)
    return (directory or ROOT / "emdash2/.cache/verification-toolchain" / profile).resolve()


def check_source_hashes(source, expected):
    for name, wanted in expected.items():
        path = (source / name).resolve()
        if not path.is_relative_to(source.resolve()) or digest(path) != wanted:
            raise ValueError(f"batch source checksum mismatch: {name}")


def check_batch_commit(manifest, source):
    pin = manifest["lambdapi"]
    commit = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True, timeout=10).strip()
    if commit != pin["commit"]:
        raise ValueError("batch checker source commit mismatch")


def check_batch_source(manifest, source):
    check_batch_commit(manifest, source)
    pin = manifest["lambdapi"]
    check_source_hashes(source, pin["batchPatch"]["patchedSources"])
    changed = subprocess.check_output(["git", "-C", str(source), "diff", "--name-only", "HEAD"], text=True, timeout=10).splitlines()
    if set(changed) != set(pin["batchPatch"]["patchedSources"]):
        raise ValueError("unexpected tracked changes in batch checker source")


def apply_batch_patch(manifest, source):
    _, patch = batch_profile(manifest)
    check_batch_commit(manifest, source)
    check_source_hashes(source, manifest["lambdapi"]["batchPatch"]["upstreamSources"])
    subprocess.run(["git", "-C", str(source), "apply", "--check", "--unidiff-zero", str(patch)], check=True, timeout=10)
    subprocess.run(["git", "-C", str(source), "apply", "--unidiff-zero", str(patch)], check=True, timeout=10)
    check_batch_source(manifest, source)


def check_build_dependencies(manifest):
    compiler = subprocess.check_output(["ocamlc", "-version"], text=True, timeout=5).strip()
    if compiler != manifest["ocaml"] or installed_packages() != manifest["opamPackages"]:
        raise ValueError("activate the pinned verification dependencies before building the batch checker")
    return compiler


def verify_batch(manifest, directory):
    profile, _ = batch_profile(manifest)
    record = json.loads((directory / "build.json").read_text())
    if record["profileSha256"] != profile:
        raise ValueError("batch build belongs to a different verification manifest")
    check_batch_source(manifest, directory / "source")
    binary = directory / "bin/lambdapi"
    if digest(binary) != record["binarySha256"]:
        raise ValueError("batch checker binary checksum mismatch")
    version = subprocess.check_output([str(binary), "--version"], text=True, timeout=5).strip()
    if version != record["version"]:
        raise ValueError("batch checker version mismatch")
    check_build_dependencies(manifest)
    return {"profileSha256": profile, "binary": str(binary),
            "binarySha256": record["binarySha256"], "version": version}


def build_batch(manifest, directory, source_repository=None):
    """Build into an isolated cache without changing any opam switch or pin."""
    profile, _ = batch_profile(manifest)
    compiler = check_build_dependencies(manifest)
    source = directory / "source"
    if directory.exists():
        if (directory / "build.json").exists():
            return verify_batch(manifest, directory)
        # A busy guard or interrupted build can resume only this exact prepared
        # source. Never overwrite a foreign/incomplete directory or a built binary.
        prepared = json.loads((directory / "prepared.json").read_text())
        if prepared != {"profileSha256": profile} or (directory / "bin").exists():
            raise ValueError("batch preparation does not match the requested profile")
        check_batch_source(manifest, source)
    else:
        directory.mkdir(parents=True)
        repository = str(source_repository or manifest["lambdapi"]["repository"])
        subprocess.run(["git", "clone", "--no-checkout", "--no-hardlinks", "--", repository, str(source)], check=True, timeout=120)
        subprocess.run(["git", "-C", str(source), "checkout", "--detach", manifest["lambdapi"]["commit"]], check=True, timeout=30)
        apply_batch_patch(manifest, source)
        (directory / "prepared.json").write_text(json.dumps({"profileSha256": profile}) + "\n")
    command = ["dune", "build", "--profile", "release", "-j", "1", "src/cli/lambdapi.exe"]
    guard = ROOT / "emdash2/scripts/lambdapi_resource_guard.sh"
    env = {**os.environ, "EMDASH_LP_TIMEOUT": "300s", "EMDASH_LP_MEMORY_MIB": "4096",
           "EMDASH_LP_FILE_MIB": "64"}
    log_path = directory / ("build-" + uuid.uuid4().hex + ".log")
    with log_path.open("x") as log:
        subprocess.run([str(guard), *command], cwd=source, env=env,
                       stdout=log, stderr=subprocess.STDOUT, check=True)
    check_batch_source(manifest, source)
    binary = directory / "bin/lambdapi"
    binary.parent.mkdir()
    shutil.copy2(source / "_build/default/src/cli/lambdapi.exe", binary)
    version = subprocess.check_output([str(binary), "--version"], text=True, timeout=5).strip()
    record = {"profileSha256": profile, "sourceCommit": manifest["lambdapi"]["commit"],
              "patchSha256": manifest["lambdapi"]["batchPatch"]["sha256"],
              "binarySha256": digest(binary), "version": version, "ocaml": compiler,
              "buildCommand": command, "guardSha256": digest(guard),
              "timeoutSeconds": 300, "memoryMiB": 4096,
              "log": log_path.name, "logSha256": digest(log_path)}
    (directory / "build.json").write_text(json.dumps(record, indent=2) + "\n")
    return verify_batch(manifest, directory)


def seed_source_archives(manifest, cache, fetch=urllib.request.urlopen):
    """Cache reviewed upstream bytes without changing any package/source pin."""
    for archive in manifest.get("opamSourceArchives", []):
        name = archive["name"]
        if manifest["opamPackages"].get(name) != archive["version"]:
            raise ValueError(f"Archive does not match the pinned package: {name}")
        digests = {kind: archive[kind] for kind in ("sha256", "md5")}
        for kind, length in (("sha256", 64), ("md5", 32)):
            value = digests[kind]
            if len(value) != length or any(c not in "0123456789abcdef" for c in value):
                raise ValueError(f"Invalid archive digest: {name}/{kind}")
        targets = [cache / kind / digest[:2] / digest for kind, digest in digests.items()]
        data = next((target.read_bytes() for target in targets if target.is_file()), None)
        if data is None:
            with fetch(archive["url"], timeout=30) as response:
                data = response.read(8 * 1024 * 1024 + 1)
        if len(data) > 8 * 1024 * 1024 or any(
                hashlib.new(kind, data).hexdigest() != digest for kind, digest in digests.items()):
            raise ValueError(f"Pinned archive checksum mismatch: {name}")
        for target in targets:
            if target.is_file() and target.read_bytes() == data:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(data)
            try:
                temporary.replace(target)
            finally:
                temporary.unlink(missing_ok=True)
        print(f"Verified source archive: {name}.{archive['version']} ({len(data)} bytes)")


def installed_packages():
    output = subprocess.check_output(
        ["opam", "list", "--installed", "--required-by=lambdapi", "--recursive", "--columns=name,version", "--short", "--color=never"],
        text=True, timeout=30,
    )
    return dict(line.split() for line in output.splitlines() if line.strip())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("verify", "install", "capture", "ci-outputs",
                                          "build-batch", "verify-batch", "batch-path"))
    parser.add_argument("--source", type=Path, help="local Git mirror for build-batch; only the pinned commit is copied")
    parser.add_argument("--directory", type=Path, help="explicit isolated batch build directory")
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text())
    if args.source is not None and args.action != "build-batch":
        parser.error("--source applies only to build-batch")
    if args.action in ("build-batch", "verify-batch", "batch-path"):
        directory = batch_directory(manifest, args.directory)
        result = (build_batch(manifest, directory, args.source) if args.action == "build-batch"
                  else verify_batch(manifest, directory))
        print(str(directory / "bin") if args.action == "batch-path" else json.dumps(result, indent=2))
        return 0
    if args.source is not None or args.directory is not None:
        parser.error("--source and --directory apply only to batch checker actions")
    if args.action == "ci-outputs":
        with open(os.environ["GITHUB_OUTPUT"], "a") as stream:
            stream.write("ocaml=" + manifest["ocaml"] + "\n")
            stream.write("repository=" + manifest["opamRepository"] + "\n")
        return 0
    if args.action == "capture":
        # The source commit is deliberately reviewed separately from dependency capture.
        manifest["opamPackages"] = installed_packages()
        MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
        print("Captured installed package versions; review the exact manifest diff.")
        return 0
    if args.action == "install":
        if os.environ.get("CI") != "true" and os.environ.get("EMDASH_INSTALL_VERIFICATION_TOOLCHAIN") != "1":
            parser.error("use a dedicated opam switch and set EMDASH_INSTALL_VERIFICATION_TOOLCHAIN=1 to install locally")
        pin = manifest["lambdapi"]
        compiler = subprocess.check_output(["ocamlc", "-version"], text=True, timeout=5).strip()
        if compiler != manifest["ocaml"]:
            parser.error("create the pinned OCaml switch before installing dependencies")
        subprocess.run(["opam", "repository", "set-url", "default", manifest["opamRepository"], "--yes"], check=True)
        subprocess.run(["opam", "pin", "add", "--yes", "--no-action", "lambdapi",
                        "git+" + pin["repository"] + "#" + pin["commit"]], check=True)
        opam_root = Path(subprocess.check_output(["opam", "var", "root"], text=True, timeout=10).strip())
        seed_source_archives(manifest, opam_root / "download-cache")
        packages = [name + "." + version for name, version in manifest["opamPackages"].items()]
        subprocess.run(["opam", "install", "--yes", "--jobs=2", *packages], check=True)
    actual = installed_packages()
    mismatches = {name: {"expected": version, "actual": actual.get(name)}
                  for name, version in manifest["opamPackages"].items() if actual.get(name) != version}
    for name in sorted(set(actual) - set(manifest["opamPackages"])):
        mismatches[name] = {"expected": None, "actual": actual[name]}
    version = subprocess.check_output(["lambdapi", "--version"], text=True, timeout=5).strip()
    compiler = subprocess.check_output(["ocamlc", "-version"], text=True, timeout=5).strip()
    pin_list = subprocess.check_output(["opam", "pin", "list"], text=True, timeout=10)
    pin_matches = manifest["lambdapi"]["commit"] in pin_list
    result = {"packageMismatches": mismatches, "lambdapi": version, "ocaml": compiler,
              "sourcePinMatches": pin_matches}
    print(json.dumps(result, indent=2))
    return int(bool(mismatches) or version != manifest["lambdapi"]["version"]
               or compiler != manifest["ocaml"] or not pin_matches)


if __name__ == "__main__":
    raise SystemExit(main())
