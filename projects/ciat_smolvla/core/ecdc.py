"""Small, dependency-free ECDC action-pair selection for offline audits."""

from itertools import combinations
from math import sqrt


def select_farthest_candidate_pair(seeds, actions):
    """Return the deterministic farthest pair among candidate 7D actions.

    The routine is an offline selection primitive, not an online controller.
    Ties are resolved by the lexicographically smallest seed pair.
    """
    if len(seeds) != len(actions) or len(seeds) < 2:
        raise ValueError("seeds and actions must have the same length of at least two")
    if len(set(seeds)) != len(seeds):
        raise ValueError("candidate seeds must be unique")
    if any(len(action) != 7 for action in actions):
        raise ValueError("every action must be seven-dimensional")

    ordered = sorted(zip((int(seed) for seed in seeds), actions), key=lambda item: item[0])
    best = None
    for (seed_a, action_a), (seed_b, action_b) in combinations(ordered, 2):
        distance = sqrt(sum((float(a) - float(b)) ** 2 for a, b in zip(action_a, action_b)))
        candidate = (distance, (seed_a, seed_b), action_a, action_b)
        if best is None or distance > best[0] or (distance == best[0] and candidate[1] < best[1]):
            best = candidate

    return {
        "seed_a": best[1][0],
        "seed_b": best[1][1],
        "action_a": best[2],
        "action_b": best[3],
        "l2_distance": best[0],
    }
