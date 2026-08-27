import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "opencv_preannotation"))

from projects.visual_preannotation.core.temporal_filter import confirmed_segments


class ConfirmedSegmentsTest(unittest.TestCase):
    def test_filters_short_runs_and_keeps_inclusive_ranges(self):
        self.assertEqual(
            confirmed_segments([False, True, True, False, True, True, True, False]),
            [(4, 6)],
        )

    def test_keeps_terminal_run(self):
        self.assertEqual(confirmed_segments([False, True, True, True]), [(1, 3)])

    def test_rejects_non_positive_threshold(self):
        with self.assertRaises(ValueError):
            confirmed_segments([True], min_consecutive_frames=0)


if __name__ == "__main__":
    unittest.main()

