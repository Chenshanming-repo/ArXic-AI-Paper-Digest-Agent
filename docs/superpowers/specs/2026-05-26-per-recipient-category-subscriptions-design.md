# Per-Recipient Category Subscriptions

**Date:** 2026-05-26
**Status:** Approved

## Goal

Let multiple recipients receive different slices of the daily ArXiv digest based on the categories they subscribe to. The summarisation pass remains run once per day; each recipient receives a filtered render with only their categories.

## Configuration

New env `RECIPIENTS_BY_CATEGORY`, parsed as JSON:

```
RECIPIENTS_BY_CATEGORY='[
  {"email": "alice@x.com", "categories": ["cs.AI", "cs.LG"]},
  {"email": "bob@y.com",   "categories": ["stat.ML", "q-bio.GN"]}
]'
```

`config.py` parses this on import into a typed list of `Subscription(email: str, categories: list[str])`. Parse errors are fatal at import (clear ValueError naming the bad field).

`EMAIL_RECIPIENTS` remains as a fallback: when `RECIPIENTS_BY_CATEGORY` is unset or empty, daily email behaviour is unchanged (single email with full digest to everyone in `EMAIL_RECIPIENTS`, original subject). When `RECIPIENTS_BY_CATEGORY` is non-empty, `EMAIL_RECIPIENTS` is ignored for the daily digest. Weekly/monthly rollups continue to use `EMAIL_RECIPIENTS`.

## Data Flow

```
fetch_recent_papers  ── papers + found_in_category ──┐
                                                     │
seen-id filter, MAX_PAPERS cap                       │
                                                     ▼
summarise_papers (once)                       digest.md / latest.md / archive
                                                     │
                                                     ▼
            for each Subscription in RECIPIENTS_BY_CATEGORY:
              filtered = entries whose found_in_category[id] ∈ sub.categories
              if not filtered: skip this subscriber
              rendered = render_digest(
                  Digest(entries=filtered),
                  category_by_id=found_in_category,
                  category_order=sub.categories,
              )
              subject  = f"ArXiv 每日论文摘要 [{','.join(sub.categories)}] {date}"
              send to sub.email
```

The summary LLM cost stays O(papers), independent of the number of subscribers.

## Edge Cases

- **Category typo / not in `ARXIV_CATEGORIES`** — log warning and drop that category from the subscription; if the subscription ends up with zero valid categories, log warning and skip the subscription entirely. Do not abort.
- **Duplicate email entries** — last occurrence wins (after a warning); prevents accidentally sending two mails to the same person.
- **Empty `categories: []`** — invalid; warn and skip.
- **All subscribers have zero matched papers today** — write digest.md / latest.md / archive as today, but send no email.
- **`RECIPIENTS_BY_CATEGORY` unset** — fall back to current behaviour (single email to `EMAIL_RECIPIENTS`).
- **`EMAIL_SEND_DAILY=false`** — disables daily email regardless of which path is in use.

## Subject Format

- New path: `ArXiv 每日论文摘要 [cs.AI,cs.LG] 2026-05-26` (categories in the order the subscription specified, comma-separated, no spaces)
- Fallback path: `ArXiv 每日论文摘要 2026-05-26` (unchanged)

## Files Touched

| File | Change |
|---|---|
| `config.py` | Add `Subscription` dataclass, `RECIPIENTS_BY_CATEGORY` env parsing, validation. |
| `main.py` | `_run_daily_digest`: branch on `config.RECIPIENTS_BY_CATEGORY`; new helper `_send_subscription_emails(entries, found_in_category, digest_date)`. Reuse `_send_digest_email`. |
| `src/writer.py` | No change (already supports `category_by_id` / `category_order`). |
| `src/emailer.py` | No change. |
| `tests/test_subscriptions.py` (new) | Parse, fallback, filter, skip-on-empty, subject, typo-warn-and-continue. |

## Testing Strategy

Unit tests, no live SMTP:

1. `RECIPIENTS_BY_CATEGORY` parse — happy path, malformed JSON raises, missing fields raises.
2. Subscription validation — unknown category in a sub: warn + drop; sub with zero valid cats: warn + skip; duplicate email: warn + last-wins.
3. Filtering — given a fixed `entries` + `found_in_category`, the right subset reaches each subscriber.
4. Subject format — single, multi, fallback.
5. Skip-on-empty — subscriber with no matched papers receives no email (assert `send_markdown_email` called 0 times for that recipient).
6. Fallback — when `RECIPIENTS_BY_CATEGORY` is empty, the old single-email path runs and `EMAIL_RECIPIENTS` is honoured.

## Out of Scope

- Per-subscriber `MAX_PAPERS` (everyone shares the same daily cap).
- Per-subscriber summary length / rollup periods (weekly/monthly rollups keep current single-recipient-list behaviour).
- A web UI / database for subscriptions.
- Unsubscribe links.
