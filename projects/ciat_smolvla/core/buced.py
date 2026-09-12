"""Dependency-free BUCED acquisition rule for offline probe design only."""

import math


def _entropy(positive: int, negative: int) -> float:
    probability = (positive + 1.0) / (positive + negative + 2.0)
    return -(probability * math.log2(probability) + (1.0 - probability) * math.log2(1.0 - probability))


def rank_axes_for_collection(train_pairs: list[dict[str, object]], axes: list[int]) -> list[dict[str, float | int]]:
    """Rank axes by likely non-tied outcome times unresolved direction.

    Inputs must exclude the future/held-out state's outcomes.  The score is an
    acquisition priority, never an action direction.
    """
    ranked = []
    for axis in sorted(set(axes)):
        targets = [float(row["direction_target"]) for row in train_pairs if int(row["axis"]) == axis]
        positive = sum(value > 0.0 for value in targets)
        negative = sum(value < 0.0 for value in targets)
        event_probability = (positive + negative + 1.0) / (len(targets) + 2.0)
        ranked.append({
            "axis": axis,
            "observations": len(targets),
            "event_probability": event_probability,
            "direction_entropy": _entropy(positive, negative),
            "acquisition_score": event_probability * _entropy(positive, negative),
        })
    return sorted(ranked, key=lambda row: (-float(row["acquisition_score"]), int(row["axis"])))

