from pathlib import Path
import subprocess
import sys
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist" / "omega-modus-v1.0.0"


class ReleaseIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_release.py")],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_static_validation_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_release.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_all_adapters_exist(self):
        expected = ["codex", "claude-code", "gemini-cli", "cursor", "github-copilot", "chatgpt", "generic"]
        for name in expected:
            with self.subTest(adapter=name):
                self.assertTrue((OUTPUT / "bundles" / name).is_dir())

    def test_copilot_includes_agent_skill_and_repository_instructions(self):
        bundle = OUTPUT / "bundles" / "github-copilot"
        self.assertTrue((bundle / ".github/copilot-instructions.md").is_file())
        self.assertTrue((bundle / ".github/skills/omega-modus/SKILL.md").is_file())

    def test_skill_contains_truthfulness_and_proportionality(self):
        content = (ROOT / "skills/omega-modus/SKILL.md").read_text(encoding="utf-8").lower()
        self.assertIn("proportionate rigor", content)
        self.assertIn("never invent evidence", content)
        self.assertIn("private chain-of-thought", content)

    def test_quality_methods_are_covered(self):
        content = (ROOT / "skills/omega-modus/references/QUALITY_INTELLIGENCE.md").read_text(encoding="utf-8").lower()
        for method in ["pdca", "five whys", "ishikawa", "poka-yoke", "fmea", "pareto", "a3", "kaizen"]:
            with self.subTest(method=method):
                self.assertIn(method, content)

    def test_twelve_scenarios_exist(self):
        scenarios = list((ROOT / "evaluation/scenarios").glob("S*.md"))
        self.assertEqual(len(scenarios), 12)

    def test_all_release_archives_are_valid(self):
        archives = list((OUTPUT / "archives").glob("*.zip"))
        self.assertEqual(len(archives), 9)
        for archive in archives:
            with self.subTest(archive=archive.name):
                with zipfile.ZipFile(archive) as zf:
                    self.assertIsNone(zf.testzip())

    def test_builder_preserves_unrelated_dist_content(self):
        unrelated = ROOT / "dist" / "keep-this-file.txt"
        unrelated.write_text("preserve", encoding="utf-8")
        try:
            subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "build_release.py")],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual(unrelated.read_text(encoding="utf-8"), "preserve")
        finally:
            unrelated.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
