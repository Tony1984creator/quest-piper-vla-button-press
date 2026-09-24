import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "projects" / "ciat_smolvla"


class CiatPortfolioNavigationTest(unittest.TestCase):
    def test_project_page_links_the_dated_evidence_ledger(self):
        text = (PROJECT / "README.md").read_text(encoding="utf-8")
        self.assertIn("[dated evidence ledger](evidence.md)", text)

    def test_evidence_page_keeps_the_current_training_boundary_explicit(self):
        text = (PROJECT / "evidence.md").read_text(encoding="utf-8")
        self.assertIn("waiting for resources", text)
        self.assertIn("no real critic training was started", text.casefold())

    def test_evidence_page_expands_the_public_experiment_names(self):
        text = (PROJECT / "evidence.md").read_text(encoding="utf-8")
        self.assertIn("Bayesian Uncertainty-Guided Counterfactual Evidence Design", text)
        self.assertIn("Adaptive-Magnitude Counterfactual Escalation", text)


if __name__ == "__main__":
    unittest.main()
