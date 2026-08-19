# Quest–Piper VLA Button-Press Research Log

> A scoped, evidence-first portfolio of a real-robot learning pipeline: Quest teleoperation, LeRobot data collection, ACT baseline planning, VLA-JEPA world-model experiments, and visual pre-annotation for an elevator-button task.

## What this repository is—and is not

This is a reproducibility and engineering record for a student internship project. It documents system contracts, measured training probes, and the next closed-loop evaluation plan. It does **not** claim a new foundation model, an end-to-end task-success benchmark, or generalization beyond the reported evidence.

The public version intentionally excludes raw demonstrations, videos, checkpoints, internal network details, robot-control configurations, credentials, and proprietary source. Measurements are reported in compact, sanitized form so that the experimental logic can be reviewed without disclosing sensitive assets.

## System path

```text
Quest VR teleoperation
  -> ROS 2 joint-command interface
  -> Pinocchio / CasADi inverse kinematics
  -> guarded Piper daemon
  -> Piper SDK / CAN
  -> single-arm robot execution

LeRobot episodes (two RGB cameras + 7D state/action)
  -> data-contract validation
  -> ACT action-chunk baseline
  -> VLA-JEPA action-conditioned auxiliary world-model ablation
  -> offline action probe
  -> guarded real-robot button-press evaluation
```

Detailed interfaces and safety boundaries are in [docs/architecture.md](docs/architecture.md). The project roadmap is in [docs/roadmap.md](docs/roadmap.md). The current private data-contract validation evidence and its public boundary are in [docs/data-contract-qc.md](docs/data-contract-qc.md). The current OpenCV scope and validation boundary are in [docs/opencv-preannotation.md](docs/opencv-preannotation.md). Public, sanitized Quest operational references are available as the [real-test safety guide](docs/quest-real-test-guide.md), [control principles](docs/quest-control-principles.md), and [VR recording contract](docs/quest-vr-recording-contract.md), and [VLA-JEPA 2.1 migration contract](docs/vla-jepa-21-migration-contract.md).

## Evidence snapshot (2026-08)

| Area | Evidence retained in this public record | Current conclusion |
| --- | --- | --- |
| Teleoperation and hardware | Quest-to-ROS 2-to-IK-to-daemon-to-SDK/CAN chain exercised on a real Piper arm | Hardware path is established; commands remain safety-gated. |
| Dataset | 40 episodes, 14,653 frames at 30 FPS; two 640x480 RGB streams; 7D state and action | Enough for a baseline/protocol, not a generalization claim. |
| Data-contract QC | 40 episodes and 14,653 frames checked; metadata, indexes, timestamps, and both video streams passed the stored-data contract | Does not establish calibration quality or a frozen train/validation/test split. |
| VLA-JEPA 2.0 -> 2.1 | 386 encoder tensors mapped; 12 reinitialized; teacher frozen contract verified | Interface upgrade and optimization path are verified. |
| Real-data training | Smoke, three-step, diverse-sample, and 100-step pilot runs completed | The auxiliary loss decreased in the pilot; action loss is variable, so convergence is not claimed. |
| Offline inference | 7x7 action chunk produced with `hardware_commands_sent=false` | Output shape and non-actuation boundary are verified. |
| Evo-Depth controlled fine-tuning | Action-head-only 300-step pilot evaluated on a fixed 187-batch real-data set; mean masked flow loss 0.8415 (30-step reference) vs. 0.2449 (300-step pilot) | A matched offline validation loss is not a task-success or cross-model comparison. |
| Evo-Depth deployment audit | Offline Piper action-chain audit: [50, 24] chunk, 25 executed steps, first 7 active dimensions; 13/13 synthetic/recorded-contract tests passed | The audit contacted no robot, CAN, camera, or GPU server; residual RL remains a specification, not production code. |
| OpenCV pre-annotation | 12 wrist-camera videos, 188,418 frames, 421 stable visual-confirmation candidates; 48 stratified audit samples | Visual candidates are useful pre-annotations, **not** task success labels. |
| Single-frame visual detection | Position-independent HSV orange detector; three regression tests cover detection, small-noise rejection, and edge-artifact rejection | Detects visual illumination only; it does not identify a floor, establish contact, or establish task success. |

## Research progression

| Stage | Question | Deliverable / acceptance criterion |
| --- | --- | --- |
| Data loop | Are demonstrations valid and unit-consistent? | Episode-level split, schema check, and a single degrees-to-radians conversion boundary. |
| ACT baseline | Can action chunks fit held-out trajectories? | Train/validation curves and open-loop action metrics before hardware evaluation. |
| VLA-JEPA ablation | Does the frozen V-JEPA teacher auxiliary objective improve the baseline under fixed data? | Seeded ACT-vs-ACT+world-model comparison with the same split and reporting protocol. |
| Button press | Does the policy complete the requested press under safety gates? | Episode-level success, failure reason, stage labels, and video-reviewed closed-loop trials. |

## Minimal local check

The small, hardware-independent utilities in `opencv_preannotation/` can be checked without a robot or a dataset:

```bash
python -m unittest discover -s tests -v
```

For full video processing, install `opencv-python` and `numpy`, supply data through an external path, and keep all outputs outside the source dataset. See [docs/opencv-preannotation.md](docs/opencv-preannotation.md).

## Repository map

```text
.
├── docs/                     # Architecture, data, experiments, portfolio evidence, roadmap
├── opencv_preannotation/     # Dataset-independent single-frame and temporal visual-candidate utilities
├── tests/                    # Unit tests for the portable utilities
├── CITATION.cff
├── LICENSE                   # MIT for original public material in this repository
├── LICENSE_SCOPE.md          # Explicit exclusions and reuse boundary
└── THIRD_PARTY_NOTICES.md
```

## References

- Zhao et al., [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705) (ACT / ALOHA).
- Kim et al., [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246).
- Bardes et al., [V-JEPA 2](https://arxiv.org/abs/2506.09985).
- The research-log presentation takes inspiration from [Diffusion Policies for Long-Horizon Robot Manipulation](https://github.com/Mendossss/Diffusion-policies-long-horizon-manipulation), while all text and code here are independently written.

## Status and responsible reuse

This repository is actively evolving. Results are preliminary and should not be used to operate a robot without independent safety review, workspace-specific limits, an emergency stop, and a trained operator.
