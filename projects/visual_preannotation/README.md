# 05 · Visual pre-annotation

## Problem solved
Reduce wrist-video review while keeping a bright visual event separate from task success.

## Key idea
- HSV threshold → non-edge largest component → ≥1,000 pixels;
- require ≥3 consecutive frames;
- emit reviewable `press_confirmed_visual`, never `success=true`.

## Core code
- [detector](core/global_confirmed_detector.py), [temporal filter](core/temporal_filter.py), [event builder](core/preannotation.py).
- [tests](../../tests/test_preannotation.py) and [detector tests](../../tests/test_global_confirmed_detector.py).

## Evidence
12 wrist videos, 188,418 frames, 421 stable candidates; stratified audit 48 yes / 0 no / 0 uncertain.

Read the [visual-review evidence](evidence.md) and use the read-only [tools](tools/).

## Boundary and next test
No floor identity, contact, or success is inferred. Next: join target identity, contact/retraction, and human-reviewed outcomes.

