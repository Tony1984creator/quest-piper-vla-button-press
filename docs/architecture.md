# System architecture and safety boundary

## Verified control path

The project integrated a single-arm real-robot teleoperation path:

Quest headset
  -> right-controller pose / button interpretation
  -> B-gated relative-pose control
  -> ROS 2 joint-command topic
  -> Pinocchio and CasADi IK computation
  -> guarded Piper command daemon
  -> vendor SDK over CAN
  -> Piper arm

This path is presented as an interface-level architecture rather than a deployable controller. Network identities, transport configuration, executable commands, calibration values, and robot limits are intentionally omitted.

## Pose-control contract

The fixed headset supplies the tracking reference for the right controller; it does not directly command task motion. Under deliberate B enable, a stable controller anchor is captured and current controller pose is interpreted relative to that anchor. Releasing B holds the last valid target. A+B is a separate home/reset state.

Before IK, the client rejects stale tracking and pose discontinuities, applies frame mapping, short-window filtering, scaling, deadbands, workspace and end-effector-step checks, then seeds IK from the preceding valid joint solution. IK generates a candidate only. The daemon remains the sole actuator owner and applies the final command freshness, fault, and joint-step checks.

## Control contracts

| Boundary | Contract | Public evidence / rule |
| --- | --- | --- |
| VR to ROS 2 | Joint command and measured joint state are 7D: six arm joints plus gripper | The recorder validates named joint ordering before capture. |
| Teleoperation mode | B produces anchored relative control; release holds the last safe target | Tracking loss or a discontinuity never creates a new target from an old pose. |
| Dataset to kinematics | Dataset arm state/action values are stored in degrees; gripper follows its declared physical convention | Convert degrees to radians exactly once only at IK, FK, Jacobian, or model-computation boundaries. |
| IK to actuation | Targets flow through one daemon owning the hardware channel | The daemon runs at a fixed rate and rejects stale input. |
| Tracking loss | New VR input is cleared when tracking is unavailable | The last safe target is held; the system does not extrapolate a new command. |
| Learning to hardware | Model inference is separate from hardware command dispatch | Offline probes stay non-actuating; real trials require an explicit guarded evaluation path. |

## Data path

Teleoperation episode
  -> LeRobot episode metadata
  -> two RGB streams (top/up, wrist) + 7D state + 7D action
  -> episode-level split
  -> ACT action-chunk baseline
  -> optional VLA-JEPA auxiliary world-model loss
  -> offline action probe
  -> safety-gated closed-loop evaluation

The dataset has 40 episodes and 14,653 frames captured at 30 FPS, with two 640x480 RGB observations and 7D state/action vectors. These quantities describe the recorded corpus, not a held-out performance result.

## Why the daemon boundary matters

Real robots are not an ordinary inference endpoint. The learning component must not own CAN access or invent actuator commands from stale observations. The architecture therefore separates:

- perception and policy inference: produces candidate action chunks;
- supervision: checks freshness, state validity, limits, and operator authorization;
- actuation: a single guarded process owns the robot channel.

The public repository is deliberately not sufficient to operate a physical robot.