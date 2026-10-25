import hashlib
import importlib.util
import json
from io import BytesIO
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import Mock, patch

spec = importlib.util.spec_from_file_location("verification_toolchain", Path(__file__).with_name("verification-toolchain.py"))
toolchain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(toolchain)


class SourceArchiveTests(unittest.TestCase):
    def manifest(self, data=b"reviewed archive"):
        archive = {"name": "example", "version": "1.0", "url": "https://example.invalid/cache",
                   "sha256": hashlib.sha256(data).hexdigest(), "md5": hashlib.md5(data).hexdigest()}
        return {"opamPackages": {"example": "1.0"}, "opamSourceArchives": [archive]}

    def test_verified_bytes_populate_both_opam_cache_keys_and_reuse_without_network(self):
        with TemporaryDirectory() as temporary:
            cache = Path(temporary)
            manifest = self.manifest()
            fetch = Mock(return_value=BytesIO(b"reviewed archive"))
            toolchain.seed_source_archives(manifest, cache, fetch)
            archive = manifest["opamSourceArchives"][0]
            for kind in ("sha256", "md5"):
                self.assertEqual((cache / kind / archive[kind][:2] / archive[kind]).read_bytes(), b"reviewed archive")
            fetch.assert_called_once_with(archive["url"], timeout=30)
            toolchain.seed_source_archives(manifest, cache, Mock(side_effect=AssertionError("unexpected network")))

    def test_mismatching_source_or_cache_is_rejected_without_installing_new_bytes(self):
        with TemporaryDirectory() as temporary:
            cache = Path(temporary)
            manifest = self.manifest()
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                toolchain.seed_source_archives(manifest, cache, Mock(return_value=BytesIO(b"changed upstream bytes")))
            self.assertEqual(list(cache.rglob("*")), [])
            archive = manifest["opamSourceArchives"][0]
            target = cache / "sha256" / archive["sha256"][:2] / archive["sha256"]
            target.parent.mkdir(parents=True)
            target.write_bytes(b"bad cache")
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                toolchain.seed_source_archives(manifest, cache, Mock(side_effect=AssertionError("unexpected network")))

    def test_archive_cannot_silently_override_a_package_version(self):
        with TemporaryDirectory() as temporary:
            manifest = self.manifest()
            manifest["opamPackages"]["example"] = "2.0"
            with self.assertRaisesRegex(ValueError, "does not match"):
                toolchain.seed_source_archives(manifest, Path(temporary), Mock(side_effect=AssertionError("unexpected network")))


class BatchCheckerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.root_patch = patch.object(toolchain, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.source = self.root / "build/source"
        self.source.mkdir(parents=True)
        self.original = b"let value = 1\n"
        self.changed = b"let value = 2\n"
        (self.source / "example.ml").write_bytes(self.original)
        self.git("init", "--quiet")
        self.git("add", "example.ml")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "commit", "--quiet", "-m", "fixture")
        self.commit = self.git("rev-parse", "HEAD").strip()
        self.patch_path = self.root / "batch.patch"
        self.patch_path.write_text("--- a/example.ml\n+++ b/example.ml\n@@ -1 +1 @@\n-let value = 1\n+let value = 2\n")
        sha = lambda data: hashlib.sha256(data).hexdigest()
        self.manifest = {"ocaml": "5.4.0", "opamPackages": {}, "lambdapi": {
            "commit": self.commit, "batchPatch": {"path": "batch.patch",
            "sha256": sha(self.patch_path.read_bytes()),
            "upstreamSources": {"example.ml": sha(self.original)},
            "patchedSources": {"example.ml": sha(self.changed)}}}}

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.source), *args], text=True)

    def test_exact_patch_and_source_inventory_are_verified(self):
        toolchain.apply_batch_patch(self.manifest, self.source)
        self.assertEqual((self.source / "example.ml").read_bytes(), self.changed)
        toolchain.check_batch_source(self.manifest, self.source)
        with self.assertRaisesRegex(ValueError, "source checksum mismatch"):
            toolchain.apply_batch_patch(self.manifest, self.source)

    def test_wrong_commit_and_corrupt_patch_fail_before_source_mutation(self):
        self.manifest["lambdapi"]["commit"] = "0" * 40
        with self.assertRaisesRegex(ValueError, "commit mismatch"):
            toolchain.apply_batch_patch(self.manifest, self.source)
        self.assertEqual((self.source / "example.ml").read_bytes(), self.original)
        self.manifest["lambdapi"]["commit"] = self.commit
        self.patch_path.write_text("changed bytes")
        with self.assertRaisesRegex(ValueError, "patch path/checksum mismatch"):
            toolchain.apply_batch_patch(self.manifest, self.source)
        self.assertEqual((self.source / "example.ml").read_bytes(), self.original)

    def test_changed_upstream_and_unexpected_tracked_edits_are_rejected(self):
        (self.source / "other.ml").write_text("old\n")
        self.git("add", "other.ml")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "commit", "--quiet", "-m", "other")
        self.manifest["lambdapi"]["commit"] = self.git("rev-parse", "HEAD").strip()
        (self.source / "example.ml").write_text("changed upstream\n")
        with self.assertRaisesRegex(ValueError, "source checksum mismatch"):
            toolchain.apply_batch_patch(self.manifest, self.source)
        (self.source / "example.ml").write_bytes(self.original)
        toolchain.apply_batch_patch(self.manifest, self.source)
        (self.source / "other.ml").write_text("new\n")
        with self.assertRaisesRegex(ValueError, "unexpected tracked changes"):
            toolchain.check_batch_source(self.manifest, self.source)

    def test_paths_cannot_escape_the_reviewed_source_or_repository(self):
        self.manifest["lambdapi"]["batchPatch"]["path"] = "../outside.patch"
        with self.assertRaisesRegex(ValueError, "patch path/checksum mismatch"):
            toolchain.batch_profile(self.manifest)
        self.manifest["lambdapi"]["batchPatch"]["path"] = "batch.patch"
        for key in ("upstreamSources", "patchedSources"):
            self.manifest["lambdapi"]["batchPatch"][key] = {"../escape.ml": "0" * 64}
        with self.assertRaisesRegex(ValueError, "must stay within"):
            toolchain.batch_profile(self.manifest)

    def test_source_symlink_escape_is_rejected(self):
        outside = self.root / "outside.ml"
        outside.write_bytes(self.original)
        (self.source / "example.ml").unlink()
        (self.source / "example.ml").symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "source checksum mismatch"):
            toolchain.apply_batch_patch(self.manifest, self.source)
        self.assertEqual(outside.read_bytes(), self.original)

    def test_cached_binary_and_manifest_changes_are_rejected(self):
        toolchain.apply_batch_patch(self.manifest, self.source)
        directory = self.source.parent
        binary = directory / "bin/lambdapi"
        binary.parent.mkdir()
        binary.write_text("fixture executable")
        profile, _ = toolchain.batch_profile(self.manifest)
        record = {"profileSha256": profile, "binarySha256": toolchain.digest(binary), "version": "fixture"}
        (directory / "build.json").write_text(json.dumps(record))
        real_output = subprocess.check_output
        def output(command, **kwargs):
            return "fixture\n" if command == [str(binary), "--version"] else real_output(command, **kwargs)
        with patch.object(toolchain, "check_build_dependencies", return_value="5.4.0"), \
                patch.object(toolchain.subprocess, "check_output", side_effect=output):
            self.assertEqual(toolchain.verify_batch(self.manifest, directory)["binarySha256"], toolchain.digest(binary))
            self.assertEqual(toolchain.selected_batch_profile(self.manifest, binary)["binarySha256"], toolchain.digest(binary))
            # Existing verified builds are reused without cloning/building/installing.
            with patch.object(toolchain.subprocess, "run", wraps=subprocess.run) as run:
                toolchain.build_batch(self.manifest, directory)
                self.assertTrue(all(call.args[0][0] == "git" for call in run.call_args_list))
                self.assertTrue(all("clone" not in call.args[0] for call in run.call_args_list))
            binary.write_text("changed executable")
            with self.assertRaisesRegex(ValueError, "binary checksum mismatch"):
                toolchain.verify_batch(self.manifest, directory)
            with self.assertRaisesRegex(ValueError, "binary checksum mismatch"):
                toolchain.selected_batch_profile(self.manifest, binary)
            self.manifest["ocaml"] = "changed"
            with self.assertRaisesRegex(ValueError, "different verification manifest"):
                toolchain.verify_batch(self.manifest, directory)

    def test_partial_cache_is_not_overwritten(self):
        with patch.object(toolchain, "check_build_dependencies", return_value="5.4.0"), \
                patch.object(toolchain.subprocess, "run", side_effect=AssertionError("unexpected mutation")):
            with self.assertRaises(FileNotFoundError):
                toolchain.build_batch(self.manifest, self.source.parent)
        self.assertEqual((self.source / "example.ml").read_bytes(), self.original)

    def test_prepared_source_can_retry_a_busy_guard_without_cloning(self):
        toolchain.apply_batch_patch(self.manifest, self.source)
        directory = self.source.parent
        profile, _ = toolchain.batch_profile(self.manifest)
        (directory / "prepared.json").write_text(json.dumps({"profileSha256": profile}))
        real_run = subprocess.run
        guard_calls = []
        def run(command, **kwargs):
            if command[0].endswith("lambdapi_resource_guard.sh"):
                guard_calls.append((command, kwargs))
                raise subprocess.CalledProcessError(75, command)
            self.assertEqual(command[0], "git")
            self.assertNotIn("clone", command)
            return real_run(command, **kwargs)
        with patch.object(toolchain, "check_build_dependencies", return_value="5.4.0"), \
                patch.object(toolchain.subprocess, "run", side_effect=run):
            for _ in range(2):
                with self.assertRaises(subprocess.CalledProcessError) as error:
                    toolchain.build_batch(self.manifest, directory)
                self.assertEqual(error.exception.returncode, 75)
        self.assertEqual(len(guard_calls), 2)
        self.assertEqual(len(list(directory.glob("build-*.log"))), 2)
        for command, kwargs in guard_calls:
            self.assertEqual(command[1:], ["dune", "build", "--profile", "release", "-j", "1", "src/cli/lambdapi.exe"])
            self.assertEqual(kwargs["env"]["EMDASH_LP_MEMORY_MIB"], "4096")
            self.assertEqual(kwargs["env"]["EMDASH_LP_TIMEOUT"], "300s")
        self.assertFalse((directory / "build.json").exists())
        self.assertFalse((directory / "bin").exists())

    def test_unrecorded_checker_is_not_assumed_to_be_the_batch_profile(self):
        self.assertIsNone(toolchain.selected_batch_profile(self.manifest, self.root / "other/bin/lambdapi"))
        directory = self.source.parent
        (directory / "build.json").write_text("{}")
        with self.assertRaisesRegex(ValueError, "not the recorded"):
            toolchain.selected_batch_profile(self.manifest, directory / "other/lambdapi")


if __name__ == "__main__":
    unittest.main()
