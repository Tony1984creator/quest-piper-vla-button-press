# Active roadmap

Each stage has a concrete acceptance gate; no stage is complete because a model merely starts running.

## 1. Data and label closure

Freeze complete-episode train/validation/test manifests; preserve degree storage and convert once at the model boundary; finish `success`, `failure_reason`, and `task_stage` review.

**Acceptance:** reproducible manifest, QC report, no frame-level leakage, and a label-review summary with excluded/ambiguous cases.

## 2. ACT baseline

Train ACT on the frozen two-RGB / 7D contract.

**Acceptance:** train/validation curves, declared checkpoint-selection rule, held-out action metrics, and an offline rollout review using the same held-out episodes.

## 3. VLA-JEPA ablation

Compare the ACT baseline with the auxiliary predictive objective under identical split, evaluation procedure, and training budget.

**Acceptance:** load/migration record, gradient and loss logs, comparable curves, and an explicit conclusion whether the auxiliary objective helps, hurts, or is inconclusive.

## 4. Guarded closed-loop evaluation

Keep any policy output behind the existing private safety gate and collect command/feedback timestamps with visual and human outcome labels.

**Acceptance:** separately reported integration validity, offline metrics, visual cues, and task outcomes—never one substituted for another.

## 5. Dual-arm readiness

Treat dual-arm work as a future systems milestone rather than a completed project.

**Acceptance:** documented power, host, driver, communication, safety, calibration, and non-actuating motion-validation gates.

