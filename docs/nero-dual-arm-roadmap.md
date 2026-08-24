# NERO dual-arm Quest roadmap (pre-power)

## Current status

The NERO dual-arm hardware has been mechanically assembled. A dedicated new host
has not yet been prepared. No power-on, CAN, ROS 2, PikaAnyArm, Quest, motion,
or dual-arm teleoperation result is claimed in this record.

This is a preparation roadmap, not an operating procedure. It intentionally
omits device addresses, CAN frame definitions, credentials, controller gains,
and robot-specific launch commands.

## Intended architecture

```text
Quest left/right controller poses
  -> ROS 2 adapter with explicit left/right namespaces and hold-to-enable gates
  -> PikaAnyArm delta-pose / inverse-kinematics layer
  -> independent left and right NERO ROS 2 drivers
  -> independent CAN interfaces
  -> NERO dual arms
```

The existing Quest–Piper work supplies reusable engineering principles:
candidate generation is separated from actuation, tracking freshness is a safety
signal, recording does not write hardware, and exactly one actuator owns each
hardware channel. It does **not** supply drop-in Piper daemon, CAN, workspace,
or gain settings for NERO.

## Evidence-gated sequence

| Gate | Required evidence before advancing | Current state |
| --- | --- | --- |
| 0. First-power preflight | Mechanical fixation, power/connector review, clear workspace, operator and stop procedure confirmed | Not started |
| 1. Per-arm communication | One driver and one feedback stream per arm; no CAN ownership conflict | Not started |
| 2. Hardware-free smoke | Quest left/right mapping reaches named Pika inputs and IK output without enabling an arm | Not started |
| 3. Guarded single-arm motion | Reviewed limits, low-risk motion, feedback/timeout/abort log | Not started |
| 4. Guarded dual-arm trial | Independent arm ownership, collision and operator review, synchronized trial log | Not started |

The vendor manual remains the authority for physical installation, power,
calibration, modes, and recovery. In particular, simulation, a URDF, a Web UI,
or a successful Piper trial are not substitutes for NERO hardware acceptance.

## Public dependencies

- [PikaAnyArm (ROS 2 branch)](https://github.com/agilexrobotics/PikaAnyArm/tree/ros2)
- [agx_arm_ros](https://github.com/agilexrobotics/agx_arm_ros)
- [agx_arm_urdf](https://github.com/agilexrobotics/agx_arm_urdf/tree/main/nero)
- [pyAgxArm](https://github.com/agilexrobotics/pyAgxArm)
