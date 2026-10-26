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

## Current snapshot — 2026-10-26

The project has moved from custom SmolVLA diagnostics to **separate, source-pinned official-baseline reproductions**. The new positive result is QGF guidance in its supported cube-triple setting; the VLA-Corrector line has completed public-data training and native inference/control checks, but has not established reliable task improvement. These are not yet an integrated VLA + task-Q + learned-trigger system.

| Track | Completed evidence | Boundary |
| --- | --- | --- |
| Official QGF configurations | Three 500,000-update runs on the full 100M public corpus. Final preset guidance succeeds 30/30, 27/30, 29/30 versus unguided 0/30, 2/30, 0/30. | Two task goals in one cube-triple layout, three task/seed configurations; not full-paper coverage, strict same-init pairing, or VLA integration. |
| Public-data VLA-Corrector training | 1,693 episodes / 273,465 frames / 40 task groups; 1,355/169/169 episode split. A 42.51M-parameter native MLP completes 30 epochs; selected validation cosine loss 0.322989. | Official-code method self-training on public data, not reproduction of the author's unknown exact training assets or paper numbers. |
| Does the predictor use actions? | Complete 169-episode / 26,104-pair validation diagnostic: actual-action cosine loss 0.322989 vs misaligned-action 0.444053; both cosine and MSE improve in every episode. | Demonstrates predictive action information, not corrective task value or success gain. |
| Native PI0.5 inference and OGG | Diagnosed duplicate language scaling; fixed-sample full-reference action error falls to 3.13e-7. Six truncation/OGG rollouts all succeed on three already-successful natural controls. | Compatibility and real gradient execution are verified. OGG is faster than truncation in one case and slower in two; no recovery opportunity or stable increment demonstrated. |
| Earlier custom task-Q work | First-event replanning gives 1 recovery/0 harms over nine exposed states. Matched first-event Q gradient adds 0 recoveries/1 harm; return/state ablations fail heldout selection. | Retain the useful simple baseline and negative ablations; do not pool them with official QGF or newly trained Corrector results. |

The October 26 check re-read live acceptance records for the official runs, recomputed validation episode counts/weighted diagnostics, and checked five earlier campaign report/acceptance hashes. It did not repeat full raw-tensor audits or retrain models. mc509 remains unreachable; no new physical robot outcome is inferred.

Read the [research rounds](docs/research-rounds.md) for the separated routes and [dated evidence ledger](evidence.md) for results. No raw data, private control code or model weights are published.

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

Complete the frozen multi-task PI0.5 natural cohort and audit its real task/init identities before comparing native truncation and OGG on matching identities/noise. The 120-identity natural batch is in progress, not a completed correction benchmark; the 240 correction conditions have not started. Only after the two official lines have separately established their applicable evidence should shared-VLA task-Q/trigger integration be evaluated. Episode counts, independent initial states and repeat evaluations remain separate.
