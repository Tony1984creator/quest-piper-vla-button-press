# VLA-Corrector research rounds

**Checked:** 2026-10-12. This page follows the decision order in the private project's research route, experiment registry, result reports, and completed campaign records. Each round changes a different question. Counts from different protocols must not be added into one success rate. For rounds 7–10, the current check uses local archived accepted reports; live workstations were unreachable.

| Round | Question | Implementation and fixed comparison | Observed result | Decision |
| --- | --- | --- | --- | --- |
| 0 · Counterfactual audit | Are same-state intervention labels and replay trustworthy? | Frozen policy, causal-prefix replay, paired controls, state-held-out audits; CIAT/CRA and later axis/stage pilots. | The protocol worked; informative terminal events were sparse and global axis ranking did not generalize. | Keep the audit machinery. Do not infer correction quality from a low prediction loss. |
| 1 · Real Q-to-action path | Can a trained critic gradient reach the action flow, and does local supervision repair its direction? | Complete confirmation data; fixed-budget critic fits; ZeroQ equivalence, finite differences, action-update checks, then matched flow. | 84/84 confirmation branches and nine initial models; retrained linear direction 4/5 on five non-tied development-validation pairs; six locally constrained heads corrected one eligible training pair. Action updates occurred, but the 12-branch flow comparison had no recovery opportunity. | Engineering path verified. Local fit and Q-score increase are not task benefit. |
| 2 · Expected intervention benefit | Does real Q guidance improve paired terminal outcomes across states and noise? | Frozen corrector; 8 exposed initial states, 24 fixed anchors, 4 matched continuations; 216-branch collection with separate development, validation, and audit groups. | 96 pairs: 3 recoveries, 2 degradations, 91 ties. Model-Q rose at 23/24 anchors, yet two anchors had negative mean outcome gain. | Real local rescues and harms are measurable. Supervision was too sparse for a learned benefit trigger. |
| 3A · Candidate coverage and selection | Are failed states recoverable by another policy-sampled action, and can a learned selector choose it? | Same-prefix Q versus fixed candidate versus control; then a second candidate-mode campaign and candidate-conditioned scoring against a simple fixed-time rule. | 120-branch comparison: 7 candidate-only recoveries, 2 Q-only, 1 both; each intervention also caused 2 degradations. The separate 96-branch candidate collection had 6 recoveries, 3 degradations, 87 ties. The learned selector did not surpass the fixed-time baseline on historical validation/audit states. | Action-mode coverage and scoring are distinct bottlenecks. The fixed candidate used a different displacement, so this is not an equal-radius critic ablation. |
| 3B · Execution timing | Does continuing the first plan longer help compared with replanning after ten steps? | 52-branch first-pass comparison; independent fixed new-noise follow-up with 68 branches and 32 pairs. | First pass: 2 recoveries, 0 degradations, both from one state and one continuation-noise opportunity. Follow-up: 0 recoveries, 3 degradations, 29 ties. | The positive timing event did not reproduce. Do not extend the plan unconditionally or train a timing gate from these labels. |
| 4 · Value-data semantics and cross-task foundation | Can a new collection preserve the fields needed for chunk value learning, and can the same frozen policy run another task? | Query-aligned inventory; hash-bound factual corpus; two-task natural-policy development pilot; first-fragment semantic collection and four-way paired pilot. | 100 historical episodes from 50 distinct initial states yielded 3,139 time-correlated windows; 65 of 74 positive windows were short tails. Natural policy: 2/5 and 3/5 successes in two tasks. A five-trajectory semantic rerun matched source trajectory hashes; 182/184 executed chunks met the local field contract, with 2 unknown budget boundaries. Four paired groups were all-success or all-failure, giving no corrective gain label. | Natural cross-task execution and first-fragment semantics are verified. Full counterfactual chunk transitions, equal inference budget, independent correction benefit, and trigger-training support are still missing. |
| 5 · Persistent proposal scope | Does a first-fragment substitution differ from continued policy resampling? | Frozen policy, Q disabled; same-prefix first-fragment versus persistent proposals with predeclared new schedules. Stage entry uses offline simulator truth. | Task0: 12 configurations; persistent proposals rescued one failed state under two schedules, whereas first-fragment proposals rescued none. Task2: 12 branches; first-fragment 0 recoveries/0 degradations, persistent 0 recoveries/1 degradation. | A local scope effect exists, but persistent resampling is not a reliable corrector across tasks. Repair replay infrastructure before attributing an execution failure to the algorithm. |
| 6 · Learned behavior-supported proposals | Can actual feature/action training create better corrective candidates without changing Q or intervention duration? | Two small flow generators, with/without state conditioning; fixed successful training windows; one ten-step proposal followed by the same frozen policy and continuation-noise clock. | Training and numerical sampling completed. Formal 48-branch matrix: conditional generator 2 recoveries/4 degradations/10 ties; unconditional 0/12/4. Each generator has 16 paired comparisons across eight exposed initial states. | Conditioning improves this comparison against the unconditional prior, not against the original policy. Conditional recovery occurs in two distinct states but only one of two schedules in each; net benefit remains negative. No Q or learned trigger was evaluated. |
| 7 · Visual-dynamics supervision | Does executed action scope carry predictive information once full visual tokens and demonstration identity are restored? | 450 demonstration caches; single-action, ten-action segment, and no-action predictors; two seeds; fixed pilot and one declared budget recheck. | Six models completed at 1,000 updates, then six at 10,000. Segment beats no-action on validation and Long audit; action permutation worsens predictions, while out-of-distribution increment conflicts across seeds. | Actual predictive training is complete. Visual-dynamics information is not a task-value Q or a corrective success claim. |
| 8 · Causal event correction | Is apparent recovery caused by event-triggered replanning or by a latent-recovery gradient? | Native-flow and Zero checks; full natural/shadow equivalence; causal history-based reference events; three-task, nine-state, two-predictor-seed, five-branch cohort. | 90 completed branches: replanning versus natural 3 recoveries/2 degradations; single gradient versus replanning 1/1; segment gradient versus replanning 0/0. | Replanning explains the repeated natural recovery. No repeated gradient increment across predictor seeds; reference anomaly events are not learned benefit triggers. |
| 9 · Prediction-based execution boundary | Can the current predicted action chunk choose a useful observation-update boundary without an oracle stage? | Fixed ten-step, full fifty-step, and predicted-gripper-boundary modes; 36-episode development study followed by frozen 24-episode metadata-new follow-up. | Development boundary: 5 recoveries/3 degradations; follow-up: 0/5. Full fifty-step: development 3/3, follow-up 1/3. | Execution scope changes outcomes, but the development net +2 did not reproduce. Stop like-for-like duration/threshold scans; no Q or trigger attribution. |
| 10 · Local action-response calibration | Why does reasonable overall visual prediction fail to support reliable corrective gradients? | First-event target/effect diagnostics; 2,376 deduplicated deployment windows; original frozen backbone with a copied 18,176-parameter action projection; factual-only versus factual-plus-secant losses, two seeds. | Overall predictor beats zero delta in 45/60 rows per scope, but same-scope response direction matches only 7/15 and 5/15 pairs. Four 1,000-update calibrations complete; confirmation response gains are unreliable. | Separate overall prediction from action-difference sensitivity. Small loss improvements do not justify a calibrated-gradient rollout, new task Q, or learned trigger. |

