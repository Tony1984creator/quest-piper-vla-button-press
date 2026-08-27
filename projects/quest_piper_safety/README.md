# 01 · Quest–Piper safety boundary

## Problem solved
Reject stale or malformed candidate commands before any private actuation layer.

## Key idea
- one command owner owns transport;
- accept only fresh, finite 7D arm-plus-gripper candidates;
- reject rather than extrapolate after tracking loss or timeout.

## Core code
- [safety gate](core/safety_gate.py): `validate_command(...)` copies only a fresh finite 7D vector.
- [tests](../../tests/test_safety_gate.py): stale and NaN regression cases.

## Evidence
Quest → ROS 2 → IK → guarded daemon → SDK/CAN → Piper was exercised; the private daemon runs at 50 Hz with timeout/tracking protection.

Read the [integration evidence](evidence.md).

## Boundary and next test
This module has no ROS/CAN/SDK imports and cannot operate a robot. Next: private command/feedback timestamp alignment.

