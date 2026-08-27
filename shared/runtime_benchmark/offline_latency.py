"""Measure an already-safe offline inference callable without robot access."""

from __future__ import annotations

import argparse
from collections.abc import Callable, Mapping
import importlib
import json
from pathlib import Path
from time import perf_counter_ns
from typing import Any


def percentile_ms(samples: list[float], percentile: float) -> float:
    """Return a linearly interpolated percentile from non-empty millisecond samples."""
    if not samples:
        raise ValueError("samples must not be empty")
    if not 0.0 <= percentile <= 100.0:
        raise ValueError("percentile must be between 0 and 100")
    ordered = sorted(float(value) for value in samples)
    position = (len(ordered) - 1) * percentile / 100.0
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (position - lower)


def _summary(samples: list[float]) -> dict[str, float | int]:
    return {
        "count": len(samples),
        "mean_ms": sum(samples) / len(samples),
        "p50_ms": percentile_ms(samples, 50.0),
        "p95_ms": percentile_ms(samples, 95.0),
    }


def _normalize_stages(result: Mapping[str, Any] | None) -> dict[str, float]:
    if result is None:
        return {}
    if not isinstance(result, Mapping):
        raise ValueError("benchmark callable must return a mapping or None")
    stages: dict[str, float] = {}
    for name, value in result.items():
        if not isinstance(name, str) or not name.endswith("_ms"):
            raise ValueError("stage keys must be strings ending in '_ms'")
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
            raise ValueError("stage values must be non-negative numbers")
        stages[name] = float(value)
    return stages


def run_offline_benchmark(
    inference: Callable[[], Mapping[str, Any] | None],
    warmup: int,
    repeats: int,
    action_metadata: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Run a reviewed callable and return JSON-safe timing evidence with no actuation path."""
    if warmup < 0 or repeats <= 0:
        raise ValueError("warmup must be non-negative and repeats must be positive")
    if not callable(inference):
        raise TypeError("inference must be callable")
    for _ in range(warmup):
        _normalize_stages(inference())

    totals: list[float] = []
    stage_samples: dict[str, list[float]] = {}
    for _ in range(repeats):
        started_ns = perf_counter_ns()
        stages = _normalize_stages(inference())
        totals.append((perf_counter_ns() - started_ns) / 1_000_000.0)
        for name, value in stages.items():
            stage_samples.setdefault(name, []).append(value)

    return {
        "schema_version": 1,
        "measurement_mode": "offline_callable",
        "hardware_commands_sent": False,
        "warmup_samples": warmup,
        "samples": repeats,
        "action_metadata": dict(action_metadata or {}),
        "end_to_end": _summary(totals),
        "stages": {name: _summary(values) for name, values in sorted(stage_samples.items())},
    }


def _load_callable(specification: str) -> Callable[[], Mapping[str, Any] | None]:
    if specification.count(":") != 1:
        raise ValueError("--callable must use module:callable syntax")
    module_name, callable_name = specification.split(":", maxsplit=1)
    if not module_name or not callable_name:
        raise ValueError("--callable must use module:callable syntax")
    candidate = getattr(importlib.import_module(module_name), callable_name)
    if not callable(candidate):
        raise ValueError("--callable target must be callable")
    return candidate


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--callable", required=True, help="offline callable in module:callable form")
    parser.add_argument("--warmup", type=int, default=0)
    parser.add_argument("--repeats", type=int, default=30)
    parser.add_argument("--action-metadata", default="{}", help="JSON object describing output only")
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args(argv)

    try:
        metadata = json.loads(arguments.action_metadata)
        if not isinstance(metadata, Mapping):
            raise ValueError("--action-metadata must be a JSON object")
        report = run_offline_benchmark(
            _load_callable(arguments.callable),
            warmup=arguments.warmup,
            repeats=arguments.repeats,
            action_metadata=metadata,
        )
    except (ImportError, AttributeError, TypeError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))

    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

