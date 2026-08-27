"""Make the storage-degrees to model-radians boundary explicit and single-use."""

from __future__ import annotations

import math
from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class ConversionToken:
    """Carries whether a vector has already crossed the radians boundary."""

    converted: bool = False

    @classmethod
    def fresh(cls) -> "ConversionToken":
        return cls(converted=False)


def convert_degrees_to_radians_once(
    values: Sequence[float], token: ConversionToken
) -> tuple[list[float], ConversionToken]:
    """Convert finite values once and return a consumed token."""
    if token.converted:
        raise ValueError("degrees-to-radians conversion was already applied")
    converted = [math.radians(float(value)) for value in values]
    if not all(math.isfinite(value) for value in converted):
        raise ValueError("values must be finite")
    return converted, ConversionToken(converted=True)

