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

Keep the frozen SmolVLA policy, LIBERO-Long task, causal anchor rule, and state-held-out split fixed. Compare the absolute terminal-outcome critic with a paired zero-control-relative advantage variant.

**Status:** v3 absolute-Q and CRA v1 paired-target audits are complete (15 states, 99 CRA pairs). CRA's 0.1719 advantage MSE is not a deployment result because only 10 nonzero advantage events support ranking.

**Next acceptance:** pre-register structured perturbation directions that increase event density, then compare absolute-Q and CRA with a state-held-out ranking metric and a written offline-only conclusion unless the deployment gate is independently met.

## 4. Guarded closed-loop evaluation

Keep any policy output behind the existing private safety gate and collect command/feedback timestamps with visual and human outcome labels.

**Acceptance:** separately reported integration validity, offline metrics, visual cues, and task outcomes—never one substituted for another.

## 5. Dual-arm readiness

Treat dual-arm work as a future systems milestone rather than a completed project.

**Acceptance:** documented power, host, driver, communication, safety, calibration, and non-actuating motion-validation gates.

