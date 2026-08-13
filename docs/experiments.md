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

The present result supports: a real teleoperation/data path, a valid VLA-JEPA 2.1 training interface, real-data training probes, an offline action probe, and a visually audited pre-annotation workflow. It does not yet support: a successful ACT baseline comparison, a causal VLA-JEPA benefit claim, or a completed real-robot button-press success rate.
