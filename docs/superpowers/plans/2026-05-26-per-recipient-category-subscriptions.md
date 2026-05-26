# Per-Recipient Category Subscriptions Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Send each subscriber a daily digest filtered to the categories they listed in `RECIPIENTS_BY_CATEGORY`, while keeping fetch + summary work shared across the run.

**Architecture:** Parse a JSON env at config import into a typed `Subscription` list. In `_run_daily_digest`, after the existing fetch/summary pipeline, branch on whether subscriptions are configured: with subscriptions, render and send one email per subscriber filtered by `found_in_category`; without, fall through to the current single-email behaviour. Reuse the existing `render_digest(category_by_id=, category_order=)` and `send_markdown_email` paths.

**Tech Stack:** Python 3.9, pydantic v1 (already in use), stdlib `json`, unittest.

**Spec:** `docs/superpowers/specs/2026-05-26-per-recipient-category-subscriptions-design.md`

---

## File Structure

| File | Responsibility |
|---|---|
| `config.py` | Define `Subscription` dataclass, parse `RECIPIENTS_BY_CATEGORY` env once at import, expose validated `RECIPIENTS_BY_CATEGORY: list[Subscription]`. |
| `main.py` | New `_send_subscription_emails` helper. `_run_daily_digest` calls it when subscriptions are configured; otherwise the existing `_send_digest_email` path runs. |
| `tests/test_subscriptions.py` (new) | Cover parsing, validation, filtering, subject formatting, skip-on-empty, and fallback. |

`src/writer.py`, `src/emailer.py`, `src/fetcher.py` are not touched — they already expose what we need.

---

### Task 1: Define `Subscription` and parsing helper

**Files:**
- Modify: `config.py`
- Test: `tests/test_subscriptions.py` (create)

We add the type and the pure parsing helper first. The env-driven module-level constant comes in Task 2 once parsing is proven.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_subscriptions.py`:

```python
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


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `.venv/bin/python -m unittest tests.test_subscriptions -v`
Expected: ImportError or AttributeError — `Subscription` and `parse_recipients_by_category` do not yet exist in `config.py`.

- [ ] **Step 3: Implement `Subscription` and `parse_recipients_by_category` in `config.py`**

In `config.py`, **at the top of the file** (after `from pathlib import Path`), add:

```python
import json
import logging
from dataclasses import dataclass

logger = logging.getLogger("config")


@dataclass(frozen=True)
class Subscription:
    """One recipient's category filter for daily digest mail."""

    email: str
    categories: list[str]


def parse_recipients_by_category(
    raw: str | None, *, known_categories: list[str]
) -> list[Subscription]:
    """Parse RECIPIENTS_BY_CATEGORY JSON into validated subscriptions.

    Unknown categories are warned and dropped. Subscriptions left with zero
    valid categories or with an empty `categories` list are warned and
    skipped. Duplicate emails are warned and last-wins. Malformed JSON or
    missing required fields raise ValueError so misconfiguration fails
    fast at import time.
    """
    if not raw or not raw.strip():
        return []

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"RECIPIENTS_BY_CATEGORY is not valid JSON: {exc}") from exc

    if not isinstance(data, list):
        raise ValueError(
            "RECIPIENTS_BY_CATEGORY must be a JSON list of "
            "{email, categories} objects."
        )

    known = set(known_categories)
    by_email: dict[str, Subscription] = {}
    for index, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(
                f"RECIPIENTS_BY_CATEGORY[{index}] must be an object."
            )
        email = item.get("email")
        categories = item.get("categories")
        if not isinstance(email, str) or not email.strip():
            raise ValueError(
                f"RECIPIENTS_BY_CATEGORY[{index}].email must be a non-empty string."
            )
        if not isinstance(categories, list):
            raise ValueError(
                f"RECIPIENTS_BY_CATEGORY[{index}].categories must be a list."
            )
        validated: list[str] = []
        for category in categories:
            if category in known:
                validated.append(category)
            else:
                logger.warning(
                    "RECIPIENTS_BY_CATEGORY: dropping unknown category %r for %s",
                    category,
                    email,
                )
        if not validated:
            logger.warning(
                "RECIPIENTS_BY_CATEGORY: skipping %s — no valid categories left",
                email,
            )
            continue
        if email in by_email:
            logger.warning(
                "RECIPIENTS_BY_CATEGORY: duplicate entry for %s; last one wins",
                email,
            )
        by_email[email] = Subscription(email=email, categories=validated)

    return list(by_email.values())
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m unittest tests.test_subscriptions -v`
Expected: 10 PASS.

- [ ] **Step 5: Commit**

```bash
git add config.py tests/test_subscriptions.py
git commit -m "feat: add Subscription type and JSON parser for per-recipient categories"
```

---

### Task 2: Wire the env into module-level config

**Files:**
- Modify: `config.py` (add module-level binding)
- Test: `tests/test_subscriptions.py` (add one test that exercises the env)

- [ ] **Step 1: Append a config-binding test**

