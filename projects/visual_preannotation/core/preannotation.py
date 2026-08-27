"""Build compact task-stage records from frame-level visual candidates."""

from __future__ import annotations

from collections.abc import Sequence

from .temporal_filter import confirmed_segments


def build_press_confirmation_segments(
    records: Sequence[dict[str, object]], *, min_consecutive_frames: int = 3
) -> list[dict[str, object]]:
    """Reduce stable visual positives to one auditable record per event."""
    offsets = confirmed_segments(
        [bool(record["is_active"]) for record in records],
        min_consecutive_frames=min_consecutive_frames,
    )
    segments: list[dict[str, object]] = []
    for start_offset, end_offset in offsets:
        representative_offset = (start_offset + end_offset) // 2
        representative = records[representative_offset]
        segments.append(
            {
                "task_stage": "press_confirmed_visual",
                "start_frame": int(records[start_offset]["frame_index"]),
                "end_frame": int(records[end_offset]["frame_index"]),
                "representative_frame": int(representative["frame_index"]),
                "duration_frames": end_offset - start_offset + 1,
                "representative_confidence": float(representative["confidence"]),
                "representative_bbox": representative["bbox"],
            }
        )
    return segments

