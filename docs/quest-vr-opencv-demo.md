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

## Test

```bash
python -m unittest discover -s tests -v
```

The renderer test creates a synthetic video, checks that confirmation begins
only on the third consecutive active frame, and verifies one event record. It
does not use robot hardware or private data.