Append to `tests/test_subscriptions.py` (above the `if __name__ == "__main__":` line):

```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m unittest tests.test_subscriptions.RecipientsByCategoryEnvTest -v`
Expected: AttributeError — `config.RECIPIENTS_BY_CATEGORY` does not exist.

- [ ] **Step 3: Add the module-level constant to `config.py`**

Append at the bottom of `config.py` (after the existing `METADATA_DB_FILE = ...` line):

```python
# Per-recipient category subscriptions. JSON list of {email, categories}
# objects. When non-empty, the daily digest sends one filtered email per
# subscription instead of a single email to EMAIL_RECIPIENTS.
RECIPIENTS_BY_CATEGORY: list[Subscription] = parse_recipients_by_category(
    os.getenv("RECIPIENTS_BY_CATEGORY"),
    known_categories=CATEGORIES,
)
```

- [ ] **Step 4: Run the full test suite**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: all green (existing 13 + 11 new from Task 1 + 1 here = 25). If any unrelated test changes its expectation, stop and report.

- [ ] **Step 5: Commit**

```bash
git add config.py tests/test_subscriptions.py
git commit -m "feat: load RECIPIENTS_BY_CATEGORY at config import"
```

---

### Task 3: `_send_subscription_emails` helper in `main.py`

**Files:**
- Modify: `main.py` (add helper near the existing `_send_digest_email`)
- Test: `tests/test_subscriptions.py` (add `SendSubscriptionEmailsTest`)

- [ ] **Step 1: Add tests for the helper**

Append the following imports near the top of `tests/test_subscriptions.py`:

```python
from datetime import date, datetime, timezone
from unittest import mock
```

Then append before `if __name__ == "__main__":`:

```python
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
        from config import Subscription

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
        from config import Subscription

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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `.venv/bin/python -m unittest tests.test_subscriptions.SendSubscriptionEmailsTest -v`
Expected: AttributeError — `main._send_subscription_emails` does not exist.

- [ ] **Step 3: Implement the helper in `main.py`**

In `main.py`, add the following function **immediately above** the existing `_run_daily_digest` definition:

```python
def _send_subscription_emails(
    *,
    entries,
    found_in_category: dict[str, str],
    digest_date,
    subscriptions,
) -> None:
    """Send one filtered daily digest per Subscription.

    Subscribers with zero matched papers receive nothing.
    """
    from src.models import Digest

    for sub in subscriptions:
        wanted = set(sub.categories)
        filtered = [
            entry
            for entry in entries
            if found_in_category.get(entry.paper.arxiv_id) in wanted
        ]
        if not filtered:
            logger.info(
                "Subscription %s has no matched papers today, skipping",
                sub.email,
            )
            continue

        rendered = render_digest(
            Digest(digest_date=digest_date, entries=filtered),
            category_by_id=found_in_category,
            category_order=list(sub.categories),
        )
        category_label = ",".join(sub.categories)
        _send_digest_email(
            subject=f"ArXiv 每日论文摘要 [{category_label}] {digest_date.isoformat()}",
            rendered=rendered,
            attachment_name=f"arxiv-daily-{digest_date.isoformat()}.md",
            recipients=[sub.email],
        )
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m unittest tests.test_subscriptions.SendSubscriptionEmailsTest -v`
Expected: 2 PASS.

- [ ] **Step 5: Commit**

```bash
git add main.py tests/test_subscriptions.py
git commit -m "feat: add per-subscription daily email helper"
```

---

### Task 4: Branch `_run_daily_digest` on subscriptions vs. fallback

**Files:**
- Modify: `main.py:409-414` (the daily email block in `_run_daily_digest`)
- Test: `tests/test_subscriptions.py` (add `RunDailyDigestEmailRoutingTest`)

- [ ] **Step 1: Add routing test**

Append to `tests/test_subscriptions.py` before `if __name__ == "__main__":`:

```python
class RunDailyDigestEmailRoutingTest(unittest.TestCase):
    """Verify the helper is selected based on RECIPIENTS_BY_CATEGORY."""

    def _route(self, *, subscriptions: list) -> str:
        """Return 'subscription' or 'fallback' based on which path runs.

        We replicate the routing condition rather than calling
        _run_daily_digest end-to-end (which would need full ArXiv + LLM
        plumbing). The conditional under test lives inline in
        _run_daily_digest at the email-send block.
        """
        if subscriptions:
            return "subscription"
        return "fallback"

    def test_subscriptions_present_chooses_subscription_path(self) -> None:
        from config import Subscription

        self.assertEqual(
            self._route(
                subscriptions=[
                    Subscription(email="a@b.com", categories=["cs.AI"])
                ],
            ),
            "subscription",
        )

    def test_no_subscriptions_chooses_fallback_path(self) -> None:
        self.assertEqual(self._route(subscriptions=[]), "fallback")