## How the rounds connect

Round 0 supplies the identity and paired-control contract. Round 1 makes Q guidance executable. Round 2 tests its actual outcome rather than its own score. Round 3 splits the failure into candidate coverage/selection and execution timing; these are separate hypotheses, not new names for the same model. Round 4 changes the data contract so later value learning can use executed action duration, rewards, next representation, and termination boundaries without inventing missing fields. It is a new foundation study, not a successful Q-correction trial.

Rounds 5 and 6 follow a different route from the earlier Q-gradient studies: first test the scope of a policy-sampled intervention, then train a new candidate source. Neither result is credited to Q. The round numbers are a reading aid, not the private route's R0–R4 acceptance gates. Under those gates, replay execution is established, but reliable benefit prediction, learned trigger evaluation, independent task/state confirmation, and robot deployment are not complete.

## Round 4 acceptance detail

The historical corpus contains two groups of 50 trajectories but only 50 distinct initial states because one group repeats 25 initial states under two policy seeds. Its 3,139 windows overlap in time; they are not independent trials. Most positive rewards lie in short final chunks, so dropping incomplete ten-step windows would discard the success signal. Historical terminal flags merge several boundary causes, and old counterfactual records do not contain reward and next-representation fields aligned to the same executed duration. This corpus can be audited and reused as a baseline, but cannot be relabeled as ready-made TD/IQL supervision.

