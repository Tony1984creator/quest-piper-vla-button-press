"""Progress-aligned counterfactual eligibility (PACE) for offline audits."""


def persistent_candidate_eligibility(
    score_a, persistent_a, score_b, persistent_b, *, min_margin=1e-3
):
    """Choose an eligible persistent candidate or explicitly abstain.

    ``score_*`` is a terminal-independent progress proxy.  This function does
    not read terminal task success and must not be interpreted as a policy
    improvement or an online action update.
    """
    if min_margin < 0:
        raise ValueError("min_margin must be non-negative")
    if persistent_a and persistent_b:
        margin = float(score_a) - float(score_b)
        if abs(margin) < min_margin:
            return {"eligible": False, "winner": None, "reason": "persistent_margin_below_threshold"}
        return {
            "eligible": True,
            "winner": "candidate_a" if margin > 0 else "candidate_b",
            "reason": "persistent_margin",
        }
    if persistent_a:
        return {"eligible": True, "winner": "candidate_a", "reason": "only_a_persistent"}
    if persistent_b:
        return {"eligible": True, "winner": "candidate_b", "reason": "only_b_persistent"}
    return {"eligible": False, "winner": None, "reason": "no_persistent_candidate"}
