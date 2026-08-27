"""Regression checks for the compact public portfolio layout."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PublicLayoutTests(unittest.TestCase):
    def test_visual_tools_have_one_canonical_home(self):
        tools = ROOT / "projects" / "visual_preannotation" / "tools"
        self.assertTrue((tools / "run_full_preannotation.py").is_file())
        self.assertTrue((tools / "visualize_press_confirmation.py").is_file())
        self.assertFalse(
            (ROOT / "opencv_preannotation" / "global_confirmed_detector.py").exists()
        )

    def test_runtime_benchmark_has_one_canonical_home(self):
        self.assertTrue(
            (ROOT / "shared" / "runtime_benchmark" / "offline_latency.py").is_file()
        )
        self.assertFalse((ROOT / "benchmarks" / "offline_latency.py").exists())

    def test_root_docs_only_keeps_shared_navigation(self):
        docs = ROOT / "docs"
        self.assertTrue((docs / "roadmap" / "README.md").is_file())
        self.assertTrue((docs / "evidence.md").is_file())
        self.assertFalse((docs / "portfolio-rebuild-spec.md").exists())


if __name__ == "__main__":
    unittest.main()

