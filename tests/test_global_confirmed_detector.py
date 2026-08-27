import unittest

try:
    import cv2  # noqa: F401
    import numpy as np

    from projects.visual_preannotation.core.global_confirmed_detector import detect_illuminated_button
except ModuleNotFoundError:
    CV2_AVAILABLE = False
else:
    CV2_AVAILABLE = True


@unittest.skipUnless(CV2_AVAILABLE, "OpenCV is required; install requirements.txt")
class GlobalConfirmedDetectorTest(unittest.TestCase):
    def test_detects_large_orange_component_away_from_edge(self):
        frame = np.zeros((120, 160, 3), dtype=np.uint8)
        frame[20:70, 40:100] = (0, 165, 255)  # BGR orange
        result = detect_illuminated_button(frame, min_orange_pixels=1_000)
        self.assertTrue(result.is_active)
        self.assertEqual(result.orange_pixels, 3_000)
        self.assertEqual(result.bbox, (40, 20, 60, 50))

    def test_rejects_edge_component(self):
        frame = np.zeros((120, 160, 3), dtype=np.uint8)
        frame[0:60, 0:60] = (0, 165, 255)
        result = detect_illuminated_button(frame, min_orange_pixels=1_000)
        self.assertFalse(result.is_active)

    def test_rejects_invalid_input(self):
        with self.assertRaises(ValueError):
            detect_illuminated_button(np.zeros((32, 32), dtype=np.uint8))


if __name__ == "__main__":
    unittest.main()

