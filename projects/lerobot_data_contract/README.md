# 02 · LeRobot data contract

## Problem solved

Make collected demonstrations trustworthy inputs to a model comparison: one unit boundary, complete-episode splits, and independently checkable frame metadata.

## Design decisions

- Store joint state/action in degrees; convert to radians exactly once at the model or kinematics boundary.
- Split complete episodes rather than adjacent frames, preventing temporal leakage between training and validation.
- Validate global indices, per-episode frame continuity, and nominal frame timing before a loader consumes the data.

## Core code

- [single-use conversion token](core/data_contract.py): blocks accidental repeated degree-to-radian conversion;
- [episode-integrity validator](core/episode_integrity.py): checks frame and timestamp metadata without opening video or accessing hardware;
- [regression tests](../../tests/test_data_contract.py) and [integrity tests](../../tests/test_episode_integrity.py).

## Evidence and boundary

The private recording set contains 40 episodes and 14,653 frames at 30 FPS, two 640×480 RGB streams, and aligned 7D state/action fields. This establishes a documented data contract, not a released dataset or a generalization result. Details are kept in [dataset evidence](evidence.md).

**Next acceptance gate:** freeze episode-level manifests, retain the QC report, and compare policies only on the same held-out episodes.

