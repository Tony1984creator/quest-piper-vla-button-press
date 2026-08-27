# Quest–Piper Robot-Learning Portfolio

> Real robot-learning integration, expressed as safe, testable engineering projects—not as unsupported task-success claims.

## Projects

| Project | Problem solved | Evidence | Core code |
| --- | --- | --- | --- |
| [01 · Quest–Piper safety](projects/quest_piper_safety/README.md) | Reject stale/malformed 7D commands before private transport. | Quest→ROS 2→IK→guarded daemon→Piper chain exercised. | Freshness + finite-value gate. |
| [02 · LeRobot data contract](projects/lerobot_data_contract/README.md) | Keep units and episode splits auditable. | 40 episodes / 14,653 frames / 2 RGB / 7D. | One degree→radian boundary. |
| [03 · VLA-JEPA integration](projects/vla_jepa_integration/README.md) | Upgrade teacher/layout contracts safely. | 386 mapped; 12 reinitialized; real-data pilot. | Layout + frozen-teacher validators. |
| [04 · Evo-Depth deployment](projects/evo_depth_deployment/README.md) | Inspect action chunks and diagnose runtime bottlenecks. | 13/13 offline checks; request p50/p95 8.43/12.26 s. | Chunk selection + delta clamp. |
| [05 · Visual pre-annotation](projects/visual_preannotation/README.md) | Produce review candidates, not success labels. | 12 videos / 188,418 frames / 421 candidates. | HSV + temporal event pipeline. |

## Active roadmap

[ACT baseline, VLA-JEPA ablation, guarded button loop, and NERO scope](docs/roadmap/README.md).

## Run locally

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

The [offline runtime API](shared/runtime_benchmark/offline_latency.py) measures only a reviewed callable and writes `hardware_commands_sent: false`.

## Public boundary

No raw demonstrations, task text, checkpoints, internal addresses/paths, device identifiers, robot settings, or actuation code is included. Integration, offline evidence, and closed-loop task success remain distinct.

## Evidence archive

Detailed evidence remains under [docs](docs/): [architecture](docs/architecture.md), [experiments](docs/experiments.md), [case studies](docs/research-case-studies.md), and [portfolio evidence](docs/portfolio-evidence.md).

