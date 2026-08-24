# OpenCV visual pre-annotation

## Scope

The portable utility looks for a visually illuminated elevator button in
wrist-camera frames. It is intentionally read-only with respect to the source
dataset and cannot start CAN, command the robot, or alter an episode.

## Single-frame detector

`opencv_preannotation/global_confirmed_detector.py` is position-independent:
it searches the full BGR frame rather than a fixed wrist-camera ROI. For each
frame it:

1. converts BGR to HSV and thresholds a configurable orange range;
2. finds connected components;
3. rejects components that touch an image-edge margin;
4. keeps the largest remaining component only when it has at least 1,000
   orange pixels;
5. returns `is_active`, area-based `confidence`, `orange_pixels`, and an
   image-space bounding box.

The retained regression tests cover an illuminated button at an arbitrary
in-frame location, small orange noise, and a large orange image-edge artifact.
They are a detector-contract check, not a task benchmark.

## Temporal pre-annotation evidence

The separate full read-only pass examined 12 wrist-camera videos comprising
188,418 frames. It generated 421 temporally stable
`press_confirmed_visual` candidates after requiring at least three consecutive
frame hits. A stratified manual audit sampled 48 candidates (four from each
video chunk): 48 were judged yes, 0 no, and 0 uncertain.

A private bookkeeping join associates those 421 candidate records with episode
metadata and task text. It is deliberately not published in this repository,
does not read or identify a button label from pixels, and must not be treated
as a target-identity or success label.

The observed 48/48 audit result is evidence that the heuristic can prioritize
review in that sample. It is not evidence of universal detector precision or
task success.


## Visual-confirmation demonstration contract

A local, read-only Quest demonstration makes the temporal rule inspectable without
exposing raw robot data. Its reference flow is:

```text
wrist-camera MP4 -> BGR frames -> HSV / connected components
  -> largest non-edge orange region with >= 1,000 pixels
  -> active-frame counter -> visual confirmation at >= 3 consecutive hits
  -> annotated MP4 plus frame-level and event-level CSV
```

The public repository retains only the portable detector and temporal-filter
logic. The demonstration's videos, task text, device paths, and robot
configuration remain private. The annotated video and CSV are visual-review
artifacts: they do not command hardware and do not turn a visual candidate into
a target-identity, contact, retraction, or task-success label.

## Strict capability boundary

`press_confirmed_visual` means only that a visually illuminated orange button
candidate is present. It does **not** identify the printed floor, prove it is
the requested target by vision, prove contact force or approach/retraction, or
determine `success` / `failure_reason` / `task_stage`.

The next validation work is separate from this detector: define reviewed task
labels, fix the episode-level split, and combine visual evidence with guarded
state/action and trial evidence under the real-robot protocol.
