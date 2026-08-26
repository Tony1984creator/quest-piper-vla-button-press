# Historical remote-inference latency audit

## What was measured

One retained client log from 2026-07-23 recorded five successful **end-to-end remote policy requests** during an Evo-Depth/Piper evaluation path. The client recorded the elapsed time around image capture, request/response, and local client-side processing before reporting a 25-step safe action chunk.

| Samples | Minimum | p50 | p95 | Maximum | Mean |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 5.95 s | 8.43 s | 12.26 s | 12.86 s | 8.64 s |

The p95 uses linear interpolation on the five observed values: 12.86, 9.86, 6.08, 5.95, and 8.43 seconds.

## Correct interpretation

This is useful deployment evidence because it exposed a practical bottleneck: the measured request loop is far longer than a 30 FPS control period. It is **not** a model-forward latency benchmark and not a task-performance result. It combines at least image handling, remote transport, server inference, response parsing, and local client processing; the log is not sufficient to attribute time to a particular subsystem.

The historical client process included a robot integration path. Therefore this page intentionally makes **no assertion** about whether an individual request actuated hardware and does not characterize the audit as offline. Internal host information, device identifiers, task inputs, control settings, and raw logs are excluded.

## How this changes the next engineering step

The correct next target is not “make the headline latency lower” without diagnosis. Use the [offline inference benchmark protocol](offline-inference-benchmark.md) with a reviewed non-actuating adapter to separate preprocessing, model, postprocessing/safety, and total latency under a fixed input contract. Then decide whether the 6GB robot-side GPU supports a lower-latency inference path, a shorter action horizon, cached visual features, asynchronous execution, or a different model/runtime.

