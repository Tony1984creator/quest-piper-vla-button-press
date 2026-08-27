"""Validate a candidate command before a private supervisor decides on transport."""

from __future__ import annotations

import math
from collections.abc import Sequence


def validate_command(
    command: Sequence[float], timestamp_ms: float, now_ms: float, max_age_ms: float
) -> list[float]:
    """Return a copied fresh 7D command or reject it; this function never actuates."""
    if len(command) != 7:
        raise ValueError("command must contain exactly seven values")
    if max_age_ms <= 0 or now_ms < timestamp_ms or now_ms - timestamp_ms > max_age_ms:
        raise ValueError("command timestamp is stale or invalid")
    copied = [float(value) for value in command]
    if not all(math.isfinite(value) for value in copied):
        raise ValueError("command values must be finite")
    return copied

