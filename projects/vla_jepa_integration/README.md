# 03 · VLA-JEPA 2.1 integration

## Problem solved
Upgrade the teacher interface without silently changing layout, optimizer ownership, or deployment path.

## Key idea
- `[B,T,C,H,W] → [B,C,T,H,W]` only at the adapter;
- teacher frozen; Qwen/action/predictor gradients audited;
- world-model loss supervises training and never directly actuates.

## Core code
- [interface contract](core/contracts.py): framework-light layout and mapping validators.
- [tests](../../tests/test_vla_jepa_contracts.py): layout and frozen-teacher regressions.

## Evidence
386 tensors mapped, 12 reinitialized; real views `[1,8,3,480,640]`; 100-step world loss 1.2344→1.1668.

Read the [migration evidence](evidence.md).

## Boundary and next test
Variable action loss means no policy gain is claimed. Next: matched ACT versus auxiliary-loss ablation.

