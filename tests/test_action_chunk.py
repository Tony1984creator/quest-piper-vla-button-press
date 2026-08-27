import unittest

from projects.evo_depth_deployment.core.action_chunk import clamp_delta, select_execution_window


class ActionChunkTest(unittest.TestCase):
    def test_selects_first_25_steps_and_only_first_seven_dimensions(self):
        chunk = [[float(index) for index in range(24)] for _ in range(50)]
        selected = select_execution_window(chunk, horizon=25)
        self.assertEqual(len(selected), 25)
        self.assertEqual(len(selected[0]), 7)

    def test_delta_clamp_limits_first_action_jump(self):
        self.assertEqual(clamp_delta([12.0, -12.0], [10.0, -10.0], 1.0), [11.0, -11.0])


if __name__ == "__main__":
    unittest.main()

