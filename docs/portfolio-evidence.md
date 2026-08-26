# Portfolio evidence and interview framing

## Resume-ready evidence

| Capability | Evidence | Careful resume framing |
| --- | --- | --- |
| Robot systems integration | Connected Quest teleoperation, ROS 2, IK, a guarded command daemon, SDK/CAN, and a real Piper arm | Built and tested a safety-bounded teleoperation-to-robot control chain for a single-arm platform. |
| Data engineering | Recorded/used a LeRobot corpus with two RGB views and 7D state/action; established degree/radian boundary | Defined data contracts and unit ownership for robot-learning training and kinematic computation. |
| Representation / VLA training | Performed V-JEPA 2.0->2.1 mapping and real-data training/inference probes | Validated frozen-teacher, gradient-flow, and action-chunk interfaces for an action-conditioned VLA-JEPA experiment. |
| Visual validation | Built an OpenCV temporal pre-annotation workflow with audit sampling | Developed read-only visual candidate mining with temporal filtering and a stratified audit protocol. |
| Experiment design | Separates smoke, pilot, offline inference, and closed-loop claims | Reports what each experiment establishes and avoids treating training loss as task success. |
| Policy validation and deployment safety | Ran a controlled Evo-Depth action-head pilot on a fixed real-data evaluation set and audited the Piper action path offline | Designed matched offline checks, traced action units/horizons and documented which safety gates remain required before hardware. |

## Microelectronics-to-robotics mapping

| Existing background | Transferable robot-system strength | Interview example |
| --- | --- | --- |
| Embedded and physical-system thinking | Timing, interfaces, fault boundaries, and safe actuation | Explain why the model must not own CAN and why stale input should hold a safe target. |
| Signals / control intuition | State conventions, calibration, coordinate/unit checks | Explain the single degrees-to-radians boundary and how double conversion is detected. |
| Hardware debugging | Layered fault isolation | Trace a failed command across VR, ROS 2, IK, daemon, SDK, and bus layers. |
| ML/VLA study | Hypothesis-driven experiments | Contrast mapping validation, smoke execution, pilot learning, and held-out closed-loop evidence. |

## A concise interview narrative

"I worked across the robot-learning stack rather than only training a model: I connected VR teleoperation to a real arm through ROS 2, IK, and a safety-bounded command path; structured the resulting LeRobot data with explicit unit contracts; verified a V-JEPA 2.1 auxiliary-world-model integration on real tensors; and built a read-only OpenCV workflow to create auditable visual stage candidates. My next milestone is a controlled ACT baseline and paired ablation followed by safety-gated button-press trials."


## Research-email summary

I work on the engineering boundary between robot learning and physical execution. In a Quest-to-Piper button-press project, I integrated a safety-bounded VR/ROS 2/IK/daemon/SDK-CAN chain, turned its demonstrations into a unit-explicit LeRobot contract, and validated a frozen-teacher VLA-JEPA 2.1 auxiliary objective on real tensors. I also built a read-only visual review signal rather than presenting image cues as task success. The next controlled question is whether that auxiliary loss improves a matched ACT baseline, followed by safety-gated closed-loop evaluation.

## Claim, evidence, boundary, next experiment

| Claim | Evidence | Boundary | Next experiment |
| --- | --- | --- | --- |
| I can integrate a learning stack with a physical robot safely. | Quest→ROS 2→IK→guarded daemon→SDK/CAN chain exercised on a Piper arm. | Not a released controller or a robustness result. | Execute a fixed, operator-reviewed trial matrix. |
| I can make robot-learning data contracts auditable. | 40 episodes / 14,653 frames; two RGB views; 7D vectors; one degree-to-radian boundary. | No held-out benchmark result yet. | Freeze an episode split and ACT baseline. |
| I can distinguish a model-interface result from a performance result. | 386/12 V-JEPA migration; real-data gradient and offline [1,7,7] action probe. | Auxiliary loss reduction is not policy improvement. | Matched multi-seed ACT versus ACT+auxiliary ablation. |
| I can reason about endpoint feasibility instead of hand-waving latency. | Historical remote request-loop p50/p95 was 8.43/12.26 s over five samples; a tested benchmark harness reports p50/p95 with a no-actuation invariant. | The historical loop combines capture, network, server, and client work; it is not model-only latency. | Benchmark one reviewed offline callable on a fixed 6GB-GPU deployment contract. |
