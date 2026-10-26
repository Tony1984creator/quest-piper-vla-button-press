# VLA-Corrector research rounds

**Checked:** 2026-10-26. Distinct rounds/protocols must not be pooled. The latest route separately reproduces official QGF and public-data VLA-Corrector, retaining all custom SmolVLA evidence below. Live acceptance and numerical-summary checks are described in the dated ledger; no experiments were started by this monitor.

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
| 11 · Strict-feedback closure | Is stepwise observation/replanning enough? | Twelve H1 episodes plus one H10 parity gate; reuse twelve sealed H10 controls. | H1 6/12 vs H10 5/12; 2 recoveries/1 degradation, repeated recovery in only one state; 9.46× policy calls. | Positive local signal, insufficient cross-state support. Close this configuration, not a universal impossibility claim. |
| 12 · Separate public-policy reference | Does a distinct frozen public actor offer a useful task condition? | Finite Long and Spatial natural references; then sixteen same-live-prefix native/repeat/single/sustained branches. | Long 1/6, Spatial 2/4 on different cohorts; opportunity matrix 0 recoveries/0 degradations. | Retain credible Spatial failures/successes; inspect missing grasp support instead of repeating noise/duration scans. |
| 13 · Failure-specific recovery support | Can a measured recovery maneuver repair an actual visited failure before handing control back? | Privileged straight/path teachers, full budget accounting, two fixed continuations on old states, then two predeclared additional states. | Path repeats whole-task rescue in one failed state but harms an old successful state under one continuation. New cohort: straight rescues another state; path fails there. | Recovery is condition-dependent. Privileged-teacher feasibility motivates observable students, not claims of Q, trigger, or robot deployment. |
| 14 · Observable recovery student | Can current observations replace teacher geometry? | Fixed grouped offline fits, then 24 native/repeat/proprio/visual student branches over four exposed states. | One failed state is rescued by three student/mode combinations; successful states are harmed and no fixed variant has positive net gain. | A real observation-only recovery opportunity, not autonomous entry, independent generalization or Q efficacy. |
| 15 · Task-return value and selection | Can actual task transitions support one-step and ten-step values, then useful candidate ranking? | Grouped deduplicated task-transition training, segment/no-action controls, and 30 accepted native/uniform/Q and fork/repeat branches. | Q and uniform each yield 2 recoveries/1 degradation on three exposed states. | Real training and selection executed; no Q superiority. Native fork outcomes and sustained-Q values use different subsequent controllers. |
| 16 · Task-Q gradient rollout | Does real value ascent improve the same-budget selected controller? | Native sampler coordinate/ZeroQ checks followed by twelve selection/ZeroQ/gradient/repeat rollouts. | Gradient vs selection: 0 recoveries/2 degradations; all 156 primary gradient queries increase final self-Q. | Freeze this negative combination. Representation reliability is the next fixed hypothesis; no effective trigger can be claimed from these labels. |
| 17 · Spatial-token value contrast | Does retaining spatial visual information change the offline value diagnostics? | Same data/rewards/splits; full/pooled/no-action × two seeds, six equal-size models, each 2,000 updates; CPU restore acceptance. | Full-token group-mean validation Bellman diagnostics are slightly lower than pooled in both seeds; no-action gradients are zero. | Completed offline structural comparison, not a new rollout or evidence of task benefit. |
| 18 · Close custom selection hypotheses | Do better offline representation, return matching or observed state improve real candidate choices? | Fifteen frozen token-selection rollouts; matched-return and observed/masked-state training; fixed first-event replanning and gradient controls. | Token variants underperform old Q/uniform; new return and state ensembles select 0/3 heldout successes vs c0 1/3. Simple first-event replan gives 1 rescue/0 harms over nine states; matched gradient adds 0/1. | Keep the causal baseline and failure diagnosis; no threshold/capacity scan or effective-trigger claim. |
| 19 · Official QGF reference | Can the source-pinned BC-flow/IQL guidance method show learning in a supported setting? | Full 100M cube-triple corpus, native 500k updates, three official task/seed configurations, all checkpoints/weights retained. | Preset final guidance 30/30, 27/30, 29/30 vs no guidance 0/30, 2/30, 0/30. | Clear positive reference in this setting, not strict paired-init inference, full paper replication, or VLA integration. |
| 20 · Native Corrector method reproduction | Can public-data training, exact predictor/actor contracts and original OGG execute credibly? | Full public 1,693-episode corpus; native 30-epoch MLP, complete validation controls, full-reference inference diagnosis and six native control rollouts. | Actual actions outperform misaligned actions across all 169 validation episodes. Six rollouts preserve three successful controls; no stable OGG increment. | Method self-training and engineering passed; official task benefit and integrated architecture remain unverified. |

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

