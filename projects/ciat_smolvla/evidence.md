# Dated evidence ledger

**Reporting date:** 2026-09-24  
**Evidence level:** offline simulation probe

## Latest paired-audit gate

| Measurement | Aggregate result | Decision use |
| --- | ---: | --- |
| Initial states / anchors | 12 / 18 | Fixed coverage for the current audit. |
| Paired comparisons | 72 | 5 recoveries, 4 degradations, 63 ties. |
| Training split | 48 pairs: 4 recoveries | Recoveries were concentrated in two initial states. |
| State-held-out split | 24 pairs: 1 recovery, 4 degradations | Not a dependable correction signal. |
| Data gate | Not met | No real critic training was started. |

One terminal-geometry accounting issue was found in an environment wrapper: a terminal call could reset before the returned geometry was recorded. Terminal and post-terminal geometry are therefore treated as **abstain** in the audit view. The original study artifacts are retained privately; the public ledger reports only the corrected interpretation.

## Experiment ledger

| Name | Expanded name / purpose | Aggregate finding | Status |
| --- | --- | --- | --- |
| CIAT | Counterfactual Intervention Audit | Paired controls are useful for measurement, but not sufficient evidence for correction. | Retained as an audit primitive. |
| CRA | Paired-Control Relative Advantage | 12 informative candidate/control events; direction accuracy 0.1733. | Archive as a training target. |
| AFCR | Axis-Factorized Counterfactual Ranker | 105 signed pairs; 4 recommendations; 0 correct directions. | Archive global axis ranking. |
| BUCED | Bayesian Uncertainty-Guided Counterfactual Evidence Design | No event-density gain on the fresh-state pilot. | Stop without a new trigger. |
| MACE | Adaptive-Magnitude Counterfactual Escalation | Larger perturbations mostly tied; no new useful evidence. | Stop magnitude escalation. |
| CST | Causal Stage-Transition trigger | Two direction events matched the legacy trigger. | Archive action-only triggering. |
| SPARC | Visual-progress anchor contrast | Valid measurement pipeline; small external evidence. | Retain as a measurement asset. |
| STAGE-CF | Task-stage-conditioned counterfactual trigger | Valid pipeline, but no generalizing external result. | Stop threshold tuning. |
| MSTE | Multi-Scale Transition Evidence | Valid pipeline, but no generalizing external result. | Stop threshold tuning. |
| GATE-V | Goal-stall and action-disagreement selector | Consistent controls but no signed-axis event. | Retain only as a conservative selector. |
| ECDC | Ensemble-Disagreement Counterfactual Direction | Complete branch/control coverage; no terminal A/B event. | Archive terminal ranking. |
| PACE | Progress-Aligned Counterfactual Eligibility | Expected eligibility observed for most test cases; no terminal outcome proof. | Keep as an eligibility check only. |

## Read this result correctly

The project has demonstrated an offline auditing workflow and several negative findings. It has **not** demonstrated online Q-gradient inference, policy improvement, real-time operation, or robot-task success. A bounded confirmation collection is **waiting for resources**; it will be reported only after completion and the same state-held-out gate.
