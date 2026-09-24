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

## Current snapshot — 2026-09-24

| Item | Verified state | Interpretation |
| --- | --- | --- |
| Frozen-state paired audit | 12 initial states and 18 anchors completed; 72 paired comparisons were reviewed. | The audit can distinguish a small number of recoveries and degradations from ties. |
| State-held-out result | Training split: 4 recoveries; held-out split: 1 recovery and 4 degradations. | The available evidence does not support a reliable correction signal. |
| Training gate | The predefined data threshold was not met. | **No real critic training was started.** |
| Follow-up collection | A bounded confirmation collection is prepared. | It is **waiting for resources**; no progress claim is made while it is incomplete. |

The full aggregate record is the [dated evidence ledger](evidence.md).

## Experiment map

| Family | Question it tested | Outcome | Decision |
| --- | --- | --- | --- |
| CIAT / CRA | Do paired controls produce a dependable relative-advantage signal? | The held-out direction result was weak. | Retain as an audit primitive; do not train from it yet. |
| AFCR | Can axis-factorized ranking choose a useful correction direction? | Recommendations did not predict the observed direction. | Archive the global axis-ranking hypothesis. |
| BUCED / MACE | Can uncertainty-guided sampling or larger perturbations create useful new evidence? | Neither increased informative event density. | Stop expanding axes or magnitudes without a new causal trigger. |
| CST / SPARC / STAGE-CF / MSTE | Can stage, visual-progress, or transition signals identify useful intervention windows? | Pipelines ran, but evidence was small or did not generalize. | Keep measurement assets; stop threshold tuning. |
| GATE-V / ECDC / PACE | Can eligibility and disagreement rules justify extra evaluation? | Controls remained consistent, but terminal ranking evidence was absent. | Keep conservative selectors; do not claim terminal improvement. |

## Why this belongs in the portfolio

The useful result is not a claimed corrective VLA. It is the discipline to stop: establish paired controls, test the state-held-out split, publish negative results, and prevent an attractive offline signal from becoming an unsupported online capability claim.

## Reusable public reference core

The existing [ECDC pair selector](core/ecdc.py) and [PACE eligibility gate](core/pace.py) are small, dependency-free offline utilities. The detailed archive of earlier falsified ideas remains in the [exploration ledger](docs/exploration-ledger.md); it is linked rather than repeated here so the project page stays readable.

## Next evidence gate

A new collection may only change the project status after it satisfies the predeclared coverage and paired-control checks. Only then may a train-only critic prototype be evaluated against a state-held-out set. Any future policy or robot conclusion requires a separate guarded closed-loop evaluation.
