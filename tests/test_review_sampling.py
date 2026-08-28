import unittest

from projects.visual_preannotation.core.review_sampling import select_stratified_review


class ReviewSamplingTests(unittest.TestCase):
    def test_selects_evenly_spaced_records_per_chunk(self):
        selected = select_stratified_review(
            [{"source_chunk": "a", "representative_frame": index} for index in range(5)],
            samples_per_chunk=3,
        )

        self.assertEqual([row["representative_frame"] for row in selected], [0, 2, 4])

    def test_samples_each_chunk_without_mutating_records(self):
        segments = [
            {"source_chunk": "b", "representative_frame": 10},
            {"source_chunk": "a", "representative_frame": 3},
            {"source_chunk": "a", "representative_frame": 1},
        ]

        selected = select_stratified_review(segments, samples_per_chunk=1)

        self.assertEqual(
            [(row["source_chunk"], row["representative_frame"]) for row in selected],
            [("a", 1), ("b", 10)],
        )
        self.assertEqual(segments[0]["representative_frame"], 10)


if __name__ == "__main__":
    unittest.main()

