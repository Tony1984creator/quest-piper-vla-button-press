import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()

