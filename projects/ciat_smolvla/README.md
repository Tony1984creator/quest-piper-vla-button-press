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

## Current snapshot — 2026-10-19

**New capability:** an observation-only learned recovery produced whole-task success on one failed simulation state without object geometry as an online input. Separately, real task-value training, candidate selection and native-flow gradient rollouts are now complete engineering stages. **Reliable net correction is still not established.**

| Stage | Completed result | Interpretation |
| --- | --- | --- |
| Observable recovery student | Fixed 24-branch pilot over four exposed states. Three student/mode combinations rescue the same failed state, but also damage successful controls; none has positive unconditional net gain. | Advances beyond privileged-teacher-only feasibility. Entry anchor/mode remain prescribed, not autonomous triggering or generalization. |
| Real task-value training | Four one-step value models, then four ten-step segment/no-action models; each 2,000 updates. Segment data: 2,353 deduplicated blocks, grouped train/validation. | Actual task-return-oriented value fitting, distinct from visual-dynamics loss and old critic studies. Q is not calibrated success probability. |
| Candidate selection | Thirty accepted simulation branches. Continuous Q selection and same-budget uniform selection each produce 2 recoveries/1 degradation on three exposed states. | Candidate support can help, but Q superiority is absent. Intervention duration and subsequent controller must match value labels. |
| Native-flow task-Q gradient | Twelve accepted rollouts: selection-only/ZeroQ preserve two successes; gradients and repeats all fail. Gradient vs selection: 0 recoveries/2 degradations. | Engineering integration works; local value ascent is not task benefit. Final Q rose at all 156 primary gradient queries. |
| Spatial-token value contrast | Full-token/pooled/no-action × two seeds: all six 468,805-parameter models completed 2,000 updates and CPU restore acceptance on the same 2,353 blocks. Full-token validation Bellman diagnostics are slightly lower than pooled for both seeds. | New offline representation evidence, not task benefit: model-dependent targets and untested rollout transfer prevent a policy-improvement claim. |

**Freshness:** research-workstation SSH is restored. This read-only check matched live report hashes to complete acceptance records for the student pilot, thirty-branch selection, twelve-gradient rollouts, and six-model token contrast. It did not rerun their tensor-level audits or simulations. mc509 still times out; no new physical robot result is inferred.

Read the [research rounds](docs/research-rounds.md) and [dated evidence ledger](evidence.md) for separate protocols and acceptance boundaries. All new outcomes are simulation, not physical robot results.

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

Keep engineering completion separate from measured utility. The fixed full-token/pooled/no-action training and CPU acceptance are complete; next assess whether its small offline diagnostic differences justify a separately frozen same-budget continuation test. Offline improvement alone cannot clear the correction-benefit gate. A fixed corrector needs real same-state intervention-versus-control outcomes before benefit-trigger learning; 544 diverged rollout queries are not 544 counterfactual labels. Observable recovery transfer and physical robot evaluation remain separately unverified.
