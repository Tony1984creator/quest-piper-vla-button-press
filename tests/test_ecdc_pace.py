"""Dependency-free regression tests for ECDC and PACE public references."""

import unittest

from projects.ciat_smolvla.core.ecdc import select_farthest_candidate_pair
from projects.ciat_smolvla.core.pace import persistent_candidate_eligibility


class EcdcPaceTests(unittest.TestCase):
    def test_ecdc_selects_full_action_pair_with_deterministic_tie_break(self):
        pair = select_farthest_candidate_pair(
            [404, 401, 403, 402],
            [[1.0] * 7, [0.0] * 7, [1.0] * 7, [0.0] * 7],
        )
        self.assertEqual((pair["seed_a"], pair["seed_b"]), (401, 403))

    def test_pace_requires_persistent_progress_before_eligibility(self):
        self.assertEqual(
            persistent_candidate_eligibility(0.03, True, 0.05, True)["winner"],
            "candidate_b",
        )
        self.assertFalse(
            persistent_candidate_eligibility(0.0, False, 0.0, False)["eligible"]
        )


if __name__ == "__main__":
    unittest.main()
