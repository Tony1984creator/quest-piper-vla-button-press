# Evo-Depth deployment evidence

## Offline action-path audit

The policy output audit uses a `[50,24]` candidate chunk, retains a 25-step execution window, and exposes only the first 7 active dimensions before any private adapter. A measured-state delta clamp guards the first action jump.

## Measured probes

- fixed evaluation loss: 0.8415 → 0.2449;
- 13/13 offline contract checks;
- retained historical whole-request timings: five samples, mean 8.64 s, p50 8.43 s, p95 12.26 s.

The request measurement spans capture, network, server, and client work. It is not model-forward latency or task-quality evidence.

