# Public research-portfolio rebuild specification

## Goal

Make this repository and the companion learning-plan workbook useful to a prospective summer-research supervisor in under five minutes: each claim must identify the engineering problem, the intervention, the retained evidence, and the result boundary.

## Public claim policy

- Retain measured project facts: Quest-to-Piper control-chain exercise; 40 episodes, 14,653 frames, 30 FPS, two 640x480 RGB streams, 7D state/action; 386 mapped and 12 reinitialized V-JEPA tensors; the documented training probes; 12 videos, 188,418 frames, 421 candidates, and 48 audited candidates.
- Distinguish integration, training continuity, offline non-actuating inference, visual pre-annotation, and closed-loop task success.
- Do not publish raw data, videos, checkpoints, internal paths, network identities, robot limits, credentials, proprietary code, or executable robot-control settings.
- Do not claim latency or deployment throughput until a versioned offline benchmark report records the data.

## Deliverables

1. A portfolio-oriented README and case-study document that use the form: problem, intervention, evidence, conclusion boundary, and next falsifiable experiment.
2. A dependency-free `benchmarks/` utility that records per-stage and end-to-end latency distributions, action chunk metadata, and optional runtime metadata from a non-actuating callable.
3. Unit tests for percentile calculation, report validation, and non-actuating benchmark execution.
4. A benchmark protocol that states how to collect a sanitized report on an existing workstation without accessing CAN or issuing robot commands.
5. In-place revisions to existing Excel sheets only: `实际进度校准`, `已有成果与简历证据`, and `面试能力矩阵`; keep the existing sheet count, visual theme, borders, wrapping, and column layout.

## Acceptance criteria

- `python -m unittest discover -s tests -v` passes.
- A fake callable creates a valid JSON report with sample count, p50/p95 end-to-end milliseconds, stage summaries, action metadata, and `hardware_commands_sent: false`.
- The repository documents no unmeasured performance number as a result.
- The workbook has no new worksheet; rendering shows no clipping, broken borders, or inconsistent fonts in edited ranges.

