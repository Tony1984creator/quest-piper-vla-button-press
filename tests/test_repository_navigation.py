import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryNavigationTest(unittest.TestCase):
    def test_root_readme_links_all_five_project_cards_and_roadmap(self):
        readme = Path("README.md").read_text(encoding="utf-8")
        for folder in [
            "quest_piper_safety",
            "lerobot_data_contract",
            "vla_jepa_integration",
            "evo_depth_deployment",
            "visual_preannotation",
        ]:
            self.assertIn(f"projects/{folder}/README.md", readme)
        self.assertIn("docs/roadmap/README.md", readme)

    def test_root_readme_has_explicit_evidence_levels_without_duplicate_cards(self):
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("## Research focus", readme)
        self.assertIn("Offline probe", readme)
        self.assertIn("Closed-loop success", readme)
        self.assertEqual(readme.count("projects/vla_jepa_integration/README.md"), 1)

    def test_visual_project_links_the_sanitized_workflow_asset(self):
        text = (ROOT / "projects/visual_preannotation/README.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("../../docs/assets/opencv-review-workflow.svg", text)
        self.assertTrue((ROOT / "docs/assets/opencv-review-workflow.svg").is_file())

    def test_root_keeps_the_two_dataset_assets_separate(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Quest VR dataset", readme)
        self.assertIn("Elevator VLA dataset", readme)
        self.assertIn("3.37M", readme)


if __name__ == "__main__":
    unittest.main()

