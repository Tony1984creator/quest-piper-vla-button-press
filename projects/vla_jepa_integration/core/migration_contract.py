"""Shape and freezing invariants for the documented V-JEPA 2.1 migration."""

from math import prod


def validate_vjepa21_migration(
    *,
    qwen_hidden_size: int,
    action_cross_attention_dim: int,
    embodied_token_count: int,
    action_token_count: int,
    jepa_hidden_size: int,
    old_grid: tuple[int, int, int],
    new_grid: tuple[int, int, int],
    teacher_frozen: bool,
) -> dict[str, int | tuple[int, int, int]]:
    """Validate the fixed dimensions and teacher boundary of the upgrade."""

    expected = {
        "qwen_hidden_size": (qwen_hidden_size, 2048),
        "action_cross_attention_dim": (action_cross_attention_dim, 2048),
        "embodied_token_count": (embodied_token_count, 32),
        "action_token_count": (action_token_count, 24),
        "jepa_hidden_size": (jepa_hidden_size, 1024),
        "old_grid": (old_grid, (4, 16, 16)),
        "new_grid": (new_grid, (4, 24, 24)),
        "teacher_frozen": (teacher_frozen, True),
    }
    for name, (actual, required) in expected.items():
        if actual != required:
            raise ValueError(f"{name} must be {required!r}, got {actual!r}")

    return {
        "qwen_hidden_size": qwen_hidden_size,
        "action_cross_attention_dim": action_cross_attention_dim,
        "embodied_token_count": embodied_token_count,
        "action_token_count": action_token_count,
        "jepa_hidden_size": jepa_hidden_size,
        "old_grid": old_grid,
        "new_grid": new_grid,
        "old_tokens": prod(old_grid),
        "new_tokens": prod(new_grid),
    }

