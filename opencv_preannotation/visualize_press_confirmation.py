"""Render read-only visual-confirmation review artifacts from a video."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import cv2

from .global_confirmed_detector import detect_illuminated_button


def render_visual_confirmation(
    *,
    input_video: Path,
    output_video: Path,
    frames_csv: Path,
    events_csv: Path,
    required_consecutive_frames: int = 3,
) -> dict[str, int]:
    """Write annotated video and CSV review artifacts without controlling hardware."""
    if required_consecutive_frames <= 0:
        raise ValueError("required_consecutive_frames must be positive")

    capture = cv2.VideoCapture(str(input_video))
    if not capture.isOpened():
        raise RuntimeError(f"cannot open input video: {input_video}")
    fps = capture.get(cv2.CAP_PROP_FPS) or 30.0
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    for path in (output_video, frames_csv, events_csv):
        path.parent.mkdir(parents=True, exist_ok=True)
    writer = cv2.VideoWriter(
        str(output_video), cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
    )
    if not writer.isOpened():
        raise RuntimeError(f"cannot open output video: {output_video}")

    frame_index = 0
    active_streak = 0
    previous_confirmed = False
    confirmed_events = 0
    with frames_csv.open("w", newline="", encoding="utf-8-sig") as frames_file, events_csv.open(
        "w", newline="", encoding="utf-8-sig"
    ) as events_file:
        frame_writer = csv.DictWriter(
            frames_file,
            fieldnames=[
                "frame_index",
                "timestamp_s",
                "button_active",
                "active_streak",
                "press_confirmed",
                "bbox",
                "orange_pixels",
                "confidence",
            ],
        )
        event_writer = csv.DictWriter(
            events_file,
            fieldnames=["event_start_frame", "event_confirmed_frame", "timestamp_s"],
        )
        frame_writer.writeheader()
        event_writer.writeheader()
        while True:
            ok, frame = capture.read()
            if not ok:
                break
            detection = detect_illuminated_button(frame)
            active_streak = active_streak + 1 if detection.is_active else 0
            confirmed = active_streak >= required_consecutive_frames
            if detection.bbox is not None:
                x, y, box_width, box_height = detection.bbox
                color = (0, 255, 0) if confirmed else (0, 180, 255)
                cv2.rectangle(frame, (x, y), (x + box_width - 1, y + box_height - 1), color, 2)
            label = (
                "PRESS CONFIRMED"
                if confirmed
                else f"ACTIVE {active_streak}/{required_consecutive_frames}"
                if detection.is_active
                else "NO ILLUMINATED BUTTON"
            )
            label_color = (0, 255, 0) if confirmed else (0, 180, 255) if detection.is_active else (80, 80, 255)
            cv2.rectangle(frame, (8, 8), (430, 48), (0, 0, 0), thickness=-1)
            cv2.putText(frame, label, (18, 36), cv2.FONT_HERSHEY_SIMPLEX, 0.75, label_color, 2)
            timestamp_s = round(frame_index / fps, 3)
            if confirmed and not previous_confirmed:
                event_writer.writerow(
                    {
                        "event_start_frame": frame_index - required_consecutive_frames + 1,
                        "event_confirmed_frame": frame_index,
                        "timestamp_s": timestamp_s,
                    }
                )
                confirmed_events += 1
            frame_writer.writerow(
                {
                    "frame_index": frame_index,
                    "timestamp_s": timestamp_s,
                    "button_active": detection.is_active,
                    "active_streak": active_streak,
                    "press_confirmed": confirmed,
                    "bbox": detection.bbox or "",
                    "orange_pixels": detection.orange_pixels,
                    "confidence": round(detection.confidence, 4),
                }
            )
            writer.write(frame)
            previous_confirmed = confirmed
            frame_index += 1
    capture.release()
    writer.release()
    return {"frames": frame_index, "confirmed_events": confirmed_events}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-video", type=Path, required=True)
    parser.add_argument("--output-video", type=Path, required=True)
    parser.add_argument("--output-frames-csv", type=Path, required=True)
    parser.add_argument("--output-events-csv", type=Path, required=True)
    parser.add_argument("--required-consecutive-frames", type=int, default=3)
    args = parser.parse_args()
    result = render_visual_confirmation(
        input_video=args.input_video,
        output_video=args.output_video,
        frames_csv=args.output_frames_csv,
        events_csv=args.output_events_csv,
        required_consecutive_frames=args.required_consecutive_frames,
    )
    print(f"frames={result['frames']} confirmed_events={result['confirmed_events']}")


if __name__ == "__main__":
    main()
