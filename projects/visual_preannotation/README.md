# 05 · Visual pre-annotation

## Problem solved

Reduce wrist-video review effort while preserving the distinction between a visible screen event and an actual task outcome.

## Retained method

- HSV thresholding finds an orange visual region.
- A non-edge connected-component filter retains the largest interior candidate only when it exceeds 1,000 pixels.
- A three-frame temporal rule turns frame evidence into a stable review candidate.
- Deterministic stratified sampling selects audit examples across every source chunk.

## Core code

- [detector](core/global_confirmed_detector.py), [temporal filter](core/temporal_filter.py), and [event builder](core/preannotation.py);
- [review sampler](core/review_sampling.py), which is dependency-free and preserves the original records;
- [pipeline tests](../../tests/test_preannotation.py), [detector tests](../../tests/test_global_confirmed_detector.py), and [sampling tests](../../tests/test_review_sampling.py).

## Evidence and boundary

The pipeline emitted 421 review candidates from 12 wrist videos / 188,418 frames. A stratified audit found all 48 sampled candidates visually valid. A single-template digit matcher was evaluated and discarded because occlusion and viewpoint changes made it unreliable. See [visual-review evidence](evidence.md).

`press_confirmed_visual` remains a review cue only; it does not assert target identity, contact, retraction, robot command, or success.

