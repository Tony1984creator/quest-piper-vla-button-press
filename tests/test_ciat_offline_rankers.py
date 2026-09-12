"""Public dependency-free tests for the CIAT offline ranker examples."""

import unittest

from afcr import axis_pair_targets, heldout_axis_sign
from buced import rank_axes_for_collection


class OfflineRankerTests(unittest.TestCase):
    def test_afcr_only_pairs_complete_signed_probes(self):
        pairs = axis_pair_targets([
            {"state_id": "s0", "delta": [-0.05, 0, 0, 0, 0, 0, 0], "outcome": 0},
            {"state_id": "s0", "delta": [0.05, 0, 0, 0, 0, 0, 0], "outcome": 1},
        ])
        self.assertEqual(pairs[0]["direction_target"], 1.0)

    def test_heldout_axis_sign_does_not_read_heldout_targets(self):
        pairs = [
            {"state_id": "train", "axis": 0, "direction_target": 1.0},
            {"state_id": "held", "axis": 0, "direction_target": -1.0},
        ]
        self.assertEqual(heldout_axis_sign(pairs, "held")[0]["prediction"], 1)

    def test_buced_prefers_likely_informative_axis(self):
        pairs = [
            {"axis": 0, "direction_target": 1.0}, {"axis": 0, "direction_target": -1.0},
            {"axis": 1, "direction_target": 0.0}, {"axis": 1, "direction_target": 0.0},
        ]
        self.assertEqual(rank_axes_for_collection(pairs, [0, 1])[0]["axis"], 0)


if __name__ == "__main__":
    unittest.main()

