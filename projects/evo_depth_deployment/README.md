# 04 · Evo-Depth deployment contract

## Problem solved
Inspect a predicted action chunk safely before any private execution layer.

## Key idea
- select a fixed chunk prefix;
- retain active dimensions only;
- limit the first jump against measured state;
- profile whole request loops before claiming endpoint feasibility.

## Core code
- [action-chunk contract](core/action_chunk.py): selection and delta clamp with no device access.
- [tests](../../tests/test_action_chunk.py): 25-step/7D and clamp regressions.

## Evidence
Fixed evaluation loss 0.8415→0.2449; `[50,24]`→25-step→first-7D audit; 13/13 offline checks; historical request p50/p95 8.43/12.26 s.

Read the [deployment evidence](evidence.md).

## Boundary and next test
The timing includes capture/network/server/client work, not model-forward time. Next: reviewed offline adapter benchmark.

