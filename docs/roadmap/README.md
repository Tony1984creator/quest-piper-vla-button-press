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

## 3.5. Official baselines before shared-VLA integration

**Completed evidence — checked 2026-10-26:** three supported official QGF task/seed configurations complete full-budget learning with strong preset-guidance results. Public-data Corrector method training, full validation action-use diagnostics, runtime scaling repair, predictor/actor contracts and six native control rollouts also complete. QGF is not yet a VLA result; successful Corrector controls started from already-successful natural cases and supply no rescue evidence.

**Next acceptance:** finish the frozen 120-identity natural PI0.5 cohort (117 new, three reused), audit task/init routing, real boundaries, raw-observation coverage, source/model identity and actual outcomes, then compare native truncation and truncation+OGG using the same declared identities/noise. Running natural coverage is not a completed corrective benchmark. Three reused cases without new full raw observations cannot be called 120 newly captured training trajectories.

**Integration gate:** separately establish applicable Corrector and task-Q guidance evidence before combining them in one VLA. Distinguish the original visual-residual detector/OGG from task-return Q and from any future learned benefit trigger. Keep original weights, independent evaluation criteria, harms and call costs protected.

**Historical closure:** simple first-event replanning has a local rescue; custom gradients, representation/return/state ablations did not establish incremental utility. Preserve those results rather than repeat threshold, radius, seed or capacity searches. [Research rounds](../../projects/ciat_smolvla/docs/research-rounds.md) retain the detailed evidence. No new physical robot result is reported.

## 4. Guarded closed-loop evaluation

Keep any policy output behind the existing private safety gate and collect command/feedback timestamps with visual and human outcome labels.

**Acceptance:** separately reported integration validity, offline metrics, visual cues, and task outcomes—never one substituted for another.

## 5. Dual-arm readiness

Treat dual-arm work as a future systems milestone rather than a completed project.

**Acceptance:** documented power, host, driver, communication, safety, calibration, and non-actuating motion-validation gates.
