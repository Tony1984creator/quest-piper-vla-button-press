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

## Current snapshot — 2026-11-02

**New VLA result:** a released author SmolVLA visual critic adapted to QGF guidance improves descriptive success from 17/120 to 23/120 in a fixed development comparison. A later five-condition study completes the visual-monitor + task-Q control loop, but does not establish stable trigger benefit. A controlled image-input replay now explains one pre-intervention action divergence, tightening what can be attributed to guidance.

| Track | Completed result | Interpretation |
| --- | --- | --- |
| PI0.5 custom-Q closure | Full 1,760-rollout coverage/data study and later controls retained. Separate scene-repaired 100-identity confirmation: natural 96, same-rule ZeroQ 98, Q seeds 98/97 successes. | Custom-Q integration ran, but no consistent increment over its stronger control. Do not merge these cohorts with SmolVLA. |
| Author VGAS + QGF | Matched 240 trajectories / 120 exposed task-init identities: ZeroQ 17 successes, QGF 23; 11 recoveries/5 harms, +5.0 pp; development 95% interval [−0.83,+10.83] pp. | Positive development signal, not stable/independent confirmation. This uses author TD+EGR visual-Q weights with a QGF inference adaptation, not Berkeley visual-IQL training. |
| Five-condition visual control | Separate 600-trajectory study: natural/replan/OGG/continuous-Q/visual-Q successes 18/17/18/23/19, each out of 120. | Visual anomaly triggering has not beaten continuous Q. Earlier 17-success controls are not reused in this new batch. |
| Cost versus performance | Visual triggering uses 7,190 vs 28,350 gradient steps (74.6% fewer), but 3,335 vs 2,835 policy queries and 719 interruptions. | Fewer gradient steps are not a measured total-latency or success-preserving efficiency gain. |
| Input-attribution diagnosis | 25/120 natural-versus-visual-Q trajectories diverge before the first alarm. In one fixed-input case, changing only six wrist-image uint8 channel values by one exactly reproduces the historical first-chunk difference. | That image intervention explains one action discrepancy, not all 25 cases or terminal success changes. All 600 outcomes remain retained. |

The November 2 read-only check independently recomputed the 240/600-study success and rescue/harm totals from stored pair records, verified the 600-summary hash linkage, and checked input-replay hash/repeat/nonimage invariance records. It did not rerun simulation, video decoding or tensor-level inference. mc509 still times out; no new physical robot result is inferred.

Read the [research rounds](docs/research-rounds.md) and [dated evidence ledger](evidence.md). Official QGF reference gains, Corrector public-data learning, earlier custom negative results and current author-model adaptations remain separate protocols.

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

Use shared real prefixes, observations and sampling noise to prove zero-intervention execution equivalence before adding the missing continuous-Q-plus-visual-interruption control. This separates guidance coverage from queue interruption. Do not delete mismatched cases, smooth images as a hidden fix, tune Q/thresholds, or retrain the author critic to improve these already-seen results. A finite mechanism comparison and subsequently frozen independent confirmation are still needed; no learned benefit-aware trigger or stable integrated-framework gain is claimed.