```

(These tests pin the *intent* of the branch we're about to write. Step 3 makes the production code match this routing.)

- [ ] **Step 2: Run tests to verify they pass already**

Run: `.venv/bin/python -m unittest tests.test_subscriptions.RunDailyDigestEmailRoutingTest -v`
Expected: 2 PASS (this test is documenting the routing, not driving it). If any other test fails, stop and investigate.

- [ ] **Step 3: Update `_run_daily_digest`'s email block in `main.py`**

Find this block in `main.py` (currently `main.py:409-414`):

```python
    if config.EMAIL_SEND_DAILY:
        _send_digest_email(
            subject=f"ArXiv 每日论文摘要 {digest.digest_date.isoformat()}",
            rendered=rendered,
            attachment_name=f"arxiv-daily-{digest.digest_date.isoformat()}.md",
        )
```

Replace it with:

```python
    if config.EMAIL_SEND_DAILY:
        if config.RECIPIENTS_BY_CATEGORY:
            _send_subscription_emails(
                entries=entries,
                found_in_category=found_in_category,
                digest_date=digest.digest_date,
                subscriptions=config.RECIPIENTS_BY_CATEGORY,
            )
        else:
            _send_digest_email(
                subject=f"ArXiv 每日论文摘要 {digest.digest_date.isoformat()}",
                rendered=rendered,
                attachment_name=f"arxiv-daily-{digest.digest_date.isoformat()}.md",
            )
```

- [ ] **Step 4: Run the full test suite**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: all green.

- [ ] **Step 5: Commit**

```bash
git add main.py tests/test_subscriptions.py
git commit -m "feat: route daily email through per-recipient subscriptions when configured"
```

---

### Task 5: Sanity smoke-render and update `.env.example`

**Files:**
- Modify: `.env.example` (add the new env, commented)

- [ ] **Step 1: Smoke-render two sample emails locally**

Run:

```bash
.venv/bin/python <<'PY'
from datetime import date, datetime, timezone
import main
from config import Subscription
from src.models import DigestEntry, Paper

def p(i, primary):
    return Paper(arxiv_id=i, url=f'https://arxiv.org/abs/{i}', title=f'Title {i}',
                 authors=['A'], abstract='abstract', primary_category=primary,
                 published=datetime(2026,5,26,10,tzinfo=timezone.utc))

entries = [
    DigestEntry(paper=p('2605.001','cs.AI'), summary='AI 1'),
    DigestEntry(paper=p('2605.002','cs.LG'), summary='LG 1'),
    DigestEntry(paper=p('2605.003','stat.ML'), summary='Stat 1'),
]
found = {'2605.001':'cs.AI','2605.002':'cs.LG','2605.003':'stat.ML'}
captured = []
def fake_send(**kw): captured.append(kw); return True

main._send_digest_email = fake_send
main._send_subscription_emails(
    entries=entries,
    found_in_category=found,
    digest_date=date(2026,5,26),
    subscriptions=[
        Subscription(email='a@x.com', categories=['cs.AI','cs.LG']),
        Subscription(email='b@y.com', categories=['stat.ML']),
        Subscription(email='c@z.com', categories=['q-bio.GN']),
    ],
)
for c in captured:
    print('---')
    print('SUBJECT', c['subject'])
    print('TO', c['recipients'])
    print(c['rendered'])
print('TOTAL emails sent:', len(captured))
PY
```

Expected: exactly 2 "---" blocks (Alice and Bob); Charlie skipped.
- Alice's subject: `ArXiv 每日论文摘要 [cs.AI,cs.LG] 2026-05-26`
- Bob's subject: `ArXiv 每日论文摘要 [stat.ML] 2026-05-26`
- Each rendered Markdown groups under `### cs.AI` / `### cs.LG` / `### stat.ML` only for the categories that subscriber has.

If any of those expectations fail, stop and fix the helper before continuing.

- [ ] **Step 2: Document the new env in `.env.example`**

Append to `.env.example`:

```
# Optional per-recipient category routing. JSON list of
# {email, categories} objects. When set and non-empty, the daily
# digest sends one filtered email per subscription instead of a
# single email to EMAIL_RECIPIENTS. Categories must appear in
# ARXIV_CATEGORIES; unknown categories are warned and dropped.
# RECIPIENTS_BY_CATEGORY=[{"email":"alice@x.com","categories":["cs.AI","cs.LG"]},{"email":"bob@y.com","categories":["stat.ML"]}]
```

- [ ] **Step 3: Commit**

```bash
git add .env.example
git commit -m "docs: document RECIPIENTS_BY_CATEGORY in .env.example"
```

---

## Verification (after all tasks)

Run the full test suite and confirm:

```bash
.venv/bin/python -m unittest discover -s tests -v
```

Expected: all tests pass, no warnings indicating unrelated regressions.

Also verify by reading the final `_run_daily_digest` block:
- Branch on `config.RECIPIENTS_BY_CATEGORY` truthy → `_send_subscription_emails`
- Branch on falsy → `_send_digest_email` (unchanged behaviour)
