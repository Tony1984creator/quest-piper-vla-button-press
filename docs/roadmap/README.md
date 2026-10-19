# Active roadmap

Each stage has a concrete acceptance gate; no stage is complete because a model merely starts running.

## 1. Data and label closure

Freeze complete-episode train/validation/test manifests for each dataset independently; preserve degree storage and convert once at the model boundary; finish `success`, `failure_reason`, and `task_stage` review.

**Acceptance:** reproducible manifest, QC report, no frame-level leakage, no cross-dataset aggregate mixing, and a label-review summary with excluded/ambiguous cases.

## 2. ACT baseline

Train ACT on the frozen two-RGB / 7D contract.

**Acceptance:** train/validation curves, declared checkpoint-selection rule, held-out action metrics, and an offline rollout review using the same held-out episodes.

## 3. VLA-JEPA ablation

Compare the ACT baseline with the auxiliary predictive objective under identical split, evaluation procedure, and training budget.

**Acceptance:** load/migration record, gradient and loss logs, comparable curves, and an explicit conclusion whether the auxiliary objective helps, hurts, or is inconclusive.

## 3.5. VLA-Corrector: engineering completion versus corrective benefit

**Completed stages — archived evidence checked 2026-10-19:** observation-only recovery pilot, real one-step and ten-step task-value training, thirty-branch candidate selection, native-flow gradient integration, and twelve gradient-controller rollouts. A student rescues one failed state but no fixed variant has positive unconditional net gain. Q and uniform selection each give 2 recoveries/1 degradation; gradients versus Q selection give 0/2 despite all primary-query final-Q scores rising.

**Next acceptance:** full-token/pooled/no-action × two-seed training and CPU restoration are now complete on the same 2,353 blocks. Interpret the modest offline differences with their model-specific targets; do not claim task benefit or a resolved failure cause. Any next continuation test must freeze the variant, same-budget controls, harm reporting and stopping criteria in advance. No new token-variant rollout result is reported.

**Trigger gate:** current outcomes are three initial-state full-controller comparisons, not hundreds of independent keyframe intervention labels. They have no positive gradient increments. Do not relabel Q ascent or old student successes as benefit labels for this controller. Learned benefit triggering and independent whole-method validation remain unfinished.

**Freshness:** research-workstation SSH is restored and live report/acceptance bindings were checked. Remote raw-tensor audits were not rerun; mc509 still times out. Physical robot outcomes remain separately unverified. The [research rounds](../../projects/ciat_smolvla/docs/research-rounds.md) retain previous protocols without pooling results.

## 4. Guarded closed-loop evaluation

Keep any policy output behind the existing private safety gate and collect command/feedback timestamps with visual and human outcome labels.

**Acceptance:** separately reported integration validity, offline metrics, visual cues, and task outcomes—never one substituted for another.

## 5. Dual-arm readiness

Treat dual-arm work as a future systems milestone rather than a completed project.

**Acceptance:** documented power, host, driver, communication, safety, calibration, and non-actuating motion-validation gates.
