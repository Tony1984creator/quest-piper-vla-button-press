import unittest

from opencv_preannotation.target_identity_queue import select_stratified_episode_review


def event(episode, floor, frame, confidence=1.0):
    return {
        "episode_index": episode,
        "target_floor": str(floor),
        "representative_frame": frame,
        "representative_confidence": confidence,
        "source_chunk": "file-000",
    }


class TargetIdentityQueueTests(unittest.TestCase):
    def test_keeps_one_deterministic_representative_per_episode(self):
        rows = [
            event(1, 29, 40, confidence=0.8),
            event(1, 29, 30, confidence=0.9),
            event(2, 29, 20),
        ]

        selected = select_stratified_episode_review(rows, samples_per_floor=10, seed=7)

        self.assertEqual(len(selected), 2)
        first_episode = next(row for row in selected if row["episode_index"] == 1)
        self.assertEqual(first_episode["representative_frame"], 30)

    def test_uses_a_balanced_deterministic_sample_for_each_floor(self):
        rows = [
            event(episode + floor * 100, floor, episode)
            for floor in (29, 30)
            for episode in range(20)
        ]

        first = select_stratified_episode_review(rows, samples_per_floor=5, seed=42)
        second = select_stratified_episode_review(rows, samples_per_floor=5, seed=42)

        self.assertEqual(first, second)
        self.assertEqual(len(first), 10)
        self.assertEqual(sum(row["target_floor"] == "29" for row in first), 5)
        self.assertEqual(sum(row["target_floor"] == "30" for row in first), 5)

    def test_does_not_duplicate_episode_when_task_floor_is_consistent(self):
        rows = [event(1, 29, 10), event(1, 29, 20), event(2, 30, 30)]

        selected = select_stratified_episode_review(rows, samples_per_floor=10, seed=3)

        self.assertEqual({row["episode_index"] for row in selected}, {1, 2})


if __name__ == "__main__":
    unittest.main()
