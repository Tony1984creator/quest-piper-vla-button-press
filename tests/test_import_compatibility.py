import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "opencv_preannotation"))

from benchmarks import offline_latency as legacy_latency
from opencv_preannotation import preannotation as legacy_preannotation
from projects.visual_preannotation.core import preannotation as canonical_preannotation
from shared.runtime_benchmark import offline_latency as canonical_latency


class ImportCompatibilityTest(unittest.TestCase):
    def test_legacy_and_canonical_preannotation_imports_reference_same_function(self):
        self.assertIs(
            legacy_preannotation.build_press_confirmation_segments,
            canonical_preannotation.build_press_confirmation_segments,
        )

    def test_legacy_and_canonical_latency_imports_reference_same_runner(self):
        self.assertIs(legacy_latency.run_offline_benchmark, canonical_latency.run_offline_benchmark)


if __name__ == "__main__":
    unittest.main()

