# Dated evidence ledger

**Reporting date:** 2026-10-19  
**Evidence level:** offline simulation probe

For the route → implementation → result → decision sequence, see [research rounds](docs/research-rounds.md). The table below groups completed measurements by study and should not be read as one combined benchmark.

## Current completed evidence — 2026-10-19

**New positive result:** a learned current-observation-only recovery reaches whole-task success on one failed simulation state. **New limiting result:** real task-Q gradients increase their own score but worsen the tested selected controller's outcomes. These are separate protocols, not contradictory measurements of one method.

| Stage | Completed evidence | Boundary |
| --- | --- | --- |
| Observable student | Archived fixed 24-branch pilot: proprio straight 1 rescue/2 harms; visual straight 1/2; proprio path 1/1; visual path 0/2. All rescues share one of four exposed states. | No object truth as online input; entry/mode still prescribed. Neither positive unconditional net gain nor autonomous triggering. |
| One-step task-value training | 14,339 deduplicated transitions from ninety old branches; four action/no-action × seed models, each 2,000 updates. | Real partial-observation IQL-style development fitting, not calibrated success probability or policy benefit. |
| Ten-step task-value training | 2,353 deduplicated blocks, grouped 1,183 train / 1,170 validation; four segment/no-action models, each 2,000 updates. | Action, duration and subsequent-policy semantics matter. Fitting and nonzero gradients alone do not establish usable action ranking. |
| Candidate-selection simulation | Thirty accepted branches; Q and same-budget uniform each 2 recoveries/1 degradation on three exposed states. | Candidate opportunity exists; Q superiority does not. Native fork labels cannot be silently used for sustained-Q control. |
| Real task-Q flow and outcomes | Probe completes native ZeroQ/coordinate/tail protection checks. Twelve full rollouts then give gradient vs selection 0 recoveries/2 degradations, with exact repeats. | All 156 primary gradient queries raise final self-Q. This is negative utility despite working engineering, not a trigger-learning success. |
| Current label boundary | Twelve rollouts contain 544 queries / 5,416 environment steps but only three initial-state full-controller comparisons, without positive gradient increments. | Not 544 independent keyframe counterfactual benefit labels; no effective learned trigger claimed. |

**Verification on the restored-access check:** live report SHA256 values match completed acceptance records for the student pilot, thirty-branch selection, twelve-rollout gradient campaign and six-model token contrast. Summaries preserve negative benefit/trigger gate flags. This is a fresh report-integrity check, not a repeated raw-tensor replay, checkpoint reload or new simulation. Research-workstation SSH works; mc509 still times out.

The archived student result describes its original independent raw-command audit; that audit was not rerun here. The spatial-token value comparison is now complete: six 468,805-parameter models, each 2,000 updates on the same 2,353 blocks, with exact CPU restoration recorded for all six. Full-token validation group-mean Bellman diagnostics are 0.018193/0.018048 versus pooled 0.019574/0.018726 for the two seeds. These model-specific-target errors are offline diagnostics, not a common-target policy-value or task-success comparison. No new rollout or trigger result is available. See [research rounds](docs/research-rounds.md) for protocol separation.

## Previously checked evidence — 2026-10-15

**Most useful new finding:** failure-specific recovery support can restore whole-task completion, but the useful recovery differs by state. This is a privileged offline-teacher feasibility result, not a learned-Q, trigger, or physical deployment result.

