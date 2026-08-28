# VLA-JEPA 2.1 migration evidence

## Compatibility work completed

The teacher-interface upgrade mapped **386** encoder parameters and deliberately reinitialized **12** unmatched parameters. Strict-load checks completed for Qwen (626/626), the action head (248/248), and the predictor (156/156). The teacher encoder remained frozen.

## Dataset boundary

The pilot uses the private **Elevator VLA dataset** (952 episodes, 188,418 frames, 12 task groups), not the 40-episode Quest VR dataset. The larger aggregate is reported only to identify the experiment asset; samples, task text, and metadata are not public.

## Real-data pilot

- two-view visual input: `[1,8,3,480,640]` per view;
- combined teacher feature: `[1,2304,2048]`;
- context, target, and prediction tensors: `[1,1728,2048]`;
- action input/output probe: `[1,7,7]`;
- 100/100 finite training steps, with finite gradients for Qwen, action, and predictor paths;
- first-ten versus last-ten mean world-model loss: **1.2343 → 1.1660**.

Action loss remained variable (approximately 1.45–58 across the pilot), so these results support interface compatibility and a real-data training smoke test only. No robot command was produced, and no policy, deployment, or task-success conclusion is claimed.

