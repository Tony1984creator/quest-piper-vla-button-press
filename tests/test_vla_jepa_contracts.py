import unittest

from projects.vla_jepa_integration.core.contracts import summarize_parameter_mapping, validate_video_layout


class VLAJEPAContractTest(unittest.TestCase):
    def test_layout_moves_time_after_channel_without_tensor_framework(self):
        self.assertEqual(validate_video_layout((1, 8, 3, 480, 640)), (1, 3, 8, 480, 640))

    def test_mapping_summary_requires_frozen_teacher(self):
        self.assertEqual(summarize_parameter_mapping(386, 12, True)["mapped"], 386)
        with self.assertRaises(ValueError):
            summarize_parameter_mapping(386, 12, False)


if __name__ == "__main__":
    unittest.main()

