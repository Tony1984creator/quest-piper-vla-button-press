"""Temporal rules for turning visual candidates into reviewable segments."""

from __future__ import annotations

from collections.abc import Sequence


def confirmed_segments(
    is_active_by_frame: Sequence[bool], *, min_consecutive_frames: int = 3
) -> list[tuple[int, int]]:
    """Return inclusive ranges that persist for the requested frame count."""
    if min_consecutive_frames <= 0:
        raise ValueError("min_consecutive_frames must be positive")

    segments: list[tuple[int, int]] = []
    start: int | None = None
    for index, is_active in enumerate(is_active_by_frame):
        if is_active and start is None:
            start = index
        elif not is_active and start is not None:
            if index - start >= min_consecutive_frames:
                segments.append((start, index - 1))
            start = None
    if start is not None and len(is_active_by_frame) - start >= min_consecutive_frames:
        segments.append((start, len(is_active_by_frame) - 1))
    return segments