## Rounds 11–13: feedback → reference policy → recovery support

**Checked live on October 15.** The research workstation is reachable again. The three recovery reports match completed CPU acceptance records; this check independently verified all 24 actor trace hashes plus child reports, restoration/zero-pair records, anchor bindings and paired rescue/harm totals. It did not rerun simulation or reload raw trajectory tensors. The second workstation remains unreachable.

### 11. Close the strict-feedback configuration

The previously pending one-step reference completed: H1 succeeds in 6/12 continuations versus H10 5/12, with **2 recoveries and 1 degradation**. Both recoveries share one of six exposed states. Recorded policy calls increase from 500 to 4,732 (9.46×); these are call counts, not synchronized GPU latency. Positive net and repeated rescue in at least two distinct states were required, so the finite configuration is closed without more horizon/seed scans. Observation updates and query budget changed together; no Q attribution is possible.

### 12. Establish a separate frozen public-policy reference

The public actor's natural results are Long 1/6 and Spatial 2/4, from different task cohorts; they are not intervention comparisons or evidence of general improvement. Spatial physical resets can preserve initial state yet yield different rendered observations and later commands. The same-prefix opportunity study therefore captures actual live anchors and includes repeat controls rather than claiming byte-identical rendered rollouts. Sixteen branches completed; single-query and sustained alternatives each gave zero rescue and zero harm, with only one failed control condition.

Failure replay points to empty-grasp continuation at inspected frames. This motivates grasp-support recovery, not a universal failure taxonomy. Old and public visual weights share 197/198 checked tensor values, but a connector projection differs; old projected caches and old predictors are not certified compatible. The new recovery track uses the current public actor's inputs and normalization explicitly.

### 13. Demonstrate conditional recovery, keep privilege and harm visible

A straight recovery stalls at contact in one visited failure despite accurate orientation tracking. A fixed raise–align–descend teacher repairs the missing grasp prerequisite. Primitive lift was first reported separately; only the later teacher-to-actor continuation establishes full task completion. All prefix, teacher and actor steps count toward the same 280-step episode budget.

| Study | Failed-state result | Successful-control result | Boundary |
| --- | --- | --- | --- |
| Old two-state cohort, continuation A | Native/repeat fail; path teacher + unchanged actor succeeds in 196 total steps. Straight fails. | Native succeeds in 77 steps; path succeeds in 273; straight fails. | Path 1 rescue/0 harms; extra cost remains material. |
| Same anchors/teachers, continuation B | The same failed state is rescued again by path; native/repeat fail. | Path now fails while native/repeat succeed; straight preserves success. | Path 1 rescue/1 harm. Repeating a continuation is not a new state. |
| Predeclared additional two-state cohort | New failed state: native/repeat fail; straight teacher + actor succeeds in 139 steps; path fails. | Other state: native/repeat 71 steps, straight 135, path 192; all succeed. | Straight 1 rescue/0 harms; path 0/0. One continuation, not final generalization. |

The additional cohort first rebuilt shared live anchors. Its earlier fresh-reset repeat had disagreed with the natural result; that reset-level success is not used as a correction control. At the new shared anchor both controls fail, allowing the straight-teacher rescue to be attributed within the declared comparison.

**What was solved:** a specific visited failure can be recovered by changing support, rather than increasing critic capacity or repeating nominal imitation. **What remains:** no single maneuver works universally; useful support depends on state, successful behavior can be harmed, and costs increase. These teachers consume simulator object geometry offline and have different durations, so this is neither a pure time-matched path ablation nor an observable deployed policy.

### Observable-student readiness, not completed student efficacy

There are eight distinct teacher traces across four exposed initial states, six of which lift the target. Repeated actor continuations do not duplicate teacher examples. Sampling every third pre-action frame gives 237 rows overall / 170 lifting-demonstration rows; these are not independent states. Failed teacher traces remain in the inventory and task-return evidence.

A fixed CPU mean/ridge/nearest-neighbor pilot groups by initial state before fitting statistics and uses observable proprioception plus a known requested recovery mode. Transfer is mixed and weak on key failed-state groups; normalized-command imitation error is not physical-position or task-success error. This is a feasibility fit, not a released student.