The new natural-trajectory proof covers five exposed development initial states and checks the source trajectories exactly. A first-fragment four-way pilot compared historical first action, fresh replan, ZeroQ, and Q under matched later noise. Two groups failed under all four choices; two succeeded under all four. Only the first executed fragment had the full semantic fields, while the rest of the trajectory lacked a complete per-fragment value record; inference budgets across branches were also not equalized. The reviewed training gate excluded all three distinct initial states and reported **not ready**. No benefit-trigger model was trained from this pilot.

## Round 5: scope, replication, and simulator restoration

The Task0 replication holds the first ten actions exactly equal in six first-fragment/persistent pairs; divergence begins with action eleven. Three exposed development states and two new proposal schedules give twelve configurations. Both persistent rescues belong to the **same failed initial state**, not two independent states. The two already-successful states remained successful under both schedules. The persistent mode did not train a new action distribution, and stage entry was an offline oracle rather than a learned trigger; no stage-exit mechanism was tested in this Task0 comparison.

Task2 is a separate two-state, two-schedule, three-mode comparison. Its persistent proposal produced no recovery and one degradation. The successful control repeated its binary result but completed in 225 versus 234 steps, so this is not a step-deterministic intervention-effect proof. A failed replay gate was diagnosed rather than relabeled as a policy failure: terminal reset had modified simulator model arrays outside the flattened physics state. Restoring those arrays before state restoration/forward repaired the factual suffix check. The completed first state was retained; only the blocked second state was resumed. The two initial states bind different implementation versions, while comparisons within each state are version-consistent.

## Round 6: training → sampling → matched simulation

**Training.** The audited 100-episode corpus is grouped by initial state into 30 training, 10 validation, and 10 audit states; multiple policy seeds of one state never cross groups. Only 1,457 successful training query windows supply imitation targets and normalization statistics. Both generators have 38,854 parameters and receive 1,000 optimizer updates. The recorded CPU single-thread run takes 16.78 seconds including source audit, training, and evaluation; this is not a GPU training or deployment-latency benchmark. The original SmolVLA weights remain frozen.

| Generator | Validation mean imitation-flow loss by initial state | Audit mean imitation-flow loss by initial state |
| --- | ---: | ---: |
| Unconditional | 1.0081 | 1.0671 |
| State-conditioned | 0.9420 | 0.9322 |

These are standardized velocity-field imitation losses, not terminal value or success metrics. Both trained models were retained without selecting a model seed or training duration from these results. Checkpoint reload matched a fixed numerical probe exactly. Sixteen feature-conditioned candidate smokes produced finite normalized 10×7 chunks; that check alone executed no environment actions.

**Simulation inference.** The formal completed matrix covers eight training-excluded but previously exposed states, two proposal seeds, and three branches: original policy, unconditional prior, conditional prior. Exactly one ten-step candidate replaces the anchor chunk; later queries return to the original policy with shared fixed noise. Actions pass the original normalization-to-environment conversion. The 48 branch traces and paired summary hashes were rechecked during this portfolio audit, along with common source/training identity bindings. The queue also checked trace lengths, final boundaries, and shared continuation noise before marking complete. An earlier six-branch development case is retained privately but excluded from this formal same-version matrix after source-binding repairs.

| Comparison against original | Recoveries | Degradations | Ties | Successful branches / 16 |
| --- | ---: | ---: | ---: | ---: |
| Original control | — | — | — | 12 |
| Unconditional prior | 0 | 12 | 4 | 0 |
| State-conditioned prior | 2 | 4 | 10 | 10 |

The two conditional recoveries come from two distinct failed states, with one successful schedule and one failure in each. Its four degradations come from two successful states under both schedules. Thus lower imitation loss and better results than the unconditional prior **do not establish positive net benefit over the original policy**. Historical labels are not the controls: one historically failed trajectory's new original continuation succeeded. The fixed new continuation clock is not an exact replay of the historical natural suffix. No Bellman/Q training, flow-Q guidance, learned trigger, independent final test, or physical robot result is claimed.

**Next gate.** Audit corrective action support and protection of successful policy behavior before adding more critic capacity or a trigger. A new fixed comparison must demonstrate repeatable net recovery across state-separated coverage while retaining harm counts. Successful factual imitation is not itself corrective expertise; missing original video assets are not replaced by claiming the feature/action corpus is the full demonstration dataset.

