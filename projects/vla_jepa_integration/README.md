# 03 · VLA-JEPA 2.1 integration

## Problem solved

Turn a V-JEPA 2.0→2.1 upgrade into an explicit compatibility experiment: verify loading, preserve tensor semantics, audit trainable ownership, and separate a finite training probe from a robotics claim.

## Integration contract

- Video changes layout only at the adapter boundary: `[B,T,C,H,W] → [B,C,T,H,W]`.
- The frozen V-JEPA teacher supplies representation targets; Qwen, action, and predictor components are audited as trainable paths.
- The documented interface keeps Qwen/action width at 2048, uses 32 embodied tokens and 24 shifted dynamics-action tokens, and retains a 1024-dimensional JEPA representation.
- The migration changes the video grid from `(4,16,16)` to `(4,24,24)` while checking its token totals.

## Core code

- [layout and mapping contract](core/contracts.py): framework-light layout and frozen-teacher checks;
- [migration contract](core/migration_contract.py): validates the fixed upgrade invariants;
- [regression tests](../../tests/test_vla_jepa_contracts.py) and [migration tests](../../tests/test_migration_contract.py).

## Evidence and boundary

The migration mapped 386 teacher tensors and intentionally reinitialized 12 unmatched tensors. A real-data compatibility pilot completed 100 finite training steps with audited gradients and offline action shape `[1,7,7]`. It is not a trained policy result. See [migration evidence](evidence.md).

**Next acceptance gate:** compare ACT and the auxiliary predictive objective under the same episode split, evaluation procedure, and training budget.

