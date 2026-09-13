"""Dependency-free Causal Stage-Transition (CST) anchor selector.

This reference function uses only already-recorded 7D actions.  It is an
offline keyframe selector, not a controller and not evidence of policy gain.
"""

from __future__ import annotations

import math


def select_stage_transition(actions: list[list[float]], *, min_step: int = 20,
                            tail_guard: int = 20) -> int:
    """Return one causal anchor from past actions only.

    A gripper-sign transition is preferred; a local action-change maximum is
    the fallback. The selected time is snapped to the five-step replay grid.
    """
    if len(actions) <= min_step + tail_guard + 2:
        raise ValueError("trajectory too short for CST")
    if any(len(row) != 7 for row in actions):
        raise ValueError("CST requires seven-dimensional action history")

    speed = [0.0] + [
        math.sqrt(sum((cur[i] - prev[i]) ** 2 for i in range(7)))
        for prev, cur in zip(actions, actions[1:])
    ]
    candidates: list[tuple[float, int]] = []
    for step in range(min_step, len(actions) - tail_guard):
        flip = actions[step - 1][6] * actions[step][6] < 0.0
        peak = speed[step] >= speed[step - 1] and speed[step] >= speed[step + 1]
        if flip or peak:
            candidates.append((speed[step] + (max(speed) + 1.0 if flip else 0.0), step))
    if not candidates:
        return (len(actions) // 2 // 5) * 5
    _, step = max(candidates, key=lambda item: (item[0], -item[1]))
    return max(min_step, min((step // 5) * 5, ((len(actions) - tail_guard - 1) // 5) * 5))
