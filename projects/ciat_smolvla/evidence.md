# Dated evidence ledger

**Reporting date:** 2026-10-02  
**Evidence level:** offline simulation probe

For the route → implementation → result → decision sequence, see [research rounds](docs/research-rounds.md). The table below groups completed measurements by study and should not be read as one combined benchmark.

## Current completed evidence — 2026-10-02

| Study | Verified observation | Decision |
| --- | --- | --- |
| Expected-benefit audit | 216/216 branches completed after bounded recovery; 96 matched pairs: 3 recoveries, 2 degradations, 91 ties. Development: 2/1; validation: 1/0; audit: 0/1. | A local rescue exists, but the net +1 across historical states does not establish a stable policy benefit or justify trigger training. |
| Critic self-score check | 23/24 anchors had a positive model-Q change, while anchor-mean outcomes included two positive and two negative cases. | Predicted Q increase is not a valid stand-in for measured intervention benefit. |
| Recoverability comparison | 120/120 branches and 96 three-way pairs audited; 7 pairs were rescued only by a fixed candidate, 2 only by Q guidance, and 1 by both. Q and the candidate each caused 2 degradations. | Alternative actions can recover some failed controls, but the candidate uses a different action displacement; this does not isolate a critic-training cause or prove a deployable policy. |
| Candidate-mode coverage | A separate 96/96 branch collection completed; the fixed candidate produced 6 recoveries, 3 degradations, 87 ties. | Additional action-mode coverage exposed recoveries and harms. The learned candidate-benefit selector did not beat a simple fixed-time rule on historical validation/audit states. |
| Temporal execution audit | The initial 52/52-branch comparison saw 2 recoveries and no degradations for longer first-plan execution, both at the same state and continuation noise. | A plausible local timing effect, not two independent confirmations. |
| New-noise temporal confirmation | 68/68 branches completed with 32 paired comparisons: zero recoveries, 3 degradations, 29 ties; two degradations in development and one in validation. | The earlier temporal rescue did not reproduce. Unconditional longer execution and a learned timing trigger are not supported. |
| Chunk-supervision inventory | 330 query-aligned windows; all 4 success rewards were in short-tail windows. | The inventory preserves duration and mask semantics. It is not TD/IQL training or proof that a new value target improves outcomes. |

These are offline simulation results on historical states. Branches sharing an initial state or control are not independent task trials. Model training and inference/execution checks are complete diagnostic stages; benefit-aware trigger training, independent new-state/task evaluation, and robot deployment remain unverified.

## Earlier evidence — 2026-09-28

| Stage | Completed evidence | What it establishes |
| --- | --- | --- |
| Training-data confirmation | 84/84 confirmation branches completed; expanded fitting used 144 training and 36 development-validation branches. | The expanded data gate passed; the September 24 waiting state is historical. |
| Real critic training | Nine fixed-budget diagnostic models were fit for 200 epochs each: linear, width-64 MLP, and action-free baseline, each with three seeds. | Real simulation supervision was used with frozen policy/state features. Training completion alone does not establish useful correction. |
| Retrained direction audit | Linear heads reached 4/5 non-tied validation directions, compared with 1/5 in the first fit; candidate selection had zero net benefit. | Better direction ranking did not translate into a positive candidate-selection result. Five pairs share controls and are concentrated in two development states. |
| Q-gradient execution | Real model finite-difference checks, ZeroQ equivalence, and nonzero action updates passed. | The gradient-to-action engineering path executes in simulation. It does not establish task improvement. |
| Local direction supervision | Six action-conditioned heads fit a local directional constraint; 6/6 corrected the one eligible training pair; 12 finite-difference checks passed. | A local fitting defect was repaired. There is only one eligible pair, so action/state generalization remains unproven. |
| Frozen-method flow comparison | 12/12 branches completed; all methods and controls succeeded in both groups; zero recoveries and zero degradations. | No failed control was available to test recovery; this is an execution and consistency result. |
| Failure coverage and replay | A conditional coverage audit observed one recovery and one degradation for the new MLP; four event replays passed. | The events were reproducible within that diagnostic selection protocol. They are not an overall success-rate estimate. |
| Fixed-noise confirmation | 28/28 branches completed over four fixed groups; each comparison method had zero recoveries, zero degradations, and four ties. | The earlier conditional benefit did not reproduce as a stable benefit under this follow-up. Only one control-failure opportunity was present. |

### What changed in the implementation

The supervision audit bound complete executed action traces to their recorded outcomes and input fingerprints. Close action pairs could still receive an incorrect learned direction after ordinary outcome and ranking losses. The next diagnostic therefore retained terminal-outcome and paired-ranking objectives and added a local constraint on the direction of the action gradient, restricted to eligible non-tied training pairs. The policy and state representation stayed frozen; fixed model seeds and budgets were used.

The local constraint repaired its observed training direction, but matched rollout comparisons have not established reliable task benefit. The next research question is whether **expected intervention benefit and risk can be predicted from information available before intervention**, using state-separated evaluation and repeated matched continuations.

### Pending work and source freshness

The expected-benefit collection, candidate-mode campaign, and temporal confirmation are complete as reported above. Benefit-aware trigger training and deployment remain unverified.

The research workstation was directly rechecked on October 2 using campaign status files and dated result reports. The second workstation was unreachable; no new robot result was inferred.

## Historical paired-audit gate — 2026-09-24

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

The project has demonstrated an offline auditing workflow and several negative findings. It has **not** demonstrated online Q-gradient inference, policy improvement, real-time operation, or robot-task success. The original confirmation collection was historically waiting for resources; recovery completed later and is reported above. Real critic fitting and simulated Q-gradient execution are complete diagnostic stages; stable policy benefit and robot-task success remain unverified.
