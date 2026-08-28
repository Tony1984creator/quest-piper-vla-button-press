# Quest–Piper integration evidence

## Engineering problem

Translate VR controller intent into a robot-control path while preventing stale tracking, malformed values, and multiple competing processes from reaching the actuator layer.

## Verified integration

Quest controller interpretation → ROS 2 interface → Pinocchio/CasADi IK → guarded command daemon → private Piper SDK/CAN transport → one robot arm. The command owner was operated at 50 Hz and rejected new targets on tracking loss or timeout.

## Public safety contract

- one daemon owns private transport;
- a candidate must be fresh, finite, and exactly 7D;
- the gate rejects rather than predicts or extrapolates;
- no public file contains configuration, calibration, or command code for a physical device.

## Scope

This supports a systems-integration claim and demonstrates the safety boundary used around it. It does not claim public hardware reproducibility, a whole-body TeleOpIt implementation, or guarded closed-loop task success.

