# Fixed target-identity review queue

## Purpose

Visual pre-annotation answers a narrow question: does a frame contain a stable
candidate for an illuminated button? It does not identify which floor button is
illuminated, and therefore cannot establish task success.

`opencv_preannotation/target_identity_queue.py` makes human verification
tractable without converting visual candidates into automatic success labels.
It creates a deterministic, episode-level review queue:

1. retain the highest-confidence (then earliest) candidate for each episode;
2. reject inconsistent data if one episode has multiple requested target floors;
3. sample a fixed number of episodes within every target-floor stratum using a
   recorded random seed;
4. render the selected frame with the candidate box and requested task floor;
5. write every selected record as `pending_human_review`.

The reviewer must independently decide whether the boxed button is the
requested floor and record that decision. A `pending_human_review` record is
not a successful press, even when the candidate appears illuminated.

## Current private execution evidence

On 2026-08-18, the private dataset execution created a frozen review cohort of
120 evidence frames from 120 distinct episodes. The cohort is balanced across
the 12 requested-floor strata (floors 24 through 35, ten episodes per floor)
and each row has an evidence image. All 120 rows remain
`pending_human_review`; no target identity, contact, retraction, or task
success claim is made from this queue.

## Example invocation

```bash
python opencv_preannotation/target_identity_queue.py \
  joined_visual_candidates.jsonl \
  review_queue.csv \
  review_evidence/ \
  --samples-per-floor 10 \
  --seed 20260818
```

Use a frozen copy of the resulting CSV for evaluation. Do not alter selected
episodes after looking at outcomes; add reviewer fields only. Keep source
videos, rendered evidence, and completed review sheets outside this public
repository.

## What it proves—and what it does not

The queue proves the sampling and review protocol is reproducible. It does not
prove OCR accuracy, target-button identity, physical contact, retraction, or
closed-loop task success. Those claims require completed human review and the
separate evaluation-stage evidence specified in the roadmap.