The current frozen-public-vision cache has collected 237 rows with zero simulator actions and zero actor queries, but its status is **not independently audited**. No visual-student training completion, student handoff success, new task-Q benefit, learned trigger, or physical robot result is reported. Next: accept that cache, run a fixed grouped visual/proprioceptive comparison on the same observations, and only then consider a budget-matched student continuation test.

## Rounds 14–16: observable recovery → task value → real gradient outcomes

**Evidence scope:** the restored-access October 19 check matched live campaign report hashes and completed acceptance records for the student, selection, gradient and token-value stages. It did not repeat their archived tensor-level CPU audits, model loading or simulation. Counts below remain exposed-state development evidence.

### 14. Observation-only recovery is now tested, not merely planned

The frozen-public-vision cache and grouped offline fits finished after the previous check. Current visual/proprioceptive inputs carry some imitation information, but improvements are not universal. The follow-on fixed pilot completed **24 branches across four exposed initial states**, including native/repeat controls and proprioceptive versus visual-plus-proprioceptive students in two requested recovery modes.

| Fixed student | Recoveries | Degradations |
| --- | ---: | ---: |
| Proprioception, straight recovery | 1 | 2 |
| Vision + proprioception, straight recovery | 1 | 2 |
| Proprioception, path recovery | 1 | 1 |
| Vision + proprioception, path recovery | 0 | 2 |

The three rescues all concern **one failed initial state**, not three independent recoverable states. The archived audit reconstructs 1,648 student commands and 2,900 actor commands from actual recorded inputs. No simulator object geometry enters the student's online input. Nevertheless the entry anchor and requested mode remain prescribed; there is no autonomous benefit trigger or independent final test. One preserved success takes 79 → 272 total steps under a student recovery. Failed teachers, harmed successes and unsuccessful student modes remain reported.

This is a substantive advance over privileged-teacher-only opportunity: a learned current-observation recovery reaches whole-task success. It is not reliable unconditional correction. Its 83/123-step feedback-recovery labels cannot be relabeled as the value of the first action chunk.

### 15. Actual task-value fitting and same-budget candidate selection

A one-environment-step IQL-style reference uses ninety historical branches / 35,186 executed steps, deduplicated into 14,339 transitions. Six training states contribute 9,559 transitions; three validation states contribute 4,780. Action-conditioned/no-action × two seeds gives four models, each 2,000 updates. Finite action gradients and changing Bellman diagnostics demonstrate fitting, not calibrated success probabilities or useful correction. Some Q predictions fall outside [0,1].

The subsequent ten-step reference uses sixty proposal trajectories and **2,353 deduplicated blocks**, split into 1,183 training and 1,170 validation blocks across five/five exposed state groups. Single-query short tails are not spliced across replanning boundaries; actual executed duration controls targets. Segment/no-action × two seeds again receives 2,000 updates each. Archived independent CPU restores check diagnostics and train-only normalization; this run has not reloaded those weights.

Thirty complete simulation branches then separate sustained candidate selection, native continuation forks and repeats:

| Exposed development state | Native fixed ten-step | Same-budget uniform | Sustained Q selection |
| --- | --- | --- | --- |
| A | Success, 428 steps | Failure, 520 | Failure, 520 |
| B | Failure, 520 | Success, 183 | Success, 187 |
| C | Failure, 520 | Success, 252 | Success, 441 |

Q and uniform both give **2 recoveries/1 degradation**; Q is not demonstrated superior or faster. At one fixed Q-prefix fork, the selected candidate fails under native continuation but succeeds under sustained Q. That is a continuation-specific ranking disagreement, not a proven error against an identical value target. Future supervision must bind actual duration and the subsequent controller.

### 16. Native-flow gradients execute, but incremental outcome is negative

The real sampler probe verifies disabled/ZeroQ equality, thirty finite nonzero denoising gradients, explicit normalized/environment coordinates, unchanged original parameters and protection of the unused action tail. It has no environment outcome by itself.

The subsequent fixed twelve-rollout campaign uses three exposed states and four controllers: Q selection without gradient, its ZeroQ equivalent, real gradient, and gradient repeat. Each query has four original candidates plus two real sampler calls, with ten-step execution and a 520-step episode limit.

| Controller | Successes across three states | Gradient increment versus selection |
| --- | ---: | --- |
| Q selection, no gradient | 2 | Reference |
| Same selector, ZeroQ | 2 | Exact equivalent |
| Real task-Q gradient | 0 | 0 recoveries / 2 degradations |
| Gradient repeat | 0 | No repeat conflicts; not three new states |

