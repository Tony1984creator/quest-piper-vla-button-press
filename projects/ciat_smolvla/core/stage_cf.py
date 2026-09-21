"""Dependency-free Task-5 geometry utilities for offline STAGE-CF analysis.

The functions consume already-recorded end-effector, book, and goal positions.
They do not access a simulator, terminal success label, policy, weights, or
robot hardware.
"""

from __future__ import annotations

import math


def _distance(left: list[float], right: list[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right, strict=True)))


def score_book_transition(anchor: dict[str, list[float]],
                          horizon: dict[str, list[float]]) -> dict[str, object]:
    """Return an abstaining geometric Task-5 stage score.

    Required keys are "eef", "book", and "back_goal". The score is positive
    only for an observed improvement, never from a terminal outcome.
    """
    try:
        goal_gain = _distance(anchor["book"], anchor["back_goal"]) - _distance(
            horizon["book"], horizon["back_goal"]
        )
        eef_gain = _distance(anchor["eef"], anchor["book"]) - _distance(
            horizon["eef"], horizon["book"]
        )
    except KeyError:
        return {"stage": "abstain", "score": 0.0}
    if goal_gain > 1e-4:
        stage = "placement" if _distance(horizon["book"], horizon["back_goal"]) <= 0.08 else "transport"
        return {"stage": stage, "score": goal_gain}
    if eef_gain > 1e-4:
        return {"stage": "approach", "score": eef_gain}
    return {"stage": "abstain", "score": 0.0}


def signed_stage_preference(negative_score: float, positive_score: float) -> int:
    """Return -1, 0, or +1 for a measured signed stage-progress contrast."""
    margin = positive_score - negative_score
    return 1 if margin > 0.0 else -1 if margin < 0.0 else 0
