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


## Archived SPARC: visual-progress anchor contrast

SPARC tested whether frozen SmolVLA features could supply a visual-progress
anchor and a low-capacity progress contrast without training another large
critic. A baseline campaign collected 20 fresh initial states (14/20 terminal
successes). A fixed random projection plus ridge head was fit only on
development states; the held-out protocol matched a SPARC visual anchor
against the archived causal action-history anchor.

| Measure | Development SPARC | Held-out SPARC | Held-out legacy |
| --- | ---: | ---: | ---: |
| States | 12 | 8 | 8 |
| Paired branches | 48 | 32 | 32 |
| Non-tied progress proxy pairs | 12 / 12 | 8 / 8 | 8 / 8 |
| Terminal direction-changing pairs | 0 | 1 | 0 |
| Correct terminal directions | — | 1 / 1 | — |

The collection and feature path are valid, but one held-out terminal event
cannot support a policy-success or Q-gradient claim. SPARC is archived as a
working visual-anchor/proxy pipeline with insufficient external outcome
evidence; more progress-head, threshold, or critic tuning is not justified.

## Archived STAGE-CF: task-stage-conditioned counterfactual trigger

STAGE-CF replaced terminal success as the *trigger label* with deterministic
simulator-observable Task-5 geometry: end-effector, book, and the caddy back
compartment. It selected anchors by replaying the frozen action prefix and
choosing the largest positive physical stage transition. The public
reference core contains only recorded-position scoring and cannot access a
simulator, model, or robot.

| Measure | Development STAGE-CF | Held-out STAGE-CF | Held-out legacy |
| --- | ---: | ---: | ---: |
| State-validated anchor coverage | 12 / 12 | 8 / 8 | 8 / 8 |
| Paired branches | 48 | 32 | 32 |
| Non-tied stage pairs | 12 / 12 | 8 / 8 | 6 / 8 |
| Stage abstentions | 0 / 12 | 0 / 8 | 2 / 8 |
| Terminal direction-changing pairs | 1 | 2 | 0 |
| Correct terminal directions | 0 / 1 | 1 / 2 | — |

STAGE-CF improves stage-label coverage over the legacy trigger, but the
external terminal evidence remains two pairs and only one correct direction.
It is therefore an engineering and measurement improvement, not evidence of
task-success improvement. Further STAGE-CF score tuning is stopped.


## Archived MSTE: multi-scale transition evidence

MSTE tested a different evidence structure rather than another critic: each signed branch records terminal-independent Task-5 geometry at 5, 20, and 60 continuation steps. A branch is called persistent only when 20- and 60-step book-to-back-compartment progress are positive and the later score does not materially regress. The scorer never reads terminal success; terminal direction is audited separately.

| Measure | Development STAGE-CF | Held-out STAGE-CF | Held-out legacy |
| --- | ---: | ---: | ---: |
| Signed groups | 12 | 8 | 8 |
| Persistent non-tied pairs | 8 / 12 | 3 / 8 | 4 / 8 |
| Reversible pairs | 0 / 12 | 2 / 8 | 1 / 8 |
| Abstention pairs | 4 / 12 | 5 / 8 | 4 / 8 |
| Terminal direction-changing pairs | 1 | 2 | 0 |
| Correct terminal directions | 1 / 1 | 0 / 2 | — |

The development signal did not generalize: held-out MSTE Stage-CF produced fewer persistent non-tied pairs than the immutable legacy arm and neither held-out terminal direction matched. MSTE is therefore archived as a sound multi-horizon measurement experiment with a negative improvement result. It does not justify policy updates, online Q-gradient guidance, or further MSTE threshold/horizon/geometry-score tuning.

The next hypothesis must change the information source or intervention design while preserving frozen-policy replay, matched signed probes, state-held-out evaluation, and strict separation between proxy labels and terminal outcomes.

## Archived GATE-V and ECDC: valid replay, no terminal lift

GATE-V used causal goal-stall anchor selection plus disagreement across four
frozen-SmolVLA action samples. ECDC then selected the farthest replayable pair
of their complete seven-dimensional actions and evaluated it under matched
controls. It is an offline counterfactual audit, not an online control loop.

| Measure | Result |
| --- | ---: |
| ECDC branches completed | 16 / 16 |
| Consistent duplicate-control groups | 4 / 4 |
| Candidate-action replay maximum absolute error | 0 |
| Terminal A/B direction-changing events | 0 / 4 |

This is a useful negative result: replay and action selection were verified,
but action diversity at these anchors did not yield terminal-outcome evidence.
ECDC is archived rather than tuned or promoted to held-out evaluation.

## PACE: a zero-rollout eligibility screen

PACE (Progress-Aligned Counterfactual Eligibility) reuses terminal-independent
5/20/60-step geometry already collected by ECDC. A candidate is eligible only
when its progress is persistent and, if both candidates persist, their margin
exceeds a predeclared threshold. It deliberately abstains otherwise.

The pre-registered development prediction was that approximately three of four
pairs would be eligible; the audit observed exactly 3 / 4. This confirms that
dense trajectory information can screen candidate pairs without more
simulation. It does **not** demonstrate terminal task success, an improved
policy, or online Q-gradient guidance.

- Reference implementations: [ECDC action-pair selection](core/ecdc.py) and
  [PACE eligibility](core/pace.py).
- Full evidence boundary and stop rules: [exploration ledger](docs/exploration-ledger.md).