The archived full audit covers twelve traces, 544 queries and 5,416 executed steps. **156/156 primary gradient queries increase final model-Q**, yet task outcomes worsen. Therefore missing wiring or lack of self-score ascent is not a sufficient explanation. The unique cause—representation, support, target or sustained intervention—remains unproven. Host elapsed run time is not an inference-latency benchmark.

These are full-controller comparisons on three initial states, not 544 same-state keyframe counterfactual labels. Neither comparison supplies positive gradient-increment examples for an effective benefit trigger. Keep the earlier Q-versus-uniform and observable-student results intact; do not borrow their positives for this different controller.

### Current next gate

The fixed full-token/pooled/no-action value-representation comparison on the **same 2,353 blocks**, two seeds and unchanged rewards/splits has now completed training and CPU acceptance (round 17 below). Retaining spatial information remains a hypothesis about value reliability, not an established explanation of rollout failure. No more radius/seed/trigger-threshold scans are justified by the current negative combination. Task-Q training and gradient engineering are now real completed stages, while reliable corrective utility, learned benefit triggering, independent final validation and physical robot performance remain open.

## Round 17: token-information ablation completed

Live report and CPU acceptance now supersede the earlier launch-only workflow note. Full-token, pooled-token and no-action variants each use two fixed seeds and 468,805 parameters; full/pooled match architecture and initialization. All six train for 2,000 updates on the same 2,353 blocks, with no new environment collection. Completed acceptance records exact independent CPU restoration for all six. This check verifies the report binding, not a new model reload.

| Validation diagnostic, group mean | Seed A | Seed B |
| --- | ---: | ---: |
| Full-token Bellman MSE | 0.018193 | 0.018048 |
| Pooled-token Bellman MSE | 0.019574 | 0.018726 |
| No-action Bellman MSE | 0.019885 | 0.022393 |

Action-conditioned gradients are finite/nonzero; no-action gradients are zero. The full-token diagnostic is modestly lower than pooled for both seeds, but each model uses its own value-backed targets. This is not a common-target accuracy contest or evidence of safer action ascent. Training elapsed time and small-model memory are not actor inference latency.

No token-variant environment rollout, increased success rate, effective benefit trigger or independent final test is reported. Before changing a deployed controller, retain the earlier 0-recovery/2-degradation gradient result and require a separately frozen same-budget paired test. Engineering completion and utility remain separate gates.

## Round 18: close custom hypotheses without losing the useful baseline

The fifteen completed full-token/pooled selection rollouts do not convert round 17's offline diagnostic improvement into better terminal outcomes. Both new variants yield one recovery/one harm versus native and zero added recoveries/one harm versus old Q or uniform. The small step saving in one success cannot offset a lost successful case.

A stronger, separate first-event reference over nine exposed states raises successes from **4/9 to 5/9: one recovery, zero harms**. The sole rescue repeats exactly, but remains one state. On three fixed event cases, deterministic native-flow task-Q guidance adds **zero recoveries and one harm** versus equal-compute ZeroQ/replanning; this is not the earlier continuously enabled twelve-rollout protocol. Self-score ascent and gradient wiring are not missing.

Return matching reuses 38 complete branches / 1,444 blocks across ten exposed initial groups. Six fixed MC/paired/no-action fits complete. New MC and paired ensembles select **0/3 successful heldout candidates**, versus candidate-zero 1/3 and measured finite-pool oracle 2/3. Four observed-state/masked-state fits also select 0/3. The added robot state affects predictions but does not repair selection. These Task0-only, already-exposed heldout pools are diagnostic, not independent testing; the finite oracle is not deployable performance or an all-action upper bound. Stop these ablations rather than keep renaming small changes.

## Stage 3: separate official baselines before integration

