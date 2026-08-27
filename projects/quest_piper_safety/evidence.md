# Quest–Piper integration evidence

## Engineering problem

Translate Quest controller intent into a private robot-control path without allowing stale tracking, malformed values, or competing processes to reach the actuator layer.

## Verified integration

Quest controller pose and button interpretation → ROS 2 → Pinocchio/CasADi IK → guarded command daemon → Piper SDK/CAN → single Piper arm. The private daemon runs at 50 Hz and rejects commands on tracking loss or timeout.

## Public safety contract

- one daemon owns private transport;
- candidate commands must be fresh, finite, and exactly 7D;
- safety gate rejects rather than extrapolates;
- public code contains no ROS, CAN, SDK, device, calibration, or actuation configuration.

## Scope

This proves an exercised systems-integration path and a testable public safety boundary. It does not claim public hardware reproduction or guarded closed-loop button-task success.

