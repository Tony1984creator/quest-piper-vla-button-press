# Offline inference benchmark protocol

## Purpose and scope

`benchmarks.offline_latency` measures a Python callable that is already known to be offline and non-actuating. The tool does not import ROS, CAN, a robot SDK, or a model framework. It cannot make an unsafe policy safe; its role is to make a safe inference path measurable.

Every report contains `hardware_commands_sent: false`. Do not adapt a callable that opens a daemon, publisher, SDK, serial port, CAN socket, or robot API.

## Report fields

| Field | Meaning |
| --- | --- |
| `end_to_end.p50_ms`, `end_to_end.p95_ms` | Wall-clock time around one callable invocation, excluding warmups. |
| `stages.*_ms` | Optional timings returned by the adapter, such as `preprocess_ms`, `model_ms`, `postprocess_ms`, or `safety_ms`. |
| `action_metadata` | Fixed input/output context such as image size, action-chunk shape, executed steps, precision, and batch size. It must not contain paths, prompts, credentials, or robot settings. |
| `hardware_commands_sent` | Must remain `false`; any other value invalidates the report for this repository. |

The top-level end-to-end measurement does not automatically equal the sum of adapter-provided stages. This is intentional: it includes Python dispatch and measures the boundary the caller actually observes.

## Fixed protocol for a real model

1. Review the adapter source and verify that it only preprocesses fixed local input and calls inference; it must not initialize ROS, CAN, SDK, daemon, device, or robot APIs.
2. Freeze model revision, runtime, precision, input size, batch size, action horizon, and preprocessing. Record these as sanitized `action_metadata`.
3. Run 20 warmups and 100 measured repeats on one fixed representative input. Synchronize the accelerator in the adapter before stopping model-stage timing when the framework requires it.
4. Keep a private raw log. Publish only a reviewed JSON report that includes p50/p95, sample count, sanitized GPU/runtime metadata, and `hardware_commands_sent: false`.
5. Treat the 6GB robot-side GPU and the 80GB training GPUs as separate deployment environments. Compare their latency only under the same model and fixed contract; do not infer task success from either number.

## Example

```bash
python -m benchmarks.offline_latency \
  --callable benchmarks.example_fake_policy:infer \
  --warmup 20 --repeats 100 \
  --action-metadata '{"image_size":[480,640],"chunk_shape":[1,7,7],"executed_steps":0}' \
  --output sanitized-report.json
```

The example callable is synthetic. Its timing values are not a model measurement and must never be reported as deployment performance.

