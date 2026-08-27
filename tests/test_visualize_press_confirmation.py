"""Regression test for the public, read-only visual-confirmation renderer."""

from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

try:
    import cv2
    import numpy as np
    from projects.visual_preannotation.tools.visualize_press_confirmation import (
        render_visual_confirmation,
    )
except ModuleNotFoundError:
    cv2 = None
    np = None


@unittest.skipUnless(cv2 is not None and np is not None, "opencv-python and numpy are required")
class VisualConfirmationRendererTests(unittest.TestCase):
    def test_writes_one_event_when_the_third_consecutive_frame_is_active(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_video = root / "input.mp4"
            output_video = root / "annotated.mp4"
            frames_csv = root / "frames.csv"
            events_csv = root / "events.csv"
            writer = cv2.VideoWriter(str(input_video), cv2.VideoWriter_fourcc(*"mp4v"), 10.0, (160, 120))
            for is_active in (False, True, True, True):
                frame = np.zeros((120, 160, 3), dtype=np.uint8)
                if is_active:
                    cv2.rectangle(frame, (40, 30), (100, 90), (0, 140, 255), thickness=-1)
                writer.write(frame)
            writer.release()

            result = render_visual_confirmation(
                input_video=input_video,
                output_video=output_video,
                frames_csv=frames_csv,
                events_csv=events_csv,
                required_consecutive_frames=3,
            )

            self.assertEqual(result["frames"], 4)
            self.assertEqual(result["confirmed_events"], 1)
            self.assertTrue(output_video.is_file())
            with events_csv.open(newline="", encoding="utf-8-sig") as handle:
                events = list(csv.DictReader(handle))
            self.assertEqual(events, [{"event_start_frame": "1", "event_confirmed_frame": "3", "timestamp_s": "0.3"}])


if __name__ == "__main__":
    unittest.main()


