# Quest–Piper Robot-Learning Portfolio

> A public, evidence-bounded portfolio of embodied-AI systems work: VR teleoperation, robot-data contracts, predictive VLA integration, deployment audits, and visual-review tooling.

## Research focus

**How can a visual teleoperation workflow become a reproducible robot-learning loop without confusing an interface test, an offline metric, and real task success?**

The private system that informed this portfolio was exercised along the following boundary:

```text
Quest VR intent → ROS 2 interface → IK → guarded command owner → private robot transport
                              │
                              ├─ LeRobot episodes → ACT / VLA-JEPA experiments
                              └─ wrist video → review candidates → human outcome labels
```

The public repository intentionally keeps only dependency-free contracts, tests, and aggregate evidence around that workflow. It contains neither a hardware driver nor a path to command a robot.

## Projects

| Project | Engineering question answered | Evidence anchor | Reusable public code |
| --- | --- | --- | --- |
| [01 · Quest–Piper safety](projects/quest_piper_safety/README.md) | How should stale, malformed, or competing teleoperation commands be stopped before transport? | An end-to-end interface path was exercised with one guarded command owner. | [Freshness and finite-value gate](projects/quest_piper_safety/core/safety_gate.py) |
| [02 · LeRobot data contract](projects/lerobot_data_contract/README.md) | How do units, episode boundaries, and stream timing stay auditable before training? | 40 episodes, 14,653 frames, two RGB streams, and a 7D state/action contract. | [Conversion boundary](projects/lerobot_data_contract/core/data_contract.py) and [episode integrity](projects/lerobot_data_contract/core/episode_integrity.py) |
| [03 · VLA-JEPA integration](projects/vla_jepa_integration/README.md) | How can a representation-model upgrade be made testable rather than silently changing a training system? | 386 teacher tensors mapped; a real-data 100-step compatibility pilot completed. | [Layout and mapping checks](projects/vla_jepa_integration/core/contracts.py) and [migration invariants](projects/vla_jepa_integration/core/migration_contract.py) |
| [04 · Evo-Depth deployment](projects/evo_depth_deployment/README.md) | What must be measured and constrained before interpreting policy output near an execution endpoint? | Fixed-protocol offline evaluation and action-path audit. | [Action-chunk contract](projects/evo_depth_deployment/core/action_chunk.py) |
| [05 · Visual pre-annotation](projects/visual_preannotation/README.md) | How can video review be reduced without turning a visual cue into a success label? | 421 review candidates plus a stratified visual audit. | [Temporal event pipeline](projects/visual_preannotation/core/) and [review sampler](projects/visual_preannotation/core/review_sampling.py) |

## Evidence levels

| Level | What it means here | What it does **not** mean |
| --- | --- | --- |
| Systems integration | Interfaces and a private real-robot path were exercised. | A public hardware reproduction or task-rate claim. |
| Offline probe | Dataset properties, tensors, losses, contract behavior, or timing scopes were measured. | A policy-quality or real-time claim unless separately evaluated. |
| Closed-loop success | Timestamped commands, feedback, and reviewed outcomes meet a stated task criterion. | Something inferred from a bright frame or a finite loss. |

For the compact resume/interview evidence map, see [docs/evidence.md](docs/evidence.md). For the next experiment gates, see the [active roadmap](docs/roadmap/README.md).

## Run locally

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

The public modules use the Python standard library. The optional visual utilities only produce offline review artifacts, and the [runtime helper](shared/runtime_benchmark/offline_latency.py) records `hardware_commands_sent: false`.

## Public boundary

No raw demonstrations, task text, checkpoints, internal addresses or paths, device identifiers, calibration values, robot settings, or actuation code is published. The repository documents engineering decisions and validates offline contracts; it cannot operate a robot.

