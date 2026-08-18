# Roadmap: Quest data loop to guarded button press

## Stage 1 — data and label closure

**Goal:** make data provenance, units, splits, and labels auditable.

**Acceptance criteria:**

- one frozen episode-level train/validation/test manifest;
- schema and timestamp alignment checks for each episode;
- a unit test that catches double degrees-to-radians conversion;
- `success`, `failure_reason`, and `task_stage` defined and annotated for the evaluation set;
- OpenCV candidates retained as review aids rather than substituted for success labels.

Current evidence: the stored-data contract QC has passed for 40 episodes and
14,653 frames. All 421 visual candidates have an episode/task-text target-floor
join. A deterministic episode-level, target-floor-stratified review queue can
now freeze a manageable evaluation subset, but target-button identities remain
pending human review; this does not satisfy the success-label criterion.

## Stage 2 — ACT baseline

**Goal:** establish the simplest action-chunk benchmark on the fixed split.

**Acceptance criteria:**

- reproducible environment and configuration file;
- train/validation curve, selected checkpoint, and held-out action metrics;
- visualized predicted-versus-demonstrated chunks in consistent units;
- a documented decision for proceeding or not proceeding to hardware.

## Stage 3 — VLA-JEPA ablation

**Goal:** isolate the effect of the action-conditioned auxiliary objective.

**Acceptance criteria:**

- matched ACT and ACT+auxiliary runs over at least multiple seeds;
- frozen-teacher and gradient-flow assertions logged for each configuration;
- validation-selected checkpoints and held-out results reported side by side;
- no positive claim unless metrics and closed-loop evidence agree.

## Stage 4 — guarded real-robot button loop

**Goal:** turn offline policy output into a reviewable real-robot experiment.

**Acceptance criteria:**

- explicit operator authorization, emergency stop, command freshness, workspace limits, and abort conditions;
- trial manifest with requested target, policy version, initial condition, and video review link stored privately;
- per-trial success/failure/stage labels;
- report success rate with numerator, denominator, confidence interval, and failure breakdown.

## Learning cadence

For a sustainable two-to-three-hours-per-day schedule, the next cycle should prioritize: one data-contract task, one baseline task, one experiment analysis task, and one concise research-log update per week. New model reading is useful only when attached to a measurable deliverable above.
