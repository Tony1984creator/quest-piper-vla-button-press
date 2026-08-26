"""A dependency-free example callable used to verify the benchmark contract."""


def infer() -> dict[str, float]:
    """Return illustrative stage timings; this function does not access a robot."""
    return {"preprocess_ms": 0.1, "model_ms": 0.2, "postprocess_ms": 0.1}

