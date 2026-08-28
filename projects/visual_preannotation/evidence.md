# Visual pre-annotation evidence

## Review problem

Wrist-camera footage needs a scalable review cue without confusing a bright visual event with task completion.

## Pipeline and audit

HSV thresholding, non-edge connected-component filtering, a ≥1,000-pixel screen, and a ≥3-frame temporal confirmation emitted **421** stable review candidates across **12** wrist videos / **188,418** frames. A deterministic stratified audit selected 48 examples (four per source chunk): **48 visually positive, 0 negative, 0 uncertain**.

The videos belong to the Elevator VLA dataset; this aggregate must not be combined with the smaller Quest VR dataset metrics.

The audit supports only this narrow statement: every sampled candidate visibly satisfied the retained visual rule. It does not estimate task success, button contact, target identity, or generalization accuracy.

## Rejected alternative

A single-template number matcher was tested but not retained: occlusion and viewpoint changes made the template too brittle. The current pipeline therefore produces review cues, leaving outcome and failure-reason attribution to downstream human labeling.

