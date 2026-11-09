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

## Current snapshot — 2026-11-09

**Strongest result:** the author's native best-of-eight selection (Bo8) repeatedly beats single sampling on Task 2 in simulation. This is task-specific reproduction of an existing method, not a new selector, a learned trigger, or a general VLA gain.

| Study | Task 2 outcomes | Evidence boundary |
| --- | --- | --- |
| Frozen confirmation | Single sampling 42/128; native Bo8 63/128 (33 recoveries, 12 harms, +16.41 pp). | 64 physical scenes with two policy draws each. Nominal adjusted scene-clustered interval [+3.91,+28.91] pp. QGF and Task 3 intervals still span zero. |
| E1 timing and dose | Single sampling 91/256; dense Bo8 122/256 (+12.11 pp). | 128 new scenes, two draws per scene. Visual-residual and Q-gap gates did not beat random Bo8 in adjusted comparisons. |
| E2 candidate count and timing | Single sampling 100/256; dense Bo8 119/256; dense Bo4 121/256. | Bo4 sampled 78.02 vs 156.72 candidates per episode. Close success point estimates and roughly half the candidates do not establish non-inferiority or lower end-to-end latency. |

These are inference/control evaluations of a frozen actor and released critic, not new model training. Earlier public-data training and QGF reference experiments remain separate. The November 9 check used local delivery evidence because both workstations timed out: manifest hashes and Task 2 confirmation pair counts were checked, and E2 summary copies matched. No fresh server or physical robot result is claimed.

Read the [research rounds](docs/research-rounds.md) and [dated evidence ledger](evidence.md) for the complete comparisons.

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

The current task-specific reproduction is reportable. A second-task Bo4 replication or further trigger work remains a research decision, not an accepted result. Keep the candidate-count trade-off separate from a prespecified success-retention gate and measured latency. Do not deploy or tune the relative-Q proxy without a true live-continuation comparator.
