"""Dependency-free AFCR pairing and train-only axis baseline.

This public module consumes aggregate rows only.  It does not load a policy,
simulator, checkpoint, device, trajectory, or robot interface.
"""

from collections import defaultdict


def axis_pair_targets(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    """Pair explicit positive/negative single-axis outcomes by state and axis."""
    grouped: dict[tuple[str, int, float], dict[int, float]] = defaultdict(dict)
    for row in rows:
        delta = [float(value) for value in row["delta"]]
        active = [(axis, value) for axis, value in enumerate(delta) if value != 0.0]
        if len(delta) != 7 or len(active) != 1:
            raise ValueError("AFCR rows require exactly one nonzero value in a 7D delta")
        axis, value = active[0]
        key = (str(row["state_id"]), axis, abs(value))
        sign = 1 if value > 0.0 else -1
        if sign in grouped[key]:
            raise ValueError("duplicate signed probe")
        grouped[key][sign] = float(row["outcome"])

    pairs = []
    for (state_id, axis, magnitude), outcomes in sorted(grouped.items()):
        if set(outcomes) != {-1, 1}:
            continue
        pairs.append({
            "state_id": state_id,
            "axis": axis,
            "magnitude": magnitude,
            "direction_target": outcomes[1] - outcomes[-1],
        })
    return pairs


def heldout_axis_sign(pairs: list[dict[str, object]], validation_state: str) -> list[dict[str, object]]:
    """Predict an axis direction from other states only; zero mean abstains."""
    train = [row for row in pairs if str(row["state_id"]) != validation_state]
    result = []
    for row in pairs:
        if str(row["state_id"]) != validation_state:
            continue
        axis_values = [float(item["direction_target"]) for item in train if int(item["axis"]) == int(row["axis"])]
        score = sum(axis_values) / len(axis_values) if axis_values else 0.0
        result.append({
            "axis": int(row["axis"]),
            "target": float(row["direction_target"]),
            "prediction": None if score == 0.0 else (1 if score > 0.0 else -1),
        })
    return result

