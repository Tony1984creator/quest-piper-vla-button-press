"""Create a fixed, balanced review queue from visual button candidates.

The queue is intentionally not a success label: it preserves the distinction
between a visually illuminated candidate and a human-confirmed task target.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


QUEUE_FIELDS = [
    "queue_set",
    "sampling_seed",
    "source_chunk",
    "representative_frame",
    "start_frame",
    "end_frame",
    "episode_index",
    "target_floor",
    "target_floor_source",
    "representative_bbox",
    "source_video",
    "target_identity_status",
    "triage_reason",
    "evidence_image",
    "human_confirmed_floor",
    "reviewer",
    "review_note",
    "reviewed_at",
]


def _representative(rows: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Prefer the strongest candidate, then the earliest frame as tie-breaker."""
    return min(
        rows,
        key=lambda row: (
            -float(row.get("representative_confidence", 0.0)),
            int(row.get("representative_frame", 0)),
            str(row.get("source_chunk", "")),
        ),
    )


def select_stratified_episode_review(
    rows: Iterable[dict[str, Any]], samples_per_floor: int, seed: int
) -> list[dict[str, Any]]:
    """Select at most one visual candidate per episode in each task-floor stratum."""
    if samples_per_floor < 1:
        raise ValueError("samples_per_floor must be positive")

    by_episode: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        episode = str(row["episode_index"])
        by_episode[episode].append(row)

    representatives: list[dict[str, Any]] = []
    for episode, episode_rows in by_episode.items():
        floors = {str(row["target_floor"]) for row in episode_rows}
        if len(floors) != 1:
            raise ValueError(f"episode {episode} maps to multiple target floors: {sorted(floors)}")
        representatives.append(_representative(episode_rows))

    by_floor: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in representatives:
        by_floor[str(row["target_floor"])].append(row)

    rng = random.Random(seed)
    selected: list[dict[str, Any]] = []
    for floor in sorted(by_floor, key=lambda value: (int(value), value)):
        candidates = sorted(by_floor[floor], key=lambda row: str(row["episode_index"]))
        selected.extend(rng.sample(candidates, k=min(samples_per_floor, len(candidates))))
    return sorted(selected, key=lambda row: (int(str(row["target_floor"])), str(row["episode_index"])))


def render_evidence_image(row: dict[str, Any], output_path: Path) -> None:
    """Render the selected frame and clearly state the task target for review."""
    import cv2

    video = cv2.VideoCapture(str(row["source_video"]))
    video.set(cv2.CAP_PROP_POS_FRAMES, int(row["representative_frame"]))
    ok, frame = video.read()
    video.release()
    if not ok:
        raise RuntimeError(f"Cannot read candidate frame from {row['source_video']}")
    x, y, width, height = map(int, row["representative_bbox"])
    cv2.rectangle(frame, (x, y), (x + width - 1, y + height - 1), (0, 255, 0), 2)
    text = f"task target floor={row['target_floor']} | confirm this boxed button"
    cv2.putText(frame, text, (8, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
    if not cv2.imwrite(str(output_path), frame):
        raise RuntimeError(f"Cannot write evidence image: {output_path}")


def write_review_queue(
    selected: Iterable[dict[str, Any]], output_csv: Path, evidence_directory: Path, seed: int
) -> int:
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    evidence_directory.mkdir(parents=True, exist_ok=True)
    rows = []
    for row in selected:
        image_name = f"episode_{int(row['episode_index']):05d}_frame_{int(row['representative_frame']):06d}.jpg"
        render_evidence_image(row, evidence_directory / image_name)
        rows.append(
            {
                "queue_set": "frozen_stratified_evaluation",
                "sampling_seed": seed,
                "source_chunk": row.get("source_chunk", ""),
                "representative_frame": row.get("representative_frame", ""),
                "start_frame": row.get("start_frame", ""),
                "end_frame": row.get("end_frame", ""),
                "episode_index": row.get("episode_index", ""),
                "target_floor": row.get("target_floor", ""),
                "target_floor_source": row.get("target_floor_source", ""),
                "representative_bbox": json.dumps(row.get("representative_bbox", [])),
                "source_video": row.get("source_video", ""),
                "target_identity_status": "pending_human_review",
                "triage_reason": "one_representative_per_episode_stratified_by_target_floor",
                "evidence_image": image_name,
                "human_confirmed_floor": "",
                "reviewer": "",
                "review_note": "",
                "reviewed_at": "",
            }
        )
    with output_csv.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=QUEUE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="joined visual candidates JSONL")
    parser.add_argument("output_csv", type=Path)
    parser.add_argument("evidence_directory", type=Path)
    parser.add_argument("--samples-per-floor", type=int, default=10)
    parser.add_argument("--seed", type=int, default=20260818)
    args = parser.parse_args()
    rows = [json.loads(line) for line in args.source.read_text(encoding="utf-8").splitlines() if line]
    selected = select_stratified_episode_review(rows, args.samples_per_floor, args.seed)
    count = write_review_queue(selected, args.output_csv, args.evidence_directory, args.seed)
    counts: dict[str, int] = defaultdict(int)
    for row in selected:
        counts[str(row["target_floor"])] += 1
    print(json.dumps({"queue_rows": count, "per_floor": dict(counts), "seed": args.seed}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
