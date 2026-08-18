# Data-contract QC evidence

## Scope and boundary

This record describes a private, hardware-independent validation run over the
Quest/LeRobot dataset. It reports only aggregate evidence; raw episodes,
videos, device paths, calibration material, and robot configuration remain
private.

The validation checks metadata and stored observations. It does not assert
camera exposure synchronization, geometric calibration quality, policy
performance, or real-robot safety.

## Verified run

The validator checked one recorded corpus with the following result:

```json
{
  "episodes_checked": 40,
  "failures": [],
  "fps": 30,
  "frames_checked": 14653,
  "passed": true,
  "timestamp_tolerance": 0.01
}
```

The checked contract requires:

* 7D `observation.state` and 7D `action` vectors;
* two 480x640x3 RGB streams (`up` and `wrist`), with an archived video for
  each stream;
* a complete episode-level frame index beginning at zero;
* a complete global index;
* per-episode timestamp increments within 0.01 seconds of 1/30 second.

This QC is a prerequisite for a frozen episode-level split, not a replacement
for that split. Camera calibration is not part of this pixel-policy contract;
if a later component uses geometric projection or pose estimation, it must
introduce a versioned calibration contract and validation separately.

## Target-button audit status

The separate visual pre-annotation workflow has joined all 421 stable visual
candidates to an episode and a task-text target floor. The generated
target-identity review table begins with every row marked `pending`; no row is
promoted to task success by this join. The next gate is human confirmation of
the illuminated button's identity, then evidence of contact and retraction.
