import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "opencv_preannotation"))

from preannotation import build_press_confirmation_segments


class PreannotationTest(unittest.TestCase):
    def test_builds_one_review_record_for_stable_frames(self):
        records = [
            {"frame_index": 10, "is_active": True, "confidence": 0.8, "bbox": (1, 2, 3, 4)},
            {"frame_index": 11, "is_active": True, "confidence": 0.9, "bbox": (2, 2, 3, 4)},
            {"frame_index": 12, "is_active": True, "confidence": 1.0, "bbox": (3, 2, 3, 4)},
        ]
        result = build_press_confirmation_segments(records)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["task_stage"], "press_confirmed_visual")
        self.assertEqual(result[0]["start_frame"], 10)
        self.assertEqual(result[0]["end_frame"], 12)
        self.assertEqual(result[0]["representative_frame"], 11)


if __name__ == "__main__":
    unittest.main()
