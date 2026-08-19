# Quest VR recording contract

## Scope

This public contract describes the read-only ROS 2 to LeRobot recording adapter
used in the Quest–Piper workflow. It omits private launch instructions, topic
endpoints, device paths, and dataset locations.

## Input contract

| Field | Contract |
| --- | --- |
| Command source | Named ROS 2 joint-command message |
| Measured source | Named ROS 2 joint-state message |
| Dimensionality | Seven values: six arm joints followed by gripper |
| Validation | Message type and joint-name ordering must be checked before capture |
| Storage | Observation state and action are float32 seven-dimensional vectors written at a configured fixed rate |

The recorder is observational: it neither owns an actuator channel nor performs
IK. Missing topics, stale data, or incompatible message types are explicit
recording errors.

## RGB provenance boundary

The stored corpus has two RGB observations, up and wrist, alongside its 7D
state/action records. Their storage-level index and timestamp alignment were
validated over 40 episodes and 14,653 frames. This is evidence of the saved
dataset contract, not evidence of exposure-level camera synchronization or
geometric calibration.

## Acceptance evidence

A recorded dataset must have a complete episode/global frame index, expected 7D
state/action schema, readable streams, and timestamps consistent with the
declared recording rate. Any later geometric component must introduce its own
versioned calibration contract.
