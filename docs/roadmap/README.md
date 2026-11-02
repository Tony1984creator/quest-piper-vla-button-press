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

## 3.5. Shared-prefix causal controls before framework claims

**Completed evidence — checked 2026-11-02:** custom PI0.5 integration/coverage studies are closed without consistent Q benefit. A released author SmolVLA visual critic with QGF shows 17/120 → 23/120 success in its own matched development batch (11 recoveries/5 harms; interval spans zero). A separate five-condition/600-trajectory study gives natural 18, continuous Q 23 and visual-Q 19 successes, not stable trigger advantage.

**Next acceptance:** branch from shared actual prefixes, exact processed observations and sampling noise; prove zero-intervention executed-plan/action equivalence before testing the missing continuous-Q-plus-visual-interruption factor. Current prefix analysis found 25/120 pre-alarm divergences; one fixed-input replay confirms that six wrist-image uint8 values differing by one can reproduce first-chunk differences. Do not silently smooth inputs or drop mismatches.

**Method boundary:** keep author TD+EGR visual-Q weights distinct from Berkeley IQL and earlier self-trained PI0.5 Q. QGF is the inference adaptation; the original visual anomaly alarm is not a learned benefit-aware trigger. Compare guidance coverage, interruption, harms and policy-query/gradient counts separately. Fewer gradients alone do not establish latency gains.

**Confirmation gate:** current identities and outcomes are exposed development data. Freeze any justified mechanism change before independent confirmation; do not tune thresholds, Q weights, amplitude or critic capacity on this cohort. Integration has run, but stable whole-framework benefit, learned benefit triggering and physical robot performance remain unverified. The [research rounds](../../projects/ciat_smolvla/docs/research-rounds.md) retain earlier official-reference and custom evidence without pooling.

## 4. Guarded closed-loop evaluation

Keep any policy output behind the existing private safety gate and collect command/feedback timestamps with visual and human outcome labels.

**Acceptance:** separately reported integration validity, offline metrics, visual cues, and task outcomes—never one substituted for another.

## 5. Dual-arm readiness

Treat dual-arm work as a future systems milestone rather than a completed project.

**Acceptance:** documented power, host, driver, communication, safety, calibration, and non-actuating motion-validation gates.
