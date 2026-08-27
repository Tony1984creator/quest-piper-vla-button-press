# 02 · LeRobot data contract

## Problem solved
Prevent unit drift and frame-level leakage from invalidating robot-learning results.

## Key idea
- storage uses degrees;
- model/kinematics use radians at one explicit boundary;
- split complete episodes, never adjacent frames.

## Core code
- [unit token](core/data_contract.py): single-use degree→radian conversion.
- [tests](../../tests/test_data_contract.py): conversion and double-conversion regressions.

## Evidence
40 episodes, 14,653 frames at 30 FPS, two 640×480 RGB streams, and 7D state/action are recorded.

## Boundary and next test
This is a data protocol, not a generalization benchmark. Next: freeze episode-level manifests and publish a sanitized data card.

