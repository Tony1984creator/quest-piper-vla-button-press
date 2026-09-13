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

## Archived AFCR v1: axis-factorized counterfactual ranking

AFCR asks a narrower question than absolute Q or CRA. For a fixed keyframe state and primary action axis it compares the two measured probes directly:

`D_i(s) = y(s, +εe_i) - y(s, -εe_i)`

The intent is to cancel a state’s broad success/failure prior and ask only whether the positive or negative axis direction was better. Its implementation reconstructs each pair from the raw bound branch delta and validates the candidate action, anchor step, branch seed, and initial-state identity before pairing. This is important because the recorded training-row action is a complete policy action rather than the isolated probe delta.

| AFCR v1 measure | Result |
| --- | --- |
| Complete same-state ±axis pairs | 105 across 15 frozen states |
| Direction-changing pairs / ties | 10 / 95 |
| Abstentions | 49 / 105 |
| Recommended nonzero events | 4 |
| Correct recommended directions | 0 / 4 |

AFCR v1 has no stable global axis-direction signal under state-held-out evaluation. Its nonzero event set is not the same as the 12 candidate/control events used by the absolute-Q/CRA audit, so these figures are not a single numerical leaderboard. This is a useful negative result: it rules out threshold tuning or a high-capacity state MLP on this sparse collection as a justified next step.

## Archived BUCED and MACE fresh-state pilots

BUCED and MACE were intentionally evaluated as **data-design hypotheses**, not as action controllers. Both used new frozen keyframe states, exact-prefix replay, and double zero-action controls.

| Pilot | Fresh states | Controls | Intervention | Result |
| --- | ---: | ---: | --- | --- |
| BUCED | 5 | 5 / 5 consistent | BUCED-prioritized axis versus a pre-registered balanced axis, each with a signed ±0.05 pair | 0 / 5 direction-changing pairs in either arm; no evidence that axis ranking increased event discovery. |
| MACE | 5 | 5 / 5 consistent | Signed primary-axis pairs escalate ±0.05 → ±0.15 → ±0.25 only after a tie | 1 / 5 states changed at ±0.05; the other 4 stayed tied through ±0.25. Larger magnitude did not enrich events in this pilot. |

These are informative negative results. The bottleneck is now localized to the causal keyframe/task-stage trigger: neither a global axis ranking nor larger perturbations generated enough non-tied outcomes for a correction learner. They do not measure policy improvement, online action quality, or robot success.

## Archived CST: causal stage-transition trigger contrast

CST tests whether a more stage-aware **action-history-only** keyframe selector can create more useful counterfactual events. It does not inspect observations, terminal outcomes, or future frames. It chooses a prior gripper sign transition when present and otherwise a local 7D action-change peak, then snaps the selected time to the replay grid.

A fresh five-state contrast (init 25–29) compared the immutable legacy action-history anchor with CST under the same budget. For each state and each trigger arm, two zero-action controls and one signed primary-axis ±0.05 pair were executed.

| Measure | Legacy anchor | CST |
| --- | ---: | ---: |
| Fresh states | 5 | 5 |
| Completed branches | 20 / 20 | 20 / 20 |
| Consistent paired-control groups | 5 / 5 | 5 / 5 |
| Direction-changing signed pairs | 2 / 5 | 2 / 5 |
| Event rate | 40.0% | 40.0% |

CST produced no event-density lift over the legacy anchor. This clean negative result rules out further tuning of an action-history-only trigger on this evidence. It does not show that task-stage information is useless; rather, the next trigger hypothesis would need pre-registered task or visual semantics and fresh matched data.

## Public offline core

The public [AFCR pairing/sign baseline](core/afcr.py), [BUCED acquisition ranker](core/buced.py), [MACE first-event rule](core/mace.py), and [CST action-history trigger](core/cst.py) are dependency-free reference implementations. They operate only on aggregate rows, contain no private paths or simulator calls, and cannot load weights or command hardware. [Focused tests](../../tests/test_ciat_offline_rankers.py) document signed-pair completeness, state-held-out isolation, acquisition ordering, and first-event stopping.

## Evidence boundary and next gate

CIAT is **not** connected to online Q-gradient action updates. It does not claim policy improvement, simulation success improvement, real-time performance, or robot task success.

The next algorithm must be stated as a fresh, pre-registered keyframe-stage/event-enrichment hypothesis and compared with the immutable CIAT baselines using the same frozen policy/runtime. The action-history-only trigger contrast is now also archived. A future hypothesis must add pre-registered task or visual stage information; it should not add another critic, global axis ranker, magnitude schedule, or action-only trigger without new evidence.
