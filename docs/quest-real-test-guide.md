# Quest–Piper real-test safety guide

## Scope and public boundary

This guide describes the verified single-arm Quest-to-Piper test contract. It records the real control modes and safety logic, but deliberately omits host and device identifiers, CAN recovery commands, workspace limits, launch commands, and proprietary source. It is not a standalone robot operating procedure.

## Current control roles

Quest headset + right controller
  -> pose / button stream
  -> ROS 2 pose-control and IK client
  -> joint-command topic
  -> guarded Piper daemon
  -> SDK / CAN
  -> single Piper arm

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Quest pose-control client | Right-controller pose processing, relative-pose mapping, filtering, workspace checks, and IK | Defaults to a non-hardware dry path. |
| Guarded daemon | Owns the only actuator channel; checks fresh commands, faults, and final joint-step limits | The only process allowed to reach the SDK/CAN boundary. |
| Recorder | Observes command and measured-state streams, then writes the dataset | Never repeats IK or writes hardware. |
| Operator | Clears the workspace, authorizes a trial, and can abort it | Remains present in every guarded trial. |

## Deliberate interaction model

- The headset is fixed and only the right controller is used for task motion; headset pose is not used as a direct control input.
- Holding B starts a new relative-pose session only after a short debounce and stable-pose anchor. The arm follows controller motion relative to that anchor, not controller world pose.
- Releasing B holds the last valid target. It does not generate a new target from stale tracking.
- A+B is a separate, deliberate home/reset request. Home motion is not inferred from ordinary controller tracking.
- Re-engaging B establishes a new anchor, preventing a controller reposition from becoming an unintended arm jump.

## Go/no-go and abort contract

Before a guarded trial: clear the workspace, verify a known stop procedure, record the task/policy/initial condition/abort rule privately, ensure exactly one daemon owns actuation, and verify current tracking, command freshness, measured state, limits, and feedback.

New target generation stops on tracking loss, stale input, invalid state, transport fault, limit violation, or operator abort. Preserve logs and timestamps, then diagnose the issue at the input, ROS 2, IK, supervisor, and actuator boundary before another trial. Do not bypass checks or add a second daemon to work around a fault.

## Recording and visual evidence

A completed episode records the command target as action and measured arm state as observation, together with the declared task and two RGB observations. The recording path is read-only with respect to actuation. The visual-confirmation tool is also read-only: it produces review evidence only and does not identify the requested target, prove contact/retraction, or determine success.

## What this establishes

The recorded evidence establishes a safety-gated teleoperation and collection path. It does not establish calibration quality, policy robustness, task success, or unattended operation.