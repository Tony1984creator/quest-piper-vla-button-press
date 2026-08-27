# Quest–Piper Robot-Learning Portfolio

> A public, safety-bounded portfolio of real robot-learning integration: from Quest teleoperation and LeRobot data contracts to VLA-JEPA probes, deployment audits, and visual-review tooling.

## What this portfolio demonstrates

The work centers on one practical question: **how can visual, teleoperation, and policy components be connected to a real robot workflow without turning incomplete evidence into an unsafe or inflated claim?**

The private system path that was exercised is:

```text
Quest controller intent → ROS 2 → IK → guarded daemon → Piper SDK/CAN → robot
                           │
                           └→ LeRobot data → ACT / VLA-JEPA → reviewed offline output
```

The public repository contains the reusable, hardware-independent contracts around that path. It deliberately omits actuation, device, calibration, raw-data, and network details.

## Projects

| Project | Problem solved | Strongest public evidence | Core code |
| --- | --- | --- | --- |
| [01 · Quest–Piper safety](projects/quest_piper_safety/README.md) | Reject stale or malformed 7D candidates before private transport. | Quest→ROS 2→IK→guarded daemon→Piper chain exercised; 50 Hz private guard. | [Freshness + finite-value gate](projects/quest_piper_safety/core/safety_gate.py) |
| [02 · LeRobot data contract](projects/lerobot_data_contract/README.md) | Prevent degree/radian drift and frame-level split leakage. | 40 episodes / 14,653 frames / 30 FPS / two RGB streams / 7D state-action. | [Single conversion boundary](projects/lerobot_data_contract/core/data_contract.py) |
| [03 · VLA-JEPA integration](projects/vla_jepa_integration/README.md) | Upgrade teacher and tensor contracts without silent training changes. | 386 tensors mapped, 12 reinitialized; real-data 100-step world loss 1.2344→1.1668. | [Layout + mapping validators](projects/vla_jepa_integration/core/contracts.py) |
| [04 · Evo-Depth deployment](projects/evo_depth_deployment/README.md) | Inspect action chunks and attribute runtime bottlenecks before endpoint claims. | 13/13 offline checks; historical whole-request p50/p95 8.43/12.26 s. | [Chunk selection + delta clamp](projects/evo_depth_deployment/core/action_chunk.py) |
| [05 · Visual pre-annotation](projects/visual_preannotation/README.md) | Reduce wrist-video review without treating a bright event as task success. | 12 videos / 188,418 frames / 421 review candidates; 48-sample visual audit. | [Detector + temporal filter](projects/visual_preannotation/core/) |

## Reading the evidence correctly

| Evidence level | Meaning in this repository |
| --- | --- |
| Systems integration | Interfaces and the private real-robot path were exercised. |
| Offline probe | Shapes, losses, data contracts, or latency contracts were measured. |
| Closed-loop success | Requires separately timestamped command/feedback and reviewed task outcomes; it is never inferred from a visual cue alone. |

The consolidated [evidence index](docs/evidence.md) gives the resume-ready and interview-ready framing. The [active roadmap](docs/roadmap/README.md) names the remaining ACT, ablation, and guarded button-loop gates.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

The [offline runtime API](shared/runtime_benchmark/offline_latency.py) invokes only a reviewed callable and records `hardware_commands_sent: false`.

## Public boundary

No raw demonstrations, task text, checkpoints, internal addresses/paths, device identifiers, robot settings, or actuation code is included. The code can validate contracts and generate offline review artifacts; it cannot operate a robot.

