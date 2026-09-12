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

## 3.5. CIAT offline correction audit

CIAT preserves the private experiment harness's frozen SmolVLA inference, LIBERO-Long runner, action chunk contract, terminal feedback interface, and model/weight ownership. Its separate research layer adds causal keyframe selection, exact-prefix replay, double zero-action controls, structured 7D action probes, immutable data artifacts, and state-held-out audits. It does not modify the checkpoint, `model_zoo`, or online inference chain.

**Status:** v3 and v4 are archived offline baselines. v3 collected 15 states and 129 terminal branches. v4 completed 240/240 primary branches with 15 consistent double-control groups, 134 success / 106 failure outcomes, and 210 candidate/control pairs. In the unified 15-state audit, absolute-Q has terminal MSE 0.3437 and nonzero-event ranking accuracy 0.5133; CRA has advantage MSE 0.0889 and nonzero-event direction accuracy 0.1733. The MSE values use different targets and are not comparable as a winner metric. Only 12 nonzero events exist, so CRA v1 has **not** established stable ranking gain.

**Next acceptance:** freeze a new algorithmic hypothesis before collection, specify its intervention and primary state-held-out ranking metric, then compare it against the frozen CIAT baselines. Any online Q-gradient action update remains out of scope unless an independent deployment gate is met.

## 4. Guarded closed-loop evaluation

Keep any policy output behind the existing private safety gate and collect command/feedback timestamps with visual and human outcome labels.

**Acceptance:** separately reported integration validity, offline metrics, visual cues, and task outcomes—never one substituted for another.

## 5. Dual-arm readiness

Treat dual-arm work as a future systems milestone rather than a completed project.

**Acceptance:** documented power, host, driver, communication, safety, calibration, and non-actuating motion-validation gates.
