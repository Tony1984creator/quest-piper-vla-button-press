"""Dependency-free MACE escalation rule for offline experiment planning only."""


def first_event_scale(signed_outcomes: list[tuple[float, bool, bool]]) -> float | None:
    """Return the first scale with different positive/negative outcomes.

    Entries must be in ascending scale order.  The result is an observation
    about experiment sensitivity, not an action command or correction sign.
    """
    previous = -float("inf")
    for scale, negative_outcome, positive_outcome in signed_outcomes:
        if scale <= previous:
            raise ValueError("scales must be strictly increasing")
        previous = scale
        if negative_outcome != positive_outcome:
            return scale
    return None

