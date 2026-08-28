"""Run read-only, compact OpenCV preannotation over all wrist-video chunks."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import cv2

from projects.visual_preannotation.core.global_confirmed_detector import detect_illuminated_button
from projects.visual_preannotation.core.preannotation import build_press_confirmation_segments


def process_video(video_path: Path, chunk_id: str, min_orange_pixels: int) -> tuple[int, list[dict[str, object]]]:
    capture = cv2.VideoCapture(str(video_path))
    if not capture.isOpened():
        raise RuntimeError(f"Cannot open video: {video_path}")
    records: list[dict[str, object]] = []
    frame_index = 0
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        result = detect_illuminated_button(frame, min_orange_pixels=min_orange_pixels)
        records.append(
            {
                "frame_index": frame_index,
                "is_active": result.is_active,
                "confidence": result.confidence,
                "bbox": list(result.bbox) if result.bbox else None,
            }
        )
        frame_index += 1
    capture.release()
    segments = build_press_confirmation_segments(records)
    for segment in segments:
        segment["source_chunk"] = chunk_id
        segment["source_video"] = str(video_path)
        segment["human_label"] = ""
    return frame_index, segments


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-directory", required=True)
    parser.add_argument("--output-directory", required=True)
    parser.add_argument("--min-orange-pixels", type=int, default=1_000)
    args = parser.parse_args()
    input_directory = Path(args.input_directory)
    output_directory = Path(args.output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    all_segments: list[dict[str, object]] = []
    summary: list[dict[str, object]] = []
    for video_path in sorted(input_directory.glob("*.mp4")):
        chunk_id = video_path.stem
        frames, segments = process_video(video_path, chunk_id, args.min_orange_pixels)
        all_segments.extend(segments)
        summary.append({"source_chunk": chunk_id, "frames": frames, "confirmation_segments": len(segments)})
        print(json.dumps(summary[-1], ensure_ascii=False), flush=True)

    with (output_directory / "press_confirmed_visual_segments.jsonl").open("w", encoding="utf-8") as output:
        for segment in all_segments:
            output.write(json.dumps(segment, ensure_ascii=False) + "\n")
    fields = ["source_chunk", "frames", "confirmation_segments"]
    with (output_directory / "preannotation_summary.csv").open("w", newline="", encoding="utf-8-sig") as output:
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        writer.writerows(summary)
    print(json.dumps({"videos": len(summary), "segments": len(all_segments)}, ensure_ascii=False))


if __name__ == "__main__":
    main()


