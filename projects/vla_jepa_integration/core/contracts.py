"""Validate public VLA-JEPA integration facts without loading a model."""

from __future__ import annotations


def validate_video_layout(shape: tuple[int, ...]) -> tuple[int, int, int, int, int]:
    """Convert a five-axis [B,T,C,H,W] shape description to [B,C,T,H,W]."""
    if len(shape) != 5 or not all(isinstance(value, int) and value > 0 for value in shape):
        raise ValueError("shape must contain five positive integer dimensions")
    batch, time, channels, height, width = shape
    return batch, channels, time, height, width


def summarize_parameter_mapping(mapped: int, reinitialized: int, frozen_teacher: bool) -> dict[str, object]:
    """Return a JSON-safe static mapping summary under the frozen-teacher contract."""
    if mapped < 0 or reinitialized < 0:
        raise ValueError("parameter counts must be non-negative")
    if not frozen_teacher:
        raise ValueError("teacher must be frozen for this integration contract")
    return {"mapped": mapped, "reinitialized": reinitialized, "frozen_teacher": True}

