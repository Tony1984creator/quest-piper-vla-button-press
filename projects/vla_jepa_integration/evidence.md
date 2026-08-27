# VLA-JEPA 2.1 migration evidence

## Upgrade record

The teacher-interface upgrade mapped 386 encoder tensors and deliberately reinitialized 12 unmatched tensors. The adapter owns the video-layout conversion from `[B,T,C,H,W]` to `[B,C,T,H,W]`; the teacher remains frozen while predictor/action components are audited separately.

## Measured probes

- real visual batch: `[1,8,3,480,640]`;
- action batch: `[1,7,7]`;
- 100-step world-model loss: 1.2344 → 1.1668.

The variable action loss supports only a compatibility and real-data-pilot conclusion; it does not establish policy quality, deployment, or task success.

