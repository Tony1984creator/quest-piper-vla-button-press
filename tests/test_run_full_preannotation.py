"""End-to-end checks for the batch visual-preannotation entry point."""

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import cv2
    import numpy as np
except ModuleNotFoundError:
    cv2 = None
    np = None


@unittest.skipUnless(cv2 is not None and np is not None, "opencv-python and numpy are required")
class RunFullPreannotationTests(unittest.TestCase):
    def test_writes_one_visual_segment_and_one_summary_row(self) -> None:
        root = Path(__file__).resolve().parents[1]
        runner = root / "opencv_preannotation" / "run_full_preannotation.py"
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            input_directory = temporary_path / "input"
            output_directory = temporary_path / "output"
            input_directory.mkdir()
            video_path = input_directory / "wrist_chunk_001.mp4"
            writer = cv2.VideoWriter(
                str(video_path), cv2.VideoWriter_fourcc(*"mp4v"), 10.0, (160, 120)
            )
            for active in [False, True, True, True, False]:
                frame = np.zeros((120, 160, 3), dtype=np.uint8)
                if active:
                    cv2.rectangle(frame, (40, 30), (80, 70), (0, 140, 255), thickness=-1)
                writer.write(frame)
            writer.release()

            subprocess.run(
                [
                    sys.executable,
                    str(runner),
                    "--input-directory",
                    str(input_directory),
                    "--output-directory",
                    str(output_directory),
                    "--min-orange-pixels",
                    "1000",
                ],
                check=True,
                cwd=root / "opencv_preannotation",
            )

            events = [
                json.loads(line)
                for line in (output_directory / "press_confirmed_visual_segments.jsonl").read_text(
                    encoding="utf-8"
                ).splitlines()
            ]
            with (output_directory / "preannotation_summary.csv").open(
                encoding="utf-8-sig", newline=""
            ) as handle:
                summary = list(csv.DictReader(handle))

            self.assertEqual(len(events), 1)
            self.assertEqual(events[0]["task_stage"], "press_confirmed_visual")
            self.assertEqual((events[0]["start_frame"], events[0]["end_frame"]), (1, 3))
            self.assertEqual(summary, [{"source_chunk": "wrist_chunk_001", "frames": "5", "confirmation_segments": "1"}])


if __name__ == "__main__":
    unittest.main()
