"""Position-independent OpenCV detector for visually illuminated buttons."""

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
    """Find the largest non-edge orange region; reports illumination only."""
    if frame.ndim != 3 or frame.shape[2] != 3:
        raise ValueError("frame must be a BGR image with shape (height, width, 3)")
    if min_orange_pixels <= 0 or edge_margin < 0:
        raise ValueError("thresholds must be positive and edge margin non-negative")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.asarray(orange_hsv_lower, dtype=np.uint8), np.asarray(orange_hsv_upper, dtype=np.uint8))
    count, _labels, stats, _centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)
    frame_height, frame_width = frame.shape[:2]
    candidates = [
        index for index in range(1, count)
        if int(stats[index, cv2.CC_STAT_LEFT]) > edge_margin
        and int(stats[index, cv2.CC_STAT_TOP]) > edge_margin
        and int(stats[index, cv2.CC_STAT_LEFT]) + int(stats[index, cv2.CC_STAT_WIDTH]) < frame_width - edge_margin
        and int(stats[index, cv2.CC_STAT_TOP]) + int(stats[index, cv2.CC_STAT_HEIGHT]) < frame_height - edge_margin
    ]
    if not candidates:
        return GlobalConfirmedResult(False, 0.0, 0, None, mask)
    index = max(candidates, key=lambda candidate: int(stats[candidate, cv2.CC_STAT_AREA]))
    x, y = int(stats[index, cv2.CC_STAT_LEFT]), int(stats[index, cv2.CC_STAT_TOP])
    width, height, pixels = int(stats[index, cv2.CC_STAT_WIDTH]), int(stats[index, cv2.CC_STAT_HEIGHT]), int(stats[index, cv2.CC_STAT_AREA])
    active = pixels >= min_orange_pixels
    return GlobalConfirmedResult(active, min(1.0, pixels / float(min_orange_pixels)), pixels if active else 0, (x, y, width, height) if active else None, mask)

