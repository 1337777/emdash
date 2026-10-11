#!/usr/bin/env python3
"""Emit full-file owner-position probes; this helper is not a proof checker."""

import hashlib
import json
from pathlib import Path
import re


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    owner = root / "emdash3_2.lp"
    expected = "6a980df34be718a23a6be121d170153650830a49f54b7e0eca415705ffb2068a"
    if digest(owner.read_bytes()) != expected:
        raise SystemExit("core changed: review this audit before updating its source pin")
    profile = root / "emdash3_2_gray_profiles.lp"
    profile_expected = "f670814a83a508bd8a77a4000c7ab04690bbfc25978d106bb1d761ce6723a69c"
    if digest(profile.read_bytes()) != profile_expected:
        raise SystemExit("profile changed: review this audit before updating its source pin")
    source = owner.read_text()
    markers = {
        "capped": "/*\n  The former capped composition cut and detached all-components law are\n",
        "whole": "/*\n  The former whole post/left and pre/right strict-functoriality accumulation\n",
        "intrinsic": "// The public whole laxity candidate is now an object projection, not an\n",
    }
    for name, marker in markers.items():
        if source.count(marker) != 1:
            raise SystemExit(name + " owner anchor changed")
    output = root / "tmp/probes/strict_default_action"
    output.mkdir(parents=True, exist_ok=True)
    fragments = {p.name: p.read_text() for p in audit.glob("*.lpfragment")}
    manifests = {}
    for variant in ("baseline", "capped", "whole", "intrinsic", "raw_endpoint", "projection", "joined"):
        controls = fragments["composition_controls.lpfragment"]
        body = source
        if variant == "baseline":
            controls = re.sub(r"(?m)^assert\b", "assertnot", controls)
        else:
            marker = markers["capped"]
            body = body.replace(marker, fragments["composition_rule.lpfragment"] + "\n" + marker)
        if variant in ("whole", "intrinsic", "projection", "joined"):
            marker = markers["whole"]
            insertion = fragments["whole_rules.lpfragment"]
            if variant == "joined":
                insertion += "\n" + fragments["projected_rules.lpfragment"]
            body = body.replace(marker, insertion + "\n" + marker)
        if variant in ("intrinsic", "projection", "joined"):
            marker = markers["intrinsic"]
            body = body.replace(marker, fragments["intrinsic_rule.lpfragment"] + "\n" + marker)
        if variant == "joined":
            package = output / "package_joined"
            package.mkdir(exist_ok=True)
            (package / "emdash3_2.lp").write_text(body)
            (package / profile.name).write_bytes(profile.read_bytes())
            (package / "lambdapi.pkg").write_bytes((root / "lambdapi.pkg").read_bytes())
            (package / "profile_consumer.lp").write_text(fragments["profile_consumer.lpfragment"])
            manifests["package_joined"] = {
                p.name: digest(p.read_bytes()) for p in sorted(package.iterdir())
                if p.suffix in (".lp", ".pkg")
            }
        body += "\n" + controls + "\n" + fragments["retained_controls.lpfragment"]
        whole_controls = fragments["whole_controls.lpfragment"]
        if variant not in ("whole", "intrinsic", "projection", "joined"):
            whole_controls = re.sub(r"(?m)^assert\b", "assertnot", whole_controls)
        body += "\n" + whole_controls
        if variant == "raw_endpoint":
            body += "\n" + fragments["compositor_boundary.lpfragment"]
        if variant in ("whole", "intrinsic", "projection", "joined"):
            intrinsic_controls = fragments["intrinsic_controls.lpfragment"]
            if variant in ("intrinsic", "projection", "joined"):
                intrinsic_controls = re.sub(r"(?m)^assertnot\b", "assert", intrinsic_controls)
            body += "\n" + intrinsic_controls
        if variant in ("projection", "joined"):
            body += "\n" + fragments["projection_controls.lpfragment"]
        target = output / (variant + ".lp")
        target.write_text(body)
        manifests[str(target.relative_to(root))] = {
            "sha256": digest(target.read_bytes()),
            "positiveAssertions": len(re.findall(r"(?m)^assert\b", body)),
            "negativeAssertions": len(re.findall(r"(?m)^assertnot\b", body)),
        }
        print(str(target.relative_to(root)))
    manifest = {
        "owner": str(owner.relative_to(root)), "ownerSha256": expected,
        "profileSha256": profile_expected,
        "inputs": {str(p.relative_to(root)): digest(p.read_bytes())
                   for p in sorted(audit.iterdir()) if p.suffix in (".py", ".lpfragment")},
        "outputs": manifests,
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
