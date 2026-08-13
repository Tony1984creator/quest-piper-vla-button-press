# VLA-JEPA 2.0 to 2.1: upgrade and measured probes

## Upgrade objective

The goal was not to replace the action policy with a generic world model. The experiment adds an action-conditioned auxiliary predictive objective while retaining a deployable visual-language-to-action route.

```text
images + language
  -> Qwen3-VL interface
  -> action model / Action DiT
  -> 7-step, 7D action chunk

images (+ action-conditioned tokens during training)
  -> frozen V-JEPA 2.1 teacher encoder
  -> trainable predictor / adapter
  -> world-model auxiliary loss
```

At deployment, the V-JEPA teacher and auxiliary world-model objective are not used to issue a hardware command. The select-action path remains image/language to action chunk.

## Static interface mapping

| Item | Result |
| --- | --- |
| Existing encoder tensors mapped to the 2.1 interface | 386 |
| Tensors requiring re-initialization | 12 |
| Old layer-normalization tensors intentionally ignored | 2 |
| Input adapter | `[B, T, C, H, W] -> [B, C, T, H, W]` |
| Teacher contract | frozen / `no_grad` |

The mapping was validated as a static compatibility step before real-data execution.

## Measured training probes

| Probe | Evidence | Interpretation |
| --- | --- | --- |
| Joint training smoke | Action loss 4.0044; world loss 1.2142; total 4.1258 | Gradient flow was verified for Qwen/action head/predictor while the teacher remained frozen. |
| Real-data smoke | Input views `[1,8,3,480,640]`; actions `[1,7,7]`; state `[1,7]`; action 8.6696; world 1.2344; total 8.7930 | Real dataset tensors traversed the intended contract. |
| Three-step continuation | Total loss 8.7930 -> 4.5576 -> 4.9161 | A short run checks execution continuity, not convergence. |
| Diverse samples | Indices 0, 17,893, 99,504; total losses 8.7930, 11.1796, 3.3298 | Samples are heterogeneous; no aggregate accuracy claim is made. |
| 100-step pilot | World loss 1.2344 -> 1.1668; final action loss 13.684 | Auxiliary loss decreased, but the action loss is variable; the experiment is preliminary. |
| Offline action probe | Action chunk `[1,7,7]`; no hardware commands sent | Inference shape and non-actuation boundary were verified. |

The saved pilot checkpoint was approximately 5.5 GB and is intentionally excluded from version control.

## Fixed ablation protocol

To claim an effect from the auxiliary objective, use this paired protocol:

1. Freeze one episode-level split and preprocessing contract.
2. Train ACT baseline and ACT + VLA-JEPA auxiliary loss with matched seeds, action horizon, steps, batch size, and augmentation.
3. Select each model only on validation evidence.
4. Compare held-out action metrics and the same safety-gated closed-loop trial suite.
5. Report mean, dispersion, sample count, failure categories, and qualitative rollouts—not loss alone.

Until this protocol is complete, the verified result is an integration and optimization-path result, not a performance advantage claim.
