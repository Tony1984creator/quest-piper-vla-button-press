"""Deterministic sampling helpers for human review of visual events."""

from collections import defaultdict
from collections.abc import Mapping, Sequence


def select_stratified_review(
    segments: Sequence[Mapping[str, object]], *, samples_per_chunk: int
) -> list[dict[str, object]]:
    """Return evenly-spaced review records from each named source chunk."""

    if samples_per_chunk <= 0:
        raise ValueError("samples_per_chunk must be positive")

    chunks: dict[object, list[Mapping[str, object]]] = defaultdict(list)
    for segment in segments:
        chunks[segment["source_chunk"]].append(segment)

    selected: list[dict[str, object]] = []
    for chunk_name in sorted(chunks, key=str):
        ordered = sorted(chunks[chunk_name], key=lambda row: row["representative_frame"])
        count = min(samples_per_chunk, len(ordered))
        positions = (
            [0]
            if count == 1
            else [round(index * (len(ordered) - 1) / (count - 1)) for index in range(count)]
        )
        selected.extend(dict(ordered[position]) for position in positions)
    return selected

