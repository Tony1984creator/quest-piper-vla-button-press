# CIAT: keyframe-triggered counterfactual action evaluation

## Scope

This is an **offline simulation research track** for keyframe-triggered Q-gradient guidance. It uses a frozen SmolVLA policy and LIBERO-Long task 5. It is independent from the Quest/Piper hardware path and does not send robot commands.

The purpose is to test whether a critic can identify action corrections at causally selected keyframes without confusing an offline terminal outcome with online policy capability.

## What was built

- A sealed runtime contract for the frozen policy, seven-dimensional normalized action interface, seeds, and execution horizon.
- Causal action-history-only keyframe selection, followed by exact recorded-prefix replay.
- Paired zero-action controls and counterfactual action perturbations before the existing action post-processor.
- Terminal branch labeling that requires two consistent controls before assigning `fragile`, `recoverable`, or `stable`.
- State-level data splits and leave-one-anchor-state-out evaluation to prevent the same anchor state from appearing in both train and validation.
- Contract, action, prefix-replay, label, and state-split regression tests.

## v3 offline evidence

| Measure | Result |
| --- | --- |
| Frozen anchor states | 15 |
| Terminal branch rows | 129 |
| Terminal outcomes | 67 success / 62 failure |
| Labels | 30 control / 89 stable / 5 fragile / 5 recoverable |
| Leave-one-anchor-state-out mean MSE | 0.3512 |

The fold error varies substantially. Some held-out states contain only one terminal class, so low MSE can reflect a state outcome prior rather than useful within-state action ranking.

## Evidence boundary

The critic is **not** used for online Q-gradient action updates. These results do not claim cross-state action ranking, simulation success improvement, real-time performance, or robot task success.

## Next approved variant: control-relative advantage

The next offline variant compares a candidate action with the zero-action control at the same anchor:

`A(s, a) = Q(s, a) - Q(s, a_control)`

This targets paired counterfactual action ranking rather than absolute terminal outcome prediction. It will be evaluated against the existing absolute-Q baseline with the same frozen policy, 15-state budget, exact-prefix replay protocol, and state-held-out splits. It is a planned experiment, not a completed result.
