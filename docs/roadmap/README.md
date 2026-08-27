# Active roadmap

## 1. Data and label closure

Freeze episode-level train/validation/test manifests; preserve degree storage and convert once at the model boundary; complete `success`, `failure_reason`, and `task_stage` review. Acceptance: reproducible manifest, QC report, and no frame-level leakage.

## 2. ACT baseline

Train on the frozen split using the two RGB streams and 7D state/action contract. Acceptance: train/validation curves, checkpoint selection rule, held-out action metrics, and a bounded offline rollout review.

## 3. VLA-JEPA ablation

Compare the ACT baseline with the auxiliary predictive objective using the same data split, evaluation protocol, and budget. Acceptance: mapping/gradient logs, comparable curves, and an explicit conclusion even if no gain appears.

## 4. Guarded button-loop evaluation

Keep policy output behind the existing private safety gate and collect timestamped command/feedback evidence plus visual and human labels. Acceptance: separately reported integration validity, visual events, and task outcomes.

## 5. NERO dual-arm readiness

NERO remains a roadmap item, not a completed portfolio project. Acceptance: power, host, driver, communication, safety, calibration, and a first non-actuating motion-validation checklist.