The new source-pinned references are [VLA-Corrector](https://github.com/ZJU-OmniAI/vla-corrector) and [Berkeley QGF](https://github.com/zhouzypaul/qgf). Their original objectives differ: visual-residual OGG is not task-return Q. Old SmolVLA losses, labels, normalization and failure rates cannot stand in for either official method. Source pinning and isolated runtime/dependency receipts preserve provenance; no upstream control implementation or private artifacts are copied into this portfolio.

### Round 19: QGF has a positive supported-setting result

Three runs use the full 100M public corpus in one cube-triple layout, two task goals and three task/seed configurations. Each completes 500,000 native offline updates with BC flow and IQL Q/V/TD, horizon five and batch 1,024. The preset final guidance weight is 0.06, not an after-the-fact best weight.

| Official configuration | Guided final successes | Unguided final successes |
| --- | ---: | ---: |
| Task 1 / seed 1 | 30/30 | 0/30 |
| Task 1 / seed 2 | 27/30 | 2/30 |
| Task 2 / seed 1 | 29/30 | 0/30 |

Five checkpoints and nine official guidance weights plus the zero-guidance control retain 1,500 evaluation records per run, 4,500 overall. These are not 4,500 independent initial states. Evaluation conditions are not strict same-initial-state pairs; this follows the public script's thirty episodes per condition rather than claiming the paper's exact episode-count protocol. All final checkpoints and non-winning settings remain retained. This is positive evidence for the reference method under these configurations, not full-paper coverage, an original algorithm contribution, SmolVLA performance or integrated keyframe + Q results.

### Round 20: public-data Corrector training and native inference

The full public LeRobot asset has **1,693 episodes, 273,465 frames and forty task groups**. Its fixed episode split is 1,355 training / 169 validation / 169 test, separate from all private portfolio datasets and the earlier 450-episode cache. The native h1/k10 MLP uses cosine loss, batch 512, learning rate 3e-4 and thirty epochs with patience five; all thirty finish and validation selects epoch thirty. The predictor has 42,510,336 parameters. This is **official-code method self-training on public data**, not author-identical training data/weights or exact paper-number reproduction. Predictor episode holdout is not proof of base-policy-unseen data or simulation-state generalization.

The full validation diagnostic covers 26,104 pairs in 169 episodes. Actual-action cosine loss is **0.322989**, versus **0.444053** for misaligned actions, 1.0 for zero residual and 0.961198 for the training-mean baseline. Actual actions improve both cosine and MSE in all 169 episodes. The October 26 read-only check independently sums episode pair counts and recomputes the weighted cosine summaries from the acceptance record. It does not re-encode images or reload the predictor; predictive information still is not task success.

**Concrete inference defect solved.** Strictly matching 813 weight keys did not guarantee equivalent execution: the installed text embedding already applied scaling, while the PI0.5 prefix applied it again. A source-traced instance-level correction preserves original weights and fixes the duplicate scaling. On the fixed real input/noise reference, early stages match exactly and final action max error is 3.13e-7. This is fixed-input numerical parity, not a blanket compatibility guarantee or a causal explanation of older SmolVLA failures.

Policy preprocessing and monitor preprocessing stay explicit and distinct. Online monitor quantized tokens/scales match the training cache; raw-action training and normalized-action sampling share a differentiable inverse transform. The training-side and native online predictors match, ZeroOGG is exact, and actual original OGG gradients execute. Those are engineering gates, not learned task-value gains.

| Known development task | Natural steps | Truncation steps / calls | Truncation + OGG steps / calls |
| --- | ---: | ---: | ---: |
| 0 | 244 | 255 / 29 | 250 / 28 |
| 2 | 221 | 213 / 23 | 223 / 24 |
| 5 | 271 | 257 / 28 | 259 / 28 |

All six intervention rollouts succeed, but all three natural controls already succeed: **zero recoveries/zero harms**, with no failed-control recovery opportunity. OGG requests total nine and execute ninety gradient steps; it is slightly faster than truncation once and slower twice, not a stable efficiency improvement. Task 2 reset observations differ despite matching initial physical states, so strict image-level pairing is not claimed.

### Current gate and source freshness

The research workstation was checked live on October 26. Two QGF acceptance sets, the complete Corrector learning diagnostic and six-rollout raw-audit record were read; their acceptance-file hashes and numerical summaries were checked. Five custom-study report/acceptance hash links were also checked. This monitor did not independently repeat all 4,500 raw evaluations, checkpoint loading or six-rollout tensor audits.

A fixed 120-task/init-identity natural PI0.5 cohort is running: ten tasks × twelve native initial states, with 117 new cases and three reused controls. Running coverage is not completed evidence, and the 240 matching truncation/OGG conditions have not started. Reused cases lack the full new raw-observation capture, so they cannot all be counted as new training transitions. No integrated VLA task-Q/benefit-trigger result or new physical robot outcome is reported. mc509 remains unreachable. Next acceptance is complete identity/coverage/raw-data auditing followed by the declared controlled correction conditions, not another local parameter search.

## Public evidence boundary

All outcomes here are offline simulation studies. A rescue in an exposed state demonstrates a specific paired outcome, not an independent held-out success rate. The two-task natural pilot tests portability of the frozen policy interface, not cross-task correction. No result on this page measures real robot performance.
