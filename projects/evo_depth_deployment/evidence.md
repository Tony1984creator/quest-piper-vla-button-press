# Evo-Depth deployment evidence

## Offline action-path audit

The public audit starts from a `[50,24]` candidate chunk, retains a 25-step execution window, and exposes only the first 7 active dimensions to a hypothetical private adapter. A measured-state delta clamp bounds the first requested change. The public module has no robot endpoint or device dependency.

## Controlled pilot result

The action-head-only controlled pilot ran for 300 steps. Under the same fixed **187-batch** real-data evaluation protocol, mean masked-flow loss changed from **0.841452** (reference) to **0.244856** (tuned); the corresponding best observed values were 0.470703 and 0.091797.

This comparison uses a fixed validation list and seed. It is an offline loss result, not an action-quality, latency, or task-success metric.

## Timing boundary

Earlier diagnostic requests measured five whole capture/network/server/client loops (mean 8.64 s, p50 8.43 s, p95 12.26 s). Those values are retained only to show why endpoint-loop timing must not be presented as model-forward latency.