| Study | Measured result | Decision |
| --- | --- | --- |
| Strict feedback, now complete | H1 vs H10: 2 recoveries/1 degradation over twelve continuations from six states. Calls 500 → 4,732; recovery repeats in one state only. | Close this finite configuration: positive local signal, insufficient cross-state admission evidence. Call counts are not GPU latency. |
| Public-policy references | Natural Long 1/6 and Spatial 2/4 on different cohorts. Sixteen same-prefix Spatial branches: alternatives each 0 recoveries/0 degradations. | Reference suitability and opportunity checks, not policy improvement; stop the continuation grid and investigate missing grasp support. |
| Path recovery + original public actor | Old two-state cohort: first continuation 1 rescue/0 harms; fixed second continuation 1/1. Same failed state rescued twice; old successful state harmed once. | Repeated conditional whole-task recovery, not two independent failed states or unconditional benefit. Straight teacher also caused one harm in the first comparison. |
| Additional recovery cohort | Two predeclared states / eight accepted branches. New failed state: straight recovery succeeds in 139 total steps, native/repeat/path fail. Successful state: native 71, straight 135, path 192 steps. | Straight 1 rescue/0 harms; path 0/0. New support contrast, with extra cost and only one continuation. Do not pool old and new protocols. |
| Observable-student feasibility | Eight teacher traces / four initial-state groups, six lifting traces; stride-three sampling gives 237 total / 170 lifting rows. Fixed grouped proprioceptive CPU fits transfer poorly on key failed-state groups. | No released student. Current visual cache collected 237 rows but is not independently accepted; no visual-student training or rollout efficacy claim. |
| Fresh read-only verification | Live report-to-acceptance bindings for three recovery studies; all 24 actor trace hashes, child report/restoration/zero-pair/anchor bindings, and recomputed rescue/harm counts checked. Strict-feedback report binding also checked. | Binary/source integrity and numerical pair totals verified, not a new full tensor-level replay or simulation rerun. |

The research workstation was directly reachable on October 15; mc509 still timed out. Teachers use simulator geometry offline and consume the same 280-step episode budget. Lift/primitive competence, terminal task success, imitation error, and intervention cost remain separate. No raw demonstrations, weights, device settings, or control code were published.

