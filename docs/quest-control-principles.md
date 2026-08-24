# Quest VR pose-control principles

## From controller pose to a safe joint candidate

Quest inside-out tracking
  -> right-controller 4x4 pose + buttons
  -> relative-pose anchor under B gate
  -> coordinate mapping and pose conditioning
  -> Pinocchio / CasADi IK
  -> ROS 2 joint-command topic
  -> guarded daemon final limit
  -> Piper arm

The headset supplies the tracking reference for the right controller; its own pose is not a task-motion input. The implementation uses the current right-controller pose rather than treating camera frames or headset motion as a robot-control signal.

## Relative pose, not absolute teleoperation

When B is deliberately held, the system records a stable controller anchor and computes the desired motion as the current controller pose relative to that anchor and the robot reference pose:

target_pose = robot_reference × inverse(controller_anchor) × controller_current

Releasing B holds the last valid target. Re-pressing B creates a new anchor. This separation prevents a controller being moved while disengaged from creating a discontinuous robot motion on re-entry. A+B is handled as an explicit home/reset state, separate from B-controlled task motion.

## Conditioning pipeline

Each control cycle reads the controller pose/button state, rejects stale or discontinuous input, maps the Quest frame to the robot task frame, compensates the wrist pivot, filters pose history, computes B-relative pose, applies scaling/workspace/end-effector limits/deadbands/smoothing, solves IK from the prior valid joint solution, and publishes a joint candidate. The daemon then applies the final actuator-side limit.

Short-window filtering and deadbands suppress hand tremor. Discontinuity rejection keeps the preceding valid state; it is a prompt to release B, re-establish stable tracking, and anchor again, not a reason to relax the safety threshold.

## IK and actuation separation

Pinocchio, CasADi, and IPOPT produce a six-joint solution from a target 4x4 end-effector pose. The prior valid joint solution seeds the next solve to reduce branch jumps. IK checks solver status, joint constraints, and abnormal jumps; it does not own CAN.

The ROS 2 candidate contains six arm joints plus gripper. The guarded daemon runs at a fixed command rate, applies its final per-step limit, and is the only component that reaches the SDK/CAN boundary.

## Data and evidence boundary

The recorder observes joint command as action and measured joint state as observation; it does not recreate IK or open an actuator channel. Dataset arm state/action are stored in degrees, with gripper data in its declared physical convention. Conversion to radians has exactly one owner at a kinematic or model-computation boundary.

A correct pose-control graph, finite IK output, or an offline action chunk is not a robot-success claim. Closed-loop success requires a guarded trial, reviewed evidence, and explicit success/failure/stage labels.