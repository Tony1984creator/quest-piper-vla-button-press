# VLA-JEPA 2.0 to 2.1 migration contract

## Scope

This document records the interface contract used to upgrade the frozen visual
teacher in an isolated VLA-JEPA lab. It is a compatibility and training-path
record, not a benchmark claim. Dataset paths, checkpoints, model files, task
text, runtime settings, and proprietary implementation details are omitted.

## Stable and changed interfaces

| Component | Migration status | Training role |
| --- | --- | --- |
| Qwen vision-language interface | Retained at hidden width 2048 | Trainable in the verified pilot |
| Action head | Retained from the VLA checkpoint | Trainable |
| Action-conditioned video predictor | Retained as the VLA-specific predictor | Trainable |
| V-JEPA visual encoder | Replaced by the 2.1 encoder | Frozen teacher, excluded from gradient updates |
| V-JEPA built-in predictor | Not used for the VLA world-model loss | Not substituted for the action-conditioned predictor |

The 2.1 migration changes the teacher visual-token grid rather than the Qwen
conditioning width. The verified action-conditioning interfaces remain 24
dynamics-action tokens and 32 embodied-action tokens, each at width 2048.

## Required adapters

- Convert video layout at the V-JEPA boundary from batch-time-channel-height-width
  to the encoder's channel-time layout.
- Concatenate two view features into the width expected by the VLA predictor.
- Account for tubelet temporal reduction and the one-step JEPA shift: the
  predictor receives 24 action tokens for the three context positions.
- Adapt positional-grid handling to the new visual grid; do not silently reuse
  the older grid assumptions.
- Pad a 7D Piper state to the retained 8D action-head state interface in one
  explicit adapter; do not change the pretrained state encoder merely to hide
  the mismatch.
- Use a video decoding path compatible with the installed data loader and
  runtime; decoder compatibility is a separate reproducibility contract.

## Verified checkpoints and gradient boundaries

The isolated validation found 386 visual-encoder tensors that could be mapped
and 12 that required reinitialization. Qwen, action head, and the
action-conditioned predictor each passed their own strict-load checks in the
pilot setup. The teacher stayed forward-only, while Qwen, action head, and
predictor had finite gradients.

The aggregate 100-step real-data pilot produced finite losses and a
non-actuating action chunk of shape [1, 7, 7]. This validates the graph,
adapters, checkpoint loading, and offline path. It does not show policy
convergence, action safety, task success, or a benefit over a baseline.

## Next evidence required

1. Freeze an episode-level train/validation split and retain configurations,
   seeds, and checkpoint-selection rules.
2. Compare matched baseline and auxiliary-loss runs across multiple seeds.
3. Apply normalization inversion, joint limits, rate limits, and offline rollout
   checks before any hardware evaluation.
4. Keep the training server non-actuating; a guarded, supervised robot protocol
   is a separate stage.
