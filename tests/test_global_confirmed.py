"""Behavior tests for position-independent illuminated-button detection."""

import unittest

try:
    import cv2
    import numpy as np
    from opencv_preannotation.global_confirmed_detector import detect_illuminated_button
except ModuleNotFoundError:
    cv2 = None
    np = None
    detect_illuminated_button = None


@unittest.skipUnless(cv2 is not None and np is not None, "opencv-python and numpy are required")
class DetectIlluminatedButtonTests(unittest.TestCase):
    def test_detects_large_orange_button_anywhere_in_frame(self) -> None:
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.rectangle(frame, (390, 250), (510, 370), (0, 140, 255), thickness=-1)

        result = detect_illuminated_button(frame, min_orange_pixels=1_000)

        self.assertTrue(result.is_active)
        self.assertGreaterEqual(result.orange_pixels, 10_000)
        self.assertEqual(result.bbox, (390, 250, 121, 121))

    def test_rejects_small_orange_noise(self) -> None:
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.rectangle(frame, (20, 20), (35, 35), (0, 140, 255), thickness=-1)

        result = detect_illuminated_button(frame, min_orange_pixels=1_000)

        self.assertFalse(result.is_active)
        self.assertEqual(result.orange_pixels, 0)
        self.assertIsNone(result.bbox)

    def test_rejects_large_orange_object_touching_image_edge(self) -> None:
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.rectangle(frame, (0, 200), (200, 479), (0, 140, 255), thickness=-1)
        cv2.rectangle(frame, (400, 260), (510, 370), (0, 140, 255), thickness=-1)

        result = detect_illuminated_button(frame, min_orange_pixels=1_000)

        self.assertTrue(result.is_active)
        self.assertEqual(result.bbox, (400, 260, 111, 111))


if __name__ == "__main__":
    unittest.main()
