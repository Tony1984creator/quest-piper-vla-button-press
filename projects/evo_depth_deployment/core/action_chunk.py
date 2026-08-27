"""Validate and select candidate actions without communicating with any device."""

from __future__ import annotations

import math
from collections.abc import Sequence


def select_execution_window(
    chunk: Sequence[Sequence[float]], horizon: int, active_dimensions: int = 7
) -> list[list[float]]:
    """Copy the first horizon steps and public active dimensions from an action chunk."""
    if horizon <= 0 or active_dimensions <= 0 or len(chunk) < horizon:
        raise ValueError("chunk must contain the requested positive horizon")
    selected: list[list[float]] = []
    for row in chunk[:horizon]:
        if len(row) < active_dimensions:
            raise ValueError("action row has fewer than active dimensions")
        copied = [float(value) for value in row[:active_dimensions]]
        if not all(math.isfinite(value) for value in copied):
            raise ValueError("action values must be finite")
        selected.append(copied)
    return selected


def clamp_delta(candidate: Sequence[float], measured: Sequence[float], max_delta: float) -> list[float]:
    """Bound a candidate action relative to measured state; no transport is involved."""
    if max_delta <= 0 or len(candidate) == 0 or len(candidate) != len(measured):
        raise ValueError("vectors must be non-empty, equal length, and use positive max_delta")
    bounded: list[float] = []
    for target, current in zip(candidate, measured):
        target_value, current_value = float(target), float(current)
        if not math.isfinite(target_value) or not math.isfinite(current_value):
            raise ValueError("vectors must contain finite values")
        bounded.append(max(current_value - max_delta, min(current_value + max_delta, target_value)))
    return bounded

