# Quest VR visual-confirmation demo

## Purpose

This portable, read-only utility turns a wrist-camera video into visual-review
artifacts for the elevator-button project. It processes frames only; it does
not open CAN, start ROS 2, command a robot, or modify the source video.

The pipeline is:

```text
MP4 -> BGR frames -> HSV orange connected components
    -> largest non-edge region with >= 1,000 pixels
    -> three consecutive active frames
    -> annotated MP4 + frame CSV + event CSV
```

A confirmation means only that a sufficiently large orange illuminated region
persisted in the image. It does not identify a floor, prove contact, retraction,
or requested-task success.

## Run on a copy of a video

```bash
python -m opencv_preannotation.visualize_press_confirmation \
  --input-video /path/to/wrist.mp4 \
  --output-video outputs/annotated.mp4 \
  --output-frames-csv outputs/frames.csv \
  --output-events-csv outputs/events.csv \
  --required-consecutive-frames 3
```

The frame CSV records candidate state, streak length, bounding box, orange-pixel
count, and confidence. The event CSV records the first frame and confirmation
frame for each newly confirmed run. Keep the outputs outside the source dataset.

## Batch handoff: MP4 directory to review queue

The delivered batch entry point accepts a directory of wrist-camera MP4 files
and writes two compact review artifacts. It is also read-only: it does not
modify source videos, start ROS 2, open CAN, or command hardware.

```bash
python opencv_preannotation/run_full_preannotation.py \
  --input-directory /path/to/wrist_video_directory \
  --output-directory outputs/run_001 \
  --min-orange-pixels 1000
```

- `press_confirmed_visual_segments.jsonl`: one record per temporally stable
  visual segment, including frame range, representative bounding box/confidence,
  source chunk, and an empty `human_label` field for subsequent review.
- `preannotation_summary.csv`: one row per input MP4 with its frame count and
  candidate-segment count.

`press_confirmed_visual` means only that a sufficiently large orange region was
visually active for at least three consecutive frames. It is not a target-floor,
contact, retraction, or task-success label.
## Test

```bash
python -m unittest discover -s tests -v
```

The renderer test creates a synthetic video, checks that confirmation begins
only on the third consecutive active frame, and verifies one event record. The
batch-entry test creates a synthetic MP4 and verifies one JSONL segment plus one
CSV summary row. Neither test uses robot hardware or private data.
