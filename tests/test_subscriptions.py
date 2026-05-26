from __future__ import annotations

import unittest
from datetime import date, datetime, timezone
from unittest import mock

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


def _entry(arxiv_id: str, *, primary: str = "cs.AI"):
    from src.models import DigestEntry, Paper

    paper = Paper(
        arxiv_id=arxiv_id,
        url=f"https://arxiv.org/abs/{arxiv_id}",
        title=f"Title {arxiv_id}",
        authors=["A"],
        abstract="abstract",
        published=datetime(2026, 5, 26, 10, tzinfo=timezone.utc),
        primary_category=primary,
    )
    return DigestEntry(paper=paper, summary="s")


class SendSubscriptionEmailsTest(unittest.TestCase):
    def setUp(self) -> None:
        import main
        self.main = main
        self.entries = [
            _entry("2605.001"),
            _entry("2605.002", primary="cs.LG"),
            _entry("2605.003", primary="stat.ML"),
        ]
        self.found_in_category = {
            "2605.001": "cs.AI",
            "2605.002": "cs.LG",
            "2605.003": "stat.ML",
        }
        self.digest_date = date(2026, 5, 26)

    def test_sends_one_filtered_email_per_subscription(self) -> None:
        subs = [
            Subscription(email="alice@x.com", categories=["cs.AI", "cs.LG"]),
            Subscription(email="bob@y.com", categories=["stat.ML"]),
        ]
        sent: list[dict] = []

        def fake_send(*, subject, rendered, attachment_name, recipients=None):
            sent.append(
                {
                    "subject": subject,
                    "rendered": rendered,
                    "recipients": recipients,
                }
            )
            return True

        with mock.patch.object(self.main, "_send_digest_email", fake_send):
            self.main._send_subscription_emails(
                entries=self.entries,
                found_in_category=self.found_in_category,
                digest_date=self.digest_date,
                subscriptions=subs,
            )

        self.assertEqual(len(sent), 2)
        alice_call = next(s for s in sent if s["recipients"] == ["alice@x.com"])
        bob_call = next(s for s in sent if s["recipients"] == ["bob@y.com"])

        self.assertEqual(
            alice_call["subject"],
            "ArXiv 每日论文摘要 [cs.AI,cs.LG] 2026-05-26",
        )
        self.assertIn("Title 2605.001", alice_call["rendered"])
        self.assertIn("Title 2605.002", alice_call["rendered"])
        self.assertNotIn("Title 2605.003", alice_call["rendered"])

        self.assertEqual(
            bob_call["subject"],
            "ArXiv 每日论文摘要 [stat.ML] 2026-05-26",
        )
        self.assertIn("Title 2605.003", bob_call["rendered"])
        self.assertNotIn("Title 2605.001", bob_call["rendered"])

    def test_skips_subscription_with_zero_matched_papers(self) -> None:
        subs = [
            Subscription(email="alice@x.com", categories=["cs.AI"]),
            Subscription(email="charlie@z.com", categories=["q-bio.GN"]),
        ]
        sent: list[str] = []

        def fake_send(*, subject, rendered, attachment_name, recipients=None):
            sent.append(recipients[0])
            return True

        with mock.patch.object(self.main, "_send_digest_email", fake_send):
            self.main._send_subscription_emails(
                entries=self.entries,
                found_in_category=self.found_in_category,
                digest_date=self.digest_date,
                subscriptions=subs,
            )

        self.assertEqual(sent, ["alice@x.com"])


if __name__ == "__main__":
    unittest.main()
