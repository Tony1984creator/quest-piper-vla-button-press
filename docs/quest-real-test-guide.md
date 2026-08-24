# Quest–Piper real-test safety guide

## Purpose and public boundary

This guide abstracts the private, working-machine procedure into a
reviewable safety contract. It intentionally omits commands, host/device
identifiers, gains, workspace limits, calibration values, and recovery
operations. It must not be used as a standalone robot launch guide.

## Roles and modes

| Role or mode | Responsibility | Hardware boundary |
| --- | --- | --- |
| Quest/IK client | Maps current controller input into candidate joint targets | Does not own CAN by default |
| Guarded actuator | Checks authorization, freshness, feedback, limits, and faults before actuation | Exactly one process owns the hardware channel |
| Recorder | Observes command and measured-state streams at a fixed declared rate | Does not execute IK or write hardware |
| Operator | Clears the workspace, authorizes the trial, and can abort | Remains present for every guarded trial |

## Go/no-go before a guarded trial

- The workspace is clear, the arm is mechanically stable, and a stop procedure
  is known to the operator.
- The intended task, initial condition, policy/teleoperation version, and
  abort condition are recorded privately.
- Exactly one actuator is present; no recorder, demo, policy, or example node
  holds a second hardware channel.
- Controller tracking, command freshness, measured-state validity, and limit
  checks are current before motion begins.
- Begin with a low-risk, small-amplitude observation; do not use a learned
  action or a visual confirmation as a substitute for a safety gate.

## Interaction and abort contract

A deliberate hold-to-enable interaction starts new targets. Releasing it holds
the last safe target rather than creating a new target from missing tracking.
Tracking loss, stale input, invalid feedback, transport fault, limit violation,
or operator abort ends new target generation.

After an abort, preserve the relevant timestamps and logs. Review the failure
at the Quest input, ROS 2 transport, IK, supervisor, and actuator boundary
before another trial. Do not solve a fault by running a second daemon or by
bypassing freshness and limit checks.

## Recording and visual evidence

Recording is a read-only observer of command and measured-state streams. The
OpenCV visual-confirmation tool is also read-only: it may create annotated
video and CSV review artifacts, but it does not identify a target, prove
contact/retraction, or determine task success. See
[the visual-confirmation demo](quest-vr-opencv-demo.md).

## NERO separation

The NERO dual-arm work is a separate, pre-power roadmap. Reusable principles
are single actuator ownership, explicit namespaces, hold-to-enable,
freshness/timeout checks, and trial logs. Piper-specific process topology,
CAN configuration, gains, workspace limits, and real-arm evidence must not be
reused as NERO operating settings. See
[the NERO roadmap](nero-dual-arm-roadmap.md).

## What this guide establishes

It establishes a safety and evidence protocol for supervised evaluation. It
does not establish calibration quality, controller robustness, task success,
or permission for unattended operation.
