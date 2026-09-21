"""Dependency-free SPARC visual-progress pair utilities.

SPARC is an offline evaluation hypothesis, not an online controller.  This
public core accepts already-recorded scalar progress values only; it cannot
load SmolVLA, checkpoints, simulator data, or robot hardware.
"""

from __future__ import annotations


def select_progress_transition(progress: list[float], *, min_step: int = 20,
                               tail_guard: int = 20, grid: int = 5) -> int:
    """Select the largest local absolute progress transition on a fixed grid."""
    if grid <= 0 or len(progress) <= min_step + tail_guard + 2 * grid:
        raise ValueError("trajectory too short for SPARC selection")
    candidates = range(min_step, len(progress) - tail_guard, grid)
    return max(
        candidates,
        key=lambda step: (
            abs(progress[min(step + grid, len(progress) - 1)] - progress[max(step - grid, 0)]),
            -step,
        ),
    )


def signed_progress_preference(negative_delta: float, positive_delta: float) -> int:
    """Return -1, 0, or +1 for a measured short-horizon progress contrast."""
    margin = positive_delta - negative_delta
    return 1 if margin > 0.0 else -1 if margin < 0.0 else 0
