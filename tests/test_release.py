from pathlib import Path
import subprocess
import sys
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from _version import read_version  # noqa: E402

OUTPUT = ROOT / "dist" / f"omega-modus-v{read_version()}"


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

    def test_minimum_twelve_scenarios_exist(self):
        scenarios = list((ROOT / "evaluation/scenarios").glob("S*.md"))
        self.assertGreaterEqual(len(scenarios), 12)

    def test_results_template_covers_every_scenario(self):
        template = (ROOT / "evaluation/RESULTS_TEMPLATE.md").read_text(encoding="utf-8")
        for scenario in sorted((ROOT / "evaluation/scenarios").glob("S*.md")):
            code = scenario.name.split("-", 1)[0]
            with self.subTest(scenario=code):
                self.assertIn(f"| {code} |", template)

    def test_version_is_declared_in_one_place(self):
        version = read_version()
        self.assertIn(f'version = "{version}"', (ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        for script in ["scripts/build_release.py", "scripts/validate_release.py"]:
            with self.subTest(script=script):
                self.assertNotIn('VERSION = "', (ROOT / script).read_text(encoding="utf-8"))

    def test_chatgpt_instructions_are_self_contained(self):
        content = (OUTPUT / "bundles/chatgpt/instructions.md").read_text(encoding="utf-8")
        for marker in ["Never fabricate evidence", "QUICK", "DEEP", "approval", "chain-of-thought"]:
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_generic_prompt_contains_all_references(self):
        content = (OUTPUT / "bundles/generic/OMEGA-MODUS-PROMPT.md").read_text(encoding="utf-8")
        references = ROOT / "skills/omega-modus/references"
        for name in ["CORE_PROTOCOL.md", "QUALITY_INTELLIGENCE.md", "SAFETY_AND_TRUST.md", "WORKFLOWS.md"]:
            heading = (references / name).read_text(encoding="utf-8").splitlines()[0].strip()
            with self.subTest(reference=name):
                self.assertIn(heading, content)

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
