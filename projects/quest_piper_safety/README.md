# 01 · Quest–Piper safety boundary

## Problem solved

Separate human tracking, kinematics, and robot transport so incomplete or stale input never becomes an unchecked actuator request.

## Engineering decisions

- A single private daemon owns robot transport, eliminating competing writers.
- The public boundary accepts only a fresh, finite 7D arm-plus-gripper candidate.
- Tracking loss, timeout, and malformed values cause rejection rather than extrapolation.
- VR intent, ROS 2 messaging, IK, safety review, and robot transport remain distinct layers.

## Core code

- [safety gate](core/safety_gate.py): copies only a fresh finite 7D vector;
- [regression tests](../../tests/test_safety_gate.py): covers stale candidates and non-finite values.

## Evidence and boundary

The private interface chain from Quest input through ROS 2, IK, a guarded command owner, and robot transport was exercised. The public code has no ROS, CAN, SDK, calibration, or device dependencies and cannot operate a robot. See [integration evidence](evidence.md).

**Next acceptance gate:** preserve timestamped command/feedback evidence behind the same private gate before reporting any closed-loop outcome.

