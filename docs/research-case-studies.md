# Research case studies: problem, evidence, and boundary

These are engineering case studies, not a claim of a new foundation model or a completed task-success benchmark. Each case names the next experiment that could disprove or strengthen its conclusion.

## 1. Safety-gated teleoperation and a unit-consistent data loop

| Element | Evidence |
| --- | --- |
| Problem | VR pose updates, robot kinematics, SDK transport, and learning data use different assumptions. A stale or double-converted command can become a physical-system fault rather than a normal model error. |
| Intervention | Connected Quest VR to ROS 2, Pinocchio/CasADi IK, a single guarded Piper command daemon, and Piper SDK/CAN. Defined seven-dimensional arm-plus-gripper ordering and stored state/action in degrees, converting to radians exactly once at kinematic or model-computation boundaries. |
| Evidence | The real single-arm control chain was exercised. The recorded LeRobot corpus contains 40 episodes and 14,653 frames at 30 FPS with two 640x480 RGB views and 7D state/action. |
| What this supports | A cross-layer teleoperation and data-contract integration result with an explicit learning-to-actuation boundary. |
| What this does not support | Stable autonomous button pressing, robustness to arbitrary users/workspaces, or public release of hardware-control settings. |
| Next falsifiable test | Freeze an episode-level split, run schema/range checks, then establish an ACT held-out action baseline before any closed-loop trial. |

## 2. Action-conditioned VLA-JEPA integration without putting a world model on the actuation path

| Element | Evidence |
| --- | --- |
| Problem | An upstream V-JEPA interface change can silently break tensor layout, freezing rules, or gradient ownership. An auxiliary objective must not be confused with a deployable command path. |
| Intervention | Mapped the V-JEPA 2.0 encoder interface to 2.1, with 386 tensors mapped and 12 reinitialized. Used a frozen teacher/no-grad contract while Qwen/action-head/predictor paths retained gradients. Kept the action probe offline. |
| Evidence | Real-data tensors traversed `[1,8,3,480,640]` views, `[1,7,7]` actions, and `[1,7]` state. In a 100-step pilot, world loss moved from 1.2344 to 1.1668; final action loss was 13.684 and variable. A `[1,7,7]` action chunk was produced with no hardware command sent. |
| What this supports | Static migration, gradient-flow, real-data execution, and non-actuating action-shape checks. |
| What this does not support | Convergence, an ACT improvement, task success, or a claim that the auxiliary world model is deployed to the robot. |
| Next falsifiable test | Compare ACT versus ACT + auxiliary loss using matched episode-level split, seed set, preprocessing, action horizon, and validation-selected checkpoints. |

## 3. Read-only visual pre-annotation for reviewable task stages

| Element | Evidence |
| --- | --- |
| Problem | Manual inspection of long wrist-camera recordings is expensive, but a visually bright button is not by itself evidence that the requested button was contacted or selected. |
| Intervention | Implemented a dataset-independent pipeline: HSV thresholding, largest connected component, edge rejection, at least 1,000 pixels, and at least three consecutive active frames. It produces review candidates only. |
| Evidence | Processing 12 wrist videos (188,418 frames) yielded 421 temporally stable candidates. A stratified audit of 48 candidates recorded 48 yes, 0 no, and 0 uncertain. |
| What this supports | A useful review-prioritization signal under the observed recordings. |
| What this does not support | Universal detector precision, causal contact evidence, or task-level success. |
| Next falsifiable test | Join candidates to requested floor, approach/contact/retraction stages, and human-reviewed `success` / `failure_reason` labels on held-out trials. |

## Runtime evidence policy

Training hardware and edge hardware answer different questions. A workstation has two A100 80GB GPUs available for training/probes, while the robot-side workstation has a GTX 1060 6GB GPU. No cross-device model-quality comparison follows from those facts. A retained historical remote-request audit found p50 8.43 seconds and p95 12.26 seconds over five client requests, each returning a 25-step chunk; its full interpretation and limits are documented in the [remote-inference audit](remote-inference-latency-audit.md). Before reporting model-only runtime, an offline callable must be benchmarked with fixed input, preprocessing, action-chunk policy, warmups, and repeats using the [offline benchmark protocol](offline-inference-benchmark.md). The current public status is **historical end-to-end bottleneck observed; per-stage safe report pending**.

