# OpenCV visual pre-annotation

## Scope

The portable utility looks for a visually illuminated elevator button in wrist-camera frames. It is intentionally read-only with respect to the source dataset and cannot start CAN, command the robot, or alter an episode.

## Detector rule

For each BGR frame:

1. convert to HSV;
2. threshold a configurable orange range;
3. find connected components;
4. reject components touching a small image-edge margin;
5. retain the largest component only if it has at least 1,000 pixels;
6. emit a stage candidate only when it remains active for at least three consecutive frames.

The output is a compact segment record with start/end/representative frame, duration, confidence, and bounding box.

## Validation evidence

The full read-only pass examined 12 wrist-camera videos comprising 188,418 frames. It generated 421 temporally stable `press_confirmed_visual` candidates. A stratified manual audit sampled 48 candidates (four from each video chunk): 48 were judged yes, 0 no, 0 uncertain.

The observed audit precision was therefore 48/48 in this sample. This is evidence that the heuristic can prioritize review, not evidence of universal detector precision or task success.

## Next validation step

Join candidate segments to episode/task metadata; verify the requested floor; and combine approach, contact, retraction, and human-reviewed outcome labels. This yields a task-level evidence chain instead of a single visual event.
