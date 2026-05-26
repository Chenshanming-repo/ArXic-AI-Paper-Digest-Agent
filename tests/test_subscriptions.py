from __future__ import annotations

import unittest

from config import Subscription, parse_recipients_by_category


class ParseRecipientsByCategoryTest(unittest.TestCase):
    def test_empty_string_returns_empty_list(self) -> None:
        self.assertEqual(parse_recipients_by_category("", known_categories=["cs.AI"]), [])

    def test_none_returns_empty_list(self) -> None:
        self.assertEqual(parse_recipients_by_category(None, known_categories=["cs.AI"]), [])

    def test_parses_valid_json_into_subscriptions(self) -> None:
        raw = (
            '[{"email": "alice@x.com", "categories": ["cs.AI", "cs.LG"]},'
            ' {"email": "bob@y.com", "categories": ["stat.ML"]}]'
        )
        subs = parse_recipients_by_category(
            raw, known_categories=["cs.AI", "cs.LG", "stat.ML"]
        )
        self.assertEqual(
            subs,
            [
                Subscription(email="alice@x.com", categories=["cs.AI", "cs.LG"]),
                Subscription(email="bob@y.com", categories=["stat.ML"]),
            ],
        )

    def test_invalid_json_raises(self) -> None:
        with self.assertRaises(ValueError):
            parse_recipients_by_category(
                "not json", known_categories=["cs.AI"]
            )

    def test_top_level_must_be_list(self) -> None:
        with self.assertRaises(ValueError):
            parse_recipients_by_category(
                '{"email": "a@b"}', known_categories=["cs.AI"]
            )

    def test_missing_email_field_raises(self) -> None:
        with self.assertRaises(ValueError):
            parse_recipients_by_category(
                '[{"categories": ["cs.AI"]}]', known_categories=["cs.AI"]
            )

    def test_missing_categories_field_raises(self) -> None:
        with self.assertRaises(ValueError):
            parse_recipients_by_category(
                '[{"email": "a@b.com"}]', known_categories=["cs.AI"]
            )

    def test_unknown_category_is_dropped_with_warning(self) -> None:
        with self.assertLogs("config", level="WARNING") as captured:
            subs = parse_recipients_by_category(
                '[{"email": "a@b.com", "categories": ["cs.AI", "cs.UNKNOWN"]}]',
                known_categories=["cs.AI"],
            )
        self.assertEqual(subs, [Subscription(email="a@b.com", categories=["cs.AI"])])
        self.assertTrue(
            any("cs.UNKNOWN" in line for line in captured.output),
            captured.output,
        )

    def test_subscription_with_zero_valid_categories_is_skipped(self) -> None:
        with self.assertLogs("config", level="WARNING"):
            subs = parse_recipients_by_category(
                '[{"email": "a@b.com", "categories": ["cs.UNKNOWN"]}]',
                known_categories=["cs.AI"],
            )
        self.assertEqual(subs, [])

    def test_empty_categories_list_is_skipped(self) -> None:
        with self.assertLogs("config", level="WARNING"):
            subs = parse_recipients_by_category(
                '[{"email": "a@b.com", "categories": []}]',
                known_categories=["cs.AI"],
            )
        self.assertEqual(subs, [])

    def test_duplicate_email_keeps_last_with_warning(self) -> None:
        raw = (
            '[{"email": "a@b.com", "categories": ["cs.AI"]},'
            ' {"email": "a@b.com", "categories": ["cs.LG"]}]'
        )
        with self.assertLogs("config", level="WARNING") as captured:
            subs = parse_recipients_by_category(
                raw, known_categories=["cs.AI", "cs.LG"]
            )
        self.assertEqual(
            subs, [Subscription(email="a@b.com", categories=["cs.LG"])]
        )
        self.assertTrue(any("a@b.com" in line for line in captured.output))


class RecipientsByCategoryEnvTest(unittest.TestCase):
    def test_module_constant_reflects_env(self) -> None:
        import importlib
        import os

        os.environ["RECIPIENTS_BY_CATEGORY"] = (
            '[{"email": "alice@x.com", "categories": ["cs.AI"]}]'
        )
        os.environ["ARXIV_CATEGORIES"] = "cs.AI,cs.LG"
        try:
            import config
            importlib.reload(config)
            self.assertEqual(
                config.RECIPIENTS_BY_CATEGORY,
                [config.Subscription(email="alice@x.com", categories=["cs.AI"])],
            )
        finally:
            del os.environ["RECIPIENTS_BY_CATEGORY"]
            del os.environ["ARXIV_CATEGORIES"]
            importlib.reload(config)


if __name__ == "__main__":
    unittest.main()
