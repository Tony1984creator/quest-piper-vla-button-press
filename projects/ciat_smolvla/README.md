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

## Current snapshot — 2026-10-02

| Item | Verified state | Interpretation |
| --- | --- | --- |
| Expanded supervision | 84/84 confirmation branches complete; 144 training / 36 development-validation branches. | The data gate passed and real critic diagnostic fitting was completed. |
| Training and gradient path | Nine diagnostic models; retrained linear direction audit 4/5; six local-direction heads and real gradient execution checks. | The training-to-action path works in simulation; useful correction remains an experimental question. |
| Matched flow | 12/12 flow branches complete; zero recoveries and zero degradations, with successful controls in both groups. | The execution check lacked a failed-control recovery opportunity. |
| Benefit confirmation | 28/28 fixed follow-up branches; zero recoveries, zero degradations across four groups. | Local fitting improvements have not established stable task benefit. |
| Expected-benefit audit | 216/216 branches, 96 matched pairs: 3 recoveries, 2 degradations, 91 ties. | Real Q-gradient intervention generated local rescue and harm; no stable benefit or trigger-training gate. |
| Candidate and timing tests | Candidate-mode campaign 96/96; temporal confirmation 68/68 with 0 recoveries and 3 degradations. | Coverage found more recoverable actions, but the learned selector did not beat a simple timing rule; longer execution did not generalize to new noise. |
| Value-data and cross-task foundation | 100 historical trajectories audited; two-task natural pilot and four-way first-fragment pilot completed. | Data semantics and frozen-policy portability advanced; these pilots supplied no independent correction-benefit label. |

Read the [research rounds](docs/research-rounds.md) for each route decision, implementation, result, and next gate. The [dated evidence ledger](evidence.md) retains the numerical audit history.

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

Evaluate the frozen corrector with matched continuations and state-separated coverage to test whether expected intervention benefit can be predicted before training a benefit-aware trigger. Any future policy or robot conclusion requires a separate guarded closed-loop evaluation.
