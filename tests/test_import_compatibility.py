import importlib.util
import unittest

from projects.visual_preannotation.core import preannotation
from shared.runtime_benchmark import offline_latency


class ImportCompatibilityTest(unittest.TestCase):
    @unittest.skipUnless(importlib.util.find_spec("cv2"), "OpenCV is required; install requirements.txt")
    def test_canonical_visual_tool_exposes_the_event_builder(self):
        from projects.visual_preannotation.tools import run_full_preannotation

        self.assertIs(
            run_full_preannotation.build_press_confirmation_segments,
            preannotation.build_press_confirmation_segments,
        )

    def test_canonical_runtime_module_exposes_the_runner(self):
        self.assertTrue(callable(offline_latency.run_offline_benchmark))


if __name__ == "__main__":
    unittest.main()