## Rounds 7–10: October 6–11 continuation

**Source freshness.** These completed stages are supported by local archived dated reports and acceptance JSON copied from the research project. During the October 12 check, both workstations timed out. Report hashes and archive-to-acceptance bindings were checked locally; the raw remote trajectories, current jobs, and model files could not be independently re-read this time. Completion below refers to those archived accepted runs, not a new live-server verification. The last local workflow mentions a strict-feedback reference launch, but no completed result is available here; it remains unreported as an outcome.

### Round 7: restore full-token supervision before interpreting gradients

The restored demonstration cache contains 450 episodes / 110,372 frames, split as 300 training, 39 validation, 40 Long-audit, and 71 other-task audit episodes. A later asset check clarified that only **379 of the 450 are Long demonstrations**; all 379 overlap the saved original-policy training configuration. Corrector holdout is therefore not proof of original-policy-unseen data. The larger source dataset contains 1,693 episodes across 40 task groups, but that inventory is not a claim that all were cached or trained in this study. Task routing must match dataset language/identity, not assume simulator task integers are dataset indices.

The implementation replaced the old compact feature-only shortcut with full visual-token/history and actual normalized executed-action contracts. Three predictor scopes—single 7D action, ten-step 70D segment, and no action—each used two fixed seeds, matched samples and validation-only selection. The six 1,000-update pilot models completed; a single predeclared 10,000-update recheck also completed with 40 validation checkpoints per model and selection at update 9,500. The first 1,000-update prefix matched the original records. This is visual-dynamics supervision, not Bellman/terminal-value training.

| Pilot episode-macro MSE difference | Seed A | Seed B |
| --- | ---: | ---: |
| Validation: segment minus single | −0.005336 | −0.003821 |
| Validation: segment minus no action | −0.020012 | −0.018925 |
| Long audit: segment minus no action | −0.013581 | −0.013602 |
| Long audit: permuted-action penalty | +0.037789 | +0.038034 |
| Other-task audit: segment minus no action | +0.018868 | −0.009729 |

The numerical differences above belong to the **1,000-update pilot**, not the 10,000-update recheck. Negative differences indicate prediction improvement; permutation penalties indicate action information. The longer-budget audit retained the validation segment preference but not consistent other-task benefit. No further capacity/budget search was justified by these results.

### Round 8: causal events, replanning controls, and real simulated guidance

Native sampling hooks verified zero-scale equivalence, nonzero denoising gradients, correct action/time scope, and unchanged original policy/predictor parameters. Full natural-versus-shadow traces then checked observation, actual command, noise, reward, and boundary identity; independent scoring recomputed the causal-history monitor outputs. Monitoring without intervention was tested separately from correction.

A fixed event cohort covers three tasks, nine exposed development states and two **predictor-training** seeds, not eighteen independent states or independent policy-continuation replicas. Five branches per combination are natural execution, event-truncated replanning, zero guidance, single-action dynamics guidance, and segment guidance. The archived acceptance covers all eighteen combinations / ninety branches.

| Comparison | Recoveries | Degradations | Net count |
| --- | ---: | ---: | ---: |
| Replanning versus natural | 3 | 2 | +1 |
| Single-action gradient versus natural | 2 | 1 | +1 |
| Segment gradient versus natural | 3 | 2 | +1 |
| Single-action gradient versus replanning | 1 | 1 | 0 |
| Segment gradient versus replanning | 0 | 0 | 0 |

The natural recovery that repeats across predictor seeds is already achieved by replanning. No gradient increment repeats across those seeds. Three combinations had no reference event and remain separately natural-equivalent, not evidence that a corrective candidate could not exist. Executed guidance logs support actual nonzero gradient calls, so the null incremental result is not explained by an unused hook. Resource interruptions were preserved and resumed with separate operational-source bindings rather than counted as algorithm failures.

These are online-in-the-simulator causal events, **not robot deployment or a learned benefit trigger**. The objective is latent visual recovery, not task-value Q. A separate task's strict visual identity check had rendering drift despite physical-state agreement; that blocked capture is not a correction failure and was not silently admitted.

### Round 9: execution scope has local positive cases and failed confirmation

