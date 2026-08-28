import unittest

from projects.vla_jepa_integration.core.migration_contract import (
    validate_vjepa21_migration,
)


class MigrationContractTests(unittest.TestCase):
    def test_accepts_the_documented_upgrade_invariants(self):
        report = validate_vjepa21_migration(
            qwen_hidden_size=2048,
            action_cross_attention_dim=2048,
            embodied_token_count=32,
            action_token_count=24,
            jepa_hidden_size=1024,
            old_grid=(4, 16, 16),
            new_grid=(4, 24, 24),
            teacher_frozen=True,
        )

        self.assertEqual(report["old_tokens"], 1024)
        self.assertEqual(report["new_tokens"], 2304)

    def test_rejects_a_trainable_teacher(self):
        with self.assertRaisesRegex(ValueError, "teacher_frozen"):
            validate_vjepa21_migration(
                qwen_hidden_size=2048,
                action_cross_attention_dim=2048,
                embodied_token_count=32,
                action_token_count=24,
                jepa_hidden_size=1024,
                old_grid=(4, 16, 16),
                new_grid=(4, 24, 24),
                teacher_frozen=False,
            )


if __name__ == "__main__":
    unittest.main()

