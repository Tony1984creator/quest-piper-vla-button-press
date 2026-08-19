# Quest–Piper real-test safety guide

## Purpose and public boundary

This high-level safety and evaluation guide is derived from the private
real-test procedure. It is not a robot launch guide: commands, network details,
device identifiers, calibration values, controller gains, workspace limits, and
recovery operations are intentionally omitted. It must not be used to operate a
physical robot without a site-specific safety review.

## Operating modes

| Mode | Learning/control behavior | Hardware boundary |
| --- | --- | --- |
| Safe dry path | Reads Quest input, performs mapping and IK, and publishes a candidate joint command | Does not own CAN or enable the arm. |
| Guarded real evaluation | A separately authorized actuator process receives a fresh candidate command | One guarded process is the sole owner of the hardware channel. |
| Recording | Observes named command and measured-state topics for dataset construction | Does not run IK, start cameras, or write hardware commands. |

## Before a guarded trial

- An operator explicitly authorizes the trial and can use an emergency stop.
- The workspace is clear, the arm is stable, and the intended task, policy version,
  initial condition, and abort condition are recorded privately.
- Exactly one actuation owner is running; recording and policy inference do not
  obtain a second hardware channel.
- Command freshness, measured-state validity, limits, and tracking status are
  valid before motion begins.
- Start with low-risk, small-amplitude motion; do not use a learned policy as a
  substitute for the safety supervisor.

## Interaction and abort rules

The teleoperation interaction uses an explicit hold-to-enable gate. Releasing
the gate holds the last safe target rather than creating a new target from
stale or missing tracking data. Loss of tracking, stale commands, invalid
state, an actuation fault, or an operator abort ends new command generation.

After an abort, preserve the relevant logs and inspect the failure at the VR,
ROS 2, IK, supervisor, and actuator boundaries. Do not repeat a trial until
the failure mode and responsible operator have been reviewed.

## What this guide establishes

It establishes the intended control ownership and safety-gate design. It does
not establish task success, controller robustness, calibration quality, or
permission for unattended operation.