See [rounds 11–13](docs/research-rounds.md#rounds-1113-feedback--reference-policy--recovery-support) for concise route decisions, paired outcomes and student-readiness boundaries.

## Previously checked evidence — 2026-10-12

**Freshness:** both SSH targets timed out on this check. The new entries below are based on local archived completed reports from October 6–11, not a new live-server read. Report SHA256 values were recomputed locally and matched the structural/follow-up acceptance bindings, event conclusion, and calibration verification records. The remote raw trajectories and weights were not accessible; their original full audits are described as archived acceptance, not re-performed today.

| Study | Archived completed measurement | Evidence decision |
| --- | --- | --- |
| Full-token supervision | 450 cached demonstrations / 110,372 frames; single-action, ten-action-segment, no-action scopes × two seeds. Six 1,000-update pilots followed by one declared six-model 10,000-update recheck, selected at update 9,500. | Segment prediction adds action information on validation/Long audit; other-task increments conflict. Not task Q or corrective success. |
| Dataset identity correction | Cache = 379 Long plus 71 other-task episodes, not 450 Long demonstrations. The 379 Long episodes overlap saved original-policy training configuration. | Corrector held-out split does not establish original-policy-unseen evaluation; dataset indices must be matched by identity rather than simulator integer. |
| Native flow and causal-history checks | Real sampler hook, zero-scale equivalence, nonzero denoising gradient, unchanged original weights, natural/shadow identity and independently recomputed history scores are recorded in completed probes. | Establishes simulated wiring and causal monitoring; not physical robot inference, terminal gain, or learned triggering. |
| Fixed event cohort | Eighteen accepted combinations / ninety branches across three tasks and nine exposed states. Replanning vs natural: 3 recoveries/2 degradations; single gradient vs replanning: 1/1; segment: 0/0. | Repeated natural recovery is already achieved by replanning. No repeated incremental gradient rescue; two predictor seeds are not independent rollout replicas. |
| Prediction-based boundary development | Thirty-six accepted episodes across six states: fixed ten-step/full fifty-step/gripper boundary successes 5/12, 5/12, 7/12. Boundary vs fixed: 5 recoveries/3 degradations. | Local net +2 with both repeated rescue and repeated harm; not a task-Q or oracle-stage result. |
| Frozen boundary follow-up | Twenty-four accepted episodes across four metadata-new states: successes 5/8, 3/8, 0/8. Full fifty-step vs fixed: 1 recovery/3 degradations; boundary: 0/5. | Positive development signal failed confirmation. Metadata-new is not a formal final holdout or policy-unseen proof. |
| Target/action-effect diagnosis | Eighteen parents, three without an event; 120 rows / ninety comparisons. Each predictor beats zero delta in 45/60 rows; same-scope local response direction agrees in 7/15 and 5/15 pairs. | Overall predictive information and action-difference sensitivity are distinct. Universal target-sign reversal is not supported; unique root cause remains unproven. |
| Bounded calibration training | Sixty deployment trajectories / ten states; 2,514 windows deduplicated to 2,376, with twenty distinct shared-prefix pairs. Four 1,000-update fits; only copied action projection has 18,176 trainable parameters. | Small prediction-loss changes do not provide reliable local response confirmation. Original models stay frozen; calibrated-gradient task rollout not reported. |
| Calibration provenance | Archived verification: 122 input/source bindings and four selected weights; forty held-out pair metrics independently CPU-recomputed within tolerance, backbone unchanged. Local report/hash linkage rechecked today. | This check does not reload remote weights or repeat raw-trajectory audits. Calibration peak 122.898 MiB allocated / 148 MiB reserved is not full-VLA memory or deployment latency. |

The [new research rounds](docs/research-rounds.md#rounds-710-october-611-continuation) keep predictive training, causal events, execution scope, and response calibration as distinct routes. A strict-feedback reference was only launched in the latest local workflow; absent a completed acceptance record, no result or current-running claim is published. Task-value Q, learned benefit-trigger training, independent final validation, and robot correction remain unverified.

## Previously checked evidence — 2026-10-06

| Study | Verified observation | Decision |
| --- | --- | --- |
| Task0 scope replication | Twelve configurations across three exposed states and two predeclared schedules. First-fragment: 0 recoveries/0 degradations; persistent: 2/0 across six comparisons per mode. | Both recoveries belong to one failed state. The first ten paired actions match exactly; persistent resampling is a local scope signal, not a new trained policy or Q result. |
| Task2 scope transfer | Twelve branches across two states, two schedules, and three modes. First-fragment: 0 recoveries/0 degradations; persistent: 0/1. | No cross-task correction benefit. Successful controls ended in 225 and 234 steps, excluding a deterministic full-trajectory claim. |
| Simulator restoration repair | Terminal reset changed model arrays outside the flattened physical state. Restoring these arrays repaired the factual suffix check; only the blocked state was resumed. | Distinguishes infrastructure failure from policy failure. Per-state comparisons are source-bound; the merged two-state matrix contains two implementation versions. |
| Actual behavior-prior training | Two 38,854-parameter flow models, each 1,000 optimizer updates; 1,457 successful training windows from the 100-episode audited corpus. CPU single-thread run: 16.78 seconds including audit and evaluation. | Frozen original policy; state-grouped splits and training-only normalization. This is feature/action imitation, not full video/action-expert finetuning or RL. |
| Imitation and sampling checks | Conditional versus unconditional validation loss: 0.9420 versus 1.0081; audit: 0.9322 versus 1.0671. Reload probe matched; 16 finite normalized 10×7 candidates. | Better imitation diagnostics are not terminal benefit; numerical sampling alone did not execute environment actions. |
| Formal learned-source matrix | Completed 48 branches: eight exposed training-excluded states × two seeds × three modes. Conditional: 2 recoveries/4 degradations/10 ties; unconditional: 0/12/4. Original, conditional, unconditional successes: 12/16, 10/16, 0/16. | Conditional proposals rescued two distinct states at one seed each, but damaged two states at both seeds. Net outcome remains worse than original; no Q, trigger, generalization, or robot claim. |
| Matrix provenance check | Summary hash, all 48 trace hashes, six-branch uniqueness per state, source/training identity bindings, and recomputed pair totals checked against completed records. | Earlier six-branch source-incomplete development case is excluded, not silently pooled with the formal matrix. Runtime queue separately audited trace lengths and shared continuation noise. |

The detailed route, training split, loss semantics, action conversion, and continuation-clock boundaries are recorded once in [rounds 5–6](docs/research-rounds.md#round-5-scope-replication-and-simulator-restoration). The small prior references flow behavior modeling but does not reproduce a full flow-Q-learning algorithm.

The research workstation was directly checked during the October 5 heartbeat, completed on October 6 local time. The second workstation again timed out; no new physical robot or dataset result was inferred. Only read-only checks were run; no experiment was started, resumed, or modified.

## Previous completed evidence — 2026-10-02

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

The expected-benefit collection, candidate-mode campaign, and temporal confirmation are complete as reported above. The newer scope and behavior-prior studies are separate rounds documented at the top of this page. Benefit-aware trigger training and deployment remain unverified.

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
