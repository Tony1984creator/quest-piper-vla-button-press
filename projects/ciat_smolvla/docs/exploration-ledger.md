# CIAT exploration ledger

This ledger records both positive engineering progress and negative algorithmic
results from the offline, frozen-SmolVLA / LIBERO-Long Task-5 research track.
It is intentionally not a claim of online Q-gradient guidance, robot control,
or task-success improvement.

| Track | What was tested | Evidence | Decision |
| --- | --- | --- | --- |
| CIAT / CRA | Absolute terminal-Q and paired candidate-control advantage at causally replayed keyframes | v4: 12 informative events; CRA held-out direction accuracy 0.1733 | Archive: sparse terminal events cannot support a critic claim |
| AFCR | Same-state, positive-versus-negative action-axis ranking | 105 axis pairs; four nonzero recommendations; zero correct | Archive: global axis direction is unsupported |
| BUCED / MACE | Budgeted uncertainty and magnitude escalation | No reliable event-density or terminal-direction gain | Archive: do not tune critic capacity or probe magnitude |
| CST / SPARC / STAGE-CF / MSTE | Trigger, visual/stage proxy, and multi-horizon progress measurement | Deterministic instrumentation works; held-out terminal evidence remains sparse or non-generalizing | Retain only as measurement assets |
| GATE-V | Causal goal-stall trigger plus four-sample frozen-policy disagreement | Four development groups; matched controls consistent; signed terminal events 0 / 4 | Archive: anchor selection is valid, terminal evidence is absent |
| ECDC | At GATE-V anchors, compare the farthest pair among four replayable full-action samples | 16 / 16 branches complete; 4 / 4 controls consistent; action-replay max error 0; terminal A/B events 0 / 4 | Archive: action diversity alone did not change terminal outcome |
| PACE | Terminal-independent persistent-progress eligibility over existing 5/20/60-step ECDC geometry | Pre-registered prediction: about 3 / 4 eligible pairs; observed 3 / 4; no new simulation | Retain as a low-cost screening gate, not as terminal evidence |

## What genuinely improved

The project now has a reproducible causal evaluation harness: sealed frozen
policy replay, matched controls, state-held-out protocol, deterministic action
replay checks, and explicit separation of dense proxy labels from terminal
success. That is real engineering and experimental progress. It localizes the
current limitation: short local perturbations and terminal binary labels do not
provide enough causal information to justify an online Q-gradient update.

It is **not** yet an algorithmic success claim. None of the archived tracks
demonstrates a stable held-out terminal-success improvement.

## Cost-control protocol for new ideas

1. State one falsifiable prediction before running new branches.
2. Audit existing artifacts first; PACE is an example that consumed zero new
   simulator rollouts and matched its 3 / 4 eligibility prediction.
3. Use matched controls, a state-level holdout, and an explicit abstention
   outcome. Do not train a larger critic until an intervention has enough
   direction-changing terminal events.
4. Stop a family after a negative predeclared result; do not rescue it through
   threshold, horizon, or model-capacity sweeps.
5. Promote only a mechanism that changes an independent terminal outcome on
   held-out states. Dense stage progress is useful screening evidence, not a
   substitute for terminal evidence.

## Reusable public reference core

`core/ecdc.py` deterministically selects the farthest replayable pair of
seven-dimensional candidate actions. `core/pace.py` applies an explicit
persistence-and-margin abstention gate. Both are dependency-free offline
utilities; neither controls a robot or updates a policy.
