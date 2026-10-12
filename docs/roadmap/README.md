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

## 3.5. VLA-Corrector: repeatable corrective evidence

Keep the original policy frozen; bind demonstration/task identity, executed action scope, causal history, and paired controls. The [research rounds](../../projects/ciat_smolvla/docs/research-rounds.md) retain separate Q, learned-proposal, visual-dynamics, event, execution-scope, and calibration studies rather than pooling their outcomes.

**Archived status — checked 2026-10-12:** real full-token predictive training and its fixed budget recheck completed. The 90-branch causal-event cohort found single-gradient versus replanning 1 recovery/1 degradation and segment 0/0. The execution-boundary development net +2 did not reproduce: follow-up 0 recoveries/5 degradations. Four bounded action-projection calibrations completed, but reliable local response improvement was absent. Both workstations were unreachable during this check; new claims use local archived accepted reports, not freshly read remote raw data or jobs.

**Next acceptance:** the latest archived route declares a strict stepwise-feedback reference against the fixed ten-step baseline, but only its launch is available. Recover live access, verify original-baseline parity and the complete fixed comparison, and retain harms, query counts, source identity, and continuation-noise scope. Progress toward feedback-budget mechanisms requires positive net recovery plus repeated recovery in at least two distinct states; otherwise close the current reliable-baseline search without adding more seeds or thresholds. Predictor seeds are not independent rollout replicas. Do not treat sampling host timers as synchronized GPU latency.

**Not yet admitted:** new task-value Q, learned benefit-trigger training, independent final evaluation, or physical robot correction. Predictive losses, local calibration metrics, and integration checks cannot substitute for terminal paired benefit.

## 4. Guarded closed-loop evaluation

Keep any policy output behind the existing private safety gate and collect command/feedback timestamps with visual and human outcome labels.

**Acceptance:** separately reported integration validity, offline metrics, visual cues, and task outcomes—never one substituted for another.

## 5. Dual-arm readiness

Treat dual-arm work as a future systems milestone rather than a completed project.

**Acceptance:** documented power, host, driver, communication, safety, calibration, and non-actuating motion-validation gates.
