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

## 3.5. VLA-Corrector: corrective-candidate evidence

Keep the original policy frozen, bind replay/model/training identities, compare candidates against contemporaneous same-prefix controls, and group evaluation by initial state. Earlier axis/stage/Q hypotheses are retained in the [research rounds](../../projects/ciat_smolvla/docs/research-rounds.md), not pooled into one benchmark.

**Status — 2026-10-06:** critic training and simulated Q-gradient execution are complete diagnostic stages. The newer persistent-proposal study found a one-state Task0 rescue but no Task2 recovery and one degradation. Two small behavior-prior flow generators have now been trained; the completed 48-branch matrix records conditional 2 recoveries/4 degradations/10 ties, versus unconditional 0/12/4. These new studies disable Q and learned triggering. They do not establish reliable correction or real robot benefit.

**Next acceptance:** fix candidate source and intervention scope before comparing selectors. Demonstrate repeatable net recovery across state-separated coverage, with separate harm counts, original-policy protection, action-conversion checks, matched continuation clocks, and declared inference costs. Only after candidate usefulness is established should Q selection/guidance and benefit-aware triggering be evaluated. Training loss, finite candidate samples, and an exposed-state rescue cannot substitute for this gate.

## 4. Guarded closed-loop evaluation

Keep any policy output behind the existing private safety gate and collect command/feedback timestamps with visual and human outcome labels.

**Acceptance:** separately reported integration validity, offline metrics, visual cues, and task outcomes—never one substituted for another.

## 5. Dual-arm readiness

Treat dual-arm work as a future systems milestone rather than a completed project.

**Acceptance:** documented power, host, driver, communication, safety, calibration, and non-actuating motion-validation gates.
