# CIAT: keyframe-triggered counterfactual action evaluation

## Scope and inheritance

CIAT is an **offline simulation research track** for keyframe-triggered Q-gradient guidance. It uses a frozen SmolVLA policy and LIBERO-Long `libero_10`, task 5. It is independent from the Quest/Piper hardware path and does not send robot commands.

It extends a private VLA-Corrector experiment harness without changing its frozen SmolVLA inference path, checkpoint/model-zoo ownership, LIBERO runner, action-chunk contract, or terminal feedback interface. The public repository contains only the aggregate protocol and evidence; it contains no private harness, raw trajectory, checkpoint, host path, or control code.

The research question is deliberately narrow: can a critic rank counterfactual action corrections at causally selected keyframes? It does **not** ask whether a robot can be controlled online.

## CIAT contribution

CIAT has two coupled contributions.

**Engineering contribution.** A keyframe trigger is made reproducible rather than treated as a screenshot heuristic: causal anchor selection reads recorded action history, the exact prefix is replayed under a sealed runtime contract, and a same-state double zero-action control verifies replay stability. Structured 7D action perturbations generate terminal branches. Logs, frozen state features, paired rows, and regression tests make each label traceable.

**Algorithmic contribution.** The baseline predicts absolute terminal outcome, (Q(s,a)). The paired-control extension, CRA, predicts the candidate's relative terminal outcome at the *same* anchor:

`A(s,a) = Q(s,a) - Q(s,a_control)`

This target is intended to reduce same-state outcome-prior confounding. Both targets are evaluated with leave-one-entire-anchor-state-out splits, so no keyframe state is shared across train and evaluation. CRA is a CIAT variant, not an online gradient update.

## What was built

- A sealed runtime contract for the frozen policy, seven-dimensional normalized action interface, seeds, and execution horizon.
- Causal action-history-only keyframe selection followed by exact recorded-prefix replay.
- Double zero-action controls and counterfactual action perturbations before the existing action post-processor.
- Terminal labels that require consistent controls before assigning `fragile`, `recoverable`, or `stable`.
- Frozen 7,688-dimensional anchor features, state-level splits, and leave-one-anchor-state-out evaluation.
- Versioned v3/v4 branch manifests, structured probe queues, target-comparison artifacts, and 55 regression tests spanning contracts, actions, replay, labels, paired rows, and state-split leakage guards.

## Archived v3 evidence

| Measure | Result |
| --- | --- |
| Frozen anchor states | 15 |
| Terminal branch rows | 129 |
| Terminal outcomes | 67 success / 62 failure |
| Labels | 30 control / 89 stable / 5 fragile / 5 recoverable |
| Leave-one-anchor-state-out mean terminal MSE | 0.3512 |

The v3 audit showed that outcome priors and sparse counterfactual events can dominate low MSE. It therefore froze the 15-state reference instead of increasing init states blindly.

## Archived v4 primary audit

v4 retains the same 15 frozen anchor states and replay contract. It adds a predeclared primary ±7D axis-probe collection with two zero-action controls per state.

| Measure | Result |
| --- | --- |
| Completed branches | 240 / 240 |
| Consistent double-control groups | 15 / 15 |
| Terminal outcomes | 134 success / 106 failure |
| Candidate/control pairs | 210 |
| Informative nonzero candidate/control events | 12 |
| Absolute-Q terminal MSE | 0.3437 |
| Absolute-Q nonzero-event ranking accuracy | 0.5133 |
| CRA advantage MSE | 0.0889 |
| CRA nonzero-event direction accuracy | 0.1733 |

The absolute-Q and CRA MSE values fit different targets and cannot be compared directly. The meaningful comparison is held-out ranking/direction on nonzero events. With only 12 such events, CRA v1 shows no stable ranking advantage. This is a recorded negative result, not an implementation failure: the collection, pairing, audit, and leakage guards all completed, but the evidence does not justify an online Q-gradient claim.

## Archived AFCR v1: axis-factorized counterfactual ranking\n\nAFCR asks a narrower question than absolute Q or CRA. For a fixed keyframe state and primary action axis it compares the two measured probes directly:\n\n`D_i(s) = y(s, +εe_i) - y(s, -εe_i)`\n\nThe intent is to cancel a state’s broad success/failure prior and ask only whether the positive or negative axis direction was better. Its implementation reconstructs each pair from the raw bound branch delta and validates the candidate action, anchor step, branch seed, and initial-state identity before pairing. This is important because the recorded training-row action is a complete policy action rather than the isolated probe delta.\n\n| AFCR v1 measure | Result |\n| --- | --- |\n| Complete same-state ±axis pairs | 105 across 15 frozen states |\n| Direction-changing pairs / ties | 10 / 95 |\n| Abstentions | 49 / 105 |\n| Recommended nonzero events | 4 |\n| Correct recommended directions | 0 / 4 |\n\nAFCR v1 has no stable global axis-direction signal under state-held-out evaluation. Its nonzero event set is not the same as the 12 candidate/control events used by the absolute-Q/CRA audit, so these figures are not a single numerical leaderboard. This is a useful negative result: it rules out threshold tuning or a high-capacity state MLP on this sparse collection as a justified next step.\n\n## Evidence boundary and next gate

CIAT is **not** connected to online Q-gradient action updates. It does not claim policy improvement, simulation success improvement, real-time performance, or robot task success.

The next algorithm must be stated as a fresh, pre-registered hypothesis and compared with the immutable CIAT v3/v4/AFCR baselines using the same frozen policy/runtime and a state-held-out metric. The preferred next direction is uncertainty-guided counterfactual data design: rank state-axis pairs for *new collection* by evidence uncertainty/disagreement rather than claiming an immediate action correction. It remains a future hypothesis until fresh data and an evaluation are complete.
