# CIAT research synthesis: what the experiments say

## The common objective

CIAT began as a narrow offline question: at a causally selected keyframe, can
counterfactual action information tell a frozen SmolVLA policy which
correction direction is better? Every result here is simulation-only,
state-held-out where applicable, and is not a robot-control or online policy
claim.

## Chronology and evidence

| Family | What changed | What was learned |
| --- | --- | --- |
| Absolute-Q / CRA | Predicted terminal outcome or same-state relative advantage from frozen features. | Only 12 informative v4 terminal events existed; CRA direction accuracy was 0.1733. The label, not MLP capacity, is the limiting factor. |
| AFCR | Compared measured positive/negative primary-axis probes directly. | 105 pairs reduced to 10 changing pairs, 49 abstentions, and 0/4 correct recommended events. A global signed-axis learner is not supported. |
| BUCED / MACE | Changed which axis or perturbation magnitude was collected. | Fresh pilots produced 0/5 directional events for BUCED; larger magnitudes did not enrich MACE events. More aggressive perturbation is not the missing ingredient. |
| CST | Used a stronger causal action-history trigger. | Event rate stayed 2/5 for both CST and legacy anchors. Action history alone is not enough stage information. |
| SPARC | Used frozen visual-feature progress to choose anchors and rank short-horizon change. | The visual pipeline worked, but held-out terminal evidence was 1 event. Proxy quality is not equivalent to task success. |
| STAGE-CF | Used simulator-observable book/caddy geometry and replayed physical stage transitions. | Held-out stage coverage improved from 6/8 legacy pairs to 8/8, but only 2 terminal events appeared and only 1 direction agreed. Measurement improved; external validation did not. |

## Diagnosis

This is primarily a **research-direction and experimental-observability
problem**, not an implementation-quality problem.

The engineering evidence is unusually strong: frozen runtime contracts,
exact-prefix replay, state-level split isolation, double controls, serial
GPU guards, bounded artifacts, and regression tests all worked across the
campaigns. The repeated failure mode is consistent across methods: a
single short-horizon signed action perturbation at one keyframe produces too
few independently auditable changes in terminal task outcome.

The algorithms also reveal a useful asymmetry:

- Better *measurement* is possible: STAGE-CF substantially reduced
  geometric-stage abstention.
- Better *task-success prediction* is not yet established: the terminal
  event count remains too small for a reliable ranking claim.
- Therefore adding a larger critic, changing a threshold, altering an axis
  ranker, or increasing perturbation magnitude would be parameter churn, not
  a new scientific hypothesis.

## Required properties of the next proposal

The next proposal must change the information available to evaluation, not
only the score function. It should:

1. collect a multi-horizon state-transition trace from each intervention
   (for example 5, 20, and longer task-relevant horizons);
2. pre-register event labels that distinguish reversible local motion from
   durable object-to-goal progress;
3. use stage consistency across horizons as a primary label, while retaining
   terminal success as a separate external audit;
4. compare against legacy and STAGE-CF anchors on held-out states; and
5. stop if the external audit remains too sparse, then redesign data
   collection rather than train another critic.

A recommended successor is **MSTE: Multi-Scale Transition Evidence**. It is
not a tuned STAGE-CF variant: it asks whether a perturbation creates
consistent, task-grounded object progress across multiple horizons. Its
first deliverable should be a fixed-data/smoke feasibility audit, not a
large training job.
