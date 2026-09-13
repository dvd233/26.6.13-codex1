"""Regression checks for the sandbox's reproducible-experiment documentation."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
TEMPLATE = ROOT / "docs" / "experiment-template.md"


class ExperimentDocumentationContractTests(unittest.TestCase):
    def test_template_keeps_reproducibility_sections(self) -> None:
        template = TEMPLATE.read_text(encoding="utf-8")
        required_sections = (
            "Goal",
            "Scope and constraints",
            "Reproduction",
            "Expected result",
            "Observed result",
            "Verification",
            "Cleanup",
            "Attribution",
        )

        missing = [
            section
            for section in required_sections
            if f"## {section}" not in template
        ]
        self.assertFalse(missing, f"template is missing sections: {missing}")

    def test_readme_template_link_resolves(self) -> None:
        readme = README.read_text(encoding="utf-8")
        match = re.search(r"\[experiment note template\]\(([^)]+)\)", readme)

        self.assertIsNotNone(match, "README should link to the experiment template")
        linked_path = ROOT / match.group(1)
        self.assertTrue(linked_path.is_file(), f"README link is missing: {linked_path}")


if __name__ == "__main__":
    unittest.main()
