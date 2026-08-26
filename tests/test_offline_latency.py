import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from benchmarks.offline_latency import percentile_ms, run_offline_benchmark


class OfflineLatencyTest(unittest.TestCase):
    def test_percentile_uses_linear_interpolation_for_p95(self):
        self.assertEqual(percentile_ms([1.0, 2.0, 3.0, 4.0], 95.0), 3.85)

    def test_runner_returns_non_actuating_report_with_stage_summary(self):
        report = run_offline_benchmark(
            lambda: {"model_ms": 2.0},
            warmup=0,
            repeats=3,
            action_metadata={"chunk_shape": [1, 7, 7]},
        )
        self.assertFalse(report["hardware_commands_sent"])
        self.assertEqual(report["samples"], 3)
        self.assertEqual(report["action_metadata"]["chunk_shape"], [1, 7, 7])
        self.assertEqual(report["stages"]["model_ms"]["count"], 3)


class OfflineLatencyCliTest(unittest.TestCase):
    def test_cli_writes_a_valid_non_actuating_json_report(self):
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "report.json"
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "benchmarks.offline_latency",
                    "--callable",
                    "benchmarks.example_fake_policy:infer",
                    "--repeats",
                    "2",
                    "--output",
                    str(output_path),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            report = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual(result.returncode, 0)
        self.assertFalse(report["hardware_commands_sent"])
        self.assertEqual(report["samples"], 2)


if __name__ == "__main__":
    unittest.main()

