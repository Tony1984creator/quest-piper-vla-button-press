"""Position-independent OpenCV detector for visually illuminated buttons.

This module never reads or writes robot-control channels. It accepts one BGR
image and returns a visual candidate suitable for human review.
"""

from __future__ import annotations

from dataclasses import dataclass

import cv2
import numpy as np


@dataclass(frozen=True)
class GlobalConfirmedResult:
    """Largest orange visual candidate detected in a BGR frame."""

    is_active: bool
    confidence: float
    orange_pixels: int
    bbox: tuple[int, int, int, int] | None
    mask: np.ndarray


def detect_illuminated_button(
    frame: np.ndarray,
    *,
    orange_hsv_lower: tuple[int, int, int] = (5, 100, 120),
    orange_hsv_upper: tuple[int, int, int] = (30, 255, 255),
    min_orange_pixels: int = 1_000,
    edge_margin: int = 8,
) -> GlobalConfirmedResult:
    """Find the largest non-edge orange region in a BGR frame.

    This reports visual illumination only. It does not identify a printed floor
    number and it does not determine task success.
    """
    if frame.ndim != 3 or frame.shape[2] != 3:
        raise ValueError("frame must be a BGR image with shape (height, width, 3)")
    if min_orange_pixels <= 0:
        raise ValueError("min_orange_pixels must be positive")
    if edge_margin < 0:
        raise ValueError("edge_margin must not be negative")

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(
        hsv,
        np.asarray(orange_hsv_lower, dtype=np.uint8),
        np.asarray(orange_hsv_upper, dtype=np.uint8),
    )
    count, _labels, stats, _centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)
    if count <= 1:
        return GlobalConfirmedResult(False, 0.0, 0, None, mask)

    frame_height, frame_width = frame.shape[:2]
    candidates: list[int] = []
    for component_index in range(1, count):
        x = int(stats[component_index, cv2.CC_STAT_LEFT])
        y = int(stats[component_index, cv2.CC_STAT_TOP])
        width = int(stats[component_index, cv2.CC_STAT_WIDTH])
        height = int(stats[component_index, cv2.CC_STAT_HEIGHT])
        touches_edge = (
            x <= edge_margin
            or y <= edge_margin
            or x + width >= frame_width - edge_margin
            or y + height >= frame_height - edge_margin
        )
        if not touches_edge:
            candidates.append(component_index)
    if not candidates:
        return GlobalConfirmedResult(False, 0.0, 0, None, mask)

    component_index = max(candidates, key=lambda index: int(stats[index, cv2.CC_STAT_AREA]))
    x = int(stats[component_index, cv2.CC_STAT_LEFT])
    y = int(stats[component_index, cv2.CC_STAT_TOP])
    width = int(stats[component_index, cv2.CC_STAT_WIDTH])
    height = int(stats[component_index, cv2.CC_STAT_HEIGHT])
    orange_pixels = int(stats[component_index, cv2.CC_STAT_AREA])
    is_active = orange_pixels >= min_orange_pixels
    return GlobalConfirmedResult(
        is_active=is_active,
        confidence=min(1.0, orange_pixels / float(min_orange_pixels)),
        orange_pixels=orange_pixels if is_active else 0,
        bbox=(x, y, width, height) if is_active else None,
        mask=mask,
    )
