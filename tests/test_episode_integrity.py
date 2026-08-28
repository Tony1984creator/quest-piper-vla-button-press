import unittest

from projects.lerobot_data_contract.core.episode_integrity import (
    validate_episode_integrity,
)


class EpisodeIntegrityTests(unittest.TestCase):
    def test_rejects_a_frame_gap_and_a_timestamp_gap(self):
        report = validate_episode_integrity(
            [(0, 0, 0.0, 0), (0, 2, 0.10, 1)],
            fps=30,
            timestamp_tolerance=0.01,
        )

        self.assertFalse(report["passed"])
        self.assertIn("frame_index_gap", report["failures"])
        self.assertIn("timestamp_alignment_gap", report["failures"])

    def test_accepts_contiguous_multi_episode_records(self):
        report = validate_episode_integrity(
            [
                (0, 0, 0.0, 0),
                (0, 1, 1 / 30, 1),
                (1, 0, 0.0, 2),
                (1, 1, 1 / 30, 3),
            ],
            fps=30,
            timestamp_tolerance=0.01,
        )

        self.assertTrue(report["passed"])
        self.assertEqual(report["episodes_checked"], 2)
        self.assertEqual(report["frames_checked"], 4)


if __name__ == "__main__":
    unittest.main()

