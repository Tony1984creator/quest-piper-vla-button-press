# Experiment ledger

## Evidence ladder

| Level | What it proves | What it does not prove |
| --- | --- | --- |
| Import / mapping | Modules and tensors can be connected | Real-data execution or quality |
| Smoke step | Shapes, losses, gradients, and freeze rules are valid for a step | Stable optimization or task competence |
| Short continuation | Loop can run for multiple updates | Convergence or generalization |
| Pilot training | Directional training behavior under a fixed run | Benchmark-quality performance |
| Offline inference | Candidate actions have expected shape and stay non-actuating | Robot success |
| Closed loop | Defined task outcome under a safety protocol | Broad robustness unless sample count and distribution support it |

## Verified VLA-JEPA 2.1 pilot evidence

The following aggregate evidence comes from one private, real-data pilot run.
It is retained here to make the current stage reproducible without publishing
raw demonstrations, checkpoints, internal paths, or task text.

| Item | Verified evidence | Interpretation boundary |
| --- | --- | --- |
| Compatibility | V-JEPA 2.0 -> 2.1 interface mapping checked 386 encoder tensors; 12 tensors require reinitialization | Static interface compatibility is not an end-to-end quality result. |
| Pilot length | 100 optimization steps completed and wrote one checkpoint (about 5.52 GB) | A saved checkpoint proves resumable execution, not convergence. |
| Optimization contract | Teacher was frozen; Qwen, predictor, and action-head gradient paths were active | The intended train/freeze boundary was exercised. |
| Auxiliary world loss | Approximately 1.2344 at the first recorded step and 1.1668 at the pilot endpoint | Directional decrease in one pilot; no causal benefit or benchmark claim. |
| Action loss | Final recorded value about 13.684; values were variable during the pilot | The action objective has not demonstrated stable convergence. |
| Offline action probe | Produced one [1, 7, 7] action chunk; `hardware_commands_sent=false` | Tensor shape and non-actuation boundary are verified, not robot behavior. |

The action probe's values and private task text are intentionally omitted. The
probe did not command the robot.


## Verified Evo-Depth controlled-finetune and deployment-audit evidence

This is a parallel action-policy engineering track. Its loss values are not
compared with the VLA-JEPA probe because the model, action representation, and
training configuration differ.

| Item | Verified evidence | Interpretation boundary |
| --- | --- | --- |
| Controlled fine-tune | Action-head-only flow-matching run completed 300 steps on a leakage-safe split | This is a limited pilot, not a model-selection protocol. |
| Fixed real-data evaluation | Same 187 fixed real-data batches and evaluator: 30-step reference mean masked flow loss 0.8415; 300-step pilot 0.2449 | The comparison is useful for this controlled offline check; it does not establish generalization or task success. |
| Offline replay | 12 task instances, one episode each, five selected keyframes each (60 inputs); two checkpoints generated 120 action-jump metric rows | Replay measures candidate-action behavior only; no robot command was issued. |
| Deployment contract audit | Recorded exchange contract was [50, 24]; client selects 25 steps and consumes only the first seven active dimensions | Runtime behavior outside the inspected session is not established. |
| Safety audit | Offline tests covered shape/mask, selection, outlier filter, limits, measured-state delta limit, smoothing, and joint/gripper order: 13/13 passed | Tests use fakes or recorded exchanges and did not open robot, CAN, camera, or GPU-server resources. |
| Residual policy | A bounded residual insertion point before the first safety filter is specified and zero-residual equivalence was tested | No residual term is wired into the deployed client. |

The public record intentionally omits dataset paths, task descriptions, camera
identifiers, server addresses, checkpoints, and deployment configuration.

## Report template for future runs

Every run should record:

- source dataset version and **episode-level** split identifier;
- unit-conversion owner and action/state convention;
- model commit, upstream revision, seed, hardware/runtime, and configuration hash;
- training/validation curves and model-selection rule;
- action metric and closed-loop metric separately;
- count of trials, success definition, failure taxonomy, and reviewed evidence;
- declared limitations and deviations from plan.

## Current honest status

The present result supports: a real teleoperation/data path, a valid VLA-JEPA 2.1 training interface, a 100-step real-data pilot with the intended gradient contract, a non-actuating offline action probe, and a visually audited pre-annotation workflow. It does not yet support: a successful ACT baseline comparison, a causal VLA-JEPA benefit claim, or a completed real-robot button-press success rate.
