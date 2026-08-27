# Dataset and unit-contract evidence

## Recorded dataset

The private LeRobot dataset contains 40 episodes and 14,653 frames at 30 FPS, with two 640×480 RGB streams and 7D joint state/action fields.

## Contract

- recorded state/action storage: degrees;
- IK, FK, Jacobian, and model-side computation: radians;
- one conversion boundary during loading, protected by a single-use token;
- train/validation/test partitions must be complete episodes, never adjacent frames.

This is a reproducibility and data-QC contract, not a data release or a generalization result.

