# Visual pre-annotation evidence

## Review problem

Wrist-camera footage needs a scalable review cue without confusing a visible bright event with task completion.

## Pipeline and aggregate

HSV thresholding, non-edge connected-component filtering, a ≥1,000-pixel screen, and a ≥3-frame temporal confirmation emitted 421 review candidates across 12 wrist videos / 188,418 frames. A stratified audit of 48 sampled candidates recorded 48 visually positive, 0 negative, and 0 uncertain.

`press_confirmed_visual` is a review cue only. It never implies floor identity, button contact, physical success, or an actuated robot command.

