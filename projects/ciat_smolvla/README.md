# VLA-Corrector: Offline Counterfactual Intervention Research

## Research question

Can a frozen visual-action policy be audited with controlled offline counterfactuals well enough to decide when an action correction is worth investigating?

This project is a **measurement and evidence-design study**, not a robot-control system. It records the work needed before any corrective policy claim: paired controls, state-held-out evaluation, abstention, and explicit stopping rules.

## What is public

- A reproducible description of aggregate, offline experiment conclusions.
- A compact record of which hypotheses were retained, rejected, or deferred.
- The decision boundary between an engineering probe and a learned critic.

## What is deliberately not public

No raw trajectories, task descriptions, model files, environment configuration, execution paths, or simulator/control code are included. Public numbers are aggregated so the portfolio communicates experimental reasoning without exposing the underlying asset.

## Current snapshot — 2026-10-12

The newest completed evidence was checked against **local archived reports dated October 6–11** and their acceptance/hash bindings. Both workstations are currently unreachable; this is not a fresh verification of remote raw trajectories, model files, or running jobs.

| Item | Verified state | Interpretation |
| --- | --- | --- |
| Earlier Q/candidate studies | Real diagnostic critic training and simulated gradient execution; expected-benefit audit 3 recoveries/2 degradations/91 ties; timing confirmation 0/3/29. | Engineering path and local events, not stable task improvement. Historical protocols remain separate. |
| Learned behavior proposals | Two 38,854-parameter flow priors; complete 48-branch comparison: conditional 2 recoveries/4 degradations/10 ties. | Real training and simulated execution, but worse net outcomes than original policy. |
| Full-token dynamics training | 450 demonstration caches / 110,372 frames; six predictor fits at 1,000 updates plus one six-fit 10,000-update recheck. Segment inputs add predictive information; other-task increments conflict across seeds. | A distinct visual-dynamics study, not task Q. Only 379 cached episodes are Long, and they overlap original-policy training configuration. |
| Causal event cohort | Three tasks, nine exposed states, 90 accepted branches. Replanning versus natural: 3 recoveries/2 degradations; single gradient versus replanning: 1/1; segment: 0/0. | Replanning explains repeated natural recovery; no repeated gradient increment. Reference events are not learned benefit triggers. |
| Execution-boundary confirmation | Development boundary rule: 5 recoveries/3 degradations; frozen follow-up: 0/5. Sixty total accepted episodes across the two distinct studies. | Local positive scope results did not reproduce. No oracle stage, Q, or learned trigger was used. |
| Action-response calibration | 2,376 deduplicated windows, twenty shared-prefix pairs; four 1,000-update fits of a copied 18,176-parameter action projection; forty held-out pair metrics CPU-recomputed in the archived verification. | Overall prediction improves slightly, but local response confirmation is unreliable. No calibrated-gradient rollout or deployment latency claim. |

Read the [research rounds](docs/research-rounds.md) for route → implementation → result → next gate, and the [dated evidence ledger](evidence.md) for measured counts and source freshness. Earlier experiments are preserved, not pooled into one benchmark. No physical robot correction result is reported here.

## Experiment map

| Family | Question it tested | Outcome | Decision |
| --- | --- | --- | --- |
| CIAT / CRA | Do paired controls produce a dependable relative-advantage signal? | The held-out direction result was weak. | Retain paired auditing; newer diagnostic critic training is detailed in the evidence ledger. |
| AFCR | Can axis-factorized ranking choose a useful correction direction? | Recommendations did not predict the observed direction. | Archive the global axis-ranking hypothesis. |
| BUCED / MACE | Can uncertainty-guided sampling or larger perturbations create useful new evidence? | Neither increased informative event density. | Stop expanding axes or magnitudes without a new causal trigger. |
| CST / SPARC / STAGE-CF / MSTE | Can stage, visual-progress, or transition signals identify useful intervention windows? | Pipelines ran, but evidence was small or did not generalize. | Keep measurement assets; stop threshold tuning. |
| GATE-V / ECDC / PACE | Can eligibility and disagreement rules justify extra evaluation? | Controls remained consistent, but terminal ranking evidence was absent. | Keep conservative selectors; do not claim terminal improvement. |

## Why this belongs in the portfolio

The useful result is not a claimed corrective VLA. It is the discipline to stop: establish paired controls, test the state-held-out split, publish negative results, and prevent an attractive offline signal from becoming an unsupported online capability claim.

## Reusable public reference core

The existing [ECDC pair selector](core/ecdc.py) and [PACE eligibility gate](core/pace.py) are small, dependency-free offline utilities. The detailed archive of earlier falsified ideas remains in the [exploration ledger](docs/exploration-ledger.md); it is linked rather than repeated here so the project page stays readable.

## Next evidence gate

Establish repeatable corrective benefit and protect successful original behavior before fitting task-value Q or a benefit-aware trigger. The latest archived route declares a strict stepwise-feedback reference against the fixed ten-step baseline; its launch has no completed result in the available archive. First recover live access and audit the complete paired outcome, including harms and query cost. Do not substitute predictive loss, source identity, or a small-model memory measurement for this gate. Any robot conclusion requires a separate guarded physical evaluation.
