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

## 3.5. VLA-Corrector: conditional recovery support

**Verified through 2026-10-15:** strict feedback completed with 2 recoveries/1 degradation but only one repeated-rescue state, closing that finite configuration. A separate public actor supplies Spatial reference conditions. Failure-specific path recovery then rescues one failed state under two continuations, but harms a successful state once; an additional two-state comparison finds a different, straight recovery is needed. These are privileged offline-teacher simulation results, not task-Q or learned-trigger gains.

**Next acceptance:** independently accept the current-public-vision cache; keep the same eight actual teacher traces and group by initial state before fitting statistics. Compare fixed visual/proprioceptive students without simulator object truth or future outcomes as online inputs. Current proprioceptive fits are insufficient, and collected visual-cache rows are not accepted student training. Only then test a fixed student-to-actor handoff with same-anchor controls, all intervention steps charged, and explicit rescue/harm/cost reporting.

**Not yet established:** reliable observable correction, new task-value Q, learned benefit-trigger training, independent final validation, or physical robot performance. Keep training/sampling/integrity checks separate from terminal success. The [research rounds](../../projects/ciat_smolvla/docs/research-rounds.md) preserve earlier negative results and the new conditional successes without merging protocols.

## 4. Guarded closed-loop evaluation

Keep any policy output behind the existing private safety gate and collect command/feedback timestamps with visual and human outcome labels.

**Acceptance:** separately reported integration validity, offline metrics, visual cues, and task outcomes—never one substituted for another.

## 5. Dual-arm readiness

Treat dual-arm work as a future systems milestone rather than a completed project.

**Acceptance:** documented power, host, driver, communication, safety, calibration, and non-actuating motion-validation gates.