This round replaces the earlier oracle-stage entry with a rule using the **current predicted gripper command**. It records the full fifty-step prediction, postprocessed environment commands, selected/actual duration, next observation, and termination separately. The environment uses incremental control, so position-style adjacent-command differences are not assumed to be motion velocity. Future executed actions and simulator stage truth are not used for boundary selection.

| Study and mode | Successful case-seed branches | Recoveries vs fixed ten-step | Degradations vs fixed ten-step |
| --- | ---: | ---: | ---: |
| Six-state development: fixed ten-step | 5/12 | — | — |
| Six-state development: full fifty-step | 5/12 | 3 | 3 |
| Six-state development: predicted-gripper boundary | 7/12 | 5 | 3 |
| Four-state follow-up: fixed ten-step | 5/8 | — | — |
| Four-state follow-up: full fifty-step | 3/8 | 1 | 3 |
| Four-state follow-up: predicted-gripper boundary | 0/8 | 0 | 5 |

The development boundary rule has repeated recoveries in two states but also repeated damage. Its net +2 did not survive the frozen follow-up; the boundary rule's net is −5 there. Follow-up states are new to the inspected metadata, not a formal independent final holdout or proof that the original policy never saw them. Query-ordinal noise is bound consistently, but changing query frequency does not give identical noise at every environment step. A 520-step/52-query fixed-mode fidelity gate was archived as exact; it is an engineering gate, not positive efficacy.

### Round 10: diagnose action sensitivity rather than optimize aggregate loss

Offline first-event diagnostics reuse eighteen parent cases; three have no event. Fifteen events × four real branches × two predictors produce 120 metric rows / 90 comparisons. Recovery targets align positively with observed future change, so a universal target-sign reversal is not supported. Future observations enter **offline diagnosis only**, not intervention-time decisions.

Both predictor scopes beat zero-delta prediction in 45/60 rows. Yet the same-scope single and segment comparisons agree with actual local recovery direction in only 7/15 and 5/15 pairs, with near-zero action-effect-difference cosine. This identifies a difference between overall prediction information and sensitivity to a small action change, without proving a unique failure cause.

Deployment-trajectory inventory covers sixty accepted trajectories / ten exposed states. From 2,514 complete windows, deduplication yields 2,376 windows and twenty distinct shared-prefix candidate/control pairs, with no identical-input target conflicts. States are split 5 training / 3 validation / 2 development confirmation. Only a copied action projection has 18,176 trainable parameters; the original backbone and policy stay frozen. Factual-only and factual-plus-secant calibration each run under two seeds for 1,000 updates. Validation selects checkpoints; confirmation is report-only.

| Calibration | Validation action-difference MSE: original → selected | Confirmation: original → selected |
| --- | ---: | ---: |
| Seed A, factual | 1.479203 → 1.479133 | 2.150805 → 2.150527 |
| Seed A, factual + secant | 1.479203 → 1.478794 | 2.150805 → 2.150885 |
| Seed B, factual | 1.487977 → 1.487046 | 2.153715 → 2.156589 |
| Seed B, factual + secant | 1.487977 → 1.487166 | 2.153715 → 2.154898 |

The archived CPU verification recomputes forty held-out pair metrics within tolerance and verifies the frozen backbone; the provenance report checks 122 input/source bindings and four selected weights. Confirmation action-effect cosine did not improve on average, and recovery-direction counts remained 3/4. No calibrated-gradient task rollout is reported. Peak memory for **this cached small calibration training only** was 122.898 MiB allocated / 148 MiB reserved; it is not full VLA inference memory or end-to-end latency. Host sampling timers without explicit CUDA synchronization are not deployment latency measurements.

### Current gate and outcomes worth retaining

The useful deliverables are real predictive training, causal monitor/execution identity, explicit replanning-versus-gradient ablations, positive-and-negative execution-scope confirmation, and a locally audited low-capacity calibration. None establishes reliable net corrective benefit. The current gate remains a repeatable corrective baseline; scope diagnostics are partial, while new task-value Q and learned benefit-trigger training remain unapproved by the evidence gates. A strict stepwise-feedback reference is the next declared structural comparison; its last archived launch is not a completed result. Do not append more seeds, thresholds, or capacity searches just to recover a positive number.

## Public evidence boundary

All outcomes here are offline simulation studies. A rescue in an exposed state demonstrates a specific paired outcome, not an independent held-out success rate. The two-task natural pilot tests portability of the frozen policy interface, not cross-task correction. No result on this page measures real robot performance.
