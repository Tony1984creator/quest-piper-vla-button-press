"""Dependency-free checks for episode/frame metadata before model loading."""

from collections import defaultdict
from typing import Iterable


EpisodeRecord = tuple[int, int, float, int]


def validate_episode_integrity(
    records: Iterable[EpisodeRecord], *, fps: float, timestamp_tolerance: float
) -> dict[str, object]:
    """Check contiguous global and per-episode indexing plus frame timing.

    Records are ``(episode_index, frame_index, timestamp_s, global_index)``.
    The function deliberately works on metadata only; it neither opens video nor
    communicates with robot hardware.
    """

    materialized = list(records)
    failures: list[str] = []
    if fps <= 0:
        raise ValueError("fps must be positive")
    if timestamp_tolerance < 0:
        raise ValueError("timestamp_tolerance must be non-negative")

    ordered_by_global = sorted(materialized, key=lambda row: row[3])
    for expected_global, row in enumerate(ordered_by_global):
        if row[3] != expected_global:
            failures.append("global_index_gap")
            break

    episodes: dict[int, list[EpisodeRecord]] = defaultdict(list)
    for row in materialized:
        episodes[row[0]].append(row)

    expected_delta = 1.0 / fps
    for episode_records in episodes.values():
        ordered = sorted(episode_records, key=lambda row: row[1])
        if ordered and ordered[0][1] != 0:
            failures.append("episode_does_not_start_at_zero")
        for previous, current in zip(ordered, ordered[1:]):
            if current[1] != previous[1] + 1 and "frame_index_gap" not in failures:
                failures.append("frame_index_gap")
            if (
                abs((current[2] - previous[2]) - expected_delta) > timestamp_tolerance
                and "timestamp_alignment_gap" not in failures
            ):
                failures.append("timestamp_alignment_gap")

    return {
        "passed": not failures,
        "failures": failures,
        "episodes_checked": len(episodes),
        "frames_checked": len(materialized),
    }

