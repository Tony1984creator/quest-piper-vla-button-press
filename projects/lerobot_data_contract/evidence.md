# Dataset and unit-contract evidence

## Recorded-data snapshot

The private LeRobot recording set contains **40 episodes** and **14,653 frames** at **30 FPS**. Every frame carries two 640×480 RGB streams and 7D joint state/action fields in a consistent joint order.

## QC checks completed

- each episode starts at frame zero and global frame indices have no gaps;
- both RGB streams have the same aggregate frame count and nominal frame rate;
- adjacent timestamps are checked against 1/30 s with a 0.01 s tolerance;
- state/action fields are finite, float-compatible 7D vectors;
- degree storage is converted once to radians only for IK, FK, Jacobian, and model-side computation.

The public [episode-integrity validator](core/episode_integrity.py) captures the metadata-level portion of this QC process. It does not include demonstrations, video, manifests, or loader credentials.

## Scope

This is reproducibility evidence for a robot-data interface. It is not a data release, a benchmark, or a claim that a learned policy generalizes.

