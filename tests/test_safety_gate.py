import unittest

from projects.quest_piper_safety.core.safety_gate import validate_command


class SafetyGateTest(unittest.TestCase):
    def test_returns_a_copy_for_a_fresh_seven_joint_command(self):
        source = [0.0] * 7
        command = validate_command(source, timestamp_ms=10, now_ms=11, max_age_ms=100)
        self.assertEqual(command, [0.0] * 7)
        self.assertIsNot(command, source)

    def test_rejects_stale_or_nonfinite_joint_command(self):
        with self.assertRaises(ValueError):
            validate_command([0.0] * 7, timestamp_ms=0, now_ms=101, max_age_ms=100)
        with self.assertRaises(ValueError):
            validate_command([0.0] * 6 + [float("nan")], timestamp_ms=10, now_ms=11, max_age_ms=100)


if __name__ == "__main__":
    unittest.main()

