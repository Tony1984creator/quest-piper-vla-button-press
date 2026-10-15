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

## Current snapshot — 2026-10-15

**New result:** a failure-specific recovery teacher followed by the unchanged public actor rescued a failed development state under two fixed continuations. A second failed state required a different recovery pattern. This establishes **conditional recovery support in simulation**, not a deployable corrector or learned-Q gain.

| Question | Completed evidence | What it means |
| --- | --- | --- |
| Does faster feedback suffice? | Strict one-step feedback: 2 recoveries/1 degradation vs ten-step execution, across six states and twelve continuations; policy calls 500 → 4,732. | One state repeats recovery; cross-state admission criterion not met. Calls, not synchronized latency. |
| Is the public actor a reliable reference? | Natural Long 1/6 and Spatial 2/4 successes on different cohorts; a 16-branch same-prefix Spatial alternative test gave 0 recoveries/0 degradations. | Usable Spatial success/failure cases, not a stronger-policy claim. Neither old normalization nor projected caches transfer automatically. |
| Does recovery-specific support help? | Path teacher rescues one failed Spatial state under both fixed continuations; one successful state is harmed under the second. A new two-state/eight-branch comparison finds one straight-teacher rescue and no success-rate harm. | Concrete whole-task recoveries, but state-dependent choices and extra steps matter. All teacher actions consume the episode budget. |
| Can an observable student replace privileged teachers? | Eight actual teacher traces across four states; six lift the target. A grouped proprioception-only CPU pilot transfers poorly on key failures. | No deployable student yet. Visual cache collected 237 rows but awaits independent acceptance; no student rollout or task Q is claimed. |
| Earlier training and ablations | Real critic, behavior-prior and full-token dynamics training; event/replanning, execution-scope and bounded calibration studies are retained separately. | Predictive or fitting gains did not establish reliable net correction. See the dated history rather than pool protocols. |

The research workstation was directly reconnected. Recovery report/acceptance bindings, all 24 continuation trace hashes across three recovery studies, restored/zero/input snapshot bindings, and paired totals were checked read-only. The second workstation timed out; no new physical robot result is inferred.

Read the [research rounds](docs/research-rounds.md) for the route and [dated evidence ledger](evidence.md) for the compact result tables. Detailed older experiments remain available without crowding the current summary.

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

Validate observable recovery support before task-value Q or benefit-trigger learning. First independently accept the frozen-current-vision cache, then compare fixed visual/proprioceptive students with leave-one-initial-state-out grouping and no privileged online inputs. Only a separately audited student handoff can establish observable-policy corrective benefit in simulation. Preserve successful-control harm, all teacher costs, and the original positive and negative cases.
