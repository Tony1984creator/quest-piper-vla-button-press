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

## CRA v1: control-relative advantage audit

The completed offline variant compares a candidate action with the zero-action control at the same anchor:

`A(s, a) = Q(s, a) - Q(s, a_control)`

It uses 99 non-control candidate/control pairs from the same fixed 15-state collection. In each leave-one-anchor-state-out fold, feature normalization and critic fitting use only the other 14 states. The supervised target is the paired terminal-outcome difference (`-1`, `0`, or `+1`).

| Measure | Result |
| --- | --- |
| Candidate/control pairs | 99 |
| Held-out anchor states | 15 |
| Mean held-out advantage MSE | 0.1719 |
| Informative nonzero advantage targets | 10 |
| Mean per-state nonzero direction accuracy | 0.35 |

CRA is a reproducible paired-target baseline, not a positive deployment result. Only 10 informative counterfactual events exist, and directional accuracy is unstable across states. It therefore does **not** establish reliable action ranking, online Q-gradient guidance, simulation success improvement, or robot capability.

The next research gate is to increase counterfactual event density and structured action-direction coverage in a newly designed collection, while preserving this v3/CRA dataset as the frozen reference baseline.
