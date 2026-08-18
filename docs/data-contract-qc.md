# Data-contract QC evidence

## Scope and boundary

This record describes a private, hardware-independent validation run over the
Quest/LeRobot dataset. It reports only aggregate evidence; raw episodes,
videos, device paths, calibration material, task text, and robot configuration
remain private.

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

## Visual-preannotation boundary

A private analysis joined 421 temporally stable visual-candidate records to
episode metadata and task text. That join is a bookkeeping aid only: it is not
a visual reading of a button label, is not published as a reusable artifact,
and does not change the detector's claim.

The current public scope is a position-independent single-frame detector for a
sufficiently large orange illuminated region. It returns a visual candidate and
image-space bounding box only. Three regression tests cover an in-frame button,
small orange noise, and a large image-edge artifact.

This evidence does not identify the printed floor, link a visual candidate to a
requested target by vision, establish contact or retraction, or establish task
success. Those questions remain evaluation-stage work and require separate task
labels, reviewed evidence, and the guarded closed-loop protocol.
