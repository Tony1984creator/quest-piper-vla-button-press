# 04 · Evo-Depth deployment contract

## Problem solved

Audit policy output and measurement scope before interpreting an endpoint experiment as safe, fast, or successful.

## Design decisions

- Select a bounded prefix from a predicted action chunk.
- Retain the seven active arm-plus-gripper dimensions explicitly.
- Clamp the first requested change against measured state before any private adapter.
- Measure a whole endpoint request separately from model-forward latency.

## Core code

- [action-chunk contract](core/action_chunk.py): selection and delta clamp with no device access;
- [regression tests](../../tests/test_action_chunk.py): 25-step/7D and first-jump cases.

## Evidence and boundary

A 300-step action-head-only pilot was evaluated under a fixed, same-187-batch real-data protocol; mean masked-flow loss changed from 0.84145 to 0.24486. This is offline optimization evidence, not a policy success or hardware result. Details are in [deployment evidence](evidence.md).

**Next acceptance gate:** run an offline adapter benchmark with separately reported preprocessing, inference, and postprocessing time.

